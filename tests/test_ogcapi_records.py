from __future__ import annotations

from datetime import date

from transpiler_mate.metadata.software_application_models import (
    AuthorRole,
    CreativeWork,
    DefinedTerm,
    Organization,
    Person,
    SoftwareApplication,
)
from transpiler_mate.ogcapi_records import (
    OgcRecordsTranspiler,
    SCIENCE_KEYWORDS_TERM_SET,
)
from transpiler_mate.ogcapi_records.sciencekeywords import ScienceKeywordRecord


def _software_application() -> SoftwareApplication:
    publisher = Organization(name="Terradue")
    author = AuthorRole(
        roleName="Principal Investigator",
        author=Person(
            givenName="Ada",
            familyName="Lovelace",
            email="ada@example.org",
            identifier="https://orcid.org/0000-0002-1825-0097",
            affiliation=Organization(
                name="Terradue", identifier="https://ror.org/03yrm5c26"
            ),
        ),
    )

    return SoftwareApplication(
        name="Example Tool",
        description="Example description",
        dateCreated=date(2026, 3, 9),
        license=[
            CreativeWork(url="https://spdx.org/licenses/Apache-2.0.html"),
            "https://spdx.org/licenses/MIT.html",
        ],
        softwareVersion="1.2.3",
        softwareHelp=CreativeWork(name="Help", url="https://example.org/help"),
        publisher=publisher,
        author=author,
        keywords=[
            "earth-observation",
            DefinedTerm(
                inDefinedTermSet=str(SCIENCE_KEYWORDS_TERM_SET),
                termCode="kw-1",
            ),
            DefinedTerm(termCode="ignored"),
        ],
    )


def test_ogc_records_transpile_maps_keywords_themes_and_contacts(monkeypatch) -> None:
    monkeypatch.setattr(
        "transpiler_mate.ogcapi_records.KEYWORDS_INDEX",
        {
            "kw-1": ScienceKeywordRecord(
                category="EARTH SCIENCE",
                topic="ATMOSPHERE",
                term="AEROSOLS",
                identifier="kw-1",
            )
        },
    )
    monkeypatch.setattr("transpiler_mate.ogcapi_records.uuid.uuid4", lambda: "abc123")

    result = OgcRecordsTranspiler().transpile(_software_application())

    assert result["id"] == "urn:uuid:abc123"
    assert result["type"] == "Feature"
    assert result["properties"]["keywords"] == ["earth-observation"]
    assert result["properties"]["themes"][0]["scheme"] == str(SCIENCE_KEYWORDS_TERM_SET)
    assert result["properties"]["themes"][0]["concepts"][0]["id"] == "EARTH SCIENCE"
    assert result["properties"]["contacts"][0]["position"] == "Principal Investigator"
    assert (
        result["properties"]["license_"]
        == "https://spdx.org/licenses/Apache-2.0.html: https://spdx.org/licenses/MIT.html"
    )
    assert result["links"][0]["href"] == "https://example.org/help"


def test_ogc_records_transpile_skips_unsupported_keywords(monkeypatch) -> None:
    app = _software_application()
    app.keywords = [DefinedTerm(termCode="x"), 42]
    monkeypatch.setattr("transpiler_mate.ogcapi_records.uuid.uuid4", lambda: "abc123")

    result = OgcRecordsTranspiler().transpile(app)

    assert "keywords" not in result["properties"]
    assert "themes" not in result["properties"]
