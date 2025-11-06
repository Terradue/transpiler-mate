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

from .datacite_4_6_models import (
    Affiliation,
    Creator,
    Contributor,
    ContributorType,
    DataCiteAttributes,
    Date,
    DateType,
    Description,
    DescriptionType,
    Identifier,
    NameIdentifier,
    NameType,
    Publisher,
    RelatedIdentifier,
    RelatedIdentifierType,
    RelationType,
    ResourceType,
    ResourceTypeGeneral,
    Right,
    Title
)
from ..metadata import Transpiler
from ..metadata.software_application_models import (
    AuthorRole,
    CreativeWork,
    Organization,
    Person,
    ContributorRole,
    SoftwareApplication
)
from datetime import date
from pydantic import AnyUrl
from typing import (
    Any,
    Mapping
)
from urllib.parse import urlparse

import time
import uuid

__ROLES_MAPPING_: Mapping[AnyUrl, ContributorType] = {
    AnyUrl('http://purl.org/spar/datacite/ContactPerson'): ContributorType.CONTACT_PERSON,
    AnyUrl('http://purl.org/spar/datacite/DataCollector'): ContributorType.DATA_COLLECTOR,
    AnyUrl('http://purl.org/spar/datacite/DataCurator'): ContributorType.DATA_CURATOR,
    AnyUrl('http://purl.org/spar/datacite/DataManager'): ContributorType.DATA_MANAGER,
    AnyUrl('http://purl.org/spar/datacite/Distributor'): ContributorType.DISTRIBUTOR,
    AnyUrl('http://purl.org/spar/datacite/Editor'): ContributorType.EDITOR,
    AnyUrl('http://purl.org/spar/datacite/HostingInstitution'): ContributorType.HOSTING_INSTITUTION,
    AnyUrl('http://purl.org/spar/datacite/Other'): ContributorType.OTHER,
    AnyUrl('http://purl.org/spar/datacite/Producer'): ContributorType.PRODUCER,
    AnyUrl('http://purl.org/spar/datacite/ProjectLeader'): ContributorType.PROJECT_LEADER,
    AnyUrl('http://purl.org/spar/datacite/ProjectManager'): ContributorType.PROJECT_MANAGER,
    AnyUrl('http://purl.org/spar/datacite/ProjectMember'): ContributorType.PROJECT_MEMBER,
    AnyUrl('http://purl.org/spar/datacite/RegistrationAgency'): ContributorType.REGISTRATION_AGENCY,
    AnyUrl('http://purl.org/spar/datacite/RegistrationAuthority'): ContributorType.REGISTRATION_AUTHORITY,
    AnyUrl('http://purl.org/spar/datacite/RelatedPerson'): ContributorType.RELATED_PERSON,
    AnyUrl('http://purl.org/spar/datacite/Researcher'): ContributorType.RESEARCHER,
    AnyUrl('http://purl.org/spar/datacite/ResearchGroup'): ContributorType.RESEARCH_GROUP,
    AnyUrl('http://purl.org/spar/datacite/RightsHolder'): ContributorType.RIGHTS_HOLDER,
    AnyUrl('http://purl.org/spar/datacite/Sponsor'): ContributorType.SPONSOR,
    AnyUrl('http://purl.org/spar/datacite/Supervisor'): ContributorType.SUPERVISOR,
    AnyUrl('http://purl.org/spar/datacite/Translator'): ContributorType.TRANSLATOR,
    AnyUrl('http://purl.org/spar/datacite/WorkPackageLeader'): ContributorType.WORK_PACKAGE_LEADER,
}

def _to_contributor(
    author: Person | ContributorRole
) -> Contributor:
    contributor_type=ContributorType.OTHER

    if isinstance(author, ContributorRole):
        if author.additional_type:
            contributor_type = __ROLES_MAPPING_.get(author.additional_type, ContributorType.OTHER)

        author = author.contributor

    contributor: Contributor = Contributor(
        contributor_type=contributor_type,
        name_type=NameType.PERSONAL,
        name=f"{author.family_name}, {author.given_name}",
        given_name=author.given_name,
        family_name=author.family_name,
    )

    _finalize(
        author=author,
        creator=contributor
    )

    return contributor

