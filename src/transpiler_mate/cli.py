# Transpiler Mate (c) 2025
# 
# Transpiler Mate is licensed under
# Creative Commons Attribution-ShareAlike 4.0 International.
# 
# You should have received a copy of the license along with this work.
# If not, see <https://creativecommons.org/licenses/by-sa/4.0/>.

from .metadata import MetadataManager
from .metadata.software_application_models import SoftwareApplication
from datetime import datetime
from functools import wraps
from loguru import logger
from pathlib import Path
from typing import (
    Any,
    List,
    Mapping,
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

@click.group
def main():
    pass

@main.command()
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

def _dump_json(
    obj: Mapping[str, Any],
    target: Path
):
    with target.open('w') as output_stream:
        json.dump(
            obj,
            output_stream,
            indent=2
        )
    
    logger.info(f"Metadata successfully traspiled to {target}.")

@main.command
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
def codemeta(
    source: Path
):
    """
    Transpiles the input CWL to CodeMeta representation.
    """
    metadata_manager: MetadataManager = MetadataManager(source)

    _dump_json(
        obj=metadata_manager.metadata.to_jsonld(),
        target=Path(source.parent, 'codemeta.json')
    )

@main.command
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
def ogcrecord(
    source: Path
):
    """
    Transpiles the input CWL to OGC API Record.
    """
    metadata_manager: MetadataManager = MetadataManager(source)
    from .ogc_record import OgcRecordsTranspiler
    ogc_record = OgcRecordsTranspiler().transpile(metadata_manager.metadata)

    _dump_json(
        obj=ogc_record.to_dict(),
        target=Path(source.parent, 'record.json')
    )

for command in [codemeta, invenio_publish, ogcrecord]:
    command.callback = _track(command.callback)
