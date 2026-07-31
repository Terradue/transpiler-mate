# Schema.org SoftwareApplication crosswalk for InvenioRDM

The InvenioRDM [metadata](https://inveniordm.docs.cern.ch/reference/metadata/#metadata)
specification defines a bibliographic record.

## Root properties

```
Metadata
```

| Schema.org                                | InvenioRDM metadata          |
|-------------------------------------------|------------------------------|
| https://schema.org/identifier             | N/A                          |
| https://schema.org/softwareVersion        | version                      |
| https://schema.org/description            | description                  |
| https://schema.org/applicationCategory    | N/A                          |
| https://schema.org/applicationSubCategory | N/A                          |
| https://schema.org/copyrightYear          | N/A                          |
| https://schema.org/dateCreated            | N/A                          |
| https://schema.org/name                   | title                        |
| https://schema.org/operatingSystem        | N/A                          |
| https://schema.org/keywords               | N/A                          |
| https://schema.org/softwareRequirements   | N/A                          |
| https://schema.org/author                 | creators                     |
| https://schema.org/contributor            | contributors                 |
| https://schema.org/license                | N/A                          |
| https://schema.org/publisher              | [publisher](#publisher)      |
| https://schema.org/softwareHelp           | N/A                          |

## Authors and contributors

```
Creator
```

| Schema.org                     | InvenioRDM Creator           |
|--------------------------------|------------------------------|
| https://schema.org/affiliation | [affiliations](#affiliation) |
| https://schema.org/familyName  | person_or_org.family_name    |
| https://schema.org/givenName   | person_or_org.given_name     |
| https://schema.org/identifier  | person_or_org.identifiers    |

The `identifier` is transpiled to `Identifier` from the URL. For example,
`https://orcid.org/0009-0000-1342-9736` becomes:

```json
{
    "scheme": "orcid",
    "identifier": "0009-0000-1342-9736"
}
```

When an author or contributor is represented by a Schema.org `Role`,
`additionalType` must contain a canonical
[CRediT](https://credit.niso.org/contributor-roles/) role URL. The URL is
mapped to `role.id`; `roleName` is descriptive and is not used for lookup.

### CRediT roles

CRediT and the InvenioRDM/DataCite contributor-role vocabulary are not
one-to-one. The following table records the nearest InvenioRDM role selected
by Transpiler Mate.

| CRediT role | Canonical `additionalType` | InvenioRDM `role.id` |
|-------------|----------------------------|-----------------------|
| Conceptualization | `https://credit.niso.org/contributor-roles/conceptualization/` | `projectleader` |
| Data curation | `https://credit.niso.org/contributor-roles/data-curation/` | `datacurator` |
| Formal analysis | `https://credit.niso.org/contributor-roles/formal-analysis/` | `researcher` |
| Funding acquisition | `https://credit.niso.org/contributor-roles/funding-acquisition/` | `sponsor` |
| Investigation | `https://credit.niso.org/contributor-roles/investigation/` | `datacollector` |
| Methodology | `https://credit.niso.org/contributor-roles/methodology/` | `researcher` |
| Project administration | `https://credit.niso.org/contributor-roles/project-administration/` | `projectmanager` |
| Resources | `https://credit.niso.org/contributor-roles/resources/` | `datamanager` |
| Software | `https://credit.niso.org/contributor-roles/software/` | `researcher` |
| Supervision | `https://credit.niso.org/contributor-roles/supervision/` | `supervisor` |
| Validation | `https://credit.niso.org/contributor-roles/validation/` | `researcher` |
| Visualization | `https://credit.niso.org/contributor-roles/visualization/` | `researcher` |
| Writing – original draft | `https://credit.niso.org/contributor-roles/writing-original-draft/` | `researcher` |
| Writing – review & editing | `https://credit.niso.org/contributor-roles/writing-review-editing/` | `editor` |

An absent or unrecognized `additionalType` maps to `other`.

### Affiliation

```
Affiliation
```

| Schema.org                    | InvenioRDM Affiliation |
|-------------------------------|-------------------------|
| https://schema.org/identifier | id                      |
| https://schema.org/name       | name                    |

## Publisher

The publisher name is stored in the root properties of `Metadata`.

| Schema.org                    | InvenioRDM Metadata |
|-------------------------------|---------------------|
| https://schema.org/email      | N/A                 |
| https://schema.org/identifier | N/A                 |
| https://schema.org/name       | publisher           |
