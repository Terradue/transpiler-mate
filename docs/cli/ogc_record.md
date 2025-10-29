# Transpile a CWL Workflow to an OGC API - Record

```
$ transpiler-mate ogcrecord --help
Usage: transpiler-mate ogcrecord [OPTIONS] SOURCE

  Transpiles the input CWL to OGC API Record.

Options:
  --help  Show this message and exit.
```

i.e.

```
$ transpiler-mate ogcrecord /path/to/pattern-1.cwl
2025-10-29 15:52:22.874 | INFO     | transpiler_mate.cli:wrapper:32 - Started at: 2025-10-29T15:52:22.874
2025-10-29 15:52:22.874 | DEBUG    | transpiler_mate.metadata:__init__:51 - Loading raw document from /path/to/pattern-1.cwl...
2025-10-29 15:52:23.554 | DEBUG    | transpiler_mate.ogc_record:transpile:158 - Discarding keyword, field_type='https://schema.org/DefinedTerm' additional_type=None identifier=None image=None url=None disambiguating_description=None description='delineation' main_entity_of_page=None same_as=None name='application-type' subject_of=None alternate_name=None potential_action=None term_code=None in_defined_term_set=None, unsupported
2025-10-29 15:52:23.554 | DEBUG    | transpiler_mate.ogc_record:transpile:158 - Discarding keyword, field_type='https://schema.org/DefinedTerm' additional_type=None identifier=None image=None url=None disambiguating_description=None description='hydrology' main_entity_of_page=None same_as=None name='domain' subject_of=None alternate_name=None potential_action=None term_code=None in_defined_term_set=None, unsupported
2025-10-29 15:52:23.555 | INFO     | transpiler_mate.cli:_dump_json:128 - Metadata successfully traspiled to /path/to/record.json.
2025-10-29 15:52:23.555 | SUCCESS  | transpiler_mate.cli:wrapper:37 - ------------------------------------------------------------------------
2025-10-29 15:52:23.555 | SUCCESS  | transpiler_mate.cli:wrapper:38 - SUCCESS
2025-10-29 15:52:23.555 | SUCCESS  | transpiler_mate.cli:wrapper:39 - ------------------------------------------------------------------------
2025-10-29 15:52:23.555 | INFO     | transpiler_mate.cli:wrapper:48 - Total time: 0.6805 seconds
2025-10-29 15:52:23.555 | INFO     | transpiler_mate.cli:wrapper:49 - Finished at: 2025-10-29T15:52:23.555
```
