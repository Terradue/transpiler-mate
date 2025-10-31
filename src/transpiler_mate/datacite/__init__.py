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
    DataCiteAttributes,
    Date,
    DateType,
    Description,
    DescriptionType,
    Identifier,
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
from collections.abc import Iterable
from datetime import date
from typing import (
    Any,
    Mapping
)

import time

def _to_creator(
    author: Person | Organization
) -> Creator:
    return Creator(
        name=author.name,
        name_type=NameType.ORGANIZATIONAL if isinstance(author, Organization) else NameType.PERSONAL,
        given_name=author.given_name if isinstance(author, Person) else None,
        family_name=author.family_name if isinstance(author, Person) else None,
        affiliation=[Affiliation(
            affiliation_identifier=author.affiliation.name if isinstance(author.affiliation, Organization) else None,
        )] if isinstance(author, Person) else None
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
                description=metadata_source.description, # type: ignore
                description_type=DescriptionType.TECHNICAL_INFO
            ), Description(
                description=metadata_source.application_category if metadata_source.application_category else 'Undefined',
                description_type=DescriptionType.TECHNICAL_INFO
            ), Description(
                description=metadata_source.application_sub_category if metadata_source.application_sub_category else 'Undefined',
                description_type=DescriptionType.TECHNICAL_INFO
            )],
            publisher=Publisher(
                name=metadata_source.publisher.name # type: ignore
            ),
            publication_year=metadata_source.copyright_year,
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
                    metadata_source.author if isinstance(metadata_source.author, Iterable) else [metadata_source.author]
                )
            )
        ).model_dump(exclude_none=True, by_alias=True)
