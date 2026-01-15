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

from cwl_loader import load_cwl_from_yaml
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
    Mapping,
    TextIO,
    Union
)

import time

# START custom built-in functions to simplify the CWL rendering

# CWLtype to string methods

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

_jinja_environment = Environment(
    loader=PackageLoader(
        package_name='transpiler_mate.markdown'
    )
)
_jinja_environment.filters.update(
    _to_mapping(
        [
            type_to_string
        ]
    )
)
_jinja_environment.tests.update(
    _to_mapping(
        [
            
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

    template = _jinja_environment.get_template(f"workflow.md")

    output_stream.write(
        template.render(
            version=_get_version(),
            timestamp=datetime.fromtimestamp(time.time()).isoformat(timespec='milliseconds'),
            software_source_code=metadata if "SoftwareSourceCode" == metadata["@type"] else None,
            software_application=metadata["targetProduct"] if "SoftwareSourceCode" == metadata["@type"] else metadata,
            workflow=process
        )
    )
