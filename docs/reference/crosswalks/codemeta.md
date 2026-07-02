# https://schema.org/SoftwareApplication Crosswalk for CodeMeta

The [CodeMeta](https://codemeta.github.io/index.html) spec defines metadata for software projects or software applications.

## Root properties:

```
@type: SoftwareApplication
```

| Schema.org                                | CodeMeta                       |
|-------------------------------------------|--------------------------------|
| https://schema.org/softwareVersion        | softwareVersion                |
| https://schema.org/description            | description                    |
| https://schema.org/applicationCategory    | applicationCategory            |
| https://schema.org/applicationSubCategory | applicationCategory            |
| https://schema.org/copyrightYear          | copyrightYear                  |
| https://schema.org/dateCreated            | dateCreated                    |
| https://schema.org/name                   | name                           |
| https://schema.org/operatingSystem        | operatingSystem                |
| https://schema.org/keywords               | keywords                       |
| https://schema.org/softwareRequirements   | softwareRequirements           |
| https://schema.org/author                 | [author](#author)              |
| https://schema.org/license                | [license](#license)            |
| https://schema.org/publisher              | [publisher](#publisher)        |
| https://schema.org/softwareHelp           | [softwareHelp](#software-help) |

## <a id="author"></a> Author

```
@type: Person
```

| Schema.org                     | CodeMeta                    |
|--------------------------------|-----------------------------|
| https://schema.org/affiliation | [affiliation](#affiliation) |
| https://schema.org/email       | email                       |
| https://schema.org/familyName  | familyName                  |
| https://schema.org/givenName   | givenName                   |
| https://schema.org/identifier  | identifier                  |
  
### <a id="affiliation"></a> Affiliation

```
@type: Organization
```

| Schema.org                    | CodeMeta   |
|-------------------------------|------------|
| https://schema.org/identifier | identifier |
| https://schema.org/name       | name       |

## <a id="license"></a> License

```
@type: CreativeWork
```

| Schema.org                    | CodeMeta   |
|-------------------------------|------------|
| https://schema.org/identifier | identifier |
| https://schema.org/name       | name       |
| https://schema.org/url        | url        |

## <a id="publisher"></a> Publisher

```
@type: Organization
```

| Schema.org                    | CodeMeta   |
|-------------------------------|------------|
| https://schema.org/email      | email      |
| https://schema.org/identifier | identifier |
| https://schema.org/name       | name       |

## <a id="software-help"></a> Software Help

```
@type: CreativeWork
```

| Schema.org              | CodeMeta |
|-------------------------|----------|
| https://schema.org/name | name     |
| https://schema.org/url  | url      |
