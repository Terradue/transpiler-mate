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

import json
import sys
from pathlib import Path
from types import SimpleNamespace

from transpiler_mate import cli


class DummyTranspiler:
    def transpile(self, metadata_source):
        return {"name": metadata_source.name, "ok": True}


class DummyManager:
    def __init__(self, source: Path):
        self.document_source = source
        self.metadata = SimpleNamespace(name="Example", software_version="1.2.3")
        self.updated = False

    def update(self) -> None:
        self.updated = True


class DummyManagerFactory:
    def __init__(self):
        self.instance = None

    def __call__(self, source: Path):
        self.instance = DummyManager(source)
        return self.instance


def test_transpile_writes_json_output(monkeypatch, tmp_path: Path) -> None:
    source = tmp_path / "input.cwl"
    source.write_text("cwlVersion: v1.2\n", encoding="utf-8")

    factory = DummyManagerFactory()
    monkeypatch.setattr(cli, "MetadataManager", factory)

    output = tmp_path / "out" / "result.json"
    cli._transpile(source=source, transpiler=DummyTranspiler(), output=output)

    assert output.exists()
    assert json.loads(output.read_text(encoding="utf-8")) == {
        "name": "Example",
        "ok": True,
    }


def test_track_catches_exceptions() -> None:
    calls = {"count": 0}

    @cli._track
    def failing():
        calls["count"] += 1
        raise RuntimeError("boom")

    # The wrapper should not re-raise.
    failing()

    assert calls["count"] == 1


def test_bump_version_updates_metadata(monkeypatch, tmp_path: Path) -> None:
    source = tmp_path / "workflow.cwl"
    source.write_text("cwlVersion: v1.2\n", encoding="utf-8")

    factory = DummyManagerFactory()
    monkeypatch.setattr(cli, "MetadataManager", factory)

    # Call undecorated callback to avoid _track swallowing potential failures.
    cli.bump_version.callback.__wrapped__(
        source=source, version_part=cli.VersionPart.PATCH
    )

    assert factory.instance is not None
    assert factory.instance.metadata.software_version == "1.2.4"
    assert factory.instance.updated is True


def test_bump_version_raises_for_invalid_semver(monkeypatch, tmp_path: Path) -> None:
    source = tmp_path / "workflow.cwl"
    source.write_text("cwlVersion: v1.2\n", encoding="utf-8")

    manager = DummyManager(source)
    manager.metadata.software_version = "not-a-version"
    monkeypatch.setattr(cli, "MetadataManager", lambda _source: manager)

    try:
        cli.bump_version.callback.__wrapped__(
            source=source, version_part=cli.VersionPart.PATCH
        )
        assert False, "Expected ValueError"
    except ValueError:
        assert True


def test_codemeta_command_uses_transpile_with_codemeta_transpiler(
    monkeypatch, tmp_path: Path
) -> None:
    source = tmp_path / "workflow.cwl"
    output = tmp_path / "codemeta.json"
    source.write_text("cwlVersion: v1.2\n", encoding="utf-8")

    captured = {}

    class DummyCodeMetaTranspiler:
        def __init__(self, code_repository):
            self.code_repository = code_repository

    monkeypatch.setitem(
        sys.modules,
        "transpiler_mate.codemeta",
        SimpleNamespace(CodeMetaTranspiler=DummyCodeMetaTranspiler),
    )
    monkeypatch.setattr(
        cli,
        "_transpile",
        lambda source, transpiler, output: captured.update(
            {"source": source, "transpiler": transpiler, "output": output}
        ),
    )

    cli.codemeta.callback.__wrapped__(
        source=source,
        code_repository="https://github.com/acme/example-tool",
        output=output,
    )

    assert captured["source"] == source
    assert captured["output"] == output
    assert (
        captured["transpiler"].code_repository == "https://github.com/acme/example-tool"
    )


def test_datacite_and_ogcrecord_commands_delegate_to_transpile(
    monkeypatch, tmp_path: Path
) -> None:
    source = tmp_path / "workflow.cwl"
    source.write_text("cwlVersion: v1.2\n", encoding="utf-8")

    calls = []
    monkeypatch.setitem(
        sys.modules,
        "transpiler_mate.datacite",
        SimpleNamespace(DataCiteTranspiler=lambda: "datacite-transpiler"),
    )
    monkeypatch.setitem(
        sys.modules,
        "transpiler_mate.ogcapi_records",
        SimpleNamespace(OgcRecordsTranspiler=lambda: "ogc-transpiler"),
    )
    monkeypatch.setattr(
        cli,
        "_transpile",
        lambda source, transpiler, output: calls.append((source, transpiler, output)),
    )

    cli.datacite.callback.__wrapped__(source=source, output=tmp_path / "datacite.json")
    cli.ogcrecord.callback.__wrapped__(source=source, output=tmp_path / "record.json")

    assert calls[0][1] == "datacite-transpiler"
    assert calls[1][1] == "ogc-transpiler"


