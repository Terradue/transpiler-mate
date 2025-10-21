# Transpiler Mate (c) 2025
# 
# Transpiler Mate is licensed under
# Creative Commons Attribution-ShareAlike 4.0 International.
# 
# You should have received a copy of the license along with this work.
# If not, see <https://creativecommons.org/licenses/by-sa/4.0/>.

from . import init_http_logging
from .metadata import (
    MetadataManager,
    Transpiler
)
from .metadata.software_application_models import (
    Organization,
    Person,
    PropertyValue,
    SoftwareApplication
)
from collections.abc import Iterable

# required when a DOI is not assigned to an applicatrion package
from invenio_rest_api_client.client import AuthenticatedClient as InvenioClient
from invenio_rest_api_client.api.drafts.reserve_a_doi import sync as reserve_a_doi

from invenio_rest_api_client.api.records.create_a_draft_record import sync as create_a_draft_record
from invenio_rest_api_client.models.create_a_draft_record_body import CreateADraftRecordBody
from invenio_rest_api_client.models.created import Created

from invenio_rest_api_client.api.drafts_files_upload.step_1_start_draft_file_uploads import sync as step_1_start_draft_file_uploads
from invenio_rest_api_client.models.file_transfer_item import FileTransferItem

from invenio_rest_api_client.api.drafts_files_upload.step_2_upload_a_draft_files_content import sync as step_2_upload_a_draft_files_content
from invenio_rest_api_client.types import File as FileContent

from invenio_rest_api_client.api.drafts_files_upload.step_3_complete_a_draft_file_upload import sync as step_3_complete_a_draft_file_upload

from invenio_rest_api_client.api.drafts.update_a_draft_record import sync as update_a_draft_record
from invenio_rest_api_client.models.access import Access
from invenio_rest_api_client.models.access_files import AccessFiles
from invenio_rest_api_client.models.access_record import AccessRecord
from invenio_rest_api_client.models.affiliation import Affiliation
from invenio_rest_api_client.models.creator import Creator
from invenio_rest_api_client.models.files import Files
from invenio_rest_api_client.models.identifier import Identifier
from invenio_rest_api_client.models.person_or_org_identifier_scheme import PersonOrOrgIdentifierScheme
from invenio_rest_api_client.models.metadata import Metadata
from invenio_rest_api_client.models.person_or_org import PersonOrOrg
from invenio_rest_api_client.models.person_or_org_type import PersonOrOrgType
from invenio_rest_api_client.models.resource_type import ResourceType
from invenio_rest_api_client.models.resource_type_id import ResourceTypeId
from invenio_rest_api_client.models.update_draft_record import UpdateDraftRecord

from invenio_rest_api_client.api.drafts.publish_a_draft_record import sync as publish_a_draft_record

from invenio_rest_api_client.api.records_versions.create_a_new_version import sync as create_a_new_version

from invenio_rest_api_client.types import UNSET

from loguru import logger
from pathlib import Path
from pydantic import AnyUrl
from shutil import copy2 as copy_file
from typing import Sequence

import hashlib
import os

def _md5(file: Path):
    hash_md5 = hashlib.md5()
    with file.open('rb') as f:
        for chunk in iter(lambda: f.read(4096), b''):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def _to_creator(
    author: Person | Organization
) -> Creator:
    return Creator(
        person_or_org=PersonOrOrg(
            type_=PersonOrOrgType.PERSONAL if isinstance(author, Person) else PersonOrOrgType.ORGANIZATIONAL,
            name=f"{author.family_name}, {author.given_name}" if isinstance(author, Person) else author.name if isinstance(author, Organization) else UNSET, # type: ignore
            given_name=author.given_name if isinstance(author, Person) else UNSET, # type: ignore
            family_name=author.family_name if isinstance(author, Person) else UNSET, # type: ignore
            identifiers=[
               Identifier(
                    scheme=PersonOrOrgIdentifierScheme(str(author.identifier.property_id).lower()), # type: ignore
                    identifier=str(author.identifier.value_reference) # type: ignore
                )
            ] if isinstance(author, Person) and author.identifier and isinstance(author.identifier, PropertyValue) else UNSET
        ),
        affiliations=[Affiliation(
            id=str(author.affiliation.identifier) if author.affiliation.identifier else UNSET,
            name=author.affiliation.name if isinstance(author.affiliation, Organization) else UNSET, # type: ignore
        )] if isinstance(author, Person) and author.affiliation else UNSET
    )

