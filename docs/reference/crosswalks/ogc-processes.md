# https://schema.org/SoftwareApplication and CWL Process Crosswalk for OGC API - Processes

The OGC API - Processes transpiler emits a static process descriptor from the annotated CWL document. The root object combines `https://schema.org/SoftwareApplication` metadata with one `processes` entry for each CWL process returned by the CWL loader.

## Root properties

```
OGC API - Processes descriptor
```

| Source                                    | OGC API - Processes output |
|-------------------------------------------|-----------------------------|
| https://schema.org/softwareVersion        | software_version            |
| https://schema.org/description            | description                 |
| https://schema.org/applicationCategory    | N/A                         |
| https://schema.org/applicationSubCategory | N/A                         |
| https://schema.org/copyrightYear          | N/A                         |
| https://schema.org/dateCreated            | N/A                         |
| https://schema.org/name                   | name                        |
| https://schema.org/operatingSystem        | N/A                         |
| https://schema.org/keywords               | N/A                         |
| https://schema.org/softwareRequirements   | N/A                         |
| https://schema.org/author                 | N/A                         |
| https://schema.org/license                | [license](#license)         |
| https://schema.org/publisher              | N/A                         |
| https://schema.org/softwareHelp           | N/A                         |
| CWL processes                             | [processes](#processes)     |

The root `name`, `description`, `software_version`, and `license` properties are omitted when the source value is missing or falsey.

## <a id="license"></a> License

The root `license` field is populated from `https://schema.org/license`.

| Schema.org                    | OGC API - Processes output |
|-------------------------------|-----------------------------|
| https://schema.org/identifier | license.identifier          |
| https://schema.org/name       | license.name                |
| https://schema.org/url        | license.url                 |

When `license` is a single `CreativeWork`, the transpiler serializes the model to an object. For non-model values, the current transpiler copies the value as-is.

## <a id="processes"></a> Processes

The CLI parses the CWL document with `cwl_loader.load_cwl_from_yaml`. If the loader returns a list, each process is emitted; otherwise the single returned process is emitted.

Each process is stored under `processes.{process.id}`.

| CWL process property | OGC API - Processes output |
|----------------------|-----------------------------|
| id                   | processes object key        |
| class_               | processes.{id}.class_       |
| label                | processes.{id}.label        |
| doc                  | processes.{id}.doc          |
| inputs               | processes.{id}.inputs       |
| outputs              | processes.{id}.outputs      |

The `class_`, `label`, and `doc` properties are omitted when the CWL process does not provide them.

## Inputs and outputs

The current transpiler delegates CWL input and output conversion to `cwl2ogc.BaseCWLtypes2OGCConverter`.

| CWL process property | Converter method | OGC API - Processes output |
|----------------------|------------------|-----------------------------|
| inputs               | get_inputs()     | processes.{id}.inputs       |
| outputs              | get_outputs()    | processes.{id}.outputs      |

The resulting `inputs` and `outputs` objects are therefore determined by `cwl2ogc`, including fields such as `schema`, `metadata`, `minOccurs`, `maxOccurs`, `valuePassing`, `title`, and `description`.
