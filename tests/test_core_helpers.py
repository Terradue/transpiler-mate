from __future__ import annotations

from httpx import Response
from pydantic import AnyUrl

from transpiler_mate import TranspilerBaseModel, _decode, _log_response
from transpiler_mate.invenio import (
    _affiliation_identifier,
    _to_creator,
    _to_identifier,
)
from transpiler_mate.metadata.software_application_models import (
    AuthorRole,
    Organization,
    Person,
)
from invenio_rest_api_client.models.role_id import RoleId


class SampleModel(TranspilerBaseModel):
    homepage: AnyUrl


def _person() -> Person:
    return Person(
        givenName="Ada",
        familyName="Lovelace",
        email="ada@example.org",
        identifier="https://orcid.org/0000-0002-1825-0097",
        affiliation=Organization(
            name="Terradue",
            identifier="https://ror.org/03yrm5c26",
        ),
    )


def test_decode_supports_empty_string_and_bytes() -> None:
    assert _decode(None) == ""
    assert _decode("") == ""
    assert _decode("abc") == "abc"
    assert _decode(b"abc") == "abc"


def test_transpiler_base_model_dump_defaults_to_json_mode() -> None:
    model = SampleModel(homepage="https://example.org/path")
    dumped = model.model_dump()
    assert dumped["homepage"] == "https://example.org/path"


def test_log_response_raises_runtime_error_on_http_errors() -> None:
    def fake_request(*args, **kwargs):
        return Response(status_code=400, content=b"bad request")

    wrapped = _log_response(fake_request)

    try:
        wrapped(method="get", url="https://example.org")
        assert False, "Expected RuntimeError"
    except RuntimeError as exc:
        message = str(exc)
        assert "GET" in message
        assert "https://example.org" in message


def test_to_identifier_extracts_scheme_and_last_path_segment() -> None:
    identifier = _to_identifier("https://orcid.org/0000-0002-1825-0097")
    assert identifier.scheme.value == "orcid"
    assert identifier.identifier == "0000-0002-1825-0097"


def test_affiliation_identifier_returns_last_path_segment() -> None:
    assert _affiliation_identifier("https://ror.org/03yrm5c26") == "03yrm5c26"


def test_to_creator_from_person_builds_identifiers_and_affiliations() -> None:
    creator = _to_creator(_person())

    assert creator.role.id == RoleId.OTHER
    assert creator.person_or_org.name == "Lovelace, Ada"
    assert creator.person_or_org.identifiers[0].identifier == "0000-0002-1825-0097"
    assert creator.affiliations[0].id == "03yrm5c26"
    assert creator.affiliations[0].name == "Terradue"


def test_to_creator_from_author_role_maps_datacite_role() -> None:
    role = AuthorRole(
        roleName="Data Curator",
        additionalType="http://purl.org/spar/datacite/DataCurator",
        author=_person(),
    )

    creator = _to_creator(role)

    assert creator.role.id == RoleId.DATACURATOR
