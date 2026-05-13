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
from enum import Enum, auto
from pathlib import Path
from typing import Any

from loguru import logger
from semver import Version

from transpiler_mate.metadata import MetadataManager


class VersionPart(Enum):
    MAJOR = auto()
    MINOR = auto()
    PATCH = auto()
    BUILD = auto()
    PRE_RELEASE = auto()


def run(
    source: Path,
    version_part: VersionPart,
    metadata_manager_factory: Callable[[Path], MetadataManager] = MetadataManager,
) -> None:
    logger.info(f"Reading metadata from {source}...")
    metadata_manager: Any = metadata_manager_factory(source)

    version = Version.parse(metadata_manager.metadata.software_version)

    if not version.is_valid:
        raise ValueError(
            f"Version {metadata_manager.metadata.software_version} is not compliant to the Semantic Versioning Specification 2.0.0, see https://semver.org/"
        )

    bumped_version = None

    match version_part:
        case VersionPart.MAJOR:
            bumped_version = version.bump_major()

        case VersionPart.MINOR:
            bumped_version = version.bump_minor()

        case VersionPart.PATCH:
            bumped_version = version.bump_patch()

        case VersionPart.BUILD:
            bumped_version = version.bump_build()

        case VersionPart.PRE_RELEASE:
            bumped_version = version.bump_prerelease()

        case _:
            raise ValueError(
                f"It's not you, it is us: {version_part} unsupported, but it shouldn't have been happened..."
            )

    logger.success(
        f"Software Version {metadata_manager.metadata.software_version} updated to {bumped_version}"
    )

    metadata_manager.metadata.software_version = str(bumped_version)

    metadata_manager.update()
