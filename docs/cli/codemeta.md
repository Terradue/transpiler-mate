# Transpile a CWL Workflow to CodeMeta

```
$ transpiler-mate codemeta --help
Usage: transpiler-mate codemeta [OPTIONS] SOURCE

  Transpiles the input CWL to CodeMeta representation.

Options:
  --help  Show this message and exit.
```

i.e.

```
$ transpiler-mate codemeta /path/to/pattern-1.cwl
2025-10-29 15:51:00.368 | INFO     | transpiler_mate.cli:wrapper:32 - Started at: 2025-10-29T15:51:00.368
2025-10-29 15:51:00.368 | DEBUG    | transpiler_mate.metadata:__init__:51 - Loading raw document from /path/to/pattern-1.cwl...
2025-10-29 15:51:01.003 | INFO     | transpiler_mate.cli:_dump_json:128 - Metadata successfully traspiled to /path/to/codemeta.json.
2025-10-29 15:51:01.003 | SUCCESS  | transpiler_mate.cli:wrapper:37 - ------------------------------------------------------------------------
2025-10-29 15:51:01.003 | SUCCESS  | transpiler_mate.cli:wrapper:38 - SUCCESS
2025-10-29 15:51:01.003 | SUCCESS  | transpiler_mate.cli:wrapper:39 - ------------------------------------------------------------------------
2025-10-29 15:51:01.003 | INFO     | transpiler_mate.cli:wrapper:48 - Total time: 0.6349 seconds
2025-10-29 15:51:01.003 | INFO     | transpiler_mate.cli:wrapper:49 - Finished at: 2025-10-29T15:51:01.003
```
