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
from datetime import datetime
from functools import wraps
import json
from pathlib import Path
import time
from typing import Any, TypeVar

from loguru import logger

from transpiler_mate.metadata import MetadataManager, Transpiler

F = TypeVar("F", bound=Callable[..., Any])


def track(func: F) -> F:
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()

        logger.info(
            f"Started at: {datetime.fromtimestamp(start_time).isoformat(timespec='milliseconds')}"
        )

        try:
            func(*args, **kwargs)

            logger.success(
                "------------------------------------------------------------------------"
            )
            logger.success("SUCCESS")
            logger.success(
                "------------------------------------------------------------------------"
            )
        except Exception as e:
            logger.error(
                "------------------------------------------------------------------------"
            )
            logger.error("FAIL")
            logger.error(e)
            logger.error(
                "------------------------------------------------------------------------"
            )

        end_time = time.time()

        logger.info(f"Total time: {end_time - start_time:.4f} seconds")
        logger.info(
            f"Finished at: {datetime.fromtimestamp(end_time).isoformat(timespec='milliseconds')}"
        )

    return wrapper  # type: ignore[return-value]


def write_json(data: Any, output: Path) -> None:
    logger.info("Serializing metadata...")
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("w") as output_stream:
        json.dump(data, output_stream, indent=2)

    logger.success(f"Metadata successfully serialized to {output}.")


def transpile(
    source: Path,
    transpiler: Transpiler,
    output: Path,
    metadata_manager_factory: Callable[[Path], MetadataManager] = MetadataManager,
) -> None:
    logger.info(f"Reading metadata from {source}...")
    metadata_manager = metadata_manager_factory(source)

    logger.success("Metadata successfully read!")
    logger.info("Transpiling metadata...")
    data = transpiler.transpile(metadata_manager.metadata)

    logger.success("Metadata successfully transpiled!")
    write_json(data, output)
