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

from transpiler_mate.metadata.software_application_models import (
    SoftwareApplication,
    SoftwareSourceCode
)
from .metadata import Transpiler

from giturlparse import parse as gitparse
from loguru import logger
from pydantic import (
    AnyUrl,
    BaseModel
)
from pyld import jsonld
from typing import (
    Any,
    List,
    Mapping,
    MutableMapping
)

class CodeMetaTranspiler(Transpiler):

    def __init__(
        self,
        code_repository: str | None
    ) -> None:
        self.code_repository = code_repository

    def transpile(
        self,
        metadata_source: SoftwareApplication
    ) -> Mapping[str, Any]:
        model: BaseModel = metadata_source

        if self.code_repository:
            parsed_url = gitparse(self.code_repository)

            continuous_integration: str | None = None
            issue_tracker: str | None = None
            related_link: List[str] | None = None

            match parsed_url.platform:
                case 'github':
                    continuous_integration = parsed_url.url2https.replace('.git', '/actions')
                    issue_tracker = parsed_url.url2https.replace('.git', '/issues')
                    related_link = [
                        parsed_url.url2https.replace('.git', page) for page in [
                            '/wiki',
                            '/releases',
                            '/deployments'
                        ]
                    ]

                case 'gitlab':
                    continuous_integration = parsed_url.url2https.replace('.git', '/-/pipelines')
                    issue_tracker = parsed_url.url2https.replace('.git', '/-/issues')
                    related_link = [
                        parsed_url.url2https.replace('.git', page) for page in [
                            '/-/wikis/home',
                            '/-/packages',
                            '/-/pipelines'
                        ]
                    ]

                case _:
                    logger.warning(f"Platform {parsed_url.platform} unsupported yet")

            model = SoftwareSourceCode(
                code_repository=parsed_url.url2https,
                target_product=metadata_source,
                continuous_integration=continuous_integration,
                issue_tracker=issue_tracker,
                related_link=related_link
            ) # type: ignore @type is a constant

        doc: MutableMapping[str, Any] = model.model_dump(
            exclude_none=True,
            by_alias=True
        )

        compacted: MutableMapping[str, Any] = jsonld.compact(
            doc,
            {
                "@context": {
                    "@vocab": "https://schema.org/",
                    # (optional) If you want relative IRIs to stay relative, omit @base.
                    # If you want to forbid a base so @id values don't get resolved, set:
                    # "@base": None,
                }
            },
            options={
                "processingMode": "json-ld-1.1",
                "ordered": None
            }
        ) # type: ignore

        compacted['@context'] = 'https://w3id.org/codemeta/3.0'

        if metadata_source.keywords and isinstance(metadata_source.keywords, list):
            compacted['keywords'] = list(
                filter(
                    lambda keyword: isinstance(keyword, str),
                    metadata_source.keywords
                )
            )

        return compacted
