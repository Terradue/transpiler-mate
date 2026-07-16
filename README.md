# Transpiler Mate

[![PyPI - Version](https://img.shields.io/pypi/v/transpiler-mate.svg)](https://pypi.org/project/transpiler-mate)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/transpiler-mate.svg)](https://pypi.org/project/transpiler-mate)

Transpiler Mate is a Python library and CLI that extracts `schema.org/SoftwareApplication` metadata from annotated CWL documents and converts it into publication-ready formats.

## What It Does

Given an input CWL metadata source, Transpiler Mate can:

- Generate **CodeMeta** JSON-LD.
- Generate **DataCite** metadata payloads.
- Generate **OGC API - Records** payloads.
- Generate **Markdown** documentation for workflows.
- Generate **OCI Annotations**.
- Bundle CWL documents into self-contained files with external references resolved.
- Publish records to **InvenioRDM**.
- Bump semantic versions in metadata files.

Documentation: <https://terradue.github.io/transpiler-mate/>

## Supported Outputs

- CodeMeta: <https://codemeta.github.io/>
- DataCite Metadata: <https://inveniordm.docs.cern.ch/reference/metadata/#metadata>
- OGC API - Records: <https://ogcapi.ogc.org/records/>
- OCI Annotations: <https://oras.land/docs/how_to_guides/manifest_annotations/>
- InvenioRDM: <https://inveniosoftware.org/products/rdm/>

## Requirements

- Python `>= 3.10`

## Installation

### From source (recommended for development)

```bash
git clone https://github.com/Terradue/transpiler-mate.git
cd transpiler-mate
pip install -e .
```

### Install tooling for local workflows

```bash
pip install hatch ruff
```

## CLI Usage

Entry point:

```bash
transpiler-mate --help
```

Main commands:

- `transpiler-mate codemeta <source> [--code-repository URL] [--output codemeta.json]`
- `transpiler-mate datacite <source> [--output datacite.json]`
- `transpiler-mate ogcrecord <source> [--output record.json]`
- `transpiler-mate markdown <source> --workflow-id <id> [--output DIR] [--code-repository URL]`
- `transpiler-mate oci-annotations <source> --workflow-id <id> [--image-source URL] [--image-revision ] [--output annotations.json]`
- `transpiler-mate invenio-publish <source> --base-url URL --auth-token TOKEN [--attach FILE ...]`
- `transpiler-mate bump-version <source> [--version-part major|minor|patch|build|pre-release]`
- `transpiler-mate bundle <source> [--output bundle.cwl] [--oci-hostname HOST] [--oci-username USER] [--oci-password PASSWORD] [--oauth2-bearer TOKEN]`

### Examples

Generate CodeMeta:

```bash
transpiler-mate codemeta ./metadata.cwl --output ./dist/codemeta.json
```

Generate DataCite metadata:

```bash
transpiler-mate datacite ./metadata.cwl --output ./dist/datacite.json
```

Generate OGC Record:

```bash
transpiler-mate ogcrecord ./metadata.cwl --output ./dist/record.json
```

Generate Markdown documentation:

```bash
transpiler-mate markdown ./workflow.cwl --workflow-id main --output ./docs
```

Bundle a CWL document and resolve its external references:

```bash
transpiler-mate bundle ./workflow.cwl --output ./dist/bundle.cwl
```

The `bundle` command was migrated from the [CWL Loader CLI](https://terradue.github.io/cwl-loader/).

Publish to InvenioRDM:

```bash
export INVENIO_AUTH_TOKEN="<token>"
transpiler-mate invenio-publish ./metadata.cwl --base-url https://invenio.example.org --auth-token "$INVENIO_AUTH_TOKEN"
```

## Development

Run lint and formatting checks:

```bash
hatch run dev:check
hatch run dev:lint
```

Run tests for one interpreter:

```bash
hatch run test.py3.12:test-q
```

Run full Hatch test matrix (local environment permitting):

```bash
hatch run test:test-q
```

## Project Tasks

`Taskfile.yaml` includes helper tasks for schema/model generation and quality checks:

- `task test`
- `task check`
- `task lint`

## License

[![Apache License, Version 2.0](https://img.shields.io/badge/license-Apache%20License%202.0-blue)](https://www.apache.org/licenses/LICENSE-2.0)
