# Transpile a CWL Workflow to an OCI Annotations JSON file

```
$ transpiler-mate oci-annotations --help
Usage: transpiler-mate oci-annotations [OPTIONS] SOURCE

  Transpiles the input CWL to OCI annotations.

Options:
  --workflow-id TEXT  ID of the main Workflow  [required]
  --output PATH       The output file path  [default: codemeta.json]
  --help              Show this message and exit.
```

i.e.

```
$ transpiler-mate oci-annotations --workflow-id pattern-1 /path/to/pattern-1.cwl
2026-03-09 16:03:57.182 | INFO     | transpiler_mate.cli:wrapper:43 - Started at: 2026-03-09T16:03:57.182
2026-03-09 16:03:57.182 | INFO     | transpiler_mate.cli:oci_annotations:185 - Reading metadata from /path/to/pattern-1.cwl...
2026-03-09 16:03:57.182 | DEBUG    | transpiler_mate.metadata:__init__:62 - Loading raw document from /path/to/pattern-1.cwl...
2026-03-09 16:03:57.199 | INFO     | transpiler_mate.metadata:__init__:78 - Resolving License details from SPDX License List...
2026-03-09 16:03:57.199 | INFO     | transpiler_mate.metadata:resolve_license:82 - Detected Apache-2.0 indexed in SPDX Licenses
2026-03-09 16:03:57.199 | SUCCESS  | transpiler_mate.cli:oci_annotations:188 - Metadata successfully read!
2026-03-09 16:03:57.199 | INFO     | transpiler_mate.cli:oci_annotations:189 - Transpiling metadata...
2026-03-09 16:03:57.201 | DEBUG    | cwl_loader:load_cwl_from_yaml:130 - Updating the model from version 'v1.0' to version 'v1.2'...
2026-03-09 16:03:57.201 | DEBUG    | cwl_loader:load_cwl_from_yaml:141 - Raw CWL document successfully updated to v1.2!
2026-03-09 16:03:57.201 | DEBUG    | cwl_loader:load_cwl_from_yaml:145 - Parsing the raw CWL document to the CWL Utils DOM...
2026-03-09 16:03:58.648 | DEBUG    | cwl_loader:load_cwl_from_yaml:158 - Raw CWL document successfully parsed to the CWL Utils DOM!
2026-03-09 16:03:58.648 | DEBUG    | cwl_loader:load_cwl_from_yaml:160 - Dereferencing the steps[].run...
2026-03-09 16:03:58.648 | DEBUG    | cwl_loader:_on_process:78 - Checking if #clt must be externally imported...
2026-03-09 16:03:58.648 | DEBUG    | cwl_loader:_on_process:82 - run_url:  - uri: io://
2026-03-09 16:03:58.648 | DEBUG    | cwl_loader:load_cwl_from_yaml:167 - steps[].run successfully dereferenced! Dereferencing the FQNs...
2026-03-09 16:03:58.648 | DEBUG    | cwl_loader:load_cwl_from_yaml:171 - CWL document successfully dereferenced! Now verifying steps[].run integrity...
2026-03-09 16:03:58.648 | DEBUG    | cwl_loader:load_cwl_from_yaml:175 - All steps[].run link are resolvable! 
2026-03-09 16:03:58.648 | DEBUG    | cwl_loader:load_cwl_from_yaml:178 - Sorting Process instances by dependencies....
2026-03-09 16:03:58.648 | DEBUG    | cwl_loader:load_cwl_from_yaml:180 - Sorting process is over.
2026-03-09 16:03:58.648 | SUCCESS  | transpiler_mate.cli:oci_annotations:202 - Metadata successfully transpiled!
2026-03-09 16:03:58.648 | INFO     | transpiler_mate.cli:oci_annotations:203 - Serializing metadata...
2026-03-09 16:03:58.648 | SUCCESS  | transpiler_mate.cli:oci_annotations:212 - Metadata successfully serialized to annotations.json.
2026-03-09 16:03:58.649 | SUCCESS  | transpiler_mate.cli:wrapper:48 - ------------------------------------------------------------------------
2026-03-09 16:03:58.649 | SUCCESS  | transpiler_mate.cli:wrapper:49 - SUCCESS
2026-03-09 16:03:58.649 | SUCCESS  | transpiler_mate.cli:wrapper:50 - ------------------------------------------------------------------------
2026-03-09 16:03:58.649 | INFO     | transpiler_mate.cli:wrapper:59 - Total time: 1.4669 seconds
2026-03-09 16:03:58.649 | INFO     | transpiler_mate.cli:wrapper:60 - Finished at: 2026-03-09T16:03:58.649
```
