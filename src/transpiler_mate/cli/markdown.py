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
from typing import TextIO

from loguru import logger

from transpiler_mate.markdown import markdown_transpile


def run(
    source: Path,
    workflow_id: str,
    output: Path,
    code_repository: str | None,
    markdown_transpile_fn: Callable[
        [Path, str, TextIO, str | None], None
    ] = markdown_transpile,
) -> None:
    output.mkdir(parents=True, exist_ok=True)

    target: Path = Path(output, f"{workflow_id}.md")

    logger.info(f"Rendering Markdown documentation of {source} to {target}...")

    with target.open("w") as output_stream:
        markdown_transpile_fn(source, workflow_id, output_stream, code_repository)

    logger.info(f"Markdown documentation successfully serialized to {target}!")
