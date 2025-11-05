# Bump the CWL Software version

```
$ transpiler-mate bump-version --help
Usage: transpiler-mate bump-version [OPTIONS] SOURCE

  Bumps the CWL SW version via SemVer Spec 2.0.0.

Options:
  --version-part [major|minor|patch|build|pre_release]
                                  The version part to update  [default: MINOR]
  --help                          Show this message and exit.
```

i.e.

```
$ transpiler-mate bump-version /path/to/pattern-1.cwl
2025-11-05 01:03:02.397 | INFO     | transpiler_mate.cli:wrapper:36 - Started at: 2025-11-05T01:03:02.397
2025-11-05 01:03:02.397 | INFO     | transpiler_mate.cli:bump_version:289 - Reading metadata from /path/to/pattern-1.cwl...
2025-11-05 01:03:02.397 | DEBUG    | transpiler_mate.metadata:__init__:56 - Loading raw document from /path/to/pattern-1.cwl...
2025-11-05 01:03:02.428 | INFO     | transpiler_mate.metadata:__init__:72 - Resolving License details from SPDX License List...
2025-11-05 01:03:02.428 | INFO     | transpiler_mate.metadata:resolve_license:76 - Detected CC-BY-4.0 indexed in SPDX Licenses
2025-11-05 01:03:02.428 | SUCCESS  | transpiler_mate.cli:bump_version:318 - Software Version 0.1.0 updated to 0.2.0
2025-11-05 01:03:02.430 | DEBUG    | transpiler_mate.metadata:update:111 - JSON-LD format compacted metadata merged to the original document
2025-11-05 01:03:02.440 | INFO     | transpiler_mate.metadata:update:115 - JSON-LD format compacted metadata merged to the original '/path/to/pattern-1.cwl' document
2025-11-05 01:03:02.440 | SUCCESS  | transpiler_mate.cli:wrapper:41 - ------------------------------------------------------------------------
2025-11-05 01:03:02.440 | SUCCESS  | transpiler_mate.cli:wrapper:42 - SUCCESS
2025-11-05 01:03:02.440 | SUCCESS  | transpiler_mate.cli:wrapper:43 - ------------------------------------------------------------------------
2025-11-05 01:03:02.440 | INFO     | transpiler_mate.cli:wrapper:52 - Total time: 0.0437 seconds
2025-11-05 01:03:02.440 | INFO     | transpiler_mate.cli:wrapper:53 - Finished at: 2025-11-05T01:03:02.440
```
