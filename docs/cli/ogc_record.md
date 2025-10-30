# Transpile a CWL Workflow to an OGC API - Record

```
$ transpiler-mate ogcrecord --help
Usage: transpiler-mate ogcrecord [OPTIONS] SOURCE

  Transpiles the input CWL to OGC API Record.

Options:
  --output PATH  The output file path  [default: record.json]
  --help         Show this message and exit.
```

i.e.

```
$ transpiler-mate ogcrecord /path/to/pattern-1.cwl
2025-10-30 13:15:36.238 | INFO     | transpiler_mate.cli:wrapper:33 - Started at: 2025-10-30T13:15:36.238
2025-10-30 13:15:36.292 | INFO     | transpiler_mate.cli:_transpile:123 - Reading metadata from /home/stripodi/Downloads/pattern-1.cwl...
2025-10-30 13:15:36.292 | DEBUG    | transpiler_mate.metadata:__init__:53 - Loading raw document from /home/stripodi/Downloads/pattern-1.cwl...
2025-10-30 13:15:36.825 | SUCCESS  | transpiler_mate.cli:_transpile:126 - Metadata successfully read!
2025-10-30 13:15:36.825 | INFO     | transpiler_mate.cli:_transpile:127 - Transpiling metadata...
2025-10-30 13:15:36.825 | DEBUG    | transpiler_mate.ogc_record:transpile:160 - Discarding keyword, field_type='https://schema.org/DefinedTerm' additional_type=None identifier=None image=None url=None disambiguating_description=None description='delineation' main_entity_of_page=None same_as=None name='application-type' subject_of=None alternate_name=None potential_action=None term_code=None in_defined_term_set=None, unsupported
2025-10-30 13:15:36.825 | DEBUG    | transpiler_mate.ogc_record:transpile:160 - Discarding keyword, field_type='https://schema.org/DefinedTerm' additional_type=None identifier=None image=None url=None disambiguating_description=None description='hydrology' main_entity_of_page=None same_as=None name='domain' subject_of=None alternate_name=None potential_action=None term_code=None in_defined_term_set=None, unsupported
2025-10-30 13:15:36.825 | SUCCESS  | transpiler_mate.cli:_transpile:130 - Metadata successfully transpiled!
2025-10-30 13:15:36.825 | INFO     | transpiler_mate.cli:_transpile:131 - Serializing metadata...
2025-10-30 13:15:36.826 | SUCCESS  | transpiler_mate.cli:_transpile:139 - Metadata successfully serialized to record.json.
2025-10-30 13:15:36.827 | SUCCESS  | transpiler_mate.cli:wrapper:38 - ------------------------------------------------------------------------
2025-10-30 13:15:36.827 | SUCCESS  | transpiler_mate.cli:wrapper:39 - SUCCESS
2025-10-30 13:15:36.827 | SUCCESS  | transpiler_mate.cli:wrapper:40 - ------------------------------------------------------------------------
2025-10-30 13:15:36.827 | INFO     | transpiler_mate.cli:wrapper:49 - Total time: 0.5885 seconds
2025-10-30 13:15:36.827 | INFO     | transpiler_mate.cli:wrapper:50 - Finished at: 2025-10-30T13:15:36.827
```
