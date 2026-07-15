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

from pathlib import Path

from cwl_loader import dump_cwl, load_cwl_from_location
from cwl_utils.parser import Process
from loguru import logger
from requests import Session
from requests.adapters import BaseAdapter, HTTPAdapter
from session_adapters.bearer_auth_http_adapter import BearerAuthHTTPAdapter
from session_adapters.file_adapter import FileAdapter
from session_adapters.oci_adapter import OCIAdapter
from session_adapters.s3_adapter import S3Adapter


def run(
    source: Path,
    output: Path,
    oci_hostname: str | None,
    oci_username: str | None,
    oci_password: str | None,
    oauth2_bearer: str | None,
) -> None:
    session = Session()

    def mount_session(scheme: str, adapter: BaseAdapter) -> None:
        logger.debug(f"Mounting '{scheme}' scheme to '{type(adapter).__name__}'...")
        session.mount(scheme, adapter)
        logger.debug(
            f"Scheme '{scheme}' successfully mount to '{type(adapter).__name__}'"
        )

    http_adapter = (
        BearerAuthHTTPAdapter(oauth2_bearer) if oauth2_bearer else HTTPAdapter()
    )
    mount_session("http://", http_adapter)
    mount_session("https://", http_adapter)
    mount_session("file://", FileAdapter())
    mount_session("s3://", S3Adapter())
    mount_session(
        "oci://",
        OCIAdapter(hostname=oci_hostname, username=oci_username, password=oci_password),
    )

    resolved_workflow: Process | list[Process] = load_cwl_from_location(
        path=str(source.absolute()), session=session
    )

    output.parent.mkdir(parents=True, exist_ok=True)

    logger.debug(f"Serializing resolved CWL to {output.absolute()}...")

    with output.open("w", encoding="utf-8") as output_stream:
        dump_cwl(resolved_workflow, output_stream)

    logger.success(f"Resolved CWL successfully serialized to {output.absolute()}.")