def _to_creator(
    author: Person | AuthorRole
) -> Creator:
    if isinstance(author, AuthorRole):
        author = author.author

    creator: Creator = Creator(
        name_type=NameType.PERSONAL,
        name=f"{author.family_name}, {author.given_name}",
        given_name=author.given_name,
        family_name=author.family_name,
    )

    _finalize(
        author=author,
        creator=creator
    )

    return creator

def _finalize(
    author: Person | Organization,
    creator: Creator
):
    if author.identifier:
        creator.name_identifiers = []
        for identifier in author.identifier if isinstance(author.identifier, list) else [author.identifier]:
            scheme, netloc, _, _, _, _ = urlparse(str(identifier))
            creator.name_identifiers.append(
                NameIdentifier(
                    name_identifier=str(identifier),
                    name_identifier_scheme=netloc.split('.')[0].upper(),
                    scheme_uri=f"{scheme}://{netloc}"
                )
            )

    if isinstance(author, Person):
        creator.affiliation = []
        for affiliation in author.affiliation if isinstance(author.affiliation, list) else [author.affiliation]:
            if affiliation.identifier:
                for identifier in affiliation.identifier if isinstance(affiliation.identifier, list) else [affiliation.identifier]:
                    scheme, netloc, _, _, _, _ = urlparse(str(identifier))
                    creator.affiliation.append(
                        Affiliation(
                            affiliation_identifier=str(identifier),
                            affiliation_identifier_scheme=netloc.split('.')[0].upper(),
                            scheme_uri=f"{scheme}://{netloc}"
                        )
                    )

class DataCiteTranspiler(Transpiler):

    def transpile(
        self,
        metadata_source: SoftwareApplication
    ) -> Mapping[str, Any]:
        return DataCiteAttributes(
            doi=metadata_source.identifier,
            types=ResourceType(
                resource_type=metadata_source.name,
                resourceTypeGeneral=ResourceTypeGeneral.SOFTWARE
            ),
            identifiers=[Identifier(
                identifier_type='DOI',
                identifier=metadata_source.identifier
            ) if metadata_source.identifier else Identifier(
                identifier_type='URN',
                identifier=f"urn:uuid:{uuid.uuid4()}"
            )], # supply a fake required identifier if the DOI hasn't been associated yet
            related_identifiers=[RelatedIdentifier(
                related_identifier=str(metadata_source.same_as),
                related_identifier_type=RelatedIdentifierType.DOI,
                relation_type=RelationType.IS_IDENTICAL_TO,
                resource_type_general=ResourceTypeGeneral.SOFTWARE
            )] if metadata_source.same_as else [],
            titles=[Title(
               title= metadata_source.name
            )],
            descriptions=[Description(
                description=metadata_source.description,
                description_type=DescriptionType.TECHNICAL_INFO
            )],
            publisher=Publisher(
                name=metadata_source.publisher.name
            ),
            publication_year=metadata_source.date_created.year,
            dates=[Date(
                date=date.fromtimestamp(time.time()),
                date_type=DateType.UPDATED,
                date_information='New version release'
            )],
            rights=[Right(
                rights=metadata_source.license.name if isinstance(metadata_source.license, CreativeWork) else None,
                rights_uri=metadata_source.license.url if isinstance(metadata_source.license, CreativeWork) else None,
                rights_identifier=metadata_source.license.identifier if isinstance(metadata_source.license, CreativeWork) else None,
                rights_identifier_scheme='SPDX'
            )],
            creators=list(
                map(
                    _to_creator,
                    metadata_source.author if isinstance(metadata_source.author, list) else [metadata_source.author]
                )
            ),
            contributors=list(
                map(
                    _to_contributor,
                    metadata_source.contributor if isinstance(metadata_source.contributor, list) else [metadata_source.contributor]
                )
            ) if metadata_source.contributor else None
        ).model_dump(exclude_none=True, by_alias=True)
