from __future__ import annotations

from datetime import date
from pathlib import Path
from types import SimpleNamespace

from invenio_rest_api_client.types import UNSET
from transpiler_mate.invenio import InvenioMetadataTranspiler, _md5
from transpiler_mate.metadata.software_application_models import (
    CreativeWork,
    Organization,
    Person,
    SoftwareApplication,
)


def _software_application(*, with_contributor: bool) -> SoftwareApplication:
    publisher = Organization(name="Terradue")
    author = Person(
        givenName="Ada",
        familyName="Lovelace",
        email="ada@example.org",
        affiliation=publisher,
        identifier="https://orcid.org/0000-0002-1825-0097",
    )

    contributor = Person(
        givenName="Grace",
        familyName="Hopper",
        email="grace@example.org",
        affiliation=publisher,
    )

    return SoftwareApplication(
        name="Example Tool",
        description="Example description",
        dateCreated=date(2026, 3, 9),
        license=CreativeWork(identifier="Apache-2.0"),
        softwareVersion="1.2.3",
        softwareHelp=CreativeWork(name="Help"),
        publisher=publisher,
        author=author,
        contributor=contributor if with_contributor else None,
    )


def test_md5_hashes_file_content(tmp_path: Path) -> None:
    data_file = tmp_path / "data.bin"
    data_file.write_bytes(b"abc")

    assert _md5(data_file) == "900150983cd24fb0d6963f7d28e17f72"


def test_invenio_transpile_maps_core_fields_with_contributors() -> None:
    transpiler = object.__new__(InvenioMetadataTranspiler)

    metadata = transpiler.transpile(_software_application(with_contributor=True))

    assert metadata.title == "Example Tool"
    assert metadata.publisher == "Terradue"
    assert metadata.version == "1.2.3"
    assert len(metadata.creators) == 1
    assert len(metadata.contributors) == 1


def test_invenio_transpile_sets_contributors_to_unset_when_missing() -> None:
    transpiler = object.__new__(InvenioMetadataTranspiler)

    metadata = transpiler.transpile(_software_application(with_contributor=False))

    assert metadata.contributors == UNSET


def test_create_or_update_process_reserves_doi_when_identifier_missing(
    monkeypatch, tmp_path: Path
) -> None:
    source = tmp_path / "workflow.cwl"
    attach = tmp_path / "readme.txt"
    source.write_text("class: Workflow\n", encoding="utf-8")
    attach.write_text("x", encoding="utf-8")

    metadata = SimpleNamespace(identifier=None, same_as=None)
    manager = SimpleNamespace(metadata=metadata, updated=False)
    manager.update = lambda: setattr(manager, "updated", True)

    class _SessionClient:
        def __enter__(self):
            return "session"

        def __exit__(self, exc_type, exc, tb):
            return False

    transpiler = object.__new__(InvenioMetadataTranspiler)
    transpiler.metadata_manager = manager
    transpiler.invenio_client = _SessionClient()
    transpiler.invenio_base_url = "https://invenio.example.org"
    transpiler.transpile = lambda _metadata: {"ok": True}

    captured = {}

    monkeypatch.setattr(
        "transpiler_mate.invenio.create_a_draft_record",
        lambda client, body: SimpleNamespace(to_dict=lambda: {"id": "42"}),
    )
    monkeypatch.setattr(
        "transpiler_mate.invenio.reserve_a_doi",
        lambda draft_id, client: SimpleNamespace(
            to_dict=lambda: {
                "doi": "10.1234/test.1",
                "doi_url": "https://doi.org/10.1234/test.1",
            }
        ),
    )
    monkeypatch.setattr(
        transpiler,
        "_finalize",
        lambda draft_id, uploading_files, session_client, invenio_metadata: (
            captured.update(
                {
                    "draft_id": draft_id,
                    "files": uploading_files,
                    "session_client": session_client,
                    "metadata": invenio_metadata,
                }
            )
            or "https://invenio.example.org/records/42"
        ),
    )

    url = transpiler.create_or_update_process(source=source, attach=(attach,))

    assert url == "https://invenio.example.org/records/42"
    assert metadata.identifier == "10.1234/test.1"
    assert str(metadata.same_as) == "https://doi.org/10.1234/test.1"
    assert manager.updated is True
    assert captured["draft_id"] == "42"
    assert captured["files"] == [source, attach]


