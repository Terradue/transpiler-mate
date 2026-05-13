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

from pydantic import BaseModel
from typing import Any, Mapping, MutableMapping
from transpiler_mate.metadata.software_application_models import SoftwareApplication
from transpiler_mate.metadata import Transpiler


class OgcProcessesTranspiler(Transpiler):
    def transpile(self, metadata_source: SoftwareApplication) -> Mapping[str, Any]:
        data: MutableMapping[str, Any] = {}

        for attribute in ["name", "description", "software_version", "license"]:
            attribute_value = getattr(metadata_source, attribute, None)
            if attribute_value:
                data[attribute] = (
                    attribute_value.model_dump()
                    if isinstance(attribute_value, BaseModel)
                    else attribute_value
                )

        return data
