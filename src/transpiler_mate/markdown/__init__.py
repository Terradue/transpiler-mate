# Copyright 2025 Terradue
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

from cwl_loader import load_cwl_from_yaml
from cwl_loader.utils import to_index
from cwl_loader.utils import search_process
from datetime import datetime
from importlib.metadata import (
    version,
    PackageNotFoundError
)
from jinja2 import (
    Environment,
    PackageLoader
)
from loguru import logger
from pathlib import Path
from transpiler_mate.metadata import MetadataManager
from transpiler_mate.codemeta import CodeMetaTranspiler
from typing import (
    get_args,
    get_origin,
    Any,
    List,
    Literal,
    Mapping,
    TextIO,
    Union,
)

import time

# START custom built-in functions to simplify the CWL rendering

# CWLtype to string methods

NA_ROLE = "N/A"

PERSON_TYPE = "https://schema.org/Person"
ROLE_TYPE = "https://schema.org/Role"

RoleKind = Literal["author", "contributor"]

def _normalize_role_people(value: Any, *, person_key: RoleKind) -> list[dict]:
    """
    Normalize a JSON-ish field that can be:
      - None
      - dict representing Person
      - dict representing Role (schema.org Role) holding a person under `person_key`
      - list (possibly nested) of any of the above

    into:
      - list of dicts, each a Role-shaped dict with:
          {"@type": "https://schema.org/Role", "role_name": <str>, person_key: <Person dict>, ...}

    For a bare Person dict, wraps it into a Role dict with role_name = "N/A".
    """

    def looks_like_person(d: dict) -> bool:
        return (
            d.get("@type") == PERSON_TYPE
            or any(k in d for k in ("given_name", "family_name", "email", "identifier", "affiliation"))
        )

    def ensure_person_dict(d: dict) -> dict:
        # shallow copy; ensure @type if you rely on it
        p = dict(d)
        p.setdefault("@type", PERSON_TYPE)
        return p

    def ensure_role_dict(role: dict) -> dict:
        r = dict(role)  # avoid mutating caller
        r.setdefault("@type", ROLE_TYPE)
        r.setdefault("role_name", NA_ROLE)
        # Normalize the nested person payload too (if present and dict)
        if isinstance(r.get(person_key), dict):
            r[person_key] = ensure_person_dict(r[person_key])
        return r

    if value is None:
        return []

    if isinstance(value, list):
        out: list[dict] = []
        for item in value:
            out.extend(_normalize_role_people(item, person_key=person_key))
        return out

    if not isinstance(value, dict):
        raise TypeError(f"{person_key} must be dict/list/None, got {type(value)!r}")

    # Already a Role wrapper if it contains the expected person key
    if person_key in value:
        return [ensure_role_dict(value)]

    # Otherwise treat it as a Person and wrap
    if looks_like_person(value):
        person = ensure_person_dict(value)
        return [ensure_role_dict({person_key: person})]

    raise ValueError(f"Unrecognized {person_key} dict shape (keys={sorted(value.keys())})")


def normalize_author(value: Any) -> list[dict]:
    return _normalize_role_people(value, person_key="author")


def normalize_contributor(value: Any) -> list[dict]:
    return _normalize_role_people(value, person_key="contributor")


def type_to_string(typ: Any) -> str:
    '''
    Serializes a CWL type to a human-readable string.

    Args:
        `typ` (`Any`): Any CWL type

    Returns:
        `str`: The human-readable string representing the input CWL type.
    '''
    if get_origin(typ) is Union:
        return " or ".join([type_to_string(inner_type) for inner_type in get_args(typ)])

    if isinstance(typ, list):
        return f"[ {', '.join([type_to_string(t) for t in typ])} ]"

    if hasattr(typ, "items"):
        return f"{type_to_string(typ.items)}[]"

    if isinstance(typ, str):
        return typ

    if hasattr(typ, '__name__'):
        return typ.__name__

    if hasattr(typ, 'type_'):
        return typ.type_
    
    # last hope to follow back
    return str(type)

def _get_version() -> str:
    try:
        return version("transpiler_mate")
    except PackageNotFoundError:
        return 'N/A'

def _to_mapping(
    functions: List[Any]
) -> Mapping[str, Any]:
    mapping: Mapping[str, Any] = {}

    for function in functions:
        mapping[function.__name__] = function

    return mapping

def nullable(
    type_: Any
) -> bool:
    return isinstance(type_, list) and "null" in type_ or hasattr(type_, "items") and "null" in getattr(type_, "items")


def get_exection_command(
    clt: Any
) -> str:
    result: List[str] = []

    if hasattr(clt, "baseCommand") and clt.baseCommand:
        if isinstance(clt.baseCommand, list):
            result += clt.baseCommand
        else:
            result.append(clt.baseCommand)

    if hasattr(clt, "arguments") and clt.arguments:
        if isinstance(clt.arguments, list):
            result += clt.arguments
        else:
            result.append(clt.arguments)

    return " ".join(result)

_jinja_environment = Environment(
    loader=PackageLoader(
        package_name='transpiler_mate.markdown'
    )
)
_jinja_environment.filters.update(
    _to_mapping(
        [
            get_exection_command,
            normalize_author,
            normalize_contributor,
            type_to_string,
        ]
    )
)
_jinja_environment.tests.update(
    _to_mapping(
        [
            nullable
        ]
    )
)

# END

def markdown_transpile(
    source: Path,
    workflow_id: str,
    output_stream: TextIO,
    code_repository: str | None
):
    logger.info(f"Reading metadata from {source}...")
    metadata_manager: MetadataManager = MetadataManager(source)

    logger.success(f"Metadata successfully read!")
    logger.info('Transpiling metadata...')

    transpiler: CodeMetaTranspiler = CodeMetaTranspiler(code_repository)
    metadata = transpiler.transpile(metadata_manager.metadata)

    logger.success(f"Metadata successfully transpiled!")
    logger.info('Reading Workflow model...')

    cwl_document = load_cwl_from_yaml(metadata_manager.raw_document)

    process = search_process(workflow_id, cwl_document)
    if not process:
        raise ValueError(f"Workflow {workflow_id} does not exist in input CWL document, only {list(map(lambda p: p.id, process)) if isinstance(process, list) else [process.id]} available.")

    logger.success(f"Workflow model successfully read!")

    template = _jinja_environment.get_template(f"index.md")

    output_stream.write(
        template.render(
            version=_get_version(),
            timestamp=datetime.fromtimestamp(time.time()).isoformat(timespec='milliseconds'),
            software_source_code=metadata if "SoftwareSourceCode" == metadata["@type"] else None,
            software_application=metadata["targetProduct"] if "SoftwareSourceCode" == metadata["@type"] else metadata,
            workflow=process,
            index=to_index(cwl_document) if isinstance(cwl_document, list) else { workflow_id: cwl_document }
        )
    )
