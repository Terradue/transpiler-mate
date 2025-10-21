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
from .invenio import InvenioMetadataTranspiler

from loguru import logger
from pathlib import Path
from pydantic import AnyUrl

import click
import time

@click.command()
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
    '--dry-run',
    type=click.BOOL,
    is_flag=True,
    default=False,
    help="Picks the Zenodo sandbox server"
)
@click.option(
    '--auth-token',
    type=click.STRING,
    required=True,
    help="The Zenodo Access token, see https://(sandbox.)zenodo.org/account/settings/applications/tokens"
)
def main(
    source: Path,
    dry_run: bool,
    auth_token: str
):
    start_time = time.time()

    logger.info(f"Started at: {datetime.fromtimestamp(start_time).isoformat(timespec='milliseconds')}")

    metadata_manager: MetadataManager = MetadataManager(source)

    metadata: SoftwareApplication = metadata_manager.metadata
    metadata.date_published = date.fromtimestamp(start_time)
    metadata_manager.update()

    zenodo_base_url = f"https://{'sandbox.' if dry_run else ''}zenodo.org"
    logger.info(f"Interacting with Invenio server at {zenodo_base_url})")

    invenio_transpiler: InvenioMetadataTranspiler = InvenioMetadataTranspiler(
        metadata_manager=metadata_manager,
        invenio_base_url=zenodo_base_url,
        auth_token=auth_token
    )

    record_url = invenio_transpiler.create_or_update_process(source)

    end_time = time.time()

    logger.success(f"Record available on '{record_url}'")

    logger.info('------------------------------------------------------------------------')
    logger.success('BUILD SUCCESS')
    logger.info('------------------------------------------------------------------------')

    logger.info(f"Total time: {end_time - start_time:.4f} seconds")
    logger.info(f"Finished at: {datetime.fromtimestamp(end_time).isoformat(timespec='milliseconds')}")
