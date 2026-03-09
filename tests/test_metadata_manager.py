from __future__ import annotations

from datetime import date
from pathlib import Path

from transpiler_mate import metadata
from transpiler_mate.metadata.software_application_models import (
    CreativeWork,
    Organization,
    Person,
    SoftwareApplication,
)


class FakeYAML:
    def __init__(self):
        self.dumped_data = None

    def load(self, _source):
        return {"$namespaces": {}, "existing": "value"}

    def dump(self, data, stream):
        self.dumped_data = dict(data)
        stream.write("ok")


def _software_application() -> SoftwareApplication:
    publisher = Organization(name="Terradue")
    author = Person(
        givenName="Ada",
        familyName="Lovelace",
        email="ada@example.org",
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
    )


def test_metadata_manager_raises_for_missing_file(tmp_path: Path) -> None:
    missing = tmp_path / "missing.cwl"
    try:
        metadata.MetadataManager(missing)
        assert False, "Expected ValueError"
    except ValueError as exc:
        assert "non existing file" in str(exc)


def test_metadata_manager_raises_for_directory(tmp_path: Path) -> None:
    try:
        metadata.MetadataManager(tmp_path)
        assert False, "Expected ValueError"
    except ValueError as exc:
        assert "is not a file" in str(exc)


def test_metadata_manager_resolves_spdx_license_and_updates_document(
    monkeypatch, tmp_path: Path
) -> None:
    source = tmp_path / "workflow.cwl"
    source.write_text("dummy", encoding="utf-8")

    fake_yaml = FakeYAML()
    monkeypatch.setattr(metadata, "YAML", lambda: fake_yaml)

    def _compact(input_, ctx, options):
        if isinstance(input_, dict) and "existing" in input_:
            return input_
        return {"@context": "https://schema.org", "softwareVersion": "2.0.0"}

    monkeypatch.setattr(metadata.jsonld, "compact", _compact)

    app = _software_application()
    monkeypatch.setattr(
        metadata.SoftwareApplication,
        "model_validate",
        classmethod(lambda cls, compacted, by_alias=True: app),
    )

    manager = metadata.MetadataManager(source)

    # SPDX index should replace the lightweight CreativeWork with indexed metadata.
    assert isinstance(manager.metadata.license, CreativeWork)
    assert manager.metadata.license.identifier == "Apache-2.0"
    assert manager.metadata.license.name is not None

    manager.metadata.software_version = "2.0.0"
    manager.update()

    assert fake_yaml.dumped_data is not None
    assert fake_yaml.dumped_data["existing"] == "value"
