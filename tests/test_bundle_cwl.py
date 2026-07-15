# Copyright 2026 Terradue
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import annotations

from pathlib import Path

from transpiler_mate.cli import bundle_cwl


class DummySession:
    def __init__(self) -> None:
        self.mounts: list[tuple[str, object]] = []

    def mount(self, scheme: str, adapter: object) -> None:
        self.mounts.append((scheme, adapter))


def test_run_resolves_and_serializes_cwl_with_configured_session(
    monkeypatch, tmp_path: Path
) -> None:
    source = tmp_path / "workflow.cwl"
    source.write_text("cwlVersion: v1.2\n", encoding="utf-8")
    output = tmp_path / "nested" / "bundle.cwl"
    session = DummySession()
    resolved_workflow = object()
    load_call: dict[str, object] = {}
    dump_call: dict[str, object] = {}

    class DummyAdapter:
        def __init__(self, *args, **kwargs) -> None:
            self.args = args
            self.kwargs = kwargs

    monkeypatch.setattr(bundle_cwl, "Session", lambda: session)
    monkeypatch.setattr(bundle_cwl, "HTTPAdapter", DummyAdapter)
    monkeypatch.setattr(bundle_cwl, "BearerAuthHTTPAdapter", DummyAdapter)
    monkeypatch.setattr(bundle_cwl, "FileAdapter", DummyAdapter)
    monkeypatch.setattr(bundle_cwl, "S3Adapter", DummyAdapter)
    monkeypatch.setattr(bundle_cwl, "OCIAdapter", DummyAdapter)
    monkeypatch.setattr(
        bundle_cwl,
        "load_cwl_from_location",
        lambda **kwargs: load_call.update(kwargs) or resolved_workflow,
    )

    def dump_cwl(process: object, stream) -> None:
        dump_call["process"] = process
        stream.write("cwlVersion: v1.2\nclass: Workflow\n")

    monkeypatch.setattr(bundle_cwl, "dump_cwl", dump_cwl)

    bundle_cwl.run(
        source=source,
        output=output,
        oci_hostname="registry.example.org",
        oci_username="user",
        oci_password="secret",
        oauth2_bearer="token",
    )

    assert load_call == {"path": str(source.absolute()), "session": session}
    assert dump_call["process"] is resolved_workflow
    assert output.read_text(encoding="utf-8") == ("cwlVersion: v1.2\nclass: Workflow\n")
    assert [scheme for scheme, _adapter in session.mounts] == [
        "http://",
        "https://",
        "file://",
        "s3://",
        "oci://",
    ]

    http_adapter = session.mounts[0][1]
    assert session.mounts[1][1] is http_adapter
    assert http_adapter.args == ("token",)

    oci_adapter = session.mounts[-1][1]
    assert oci_adapter.kwargs == {
        "hostname": "registry.example.org",
        "username": "user",
        "password": "secret",
    }


def test_run_uses_standard_http_adapter_without_bearer_token(
    monkeypatch, tmp_path: Path
) -> None:
    source = tmp_path / "workflow.cwl"
    output = tmp_path / "bundle.cwl"
    session = DummySession()
    standard_http_adapter = object()

    monkeypatch.setattr(bundle_cwl, "Session", lambda: session)
    monkeypatch.setattr(bundle_cwl, "HTTPAdapter", lambda: standard_http_adapter)
    monkeypatch.setattr(bundle_cwl, "FileAdapter", lambda: object())
    monkeypatch.setattr(bundle_cwl, "S3Adapter", lambda: object())
    monkeypatch.setattr(bundle_cwl, "OCIAdapter", lambda **_kwargs: object())
    monkeypatch.setattr(
        bundle_cwl, "load_cwl_from_location", lambda **_kwargs: object()
    )
    monkeypatch.setattr(bundle_cwl, "dump_cwl", lambda _process, _stream: None)

    bundle_cwl.run(source, output, None, None, None, None)

    assert session.mounts[0] == ("http://", standard_http_adapter)
    assert session.mounts[1] == ("https://", standard_http_adapter)
