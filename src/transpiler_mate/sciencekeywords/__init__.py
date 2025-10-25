# Transpiler Mate (c) 2025
# 
# Transpiler Mate is licensed under
# Creative Commons Attribution-ShareAlike 4.0 International.
# 
# You should have received a copy of the license along with this work.
# If not, see <https://creativecommons.org/licenses/by-sa/4.0/>.

from ..metadata.software_application_models import SoftwareApplication
from ..metadata import Transpiler
from abc import ABC
from csv import DictReader
from loguru import logger
from pydantic import (
    BaseModel,
    Field
)
from typing import (
    List,
    MutableMapping,
    Optional
)
import os

class ScienceKeywordRecord(BaseModel):
    category: str = Field(..., alias='Category')
    topic: Optional[str] = Field(default=None, alias='Topic')
    term: Optional[str] = Field(default=None, alias='Term')
    variable_level_1: Optional[str] = Field(default=None, alias='Variable_Level_1')
    variable_level_2: Optional[str] = Field(default=None, alias='Variable_Level_2')
    variable_level_3: Optional[str] = Field(default=None, alias='Variable_Level_3')
    detailed_variable: Optional[str] = Field(default=None, alias='Detailed_Variable')
    uuid: str = Field(..., alias='UUID')

class ScienceKeywordsTranspiler(Transpiler):

    def __init__(self) -> None:
        self.sciencekeywords_index: MutableMapping[str, ScienceKeywordRecord] = {}
        logger.trace(f"Initializing sciencekeywords index...")

        with open(f"{os.path.dirname(os.path.realpath(__file__))}/sciencekeywords.csv") as sciencekeywords_csv_file:
            sciencekeywords_csv = DictReader(sciencekeywords_csv_file)
            for line in sciencekeywords_csv:
                logger.trace(f"Analyzing record {line}")
                record = ScienceKeywordRecord.model_validate(line)
                self.sciencekeywords_index[record.uuid] = record
                logger.trace(f"Indexed record {record.uuid}")

        logger.trace(f"sciencekeywords index initialized")

    def transpile(
        self,
        metadata_source: SoftwareApplication
    ) -> List[ScienceKeywordRecord]:
        sciencekeywords: List[ScienceKeywordRecord] = []

        if metadata_source.genre:
            raw_keywords = metadata_source.genre if isinstance(metadata_source.genre, list) else [metadata_source.genre]
            for raw_keyword in raw_keywords:
                if not raw_keyword in self.sciencekeywords_index:
                    logger.warning(f"Science Keyword UUID {raw_keyword} not found in the index")
                else:
                    sciencekeywords.append(self.sciencekeywords_index[str(raw_keyword)])

        return sciencekeywords
