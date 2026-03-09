# Copyright 2026 Terradue
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

from .oras_annotations_models import OrasAnnotations
from ..metadata import Transpiler
from ..metadata.software_application_models import CreativeWork, SoftwareApplication
from cwl_utils.parser import Process
from pydantic import AnyUrl
from ruamel.yaml.comments import CommentedMap
from typing import Any, Mapping


def _to_license_spdx(license: CreativeWork | AnyUrl) -> str:
    if isinstance(license, CreativeWork):
        return str(license.identifier)
    return str(license).split("/")[-1]


class OrasAnnotationsTranspiler(Transpiler):
    def __init__(self, process: Process):
        self.process: Process = process

    def transpile(self, metadata_source: SoftwareApplication) -> Mapping[str, Any]:
        oras_annotations: OrasAnnotations = OrasAnnotations()

        # org.opencontainers.image.* properties
        oras_annotations.org_opencontainers_image_title = metadata_source.name
        oras_annotations.org_opencontainers_image_description = (
            metadata_source.description
        )
        oras_annotations.org_opencontainers_image_version = (
            metadata_source.software_version
        )
        # oras_annotations.org_opencontainers_image_source = ?
        # oras_annotations.org_opencontainers_image_revision = ?
        oras_annotations.org_opencontainers_image_created = metadata_source.date_created
        oras_annotations.org_opencontainers_image_licenses = (
            " OR ".join(
                [_to_license_spdx(license) for license in metadata_source.license]
            )
            if isinstance(metadata_source.license, list)
            else _to_license_spdx(metadata_source.license)
        )

        # org.cwl.* properties
        oras_annotations.org_cwl_entrypoint = self.process.id
        oras_annotations.org_cwl_spec = self.process.cwlVersion
        oras_annotations.org_cwl_type = self.process.class_

        return oras_annotations.model_dump()
