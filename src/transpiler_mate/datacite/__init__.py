# Transpiler Mate (c) 2025
# 
# Transpiler Mate is licensed under
# Creative Commons Attribution-ShareAlike 4.0 International.
# 
# You should have received a copy of the license along with this work.
# If not, see <https://creativecommons.org/licenses/by-sa/4.0/>.

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
    CreativeWork,
    Organization,
    Person,
    SoftwareApplication
)
from datetime import date
from typing import (
    Any,
    Mapping
)
from urllib.parse import urlparse

import time

def _to_contributor(
    author: Person
) -> Contributor:
    contributor: Contributor = Contributor(
        contributor_type=ContributorType.OTHER,
        name_type=NameType.PERSONAL,
        name=f"{author.family_name}, {author.given_name}" if isinstance(author, Person) else author.name,
        given_name=author.given_name if isinstance(author, Person) else None,
        family_name=author.family_name if isinstance(author, Person) else None,
    )

    _finalize(
        author=author,
        creator=contributor
    )

    return contributor

def _to_creator(
    author: Person | Organization
) -> Creator:
    creator: Creator = Creator(
        name_type=NameType.ORGANIZATIONAL if isinstance(author, Organization) else NameType.PERSONAL,
        name=f"{author.family_name}, {author.given_name}" if isinstance(author, Person) else author.name,
        given_name=author.given_name if isinstance(author, Person) else None,
        family_name=author.family_name if isinstance(author, Person) else None,
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
            )],
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
