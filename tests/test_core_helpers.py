from __future__ import annotations

from datetime import date
from types import SimpleNamespace

import pytest
from httpx import Response
from invenio_rest_api_client.models import RoleId
from pydantic import AnyUrl

from transpiler_mate import TranspilerBaseModel, _decode, _log_response
from transpiler_mate.invenio import (
    __ROLES_MAPPING_,
    _affiliation_identifier,
    _to_creator,
    _to_identifier,
)
from transpiler_mate.metadata.software_application_models import (
    CreativeWork,
    Organization,
    Person,
)
from transpiler_mate.oci import OrasAnnotationsTranspiler, _to_license_spdx


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
        raise AssertionError("Expected RuntimeError")
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


@pytest.mark.parametrize(
    ("credit_role", "role_id"),
    [
        ("conceptualization", RoleId.PROJECTLEADER),
        ("data-curation", RoleId.DATACURATOR),
        ("formal-analysis", RoleId.RESEARCHER),
        ("funding-acquisition", RoleId.SPONSOR),
        ("investigation", RoleId.DATACOLLECTOR),
        ("methodology", RoleId.RESEARCHER),
        ("project-administration", RoleId.PROJECTMANAGER),
        ("resources", RoleId.DATAMANAGER),
        ("software", RoleId.RESEARCHER),
        ("supervision", RoleId.SUPERVISOR),
        ("validation", RoleId.RESEARCHER),
        ("visualization", RoleId.RESEARCHER),
        ("writing-original-draft", RoleId.RESEARCHER),
        ("writing-review-editing", RoleId.EDITOR),
    ],
)
def test_credit_role_maps_to_invenio_role_id(credit_role: str, role_id: RoleId) -> None:
    role_url = AnyUrl(f"https://credit.niso.org/contributor-roles/{credit_role}/")

    assert __ROLES_MAPPING_[role_url] == role_id


def test_to_license_spdx_supports_creative_work_and_url() -> None:
    assert _to_license_spdx(CreativeWork(identifier="Apache-2.0")) == "Apache-2.0"
    assert _to_license_spdx("https://spdx.org/licenses/MIT.html") == "MIT.html"


def test_oras_annotations_transpiler_generates_oci_annotations() -> None:
    metadata = SimpleNamespace(
        name="Example Tool",
        description="Example workflow metadata",
        software_version="1.2.3",
        date_created=date(2026, 3, 9),
        license=[
            CreativeWork(identifier="Apache-2.0"),
            "https://spdx.org/licenses/MIT.html",
        ],
    )
    process = SimpleNamespace(id="#main", cwlVersion="v1.2", class_="Workflow")

    annotations = OrasAnnotationsTranspiler(
        process=process,
        image_source="https://github.com/acme/example-tool",
        image_revision="abc123def",
    ).transpile(metadata)["$manifest"]

    assert annotations["org.opencontainers.image.title"] == "Example Tool"
    assert (
        annotations["org.opencontainers.image.description"]
        == "Example workflow metadata"
    )
    assert annotations["org.opencontainers.image.version"] == "1.2.3"
    assert (
        annotations["org.opencontainers.image.source"]
        == "https://github.com/acme/example-tool"
    )
    assert annotations["org.opencontainers.image.revision"] == "abc123def"
    assert annotations["org.opencontainers.image.licenses"] == "Apache-2.0 OR MIT.html"
    assert annotations["org.cwl.entrypoint"] == "#main"
    assert annotations["org.cwl.spec"] == "v1.2"
    assert annotations["org.cwl.type"] == "Workflow"
