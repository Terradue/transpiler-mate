# Transpiler Mate (c) 2025
# 
# Transpiler Mate is licensed under
# Creative Commons Attribution-ShareAlike 4.0 International.
# 
# You should have received a copy of the license along with this work.
# If not, see <https://creativecommons.org/licenses/by-sa/4.0/>.

from .software_application_models import (
    CreativeWork,
    SoftwareApplication
)
from .licenses import LICENSES_INDEX
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
__NAMESPACES_KEY__ = '$namespaces'

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

        compacted = jsonld.compact(
            input_=self.raw_document,
            ctx={},
            options={
                'expandContext': self.raw_document.get(__NAMESPACES_KEY__)
            }
        )
        self.metadata: SoftwareApplication = SoftwareApplication.model_validate(compacted, by_alias=True)

        logger.info('Resolving License details from SPDX License List...')

        def resolve_license(license: CreativeWork) -> CreativeWork:
            if license.identifier and license.identifier in LICENSES_INDEX:
                logger.info(f"Detected {license.identifier} indexed in SPDX Licenses")
                return LICENSES_INDEX[str(license.identifier)]
            logger.info('License is not indexed in SPDX Licenses')
            return license

        if isinstance(self.metadata.license, list):
            for i, license in enumerate(self.metadata.license):
                if isinstance(license, CreativeWork):
                    self.metadata.license[i] = resolve_license(license)
        elif isinstance(self.metadata.license, CreativeWork):
            self.metadata.license = resolve_license(self.metadata.license)

    def update(self):
        metadata_dict = self.metadata.model_dump(exclude_none=True, by_alias=True)

        namespaces = self.raw_document.get(__NAMESPACES_KEY__)

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
                indent=2,
                sort_keys=False
            )

        logger.debug(f"JSON-LD format compacted metadata merged to the original document")
        with self.document_source.open('w') as output_stream:
            _dump(output_stream)

        logger.info(f"JSON-LD format compacted metadata merged to the original '{self.document_source}' document")
