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

from collections.abc import Callable
from pathlib import Path
from typing import Any

from loguru import logger

from transpiler_mate.cli.common import write_json
from transpiler_mate.metadata import MetadataManager


def run(
    source: Path,
    workflow_id: str,
    image_source: str | None,
    image_revision: str | None,
    output: Path,
    metadata_manager_factory: Callable[[Path], MetadataManager] = MetadataManager,
) -> None:
    logger.info(f"Reading metadata from {source}...")
    metadata_manager: Any = metadata_manager_factory(source)

    logger.success("Metadata successfully read!")
    logger.info("Transpiling metadata...")

    from cwl_loader import load_cwl_from_yaml
    from cwl_loader.utils import search_process
    from transpiler_mate.oci import OrasAnnotationsTranspiler

    workflow = load_cwl_from_yaml(metadata_manager.raw_document)

    resolved_process = search_process(workflow_id, workflow)
    if not resolved_process:
        raise ValueError(
            f"Process {workflow_id} does not exist in input CWL document, only {list(map(lambda p: p.id, resolved_process)) if isinstance(resolved_process, list) else ['']} available."
        )

    data = OrasAnnotationsTranspiler(
        resolved_process, image_source, image_revision
    ).transpile(metadata_manager.metadata)

    logger.success("Metadata successfully transpiled!")
    write_json(data, output)
