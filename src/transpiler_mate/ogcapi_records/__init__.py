# Transpiler Mate (c) 2025
# 
# Transpiler Mate is licensed under
# Creative Commons Attribution-ShareAlike 4.0 International.
# 
# You should have received a copy of the license along with this work.
# If not, see <https://creativecommons.org/licenses/by-sa/4.0/>.

from .ogcapi_records_models import (
    Concept,
    Contact1,
    Email,
    Format1,
    Language,
    RecordCommonProperties,
    RecordGeoJSON,
    Theme,
    Type7
)
from .sciencekeywords import (
    KEYWORDS_INDEX,
    ScienceKeywordRecord
)
from ..metadata.software_application_models import (
    CreativeWork,
    DefinedTerm,
    SoftwareApplication
)
from ..metadata import Transpiler
from datetime import (
    date,
    datetime,
    timezone
)
from loguru import logger

from pydantic import AnyUrl
from typing import (
    Any,
    Mapping,
    List
)

import os
import time
import uuid

SCIENCE_KEYWORDS_TERM_SET = AnyUrl('https://gcmd.earthdata.nasa.gov/kms/concepts/concept_scheme/sciencekeywords')

DEFAULT_LANGUAGE: Language = Language(
    code='en-US',
    name='English (United States)',
    dir=None
)

def _to_datetime(value: date | datetime):
    if isinstance(value, datetime):
        return value if value.tzinfo else value.replace(tzinfo=timezone.utc)
    return datetime.combine(value, datetime.min.time(), tzinfo=timezone.utc)

class OgcRecordsTranspiler(Transpiler):

    def transpile(
        self,
        metadata_source: SoftwareApplication
    ) -> Mapping[str, Any]:
        keywords: List[str] = []
        themes: List[Theme] = []

        if metadata_source.keywords:
            for raw_keyword in metadata_source.keywords if isinstance(metadata_source.keywords, list) else [metadata_source.keywords]:
                if isinstance(raw_keyword, str):
                    keywords.append(raw_keyword)
                elif isinstance(raw_keyword, DefinedTerm):
                    if SCIENCE_KEYWORDS_TERM_SET == raw_keyword.in_defined_term_set and raw_keyword.term_code:
                        if not raw_keyword.term_code in KEYWORDS_INDEX:
                            logger.warning(f"Science Keyword UUID {raw_keyword.term_code} not found in the index")
                        else:
                            science_keyword_record: ScienceKeywordRecord = KEYWORDS_INDEX[str(raw_keyword.term_code)]

                            concepts: List[Concept] = []

                            for i, keyword in enumerate(science_keyword_record.hierarchy_list):
                                concepts.append(
                                    Concept(
                                        id=keyword,
                                        title=None,
                                        description=' > '.join(science_keyword_record.hierarchy_list[0:i+1]),
                                        url=science_keyword_record.uri
                                    )
                                )

                            themes.append(
                                Theme(
                                    scheme=str(SCIENCE_KEYWORDS_TERM_SET),
                                    concepts=concepts
                                )
                            )
                    else:
                        logger.debug(f"Discarding keyword, {raw_keyword}, unsupported")
                else:
                    logger.debug(f"Discarding keyword, {raw_keyword}, unsupported type {type(raw_keyword)}")

        record_geojson: RecordGeoJSON = RecordGeoJSON(
            id=f"urn:uuid:{uuid.uuid4()}",
            type=Type7.FEATURE,
            geometry=None,
            time=None,
            links=None,
            properties=RecordCommonProperties(
                created=_to_datetime(metadata_source.date_created),
                updated=_to_datetime(datetime.fromtimestamp(time.time())),
                title=metadata_source.name,
                description=metadata_source.description if metadata_source.description else None,
                keywords=keywords if keywords else None,
                themes=themes if themes else None,
                language=DEFAULT_LANGUAGE,
                resource_languages=[DEFAULT_LANGUAGE],
                formats=[Format1(
                    name='CWL',
                    media_type='application/cwl'
                )],
                contacts=list(
                    map(
                        lambda author: Contact1(
                            identifier=str(author.identifier),
                            name=f"{author.family_name}, {author.given_name}",
                            organization=author.affiliation.name,
                            emails=[Email(
                                value=author.email
                            )]
                        ),
                        metadata_source.author if isinstance(metadata_source.author, list) else [metadata_source.author]
                    )
                ),
                license_=': '.join(
                    list(
                        map(
                            lambda license: str(license.url) if isinstance(license, CreativeWork) else str(license),
                            metadata_source.license if isinstance(metadata_source.license, list) else [metadata_source.license]
                        )
                    )
                )
            )
        )

        return record_geojson.model_dump(by_alias=True, exclude_none=True)
