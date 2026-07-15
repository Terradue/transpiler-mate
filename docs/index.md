# Transpiler Mate

Transpiler Mate is a Python library and CLI that extracts [Schema.org/SoftwareApplication](https://schema.org/SoftwareApplication) metadata from annotated [CWL](https://www.commonwl.org/) documents and converts it into publication-ready formats.

It can generate CodeMeta, DataCite, OGC API - Records, OGC API - Processes, Markdown workflow documentation, and OCI annotations. It can also bundle CWL documents with external references resolved, publish records to InvenioRDM, and bump CWL software versions according to Semantic Versioning.

## Documentation map

This documentation is organized with the [Diataxis](https://diataxis.fr/) framework:

- [Tutorials](tutorials/index.md) are for learning a workflow from start to finish.
- [How-to guides](how-to-guides/index.md) are for completing a concrete task.
- [Reference](reference/index.md) is for looking up commands, schemas, crosswalks, and generated API details.
- [Explanation](explanation/index.md) is for understanding the metadata model and conventions behind the tool.

## Installation

```bash
pip install transpiler-mate
```

## Common commands

```bash
transpiler-mate codemeta ./metadata.cwl --output ./dist/codemeta.json
transpiler-mate datacite ./metadata.cwl --output ./dist/datacite.json
transpiler-mate ogcrecord ./metadata.cwl --output ./dist/record.json
transpiler-mate markdown ./workflow.cwl --workflow-id main --output ./docs
transpiler-mate oci-annotations ./workflow.cwl --workflow-id main --output annotations.json
transpiler-mate bundle ./workflow.cwl --output ./dist/bundle.cwl
```

Use the [how-to guides](how-to-guides/index.md) for task-specific options and examples.
