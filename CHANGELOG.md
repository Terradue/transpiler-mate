# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

### Changed

### Deprecated

### Removed

### Fixed

### Security

## [0.47.0] - 2026-07-15

### Added

- Added the `bundle` CLI command, migrated from the [CWL Loader CLI](https://terradue.github.io/cwl-loader/), to create self-contained CWL documents with external references resolved.
- Added unit and CLI integration tests for CWL bundling, session adapters, authentication options, serialization, and default output handling.

### Changed

- Bumped `cwl-loader` from `0.20.0` to `0.21.0` and added `session-adapters` for HTTP(S), local file, S3, and OCI reference resolution.

## [0.46.0] - 2026-06-26

### Fixed

- `s:description` can't be a multi-line text in OCI annotations

## [0.45.0] - 2026-06-16

### Changed

- Bumped `click` from `8.3.3` to `8.4.1`.
- Bumped `cwl-loader` from `0.18.0` to `0.20.0`.

## [0.44.0] - 2026-05-13

### Added

- Added an `ogcprocesses` CLI command to generate OGC API - Processes JSON from CWL workflows.
- Added OGC API - Processes documentation and OCI Annotations schema documentation.
- Added tests for the refactored OGC Records CLI path and default output handling.

### Changed

- Refactored CLI commands into dedicated modules under `transpiler_mate.cli`.
- Moved OGC Records code under `transpiler_mate.ogcapi.records`.
- Reworked Taskfile usage to rely on shared remote task definitions.
- Updated runtime dependencies, including `click`, `cwl-loader`, and `cwl2ogc`.

### Fixed

- Fixed OGC API Processes command/module naming and registration.
- Fixed lint issues introduced during the CLI and OGC package refactor.

## [0.43.0] - 2026-04-08

### Changed

- Updated GitHub Actions workflow dependencies to `actions/checkout@v6` and `actions/setup-python@v6`.
- Updated project dependencies, including `cwl-loader` and the `ruamel.yaml` constraint.

### Fixed

- Fixed Markdown type rendering when a CWL parent process is not available.

## [0.42.0] - 2026-04-07

### Changed

- Bumped release metadata for the next package version.

## [0.41.0] - 2026-03-31

### Changed

- Changed generated OGC Record links to use the canonical `via` relation instead of `help`.

## [0.40.0] - 2026-03-30

### Added

- Added support for default values on OGC API Record type fields.

### Fixed

- Removed unused imports.

## [0.39.0] - 2026-03-30

### Fixed

- Fixed handling for concepts whose title is `None`.

## [0.38.0] - 2026-03-30

### Added

- Added OGC API Processes JSON Schema diagrams for generated workflow inputs and outputs.
- Added license resolution from both SPDX identifiers and SPDX URLs.

### Fixed

- Fixed duplicated keys in generated output.
- Fixed license serialization in OGC API Records to prefer resolved SPDX identifiers.

## [0.37.0] - 2026-03-26

### Fixed

- Fixed OGC API Record metadata assessment.
- Fixed generated model declaration order from `datamodel-codegen`.
- Removed unused imports and lint issues.

## [0.36.0] - 2026-03-25

### Fixed

- Fixed OGC API Record links so relative paths are accepted, not only absolute URLs.

## [0.35.0] - 2026-03-16

### Added

- Added human-readable serialization for external schema-defined CWL types.
- Added missing license metadata.

## [0.34.0] - 2026-03-16

### Added

- Added links for input and output types in generated Markdown documentation.
- Added direct enum links in generated Markdown documentation.

### Fixed

- Fixed Python 3.10 compatibility by avoiding Python 3.12-only f-string syntax.
- Fixed tests and lint issues.

## [0.33.0] - 2026-03-13

### Added

- Added Dependabot configuration for Python and GitHub Actions dependencies.

### Changed

- Reduced redundant generated Markdown sections and added direct links to diagram documentation.

### Fixed

- Fixed generated Markdown ordering so `Run in step` sections are easier to read.

## [0.32.0] - 2026-03-11

### Added

- Added a Requirements section to generated Workflow Markdown documentation.

### Changed

- Omitted the `Execution usage example` section for ExpressionTool documentation.

## [0.31.0] - 2026-03-10

### Fixed

- Fixed OCI annotations output to include the required `$metadata` root key.

## [0.30.0] - 2026-03-10

### Fixed

- Fixed Markdown indentation for MkDocs rendering.

## [0.29.0] - 2026-03-10

### Fixed

- Fixed Markdown indentation for MkDocs visualization.

### Changed

- Updated README release documentation.

## [0.28.0] - 2026-03-09

### Added

- Added the initial Python library and CLI for extracting `schema.org/SoftwareApplication` metadata from annotated CWL documents.
- Added CodeMeta, DataCite, OGC API Records, Markdown, OCI Annotations, and InvenioRDM publication support.
- Added JSON-LD load and dump support on the Pydantic metadata model.
- Added configurable Invenio base URLs, environment-based Invenio auth tokens, multiple file attachments, and bearer token obfuscation in logs.
- Added generated Pydantic models from JSON Schema for supported metadata formats.
- Added SPDX license resolution, role support, contributor metadata, thumbnail support, and SoftwareSourceCode generation from repository URLs.
- Added Markdown workflow documentation generation, including software help, team members, workflow steps, and CLI documentation.
- Added a semantic version bump command that preserves YAML ordering and comments.
- Added OCI Annotations support with image source and image revision fields.
- Added project documentation, crosswalks, conventions, publishing workflows, CI, linting, and tests.

### Changed

- Replaced the ScienceKeywords transpiler prototype with the broader OGC Records transpiler.
- Renamed ORAS annotations support to OCI annotations.
- Relicensed the project under Apache-2.0.
- Isolated the RecordGeoJSON schema from unrelated OGC API schemas.
- Updated OGC API Record models and allowed extra model fields.

### Fixed

- Fixed Invenio naming and documentation references after the Zenodo-to-Invenio rename.
- Fixed invalid CodeMeta output and broken metadata mappings.
- Fixed the missing `email-validator` dependency.
- Fixed DOI handling by supplying a temporary URN identifier until a DOI is available.
- Fixed Markdown serialization issues for CWL `CommandLineBinding` and `InputArraySchema`.
- Fixed generated model defaults and declaration order from `datamodel-codegen`.
- Fixed README, documentation, lint, and release metadata issues.

[unreleased]: https://github.com/Terradue/transpiler-mate/compare/v0.47.0...HEAD
[0.47.0]: https://github.com/Terradue/transpiler-mate/compare/v0.46.0...v0.47.0
[0.46.0]: https://github.com/Terradue/transpiler-mate/compare/v0.45.0...v0.46.0
[0.45.0]: https://github.com/Terradue/transpiler-mate/compare/v0.44.0...v0.45.0
[0.44.0]: https://github.com/Terradue/transpiler-mate/compare/v0.43.0...v0.44.0
[0.43.0]: https://github.com/Terradue/transpiler-mate/compare/v0.42.0...v0.43.0
[0.42.0]: https://github.com/Terradue/transpiler-mate/compare/v0.41.0...v0.42.0
[0.41.0]: https://github.com/Terradue/transpiler-mate/compare/v0.40.0...v0.41.0
[0.40.0]: https://github.com/Terradue/transpiler-mate/compare/v0.39.0...v0.40.0
[0.39.0]: https://github.com/Terradue/transpiler-mate/compare/v0.38.0...v0.39.0
[0.38.0]: https://github.com/Terradue/transpiler-mate/compare/v0.37.0...v0.38.0
[0.37.0]: https://github.com/Terradue/transpiler-mate/compare/v0.36.0...v0.37.0
[0.36.0]: https://github.com/Terradue/transpiler-mate/compare/v0.35.0...v0.36.0
[0.35.0]: https://github.com/Terradue/transpiler-mate/compare/v0.34.0...v0.35.0
[0.34.0]: https://github.com/Terradue/transpiler-mate/compare/v0.33.0...v0.34.0
[0.33.0]: https://github.com/Terradue/transpiler-mate/compare/v0.32.0...v0.33.0
[0.32.0]: https://github.com/Terradue/transpiler-mate/compare/v0.31.0...v0.32.0
[0.31.0]: https://github.com/Terradue/transpiler-mate/compare/v0.30.0...v0.31.0
[0.30.0]: https://github.com/Terradue/transpiler-mate/compare/v0.29.0...v0.30.0
[0.29.0]: https://github.com/Terradue/transpiler-mate/compare/v0.28.0...v0.29.0
[0.28.0]: https://github.com/Terradue/transpiler-mate/releases/tag/v0.28.0
