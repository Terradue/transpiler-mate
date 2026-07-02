# https://schema.org/SoftwareApplication Crosswalk for Invenio Records Metadata

The Invenio [Metadata](https://inveniordm.docs.cern.ch/reference/metadata/#metadata) spec defines a bibliographic record in [InvenioRDM](https://inveniordm.docs.cern.ch/).

## Root properties:

```
Metadata
```

| Schema.org                                | Metadata                |
|-------------------------------------------|-------------------------|
| https://schema.org/identifier             | N/A                     |
| https://schema.org/softwareVersion        | version                 |
| https://schema.org/description            | description             |
| https://schema.org/applicationCategory    | N/A                     |
| https://schema.org/applicationSubCategory | N/A                     |
| https://schema.org/copyrightYear          | N/A                     |
| https://schema.org/dateCreated            | N/A                     |
| https://schema.org/name                   | title                   |
| https://schema.org/operatingSystem        | N/A                     |
| https://schema.org/keywords               | N/A                     |
| https://schema.org/softwareRequirements   | N/A                     |
| https://schema.org/author                 | [author](#author)       |
| https://schema.org/license                | N/A                     |
| https://schema.org/publisher              | [publisher](#publisher) |
| https://schema.org/softwareHelp           | N/A                     |

## <a id="author"></a> Author

```
PersonOrOrg
```


| Schema.org                     | Metadata                    |
|--------------------------------|-----------------------------|
| https://schema.org/affiliation | [affiliation](#affiliation) |
| https://schema.org/email       | email                       |
| https://schema.org/familyName  | name                        |
| https://schema.org/givenName   | name                        |
| https://schema.org/identifier  | identifier                  |


The `identifier` is transpiled to `Identifier` from the URL, i.e. `https://orcid.org/0009-0000-1342-9736` becomes

```
{
    "scheme": "orcid",
    "identifier": "0009-0000-1342-9736"
}
```
  
### <a id="affiliation"></a> Affiliation

```
Affiliation
```

| Schema.org                    | Metadata   |
|-------------------------------|------------|
| https://schema.org/identifier | id         |
| https://schema.org/name       | name       |

## <a id="publisher"></a> Publisher

Publihser name is in the root properties of `Metadata`

| Schema.org                    | Metadata   |
|-------------------------------|------------|
| https://schema.org/email      | N/A        |
| https://schema.org/identifier | N/A        |
| https://schema.org/name       | name       |
