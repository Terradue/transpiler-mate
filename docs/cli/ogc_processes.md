# Transpile a CWL Workflow to an OGC API - Processes

Since version `0.44.0`, `transpiler-mate` includes a simple CLI to generate a static _OGC API - Processes_ process descriptor.

## Help usage

```
$ transpiler-mate ogcprocesses --help
Usage: transpiler-mate ogcprocesses [OPTIONS] SOURCE

  Transpiles the input CWL to OGC API Record.

Options:
  --output PATH  The output file path  [default: processes.json]
  --help         Show this message and exit.
```

## Sample execution

```
$ transpiler-mate ogcprocesses /path/to/pattern-1.cwl

2026-05-13 16:04:36.004 | INFO     | transpiler_mate.cli.common:wrapper:37 - Started at: 2026-05-13T16:04:36.004
2026-05-13 16:04:36.004 | INFO     | transpiler_mate.cli.ogcprocesses:run:39 - Reading metadata from /path/to/pattern-1.cwl...
2026-05-13 16:04:36.004 | DEBUG    | transpiler_mate.metadata:__init__:51 - Loading raw document from /path/to/pattern-1.cwl...
2026-05-13 16:04:36.026 | INFO     | transpiler_mate.metadata:__init__:67 - Resolving License details from SPDX License List...
2026-05-13 16:04:36.026 | SUCCESS  | transpiler_mate.cli.ogcprocesses:run:42 - Metadata successfully read!
2026-05-13 16:04:36.026 | INFO     | transpiler_mate.cli.ogcprocesses:run:43 - Transpiling metadata...
2026-05-13 16:04:36.026 | SUCCESS  | transpiler_mate.cli.ogcprocesses:run:48 - Metadata successfully transpiled!
2026-05-13 16:04:36.026 | DEBUG    | cwl_loader:load_cwl_from_yaml:147 - No needs to update the Raw CWL document since it targets already the v1.2
2026-05-13 16:04:36.026 | DEBUG    | cwl_loader:load_cwl_from_yaml:151 - Parsing the raw CWL document to the CWL Utils DOM...
2026-05-13 16:04:36.435 | DEBUG    | cwl_loader:load_cwl_from_yaml:160 - Raw CWL document successfully parsed to the CWL Utils DOM!
2026-05-13 16:04:36.435 | DEBUG    | cwl_loader:load_cwl_from_yaml:162 - Dereferencing the steps[].run...
2026-05-13 16:04:36.435 | DEBUG    | cwl_loader:_on_process:54 - Checking if #publish_experiment_cli must be externally imported...
2026-05-13 16:04:36.435 | DEBUG    | cwl_loader:_on_process:58 - run_url:  - uri: io://
2026-05-13 16:04:36.435 | DEBUG    | cwl_loader:_on_process:54 - Checking if #publish_product_cli must be externally imported...
2026-05-13 16:04:36.435 | DEBUG    | cwl_loader:_on_process:58 - run_url:  - uri: io://
2026-05-13 16:04:36.435 | DEBUG    | cwl_loader:load_cwl_from_yaml:166 - steps[].run successfully dereferenced! Dereferencing the FQNs...
2026-05-13 16:04:36.435 | DEBUG    | cwl_loader:load_cwl_from_yaml:170 - CWL document successfully dereferenced! Now verifying steps[].run integrity...
2026-05-13 16:04:36.435 | DEBUG    | cwl_loader:load_cwl_from_yaml:176 - All steps[].run link are resolvable! 
2026-05-13 16:04:36.435 | DEBUG    | cwl_loader:load_cwl_from_yaml:179 - Sorting Process instances by dependencies....
2026-05-13 16:04:36.436 | DEBUG    | cwl_loader:load_cwl_from_yaml:181 - Sorting process is over.
2026-05-13 16:04:36.436 | INFO     | transpiler_mate.cli.common:write_json:72 - Serializing metadata...
2026-05-13 16:04:36.436 | SUCCESS  | transpiler_mate.cli.common:write_json:77 - Metadata successfully serialized to processes.json.
2026-05-13 16:04:36.436 | SUCCESS  | transpiler_mate.cli.common:wrapper:44 - ------------------------------------------------------------------------
2026-05-13 16:04:36.436 | SUCCESS  | transpiler_mate.cli.common:wrapper:47 - SUCCESS
2026-05-13 16:04:36.436 | SUCCESS  | transpiler_mate.cli.common:wrapper:48 - ------------------------------------------------------------------------
2026-05-13 16:04:36.436 | INFO     | transpiler_mate.cli.common:wrapper:63 - Total time: 0.4328 seconds
2026-05-13 16:04:36.436 | INFO     | transpiler_mate.cli.common:wrapper:64 - Finished at: 2026-05-13T16:04:36.436
```

then

```
vim ./processes.json
```
