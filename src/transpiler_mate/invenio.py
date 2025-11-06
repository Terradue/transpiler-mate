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

from . import init_http_logging
from .metadata import (
    MetadataManager,
    Transpiler
)
from .metadata.software_application_models import (
    AuthorRole,
    ContributorRole,
    Organization,
    Person,
    Role as SWARole,
    SoftwareApplication
)
from datetime import date

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
from invenio_rest_api_client.models.role import Role
from invenio_rest_api_client.models.role_id import RoleId
from invenio_rest_api_client.models.update_draft_record import UpdateDraftRecord

from invenio_rest_api_client.api.drafts.publish_a_draft_record import sync as publish_a_draft_record

from invenio_rest_api_client.api.records_versions.create_a_new_version import sync as create_a_new_version

from invenio_rest_api_client.types import UNSET

from loguru import logger
from pathlib import Path
from pydantic import AnyUrl
from typing import (
    List,
    Mapping,
    Optional,
    Tuple
)
from urllib.parse import urlparse

import hashlib
import time
import os

__ROLES_MAPPING_: Mapping[AnyUrl, RoleId] = {
    AnyUrl('http://purl.org/spar/datacite/ContactPerson'): RoleId.CONTACTPERSON,
    AnyUrl('http://purl.org/spar/datacite/DataCollector'): RoleId.DATACOLLECTOR,
    AnyUrl('http://purl.org/spar/datacite/DataCurator'): RoleId.DATACURATOR,
    AnyUrl('http://purl.org/spar/datacite/DataManager'): RoleId.DATAMANAGER,
    AnyUrl('http://purl.org/spar/datacite/Distributor'): RoleId.DISTRIBUTOR,
    AnyUrl('http://purl.org/spar/datacite/Editor'): RoleId.EDITOR,
    AnyUrl('http://purl.org/spar/datacite/HostingInstitution'): RoleId.HOSTINGINSTITUTION,
    AnyUrl('http://purl.org/spar/datacite/Other'): RoleId.OTHER,
    AnyUrl('http://purl.org/spar/datacite/Producer'): RoleId.PRODUCER,
    AnyUrl('http://purl.org/spar/datacite/ProjectLeader'): RoleId.PROJECTLEADER,
    AnyUrl('http://purl.org/spar/datacite/ProjectManager'): RoleId.PROJECTMANAGER,
    AnyUrl('http://purl.org/spar/datacite/ProjectMember'): RoleId.PROJECTMEMBER,
    AnyUrl('http://purl.org/spar/datacite/RegistrationAgency'): RoleId.REGISTRATIONAGENCY,
    AnyUrl('http://purl.org/spar/datacite/RegistrationAuthority'): RoleId.REGISTRATIONAUTHORITY,
    AnyUrl('http://purl.org/spar/datacite/RelatedPerson'): RoleId.RELATEDPERSON,
    AnyUrl('http://purl.org/spar/datacite/Researcher'): RoleId.RESEARCHER,
    AnyUrl('http://purl.org/spar/datacite/ResearchGroup'): RoleId.RESEARCHGROUP,
    AnyUrl('http://purl.org/spar/datacite/RightsHolder'): RoleId.RIGHTSHOLDER,
    AnyUrl('http://purl.org/spar/datacite/Sponsor'): RoleId.SPONSOR,
    AnyUrl('http://purl.org/spar/datacite/Supervisor'): RoleId.SUPERVISOR,
    AnyUrl('http://purl.org/spar/datacite/WorkPackageLeader'): RoleId.WORKPACKAGELEADER,
}

def _md5(file: Path):
    hash_md5 = hashlib.md5()
    with file.open('rb') as f:
        for chunk in iter(lambda: f.read(4096), b''):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def _to_identifier(
    url_identifier: str | AnyUrl
) -> Identifier:
    _, netloc, path, _, _, _ = urlparse(str(url_identifier))
    return Identifier(
        scheme=PersonOrOrgIdentifierScheme(netloc.split('.')[0]),
        identifier=path.split('/')[-1]
    )

def _affiliation_identifier(
    url_identifier: str | AnyUrl
) -> str:
    _, _, path, _, _, _ = urlparse(str(url_identifier))
    return path.split('/')[-1]

def _to_creator(
    author: Person | SWARole
) -> Creator:
    role_id: RoleId = RoleId.OTHER

    if isinstance(author, SWARole):
        if author.additional_type:
            role_id = __ROLES_MAPPING_.get(author.additional_type, RoleId.OTHER)

        if isinstance(author, AuthorRole):
            author = author.author
        elif isinstance(author, ContributorRole):
            author = author.contributor

    creator: Creator = Creator(
        person_or_org=PersonOrOrg(
            type_=PersonOrOrgType.PERSONAL,
            name=f"{author.family_name}, {author.given_name}" if isinstance(author, Person) else UNSET,
            given_name=author.given_name if isinstance(author, Person) else UNSET,
            family_name=author.family_name if isinstance(author, Person) else UNSET,
            identifiers=[_to_identifier(author.identifier)] if isinstance(author, Person) and author.identifier else UNSET
        ),
        role=Role(
            id=role_id
        )
    )

    if isinstance(author, Person):
        creator.affiliations = []
        for affiliation in author.affiliation if isinstance(author.affiliation, list) else [author.affiliation]:
            creator.affiliations.append(
                Affiliation(
                    id=_affiliation_identifier(affiliation.identifier) if affiliation.identifier else UNSET,
                    name=affiliation.name
                )
            )

    return creator

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
            title=metadata_source.name,
            publication_date=date.fromtimestamp(time.time()),
            publisher=metadata_source.publisher.name,
            description=metadata_source.description if metadata_source.description else UNSET,
            creators=list(
                map(
                    _to_creator,
                    metadata_source.author if isinstance(metadata_source.author, list) else [metadata_source.author]
                )
            ),
            contributors=list(
                map(
                    _to_creator,
                    metadata_source.contributor if isinstance(metadata_source.contributor, list) else [metadata_source.contributor]
                )
            ) if metadata_source.contributor else UNSET,
            version=metadata_source.software_version
        )

    def _finalize(
        self,
        draft_id: str,
        uploading_files: List[Path],
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
            ) for file in uploading_files]
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
        source: Path,
        attach: Optional[Tuple[Path]] = None
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

            uploading_files = [source]
            if attach:
                for attach_item in attach:
                    uploading_files.append(attach_item)

            return self._finalize(
                draft_id=draft_id,
                uploading_files=uploading_files,
                session_client=invenio_rest_client,
                invenio_metadata=self.transpile(metadata)
            )
