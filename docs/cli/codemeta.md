# Transpile a CWL Workflow to CodeMeta

```
$ transpiler-mate codemeta --help
Usage: transpiler-mate codemeta [OPTIONS] SOURCE

  Transpiles the input CWL to CodeMeta representation.

Options:
  --output PATH  The output file path  [default: codemeta.json]
  --help         Show this message and exit.
```

i.e.

```
$ transpiler-mate codemeta /path/to/pattern-1.cwl
2025-10-30 13:12:46.203 | INFO     | transpiler_mate.cli:wrapper:33 - Started at: 2025-10-30T13:12:46.203
2025-10-30 13:12:46.203 | INFO     | transpiler_mate.cli:_transpile:123 - Reading metadata from /home/stripodi/Downloads/pattern-1.cwl...
2025-10-30 13:12:46.203 | DEBUG    | transpiler_mate.metadata:__init__:53 - Loading raw document from /home/stripodi/Downloads/pattern-1.cwl...
2025-10-30 13:12:46.758 | SUCCESS  | transpiler_mate.cli:_transpile:126 - Metadata successfully read!
2025-10-30 13:12:46.758 | INFO     | transpiler_mate.cli:_transpile:127 - Transpiling metadata...
2025-10-30 13:12:46.759 | SUCCESS  | transpiler_mate.cli:_transpile:130 - Metadata successfully transpiled!
2025-10-30 13:12:46.759 | INFO     | transpiler_mate.cli:_transpile:131 - Serializing metadata...
2025-10-30 13:12:46.759 | SUCCESS  | transpiler_mate.cli:_transpile:139 - Metadata successfully serialized to codemeta.json.
2025-10-30 13:12:46.760 | SUCCESS  | transpiler_mate.cli:wrapper:38 - ------------------------------------------------------------------------
2025-10-30 13:12:46.760 | SUCCESS  | transpiler_mate.cli:wrapper:39 - SUCCESS
2025-10-30 13:12:46.760 | SUCCESS  | transpiler_mate.cli:wrapper:40 - ------------------------------------------------------------------------
2025-10-30 13:12:46.760 | INFO     | transpiler_mate.cli:wrapper:49 - Total time: 0.5564 seconds
2025-10-30 13:12:46.760 | INFO     | transpiler_mate.cli:wrapper:50 - Finished at: 2025-10-30T13:12:46.760
```
