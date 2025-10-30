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

import yaml

__CONTEXT_KEY__ = '@context'

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

        self.metadata: SoftwareApplication = SoftwareApplication.from_jsonld(self.raw_document)

    def update(self):
        metadata_dict = self.metadata.model_dump(exclude_none=True, by_alias=True)

        namespaces = self.raw_document.get('$namespaces')

        updated_metadata: MutableMapping[str, Any] = jsonld.compact(
            input_=metadata_dict,
            ctx=namespaces,
            options={
                'expandContext': namespaces
            }
        ) # type: ignore

        updated_metadata.pop('@context') # remove undesired keys, $namespace already in the source document

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
