# https://schema.org/SoftwareApplication and CWL Process Crosswalk for OCI Annotations

The [OCI Annotations](https://oras.land/docs/how_to_guides/manifest_annotations/) transpiler emits annotations for an OCI manifest. The output is wrapped under the `$manifest` key used by ORAS annotation files.

## Root properties

```
$manifest
```

| Source                                    | OCI annotation                              |
|-------------------------------------------|---------------------------------------------|
| https://schema.org/softwareVersion        | org.opencontainers.image.version            |
| https://schema.org/description            | org.opencontainers.image.description        |
| https://schema.org/applicationCategory    | N/A                                         |
| https://schema.org/applicationSubCategory | N/A                                         |
| https://schema.org/copyrightYear          | N/A                                         |
| https://schema.org/dateCreated            | N/A                                         |
| https://schema.org/name                   | org.opencontainers.image.title              |
| https://schema.org/operatingSystem        | N/A                                         |
| https://schema.org/keywords               | N/A                                         |
| https://schema.org/softwareRequirements   | N/A                                         |
| https://schema.org/author                 | N/A                                         |
| https://schema.org/license                | [license](#license)                         |
| https://schema.org/publisher              | N/A                                         |
| https://schema.org/softwareHelp           | N/A                                         |
| CLI `--image-source`                      | org.opencontainers.image.source             |
| CLI `--image-revision`                    | org.opencontainers.image.revision           |
| CWL selected process `id`                 | org.cwl.entrypoint                          |
| CWL selected process `cwlVersion`         | org.cwl.spec                                |
| CWL selected process `class_`             | org.cwl.type                                |

The selected CWL process is resolved from the CLI `--workflow-id` option. If the process cannot be found in the input CWL document, the command raises an error instead of emitting annotations.

`https://schema.org/description` is normalized before serialization: newline characters are replaced by spaces and carriage returns are removed.

## <a id="license"></a> License

The `org.opencontainers.image.licenses` annotation is populated from `https://schema.org/license`.

| Schema.org                    | OCI annotation                       |
|-------------------------------|--------------------------------------|
| https://schema.org/identifier | org.opencontainers.image.licenses    |
| https://schema.org/name       | N/A                                  |
| https://schema.org/url        | org.opencontainers.image.licenses    |

When `license` is a `CreativeWork`, the transpiler uses its `identifier`. When `license` is a URL value, the transpiler uses the last URL path segment. Multiple license values are joined with ` OR `.

i.e. given this input:

```yaml
s:license:
- '@type': s:CreativeWork
  s:identifier: Apache-2.0
- https://spdx.org/licenses/MIT.html
```

the resulting annotation is:

```json
{
  "$manifest": {
    "org.opencontainers.image.licenses": "Apache-2.0 OR MIT.html"
  }
}
```
