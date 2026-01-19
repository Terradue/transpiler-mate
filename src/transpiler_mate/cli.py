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

from .metadata import (
    MetadataManager,
    Transpiler
)
from .markdown import markdown_transpile
from datetime import datetime
from enum import (
    auto,
    Enum
)
from functools import wraps
from loguru import logger
from pathlib import Path
from semver import Version
from typing import (
    Tuple,
    Optional
)

import click
import json
import time    

def _track(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()

        logger.info(f"Started at: {datetime.fromtimestamp(start_time).isoformat(timespec='milliseconds')}")

        try:
            func(*args, **kwargs)

            logger.success('------------------------------------------------------------------------')
            logger.success('SUCCESS')
            logger.success('------------------------------------------------------------------------')
        except Exception as e:
            logger.error('------------------------------------------------------------------------')
            logger.error('FAIL')
            logger.error(e)
            logger.error('------------------------------------------------------------------------')

        end_time = time.time()

        logger.info(f"Total time: {end_time - start_time:.4f} seconds")
        logger.info(f"Finished at: {datetime.fromtimestamp(end_time).isoformat(timespec='milliseconds')}")

    return wrapper

@click.group()
def main():
    pass

@main.command(context_settings={'show_default': True})
@click.argument(
    'source',
    type=click.Path(
        path_type=Path,
        exists=True,
        readable=True,
        resolve_path=True
    ),
    required=True
)
@click.option(
    '--base-url',
    type=click.STRING,
    required=True,
    help="The Invenio server base URL"
)
@click.option(
    '--auth-token',
    type=click.STRING,
    required=True,
    envvar='INVENIO_AUTH_TOKEN',
    help="The Invenio Access token"
)
@click.option(
    '--attach',
    type=click.Path(
        path_type=Path,
        exists=True,
        readable=True,
        resolve_path=True
    ),
    multiple=True
)
def invenio_publish(
    source: Path,
    base_url: str,
    auth_token: str,
    attach: Optional[Tuple[Path]]
):
    """
    Publishes the input CWL to an Invenio instance.
    """
    metadata_manager: MetadataManager = MetadataManager(source)

    logger.info(f"Interacting with Invenio server at {base_url})")

    from .invenio import InvenioMetadataTranspiler
    invenio_transpiler: InvenioMetadataTranspiler = InvenioMetadataTranspiler(
        metadata_manager=metadata_manager,
        invenio_base_url=base_url,
        auth_token=auth_token
    )

    record_url = invenio_transpiler.create_or_update_process(
        source=source,
        attach=attach
    )

    logger.success(f"Record available on '{record_url}'")

def _transpile(
    source: Path,
    transpiler: Transpiler,
    output: Path
):
    logger.info(f"Reading metadata from {source}...")
    metadata_manager: MetadataManager = MetadataManager(source)

    logger.success(f"Metadata successfully read!")
    logger.info('Transpiling metadata...')
    data = transpiler.transpile(metadata_manager.metadata)

    logger.success(f"Metadata successfully transpiled!")
    logger.info('Serializing metadata...')
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open('w') as output_stream:
        json.dump(
            data,
            output_stream,
            indent=2
        )
    
    logger.success(f"Metadata successfully serialized to {output}.")

@main.command(context_settings={'show_default': True})
@click.argument(
    'source',
    type=click.Path(
        path_type=Path,
        exists=True,
        readable=True,
        resolve_path=True
    ),
    required=True
)
@click.option(
    '--code-repository',
    required=False,
    help="The (SVN, GitHub, CodePlex, ...) code repository URL"
)
@click.option(
    '--output',
    type=click.Path(path_type=Path),
    required=False,
    default='codemeta.json',
    help="The output file path"
)
def codemeta(
    source: Path,
    code_repository: str | None,
    output: Path
):
    """
    Transpiles the input CWL to CodeMeta representation.
    """
    from .codemeta import CodeMetaTranspiler
    transpiler: CodeMetaTranspiler = CodeMetaTranspiler(code_repository)

    _transpile(
        source=source,
        transpiler=transpiler,
        output=output
    )

@main.command(context_settings={'show_default': True})
@click.argument(
    'source',
    type=click.Path(
        path_type=Path,
        exists=True,
        readable=True,
        resolve_path=True
    ),
    required=True
)
@click.option(
    '--output',
    type=click.Path(path_type=Path),
    required=False,
    default='record.json',
    help="The output file path"
)
def ogcrecord(
    source: Path,
    output: Path
):
    """
    Transpiles the input CWL to OGC API Record.
    """
    from .ogcapi_records import OgcRecordsTranspiler
    transpiler = OgcRecordsTranspiler()

    _transpile(
        source=source,
        transpiler=transpiler,
        output=output
    )

@main.command(context_settings={'show_default': True})
@click.argument(
    'source',
    type=click.Path(
        path_type=Path,
        exists=True,
        readable=True,
        resolve_path=True
    ),
    required=True
)
@click.option(
    '--output',
    type=click.Path(path_type=Path),
    required=False,
    default='datacite.json',
    help="The output file path"
)
def datacite(
    source: Path,
    output: Path
):
    """
    Transpiles the input CWL to DataCite Metadata.
    """
    from .datacite import DataCiteTranspiler
    transpiler = DataCiteTranspiler()

    _transpile(
        source=source,
        transpiler=transpiler,
        output=output
    )

@main.command(context_settings={'show_default': True})
@click.argument(
    'source',
    type=click.Path(
        path_type=Path,
        exists=True,
        readable=True,
        resolve_path=True
    ),
    required=True
)
@click.option(
    '--workflow-id',
    required=True,
    type=click.STRING,
    default="main",
    help="ID of the main Workflow"
)
@click.option(
    '--output',
    type=click.Path(path_type=Path),
    required=False,
    default='.',
    help="The output directory path"
)
@click.option(
    '--code-repository',
    required=False,
    help="The (SVN, GitHub, CodePlex, ...) code repository URL"
)
def markdown(
    source: Path,
    workflow_id: str,
    output: Path,
    code_repository: str | None
):
    """
    Transpiles the input CWL to Markdown documentation.
    """
    output.mkdir(parents=True, exist_ok=True)

    target: Path = Path(output, f"{workflow_id}.md")

    logger.info(f"Rendering Markdown documentation of {source} to {target}...")

    with target.open("w") as output_stream:
        markdown_transpile(
            source,
            workflow_id,
            output_stream,
            code_repository
        )

    logger.info(f"Markdown documentation successfully serialized to {target}!")


class VersionPart(Enum):
    MAJOR = auto()
    MINOR = auto()
    PATCH = auto()
    BUILD = auto()
    PRE_RELEASE = auto()

@main.command(context_settings={'show_default': True})
@click.argument(
    'source',
    type=click.Path(
        path_type=Path,
        exists=True,
        readable=True,
        resolve_path=True
    ),
    required=True
)
@click.option(
    '--version-part',
    type=click.Choice(
        VersionPart,
        case_sensitive=False
    ),
    required=False,
    default=VersionPart.MINOR,
    help="The version part to update"
)
def bump_version(
    source: Path,
    version_part: VersionPart
):
    """
    Bumps the CWL SW version via SemVer Spec 2.0.0.
    """
    logger.info(f"Reading metadata from {source}...")
    metadata_manager: MetadataManager = MetadataManager(source)

    version = Version.parse(metadata_manager.metadata.software_version)

    if not version.is_valid:
        raise ValueError(f"Version {metadata_manager.metadata.software_version} is not compliant to the Semantic Versioning Specification 2.0.0, see https://semver.org/")

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
            raise ValueError(f"It's not you, it is us: {version_part} unsupported, but it shouldn't have been happened...")

    logger.success(f"Software Version {metadata_manager.metadata.software_version} updated to {bumped_version}")

    metadata_manager.metadata.software_version = str(bumped_version)

    metadata_manager.update()

for command in [bump_version, codemeta, datacite, invenio_publish, ogcrecord, ]:
    command.callback = _track(command.callback)
