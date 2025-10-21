# Transpiler Mate (c) 2025
# 
# Transpiler Mate is licensed under
# Creative Commons Attribution-ShareAlike 4.0 International.
# 
# You should have received a copy of the license along with this work.
# If not, see <https://creativecommons.org/licenses/by-sa/4.0/>.

from .software_application_models import SoftwareApplication
from abc import (
    abstractmethod
)
from loguru import logger
from pathlib import Path
from pyld import jsonld
from typing import (
    Any,
    Generic,
    MutableMapping,
    TextIO,
    TypeVar
)

T = TypeVar('T')

class Transpiler(Generic[T]):

    @abstractmethod
    def transpile(
        self,
        metadata_source: SoftwareApplication
    ) -> T:
        pass

import json
import yaml

__CONTEXT_KEY__ = '@context'
__NAMESPACE_KEY__ = '$namespaces'

class MetadataManager():

    def __init__(
        self,
        document_source: str | Path
    ):
        if isinstance(document_source, str):
            document_source = Path(document_source)

        if not document_source.exists():
            raise ValueError(f"Input source document {document_source} points to a non existing file.")
        if not document_source.is_file():
            raise ValueError(f"Input source document {document_source} is not a file.")

        logger.debug(f"Loading raw document from {document_source}...")

        self.document_source = document_source

        with document_source.open() as input_stream:
            self.raw_document: MutableMapping[str, Any] = yaml.safe_load(input_stream)

        logger.debug('Reading the input dictionary and extracting Schema.org metadata in JSON-LD format...')

        compacted = jsonld.compact(
            input_=self.raw_document,
            ctx={},
            options={
                'expandContext': self.raw_document.get(__NAMESPACE_KEY__)
            }
        )

        logger.debug('Schema.org metadata successfully extracted in in JSON-LD format!')

        self.metadata: SoftwareApplication = SoftwareApplication.model_validate(compacted, by_alias=True)

    def update(self):
        metadata_dict = self.metadata.model_dump(exclude_none=True, by_alias=True)

        updated_metadata: MutableMapping[str, Any] = jsonld.compact(
            input_=metadata_dict,
            ctx=self.raw_document.get(__NAMESPACE_KEY__),
            options={
                'expandContext': self.raw_document.get(__NAMESPACE_KEY__)
            }
        ) # type: ignore

        updated_metadata.pop(__CONTEXT_KEY__) # remove undesired keys, $namespace already in the source document
        
        logger.debug(f'JSON-LD format compacted metadata ready to be merged to the original raw CWL document...')

        self.raw_document.update(updated_metadata)

        def _dump(stream: TextIO):
            yaml.dump(
                self.raw_document,
                stream,
                indent=2
            )

        logger.debug(f"JSON-LD format compacted metadata merged to the original document")
        with self.document_source.open('w') as output_stream:
            _dump(output_stream)

        logger.info(f"JSON-LD format compacted metadata merged to the original '{self.document_source}' document")

    def save_as_codemeta(
        self,
        sink: TextIO
    ):
        compacted = jsonld.compact(
            input_=self.raw_document,
            ctx=self.raw_document.get(__NAMESPACE_KEY__),
            options={
                'expandContext': self.raw_document.get(__NAMESPACE_KEY__)
            }
        )

        json.dump(
            compacted,
            sink,
            indent=2,
            sort_keys=False
        )
