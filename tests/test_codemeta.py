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

from __future__ import annotations

from datetime import date

from transpiler_mate.codemeta import CodeMetaTranspiler
from transpiler_mate.metadata.software_application_models import (
    CreativeWork,
    DefinedTerm,
    Organization,
    Person,
    SoftwareApplication,
)


def _software_application() -> SoftwareApplication:
    publisher = Organization(name="Terradue")
    author = Person(
        givenName="Ada",
        familyName="Lovelace",
        email="ada@example.org",
        affiliation=publisher,
        identifier="https://orcid.org/0000-0002-1825-0097",
    )

    return SoftwareApplication(
        name="Example Tool",
        description="Example description",
        dateCreated=date(2026, 3, 9),
        license="https://spdx.org/licenses/Apache-2.0",
        softwareVersion="1.2.3",
        softwareHelp=CreativeWork(name="Help"),
        publisher=publisher,
        author=author,
        keywords=["remote-sensing", DefinedTerm(name="EO"), "cwl"],
    )


def test_codemeta_without_repository_keeps_application_and_filters_keywords() -> None:
    result = CodeMetaTranspiler(code_repository=None).transpile(_software_application())

    assert result["@context"] == "https://w3id.org/codemeta/3.0"
    assert result["@type"] == "SoftwareApplication"
    assert result["name"] == "Example Tool"
    assert result["keywords"] == ["remote-sensing", "cwl"]


def test_codemeta_with_github_repository_adds_repository_urls() -> None:
    result = CodeMetaTranspiler(
        code_repository="https://github.com/acme/example-tool.git"
    ).transpile(_software_application())

    assert result["@context"] == "https://w3id.org/codemeta/3.0"
    assert result["@type"] == "SoftwareSourceCode"
    assert result["codeRepository"] == "https://github.com/acme/example-tool.git"
    assert (
        result["continuousIntegration"]
        == "https://github.com/acme/example-tool/actions"
    )
    assert result["issueTracker"] == "https://github.com/acme/example-tool/issues"
    assert result["relatedLink"] == [
        "https://github.com/acme/example-tool/wiki",
        "https://github.com/acme/example-tool/releases",
        "https://github.com/acme/example-tool/deployments",
    ]
