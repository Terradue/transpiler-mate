# Transpiler Mate (c) 2025
# 
# Transpiler Mate is licensed under
# Creative Commons Attribution-ShareAlike 4.0 International.
# 
# You should have received a copy of the license along with this work.
# If not, see <https://creativecommons.org/licenses/by-sa/4.0/>.

from .metadata import MetadataManager
from .metadata.software_application_models import SoftwareApplication
from datetime import (
    date,
    datetime
)
from functools import wraps
from loguru import logger
from pathlib import Path
from pydantic import AnyUrl

import click
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
def invenio_publish(
    source: Path,
    invenio_base_url: str,
    auth_token: str
):
    metadata_manager: MetadataManager = MetadataManager(source)

    metadata: SoftwareApplication = metadata_manager.metadata
    metadata.date_published = date.fromtimestamp(time.time())
    metadata_manager.update()

    logger.info(f"Interacting with Invenio server at {invenio_base_url})")

    from .invenio import InvenioMetadataTranspiler
    invenio_transpiler: InvenioMetadataTranspiler = InvenioMetadataTranspiler(
        metadata_manager=metadata_manager,
        invenio_base_url=invenio_base_url,
        auth_token=auth_token
    )

    record_url = invenio_transpiler.create_or_update_process(source)

    logger.success(f"Record available on '{record_url}'")

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
def ogcrecord_transpile(
    source: Path
):
    metadata_manager: MetadataManager = MetadataManager(source)
    from .ogc_record import OgcRecordsTranspiler
    ogc_record = OgcRecordsTranspiler().transpile(metadata_manager.metadata)

    import json
    import sys
    json.dump(
        ogc_record.to_dict(),
        sys.stdout,
        indent=2
    )

for command in [invenio_publish, ogcrecord_transpile]:
    command.callback = _track(command.callback)