def test_create_or_update_process_creates_new_version_for_existing_identifier(
    monkeypatch, tmp_path: Path
) -> None:
    source = tmp_path / "workflow.cwl"
    source.write_text("class: Workflow\n", encoding="utf-8")

    metadata = SimpleNamespace(identifier="10.1234/example.8", same_as=None)
    manager = SimpleNamespace(metadata=metadata, updated=False)
    manager.update = lambda: setattr(manager, "updated", True)

    class _SessionClient:
        def __enter__(self):
            return "session"

        def __exit__(self, exc_type, exc, tb):
            return False

    transpiler = object.__new__(InvenioMetadataTranspiler)
    transpiler.metadata_manager = manager
    transpiler.invenio_client = _SessionClient()
    transpiler.invenio_base_url = "https://invenio.example.org"
    transpiler.transpile = lambda _metadata: {"ok": True}

    monkeypatch.setattr(
        "transpiler_mate.invenio.create_a_new_version",
        lambda record_id, client: SimpleNamespace(to_dict=lambda: {"id": "77"}),
    )
    monkeypatch.setattr(
        transpiler,
        "_finalize",
        lambda draft_id, uploading_files, session_client, invenio_metadata: (
            f"https://invenio.example.org/records/{draft_id}"
        ),
    )

    url = transpiler.create_or_update_process(source=source, attach=None)

    assert url == "https://invenio.example.org/records/77"
    assert manager.updated is False


def test_finalize_uploads_files_and_publishes(monkeypatch, tmp_path: Path) -> None:
    source = tmp_path / "workflow.cwl"
    attach = tmp_path / "asset.txt"
    source.write_text("cwlVersion: v1.2\n", encoding="utf-8")
    attach.write_text("asset", encoding="utf-8")

    transpiler = object.__new__(InvenioMetadataTranspiler)
    transpiler.invenio_base_url = "https://invenio.example.org"

    calls = {
        "start": 0,
        "upload": 0,
        "complete": 0,
        "update": 0,
        "publish": 0,
    }

    monkeypatch.setattr(
        "transpiler_mate.invenio.step_1_start_draft_file_uploads",
        lambda draft_id, client, body: calls.__setitem__("start", calls["start"] + 1),
    )
    monkeypatch.setattr(
        "transpiler_mate.invenio.step_2_upload_a_draft_files_content",
        lambda draft_id, file_name, body, client: calls.__setitem__(
            "upload", calls["upload"] + 1
        ),
    )
    monkeypatch.setattr(
        "transpiler_mate.invenio.step_3_complete_a_draft_file_upload",
        lambda draft_id, file_name, client: calls.__setitem__(
            "complete", calls["complete"] + 1
        ),
    )
    monkeypatch.setattr(
        "transpiler_mate.invenio.update_a_draft_record",
        lambda draft_id, body, client: calls.__setitem__("update", calls["update"] + 1),
    )
    monkeypatch.setattr(
        "transpiler_mate.invenio.publish_a_draft_record",
        lambda draft_id, client: calls.__setitem__("publish", calls["publish"] + 1),
    )

    record_url = transpiler._finalize(
        draft_id="12",
        uploading_files=[source, attach],
        session_client="session",
        invenio_metadata={"title": "Example"},
    )

    assert record_url == "https://invenio.example.org/records/12"
    assert calls == {"start": 1, "upload": 2, "complete": 2, "update": 1, "publish": 1}