def test_oci_annotations_command_writes_output(monkeypatch, tmp_path: Path) -> None:
    source = tmp_path / "workflow.cwl"
    source.write_text("cwlVersion: v1.2\n", encoding="utf-8")
    output = tmp_path / "annotations.json"

    metadata_manager = SimpleNamespace(
        raw_document={"id": "#main"},
        metadata=SimpleNamespace(name="Example"),
    )
    monkeypatch.setattr(cli, "MetadataManager", lambda _source: metadata_manager)
    monkeypatch.setitem(
        sys.modules,
        "cwl_loader",
        SimpleNamespace(load_cwl_from_yaml=lambda _raw: "doc"),
    )
    monkeypatch.setitem(
        sys.modules,
        "cwl_loader.utils",
        SimpleNamespace(
            search_process=lambda workflow_id, workflow: SimpleNamespace(id="#main")
        ),
    )
    monkeypatch.setitem(
        sys.modules,
        "transpiler_mate.oci",
        SimpleNamespace(
            OrasAnnotationsTranspiler=lambda process, image_source, image_revision: (
                SimpleNamespace(transpile=lambda _metadata: {"ok": True})
            )
        ),
    )

    cli.oci_annotations.callback.__wrapped__(
        source=source,
        workflow_id="main",
        image_source=None,
        image_revision=None,
        output=output,
    )

    assert json.loads(output.read_text(encoding="utf-8")) == {"ok": True}


def test_oci_annotations_command_raises_when_process_missing(
    monkeypatch, tmp_path: Path
) -> None:
    source = tmp_path / "workflow.cwl"
    source.write_text("cwlVersion: v1.2\n", encoding="utf-8")

    metadata_manager = SimpleNamespace(
        raw_document={"id": "#main"},
        metadata=SimpleNamespace(name="Example"),
    )
    monkeypatch.setattr(cli, "MetadataManager", lambda _source: metadata_manager)
    monkeypatch.setitem(
        sys.modules,
        "cwl_loader",
        SimpleNamespace(load_cwl_from_yaml=lambda _raw: "doc"),
    )
    monkeypatch.setitem(
        sys.modules,
        "cwl_loader.utils",
        SimpleNamespace(search_process=lambda workflow_id, workflow: None),
    )
    monkeypatch.setitem(
        sys.modules,
        "transpiler_mate.oci",
        SimpleNamespace(OrasAnnotationsTranspiler=lambda *args, **kwargs: None),
    )

    try:
        cli.oci_annotations.callback.__wrapped__(
            source=source,
            workflow_id="main",
            image_source=None,
            image_revision=None,
            output=tmp_path / "annotations.json",
        )
        assert False, "Expected ValueError"
    except ValueError as exc:
        assert "Process main does not exist" in str(exc)


def test_markdown_and_invenio_publish_commands(monkeypatch, tmp_path: Path) -> None:
    source = tmp_path / "workflow.cwl"
    attach = tmp_path / "asset.txt"
    source.write_text("cwlVersion: v1.2\n", encoding="utf-8")
    attach.write_text("asset", encoding="utf-8")

    rendered = []
    monkeypatch.setattr(
        cli,
        "markdown_transpile",
        lambda source, workflow_id, output_stream, code_repository: (
            rendered.append((source, workflow_id, code_repository)),
            output_stream.write("# doc"),
        ),
    )
    cli.markdown.callback(
        source=source, workflow_id="main", output=tmp_path, code_repository=None
    )
    assert rendered[0][1] == "main"
    assert (tmp_path / "main.md").exists()

    created = {}
    monkeypatch.setattr(cli, "MetadataManager", lambda _source: "manager")
    monkeypatch.setitem(
        sys.modules,
        "transpiler_mate.invenio",
        SimpleNamespace(
            InvenioMetadataTranspiler=lambda metadata_manager, invenio_base_url, auth_token: (
                SimpleNamespace(
                    create_or_update_process=lambda source, attach: (
                        created.update({"source": source, "attach": attach})
                        or "https://invenio.example.org/records/1"
                    )
                )
            )
        ),
    )

    cli.invenio_publish.callback.__wrapped__(
        source=source,
        base_url="https://invenio.example.org",
        auth_token="token",
        attach=(attach,),
    )

    assert created["source"] == source
    assert created["attach"] == (attach,)
