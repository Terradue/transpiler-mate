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

from pathlib import Path
from typing import Optional

import click

from transpiler_mate.markdown import markdown_transpile
from transpiler_mate.metadata import MetadataManager, Transpiler

__path__ = [str(Path(__file__).with_suffix(""))]

from transpiler_mate.cli.bump_version import VersionPart, run as run_bump_version
from transpiler_mate.cli.codemeta import run as run_codemeta
from transpiler_mate.cli.common import track as _track
from transpiler_mate.cli.common import transpile as run_transpile
from transpiler_mate.cli.datacite import run as run_datacite
from transpiler_mate.cli.invenio_publish import run as run_invenio_publish
from transpiler_mate.cli.markdown import run as run_markdown
from transpiler_mate.cli.oci_annotations import run as run_oci_annotations
from transpiler_mate.cli.ogcprocesses import run as run_ogcprocesses
from transpiler_mate.cli.ogcrecord import run as run_ogcrecord


def _transpile(source: Path, transpiler: Transpiler, output: Path):
    return run_transpile(
        source=source,
        transpiler=transpiler,
        output=output,
        metadata_manager_factory=MetadataManager,
    )


@click.group()
def main():
    pass


@main.command(context_settings={"show_default": True})
@click.argument(
    "source",
    type=click.Path(path_type=Path, exists=True, readable=True, resolve_path=True),
    required=True,
)
@click.option(
    "--base-url", type=click.STRING, required=True, help="The Invenio server base URL"
)
@click.option(
    "--auth-token",
    type=click.STRING,
    required=True,
    envvar="INVENIO_AUTH_TOKEN",
    help="The Invenio Access token",
)
@click.option(
    "--attach",
    type=click.Path(path_type=Path, exists=True, readable=True, resolve_path=True),
    multiple=True,
)
def invenio_publish(
    source: Path, base_url: str, auth_token: str, attach: Optional[tuple[Path, ...]]
):
    """
    Publishes the input CWL to an Invenio instance.
    """
    return run_invenio_publish(
        source=source,
        base_url=base_url,
        auth_token=auth_token,
        attach=attach,
        metadata_manager_factory=MetadataManager,
    )


@main.command(context_settings={"show_default": True})
@click.argument(
    "source",
    type=click.Path(path_type=Path, exists=True, readable=True, resolve_path=True),
    required=True,
)
@click.option(
    "--workflow-id", required=True, type=click.STRING, help="ID of the main Workflow"
)
@click.option(
    "--image-source",
    required=False,
    default=None,
    type=click.STRING,
    help="URL to get source code for building the image",
)
@click.option(
    "--image-revision",
    required=False,
    default=None,
    type=click.STRING,
    help="Source control revision identifier for the packaged software",
)
@click.option(
    "--output",
    type=click.Path(path_type=Path),
    required=False,
    default="annotations.json",
    help="The output file path",
)
def oci_annotations(
    source: Path,
    workflow_id: str,
    image_source: str | None,
    image_revision: str | None,
    output: Path,
):
    """
    Transpiles the input CWL to OCI annotations.
    """
    return run_oci_annotations(
        source=source,
        workflow_id=workflow_id,
        image_source=image_source,
        image_revision=image_revision,
        output=output,
        metadata_manager_factory=MetadataManager,
    )


@main.command(context_settings={"show_default": True})
@click.argument(
    "source",
    type=click.Path(path_type=Path, exists=True, readable=True, resolve_path=True),
    required=True,
)
@click.option(
    "--code-repository",
    required=False,
    help="The (SVN, GitHub, CodePlex, ...) code repository URL",
)
@click.option(
    "--output",
    type=click.Path(path_type=Path),
    required=False,
    default="codemeta.json",
    help="The output file path",
)
def codemeta(source: Path, code_repository: str | None, output: Path):
    """
    Transpiles the input CWL to CodeMeta representation.
    """
    return run_codemeta(
        source=source,
        code_repository=code_repository,
        output=output,
        transpile=_transpile,
    )


@main.command(context_settings={"show_default": True})
@click.argument(
    "source",
    type=click.Path(path_type=Path, exists=True, readable=True, resolve_path=True),
    required=True,
)
@click.option(
    "--output",
    type=click.Path(path_type=Path),
    required=False,
    default="record.json",
    help="The output file path",
)
def ogcrecord(source: Path, output: Path):
    """
    Transpiles the input CWL to OGC API Record.
    """
    return run_ogcrecord(source=source, output=output, transpile=_transpile)


@main.command(context_settings={"show_default": True})
@click.argument(
    "source",
    type=click.Path(path_type=Path, exists=True, readable=True, resolve_path=True),
    required=True,
)
@click.option(
    "--output",
    type=click.Path(path_type=Path),
    required=False,
    default="processes.json",
    help="The output file path",
)
def ogcprocesses(source: Path, output: Path):
    """
    Transpiles the input CWL to OGC API Processes.
    """
    return run_ogcprocesses(
        source=source,
        output=output,
        metadata_manager_factory=MetadataManager,
    )


@main.command(context_settings={"show_default": True})
@click.argument(
    "source",
    type=click.Path(path_type=Path, exists=True, readable=True, resolve_path=True),
    required=True,
)
@click.option(
    "--output",
    type=click.Path(path_type=Path),
    required=False,
    default="datacite.json",
    help="The output file path",
)
def datacite(source: Path, output: Path):
    """
    Transpiles the input CWL to DataCite Metadata.
    """
    return run_datacite(source=source, output=output, transpile=_transpile)


@main.command(context_settings={"show_default": True})
@click.argument(
    "source",
    type=click.Path(path_type=Path, exists=True, readable=True, resolve_path=True),
    required=True,
)
@click.option(
    "--workflow-id",
    required=True,
    type=click.STRING,
    default="main",
    help="ID of the main Workflow",
)
@click.option(
    "--output",
    type=click.Path(path_type=Path),
    required=False,
    default=".",
    help="The output directory path",
)
@click.option(
    "--code-repository",
    required=False,
    help="The (SVN, GitHub, CodePlex, ...) code repository URL",
)
def markdown(source: Path, workflow_id: str, output: Path, code_repository: str | None):
    """
    Transpiles the input CWL to Markdown documentation.
    """
    return run_markdown(
        source=source,
        workflow_id=workflow_id,
        output=output,
        code_repository=code_repository,
        markdown_transpile_fn=markdown_transpile,
    )


@main.command(context_settings={"show_default": True})
@click.argument(
    "source",
    type=click.Path(path_type=Path, exists=True, readable=True, resolve_path=True),
    required=True,
)
@click.option(
    "--version-part",
    type=click.Choice(VersionPart, case_sensitive=False),
    required=False,
    default=VersionPart.MINOR,
    help="The version part to update",
)
def bump_version(source: Path, version_part: VersionPart):
    """
    Bumps the CWL SW version via SemVer Spec 2.0.0.
    """
    return run_bump_version(
        source=source,
        version_part=version_part,
        metadata_manager_factory=MetadataManager,
    )


for command in [
    bump_version,
    codemeta,
    datacite,
    invenio_publish,
    ogcrecord,
    ogcprocesses,
    oci_annotations,
]:
    if command.callback is not None:
        command.callback = _track(command.callback)
