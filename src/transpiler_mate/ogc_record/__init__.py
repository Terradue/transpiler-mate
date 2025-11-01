# Transpiler Mate (c) 2025
# 
# Transpiler Mate is licensed under
# Creative Commons Attribution-ShareAlike 4.0 International.
# 
# You should have received a copy of the license along with this work.
# If not, see <https://creativecommons.org/licenses/by-sa/4.0/>.

from ..metadata.software_application_models import (
    CreativeWork,
    DefinedTerm,
    SoftwareApplication
)
from ..metadata import Transpiler
from csv import DictReader
from datetime import (
    date,
    datetime,
    timezone
)
from loguru import logger
from ogc_api_records_core_client.models.language import Language
from ogc_api_records_core_client.models.record_geo_json import RecordGeoJSON
from ogc_api_records_core_client.models.record_geo_json_properties import RecordGeoJSONProperties
from ogc_api_records_core_client.models.record_geo_json_type import RecordGeoJSONType
from ogc_api_records_core_client.models.theme import Theme
from ogc_api_records_core_client.models.theme_concepts_item import ThemeConceptsItem
from ogc_api_records_core_client.types import UNSET
from pydantic import (
    AnyUrl,
    BaseModel,
    computed_field,
    Field
)
from typing import (
    Any,
    Mapping,
    MutableMapping,
    Optional,
    Sequence
)

import os
import time
import uuid

class ScienceKeywordRecord(BaseModel):
    @computed_field
    @property
    def scheme(self) -> str:
        return 'GCMD Science Keywords'
    category: str = Field(..., alias='Category')
    topic: Optional[str] = Field(default=None, alias='Topic')
    term: Optional[str] = Field(default=None, alias='Term')
    variable_level_1: Optional[str] = Field(default=None, alias='Variable_Level_1')
    variable_level_2: Optional[str] = Field(default=None, alias='Variable_Level_2')
    variable_level_3: Optional[str] = Field(default=None, alias='Variable_Level_3')
    detailed_variable: Optional[str] = Field(default=None, alias='Detailed_Variable')
    identifier: str = Field(..., alias='UUID')
    @computed_field
    @property
    def uri(self) -> str:
        return f"https://cmr.earthdata.nasa.gov/kms/concept/{self.identifier}"
    @computed_field
    @property
    def hierarchy_list(self) -> Sequence[str]:
        hierarchy = [self.category]

        def _add(keyword: str | None):
            if keyword:
                hierarchy.append(keyword)

        _add(self.topic)
        _add(self.term)
        _add(self.variable_level_1)
        _add(self.variable_level_2)
        _add(self.variable_level_3)
        _add(self.detailed_variable)

        return hierarchy

SCIENCE_KEYWORDS_TERM_SET = AnyUrl('https://gcmd.earthdata.nasa.gov/kms/concepts/concept_scheme/sciencekeywords')

DEFAULT_LANGUAGE: Language = Language(
    code='en-US',
    name='English (United States)'
)

def _to_datetime(value: date | datetime):
    if isinstance(value, datetime):
        return value if value.tzinfo else value.replace(tzinfo=timezone.utc)
    return datetime.combine(value, datetime.min.time(), tzinfo=timezone.utc)

class OgcRecordsTranspiler(Transpiler):

    def __init__(self):
        self.sciencekeywords_index: MutableMapping[str, ScienceKeywordRecord] = {}
        logger.trace(f"Initializing sciencekeywords index...")

        with open(f"{os.path.dirname(os.path.realpath(__file__))}/sciencekeywords.csv") as sciencekeywords_csv_file:
            sciencekeywords_csv = DictReader(sciencekeywords_csv_file)
            for line in sciencekeywords_csv:
                logger.trace(f"Analyzing record {line}")
                record = ScienceKeywordRecord.model_validate(line)
                self.sciencekeywords_index[record.identifier] = record
                logger.trace(f"Indexed record {record.identifier}")

        logger.trace(f"sciencekeywords index initialized")

    def transpile(
        self,
        metadata_source: SoftwareApplication
    ) -> Mapping[str, Any]:
        record_geojson: RecordGeoJSON = RecordGeoJSON(
            id=f"urn:uuid:{uuid.uuid4()}",
            type_=RecordGeoJSONType.FEATURE,
            geometry=None,
            properties=RecordGeoJSONProperties(
                created=_to_datetime(metadata_source.date_created),
                updated=datetime.fromtimestamp(time.time()),
                title=metadata_source.name,
                description=metadata_source.description if metadata_source.description else UNSET,
                keywords=[],
                themes=[],
                language=DEFAULT_LANGUAGE,
                resource_languages=[DEFAULT_LANGUAGE],
                formats=[{ 'name': 'CWL', 'mediaType': 'application/cwl' }],
                contacts=[author.email for author in metadata_source.author] if isinstance(metadata_source.author, list) else [metadata_source.author.email],
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

        if metadata_source.publisher.email:
            record_geojson.properties.contacts.append(metadata_source.publisher.email) # type: ignore previously set

        if metadata_source.keywords:
            raw_keywords = metadata_source.keywords if isinstance(metadata_source.keywords, list) else [metadata_source.keywords]
            for raw_keyword in raw_keywords:
                if isinstance(raw_keyword, str):
                    record_geojson.properties.keywords.append(raw_keyword) # type: ignore - manually set
                elif isinstance(raw_keyword, DefinedTerm):
                    if SCIENCE_KEYWORDS_TERM_SET == raw_keyword.in_defined_term_set and raw_keyword.term_code:
                        if not raw_keyword.term_code in self.sciencekeywords_index:
                            logger.warning(f"Science Keyword UUID {raw_keyword.term_code} not found in the index")
                        else:
                            science_keyword_record: ScienceKeywordRecord = self.sciencekeywords_index[str(raw_keyword.term_code)]

                            current_theme: Theme = Theme(
                                scheme=str(SCIENCE_KEYWORDS_TERM_SET),
                                concepts=[]
                            )

                            for i, keyword in enumerate(science_keyword_record.hierarchy_list):
                                current_theme.concepts.append(
                                    ThemeConceptsItem(
                                        id=keyword,
                                        description=' > '.join(science_keyword_record.hierarchy_list[0:i+1]),
                                        url=science_keyword_record.uri
                                    )
                                )
                            
                            record_geojson.properties.themes.append(current_theme) # type: ignore - manually set
                    else:
                        logger.debug(f"Discarding keyword, {raw_keyword}, unsupported")
                else:
                    logger.debug(f"Discarding keyword, {raw_keyword}, unsupported type {type(raw_keyword)}")

        return record_geojson.to_dict()
