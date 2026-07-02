# Transpile a CWL Workflow to DataCite

```
$ transpiler-mate datacite --help
Usage: transpiler-mate datacite [OPTIONS] SOURCE

  Transpiles the input CWL to DataCite Metadata.

Options:
  --output PATH  The output file path  [default: datacite.json]
  --help         Show this message and exit.
```

i.e.

```
$ transpiler-mate datacite /path/to/pattern-1.cwl
2025-10-31 11:37:39.863 | INFO     | transpiler_mate.cli:wrapper:33 - Started at: 2025-10-31T11:37:39.863
2025-10-31 11:37:39.884 | INFO     | transpiler_mate.cli:_transpile:124 - Reading metadata from /home/stripodi/Downloads/pattern-1.cwl...
2025-10-31 11:37:39.884 | DEBUG    | transpiler_mate.metadata:__init__:53 - Loading raw document from /home/stripodi/Downloads/pattern-1.cwl...
2025-10-31 11:37:40.425 | SUCCESS  | transpiler_mate.cli:_transpile:127 - Metadata successfully read!
2025-10-31 11:37:40.425 | INFO     | transpiler_mate.cli:_transpile:128 - Transpiling metadata...
2025-10-31 11:37:40.425 | SUCCESS  | transpiler_mate.cli:_transpile:131 - Metadata successfully transpiled!
2025-10-31 11:37:40.425 | INFO     | transpiler_mate.cli:_transpile:132 - Serializing metadata...
2025-10-31 11:37:40.426 | SUCCESS  | transpiler_mate.cli:_transpile:140 - Metadata successfully serialized to datacite.json.
2025-10-31 11:37:40.426 | SUCCESS  | transpiler_mate.cli:wrapper:38 - ------------------------------------------------------------------------
2025-10-31 11:37:40.426 | SUCCESS  | transpiler_mate.cli:wrapper:39 - SUCCESS
2025-10-31 11:37:40.426 | SUCCESS  | transpiler_mate.cli:wrapper:40 - ------------------------------------------------------------------------
2025-10-31 11:37:40.426 | INFO     | transpiler_mate.cli:wrapper:49 - Total time: 0.5628 seconds
2025-10-31 11:37:40.426 | INFO     | transpiler_mate.cli:wrapper:50 - Finished at: 2025-10-31T11:37:40.426
```
