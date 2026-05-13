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

from transpiler_mate.metadata import MetadataManager


def run(
    source: Path,
    base_url: str,
    auth_token: str,
    attach: tuple[Path, ...] | None,
    metadata_manager_factory: Callable[[Path], MetadataManager] = MetadataManager,
) -> None:
    metadata_manager: Any = metadata_manager_factory(source)

    logger.info(f"Interacting with Invenio server at {base_url})")

    from transpiler_mate.invenio import InvenioMetadataTranspiler

    invenio_transpiler = InvenioMetadataTranspiler(
        metadata_manager=metadata_manager,
        invenio_base_url=base_url,
        auth_token=auth_token,
    )

    record_url = invenio_transpiler.create_or_update_process(
        source=source, attach=attach
    )

    logger.success(f"Record available on '{record_url}'")