class InvenioMetadataTranspiler(Transpiler):

    def __init__(
        self,
        metadata_manager: MetadataManager,
        invenio_base_url: str,
        auth_token: str
    ):
        self.metadata_manager = metadata_manager
        
        self.invenio_base_url = invenio_base_url
        self.invenio_client: InvenioClient = InvenioClient(
            base_url=invenio_base_url,
            token=auth_token
        )

        logger.debug('Setting up the HTTP logger...')
        init_http_logging(self.invenio_client.get_httpx_client())
        logger.debug('HTTP logger correctly setup')        

    def transpile(
        self,
        metadata_source: SoftwareApplication
    ) -> Metadata:
        return Metadata(
            resource_type=ResourceType(
                id=ResourceTypeId.WORKFLOW
            ),
            title=str(metadata_source.headline),
            publication_date=metadata_source.date_published, # type: ignore
            publisher=metadata_source.publisher.name, # type: ignore
            description=metadata_source.about.description, # type: ignore
            creators=list(
                map(
                    _to_creator,
                    metadata_source.author if isinstance(metadata_source.author, Iterable) else [metadata_source.author] # type: ignore
                )
            ),
            version=metadata_source.software_version # type: ignore
        )

    def _finalize(
        self,
        draft_id: str,
        uploading_files: Sequence[Path],
        session_client: InvenioClient,
        invenio_metadata: Metadata
    ) -> str:
        uploading_files_names = ', '.join([file.name for file in uploading_files])
        logger.info(f"Drafting file upload [{uploading_files_names}] to Record '{draft_id}'...")

        step_1_start_draft_file_uploads(
            draft_id=draft_id,
            client=session_client,
            body=[FileTransferItem(
                key=file.name,
                size=file.stat().st_size,
                checksum=f"md5:{_md5(file)}"
            ) for file in uploading_files ]
        )

        logger.success(f"File upload {uploading_files_names} drafted to Record '{draft_id}'")

        for file in uploading_files:
            logger.info(f"Uploading file content '{file.name})' to Record '{draft_id}'...")

            with file.open('rb') as binary_stream:
                step_2_upload_a_draft_files_content(
                    draft_id=draft_id,
                    file_name=file.name,
                    body=FileContent(
                        file_name=file.name,
                        mime_type='application/octet-stream',
                        payload=binary_stream
                    ),
                    client=session_client
                )

            logger.success(f"File content {file.name} uploaded to Record {draft_id}")

            logger.info(f"Completing file upload {file.name}] to Record '{draft_id}'...")

            step_3_complete_a_draft_file_upload(
                draft_id=draft_id,
                file_name=file.name,
                client=session_client
            )

            logger.success(f"File upload {file.name} to Record '{draft_id}' completed")

        update_a_draft_record(
            draft_id=draft_id,
            body=UpdateDraftRecord(
                access=Access(
                    files=AccessFiles.PUBLIC,
                    record=AccessRecord.PUBLIC
                ),
                files=Files(
                    enabled=True
                ),
                metadata=invenio_metadata
            ),
            client=session_client
        )

        logger.success(f"Draft Record '{draft_id}' metadata updated!")

        logger.info(f"Publishing the Draft Record '{draft_id}'...")

        publish_a_draft_record(
            draft_id=draft_id,
            client=session_client
        )

        logger.success(f"Draft Record '{draft_id}' metadata updated!")

        return f"{self.invenio_base_url}/records/{draft_id}"

    def create_or_update_process(
        self,
        source: Path
    ) -> str:
        metadata: SoftwareApplication = self.metadata_manager.metadata

        with self.invenio_client as invenio_rest_client:
            draft_id: str = ''

            if not metadata.identifier:
                logger.warning("'identifier' key not found in source document, reserving a DOI...")

                draft_record = create_a_draft_record(
                    client=invenio_rest_client,
                    body=CreateADraftRecordBody()
                )

                draft_id = draft_record.id if draft_record and isinstance(draft_record, Created) else draft_record.to_dict()['id'] if draft_record else '' # type: ignore
                
                logger.success(f"Successfully reserved a draft record with ID: {draft_id}")

                doi = reserve_a_doi(
                    draft_id=draft_id,
                    client=invenio_rest_client
                )

                doi_dict = doi.to_dict()  # type: ignore
                doi = doi_dict['doi']
                doi_url = doi_dict['doi_url']
                logger.success(f"Successfully reserved a DOI with ID {doi} (URL: {doi_url})")

                metadata.identifier = doi
                metadata.same_as = AnyUrl(doi_url)

                self.metadata_manager.update()
            else:
                logger.info(f"Identifier {metadata.identifier} already assigned to {source}")

                record_id = metadata.identifier.split('.')[-1] # type: ignore

                logger.info(f"Creating a new version for already existing Record {record_id}")

                version = create_a_new_version(
                    record_id=record_id,
                    client=invenio_rest_client
                )

                draft_id = version.to_dict()['id'] # type: ignore

                logger.info(f"New version {draft_id} for already existing Record {record_id} created!")

            # Split the file name and extension
            base_name, extension = os.path.splitext(source.name)
            # Retrieve the version
            version = metadata.software_version
            # Construct the new file name by appending "_edited"
            new_file_name = f"{base_name}_v{version}{extension}"
            target = Path(source.parent, new_file_name)
            copy_file(
                src=source.absolute(),
                dst=target.absolute()
            )

            codemeta_file = Path(source.parent, 'codemeta.json')
            with codemeta_file.open('w') as output_stream:
                self.metadata_manager.save_as_codemeta(output_stream)

            return self._finalize(
                draft_id=draft_id,
                uploading_files=[target, codemeta_file],
                session_client=invenio_rest_client,
                invenio_metadata=self.transpile(metadata)
            )
