# https://schema.org/SoftwareApplication Crosswalk for DataCite Metadata Properties 4.6 

The [DataCite Metadata Properties](https://inveniordm.docs.cern.ch/reference/metadata/#metadata) defines spec for Publication and Citation of Research Data and Other Research Outputs.

## Root properties:

```
Metadata
```

| Schema.org                                | Metadata                |
|-------------------------------------------|-------------------------|
| https://schema.org/identifier             | doi, identifiers        |
| https://schema.org/sameAs                 | related_identifiers     |
| https://schema.org/softwareVersion        | version                 |
| https://schema.org/description            | description             |
| https://schema.org/applicationCategory    | descriptions            |
| https://schema.org/applicationSubCategory | descriptions            |
| https://schema.org/copyrightYear          | publication_year        |
| https://schema.org/dateCreated            | N/A                     |
| https://schema.org/name                   | title                   |
| https://schema.org/operatingSystem        | N/A                     |
| https://schema.org/keywords               | N/A                     |
| https://schema.org/softwareRequirements   | N/A                     |
| https://schema.org/author                 | [author](#author)       |
| https://schema.org/license                | [rights](#rights)       |
| https://schema.org/publisher              | [publisher](#publisher) |
| https://schema.org/softwareHelp           | N/A                     |

## <a id="author"></a> Author

```
Creator
```


| Schema.org                     | Metadata                    |
|--------------------------------|-----------------------------|
| https://schema.org/affiliation | [affiliation](#affiliation) |
| https://schema.org/email       | email                       |
| https://schema.org/name        | N/A                         |
| https://schema.org/familyName  | family_name                 |
| https://schema.org/givenName   | given_name                  |
| https://schema.org/identifier  | N/A                         |

  
### <a id="affiliation"></a> Affiliation

```
Affiliation
```

| Schema.org                    | Metadata               |
|-------------------------------|------------------------|
| https://schema.org/identifier | affiliation_identifier |
| https://schema.org/name       | N/A                    |

## <a id="rights"></a> Rights

```
Right
```

| Schema.org                    | Metadata          |
|-------------------------------|-------------------|
| https://schema.org/url        | rights_uri        |
| https://schema.org/name       | rights            |
| https://schema.org/identifier | rights_identifier |

## <a id="publisher"></a> Publisher

`publisher` is in the root properties of `Metadata`

| Schema.org                    | Metadata   |
|-------------------------------|------------|
| https://schema.org/email      | N/A        |
| https://schema.org/identifier | N/A        |
| https://schema.org/name       | name       |
