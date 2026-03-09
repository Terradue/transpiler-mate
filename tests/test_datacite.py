from __future__ import annotations

from datetime import date

from transpiler_mate.datacite import DataCiteTranspiler
from transpiler_mate.metadata.software_application_models import (
    AuthorRole,
    ContributorRole,
    CreativeWork,
    Organization,
    Person,
    SoftwareApplication,
)


def _software_application(*, with_identifier: bool) -> SoftwareApplication:
    publisher = Organization(name="Terradue")
    author = AuthorRole(
        roleName="Lead",
        author=Person(
            givenName="Ada",
            familyName="Lovelace",
            email="ada@example.org",
            identifier="https://orcid.org/0000-0002-1825-0097",
            affiliation=Organization(
                name="Terradue",
                identifier="https://ror.org/03yrm5c26",
            ),
        ),
    )
    contributor = ContributorRole(
        roleName="Data Curator",
        additionalType="http://purl.org/spar/datacite/DataCurator",
        contributor=Person(
            givenName="Grace",
            familyName="Hopper",
            email="grace@example.org",
            identifier="https://orcid.org/0000-0002-1825-0100",
            affiliation=Organization(
                name="Navy", identifier="https://ror.org/01aaaab11"
            ),
        ),
    )

    kwargs = {}
    if with_identifier:
        kwargs["identifier"] = "10.1234/example.1"
        kwargs["sameAs"] = "https://doi.org/10.1234/example.1"

    return SoftwareApplication(
        name="Example Tool",
        description="Example description",
        dateCreated=date(2026, 3, 9),
        license=CreativeWork(
            name="Apache License 2.0",
            url="https://spdx.org/licenses/Apache-2.0.html",
            identifier="Apache-2.0",
        ),
        softwareVersion="1.2.3",
        softwareHelp=CreativeWork(name="Help"),
        publisher=publisher,
        author=author,
        contributor=contributor,
        **kwargs,
    )


def test_datacite_transpile_maps_identifier_and_people() -> None:
    result = DataCiteTranspiler().transpile(_software_application(with_identifier=True))

    assert result["doi"] == "10.1234/example.1"
    assert result["identifiers"][0]["identifierType"] == "DOI"
    assert result["identifiers"][0]["identifier"] == "10.1234/example.1"
    assert (
        result["relatedIdentifiers"][0]["relatedIdentifier"]
        == "https://doi.org/10.1234/example.1"
    )

    assert result["creators"][0]["name"] == "Lovelace, Ada"
    assert (
        result["creators"][0]["nameIdentifiers"][0]["nameIdentifierScheme"] == "ORCID"
    )
    assert (
        result["creators"][0]["affiliation"][0]["affiliationIdentifierScheme"] == "ROR"
    )

    assert result["contributors"][0]["contributorType"] == "DataCurator"
    assert result["rights"][0]["rightsIdentifier"] == "Apache-2.0"


def test_datacite_transpile_generates_urn_when_identifier_missing(monkeypatch) -> None:
    monkeypatch.setattr("transpiler_mate.datacite.uuid.uuid4", lambda: "deadbeef")

    result = DataCiteTranspiler().transpile(
        _software_application(with_identifier=False)
    )

    assert result["identifiers"][0]["identifierType"] == "URN"
    assert result["identifiers"][0]["identifier"] == "urn:uuid:deadbeef"
    assert result["types"]["resourceTypeGeneral"] == "Software"


def test_datacite_transpile_omits_contributors_when_missing() -> None:
    app = _software_application(with_identifier=False)
    app.contributor = None

    result = DataCiteTranspiler().transpile(app)

    assert "contributors" not in result
