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

from .oci_annotations_models import OciAnnotations
from ..metadata import Transpiler
from ..metadata.software_application_models import CreativeWork, SoftwareApplication
from cwl_utils.parser import Process
from pydantic import AnyUrl
from typing import Any, Mapping


def _to_license_spdx(license: CreativeWork | AnyUrl) -> str:
    if isinstance(license, CreativeWork):
        return str(license.identifier)
    return str(license).split("/")[-1]


class OrasAnnotationsTranspiler(Transpiler):
    def __init__(
        self,
        process: Process,
        image_source: str | None,
        image_revision: str | None,
    ):
        self.process: Process = process
        self.image_source = image_source
        self.image_revision = image_revision

    def transpile(self, metadata_source: SoftwareApplication) -> Mapping[str, Any]:
        oci_annotations: OciAnnotations = OciAnnotations()

        # org.opencontainers.image.* properties
        oci_annotations.org_opencontainers_image_title = metadata_source.name
        oci_annotations.org_opencontainers_image_description = (
            metadata_source.description
        )
        oci_annotations.org_opencontainers_image_version = (
            metadata_source.software_version
        )
        oci_annotations.org_opencontainers_image_source = self.image_source
        oci_annotations.org_opencontainers_image_revision = self.image_revision
        oci_annotations.org_opencontainers_image_licenses = (
            " OR ".join(
                [_to_license_spdx(license) for license in metadata_source.license]
            )
            if isinstance(metadata_source.license, list)
            else _to_license_spdx(metadata_source.license)
        )

        # org.cwl.* properties
        oci_annotations.org_cwl_entrypoint = self.process.id
        oci_annotations.org_cwl_spec = self.process.cwlVersion
        oci_annotations.org_cwl_type = self.process.class_

        return {
            "$manifest": oci_annotations.model_dump(by_alias=True, exclude_none=True)
        }
