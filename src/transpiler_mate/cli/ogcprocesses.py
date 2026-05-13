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
from typing import Any, MutableMapping

from loguru import logger

from transpiler_mate.cli.common import write_json
from transpiler_mate.metadata import MetadataManager


def run(
    source: Path,
    output: Path,
    metadata_manager_factory: Callable[[Path], MetadataManager] = MetadataManager,
) -> None:
    from cwl_loader import load_cwl_from_yaml
    from cwl_utils.parser import Process
    from cwl2ogc import BaseCWLtypes2OGCConverter
    from transpiler_mate.ogcapi.processes import OgcProcessesTranspiler

    transpiler = OgcProcessesTranspiler()

    logger.info(f"Reading metadata from {source}...")
    metadata_manager: Any = metadata_manager_factory(source)

    logger.success("Metadata successfully read!")
    logger.info("Transpiling metadata...")
    data: MutableMapping[str, Any] = dict(
        transpiler.transpile(metadata_manager.metadata)
    )

    logger.success("Metadata successfully transpiled!")

    data["processes"] = {}

    def _wf_ogc_data(process: Process):
        process_data: MutableMapping[str, Any] = {}

        for attribute in ["class_", "label", "doc"]:
            if hasattr(process, attribute):
                attribute_value = getattr(process, attribute, None)
                if attribute_value:
                    process_data[attribute] = attribute_value

        cwl_converter = BaseCWLtypes2OGCConverter(process)

        process_data["inputs"] = cwl_converter.get_inputs()
        process_data["outputs"] = cwl_converter.get_outputs()

        data["processes"][process.id] = process_data

    workflows: Process | list[Process] = load_cwl_from_yaml(
        metadata_manager.raw_document
    )

    if isinstance(workflows, list):
        for workflow in workflows:
            _wf_ogc_data(workflow)
    else:
        _wf_ogc_data(workflows)

    write_json(data, output)
