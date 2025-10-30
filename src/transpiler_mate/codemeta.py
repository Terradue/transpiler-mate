# Transpiler Mate (c) 2025
# 
# Transpiler Mate is licensed under
# Creative Commons Attribution-ShareAlike 4.0 International.
# 
# You should have received a copy of the license along with this work.
# If not, see <https://creativecommons.org/licenses/by-sa/4.0/>.

from transpiler_mate.metadata.software_application_models import SoftwareApplication
from .metadata import Transpiler

from pyld import jsonld
from typing import (
    Any,
    Mapping,
    MutableMapping
)

class CodeMetaTranspiler(Transpiler):

    def transpile(
        self,
        metadata_source: SoftwareApplication
    ) -> Mapping[str, Any]:
        doc: MutableMapping[str, Any] = metadata_source.model_dump(exclude_none=True, by_alias=True)

        compacted: MutableMapping[str, Any] = jsonld.compact(
            doc,
            {
                "@context": {
                    "@vocab": "https://schema.org/",
                    # (optional) If you want relative IRIs to stay relative, omit @base.
                    # If you want to forbid a base so @id values don't get resolved, set:
                    # "@base": None,
                }
            },
            options={
                "processingMode": "json-ld-1.1",
                "ordered": True
            }
        ) # type: ignore

        compacted['@context'] = 'https://w3id.org/codemeta/3.0'

        if metadata_source.keywords and isinstance(metadata_source.keywords, list):
            compacted['keywords'] = list(
                filter(
                    lambda keyword: isinstance(keyword, str),
                    metadata_source.keywords
                )
            )

        return compacted
