# CWL Metadata code conventions

```yaml
$namespaces:
  s: https://schema.org/
'@type': s:SoftwareApplication
```

The following is the recommended ordering for all CWL files:

## The software itself

| Property      | Mandatory |
|---------------|-----------|
| Name          | YES       |
| Description   | YES       |
| Creation date | YES       |
| License(s)    | YES       |

```yaml
s:name: My shiny workflow
s:description: There's no workflow on earth like this one that solves NP-complete problems.
s:dateCreated: '2025-01-01'
s:license:
  '@type': s:CreativeWork
  s:identifier: CC-BY-4.0
```

Please note that the `traspiler-mate` is able to automatically deduce, for the `s:license`, all the license informations according to the License IDs from [SPDX License List](https://spdx.org/licenses/).

## Discoverability and citation

| Property                  | Mandatory |
|---------------------------|-----------|
| Unique identifier         | YES       |
| Alternative identifier(s) | YES       |
| Keywords                  | no        |

Identifiers can be _ISBNs_, _GTIN_ codes, _UUID_s, _DOI_s, etc.

```yaml
s:identifier: 10.5072/zenodo.393958
s:sameAs: https://handle.test.datacite.org/10.5072/zenodo.393958
s:keywords:
- CWL
- Workflow
- Earth Observation
- '@type': s:DefinedTerm
  s:description: delineation
  s:name: application-type
- '@type': s:DefinedTerm
  s:description: hydrology
  s:name: domain
- '@type': s:DefinedTerm
  s:inDefinedTermSet: https://gcmd.earthdata.nasa.gov/kms/concepts/concept_scheme/sciencekeywords
  s:termCode: 959f1861-a776-41b1-ba6b-d23c71d4d1eb
```

## Run-time environment

| Property              | Mandatory |
|-----------------------|-----------|
| Operating system      | no        |
| Software requirements | no        |

```yaml
s:operatingSystem:
- Linux
- macOS
s:softwareRequirements:
- https://cwltool.readthedocs.io/en/latest/
- https://www.python.org/
```

## Current version of the software

| Property         | Mandatory |
|------------------|-----------|
| Version number   | YES       |
| Application help | YES       |

```yaml
s:softwareVersion: 3.0.0
s:softwareHelp:
- '@type': s:CreativeWork
  s:name: User Manual
  s:url: https://meoga-shiny-workflow.readthedocs.io/en/latest/
- '@type': s:CreativeWork
  s:name: Admin Manual
  s:url: https://meoga.io/meoga/shiny-workflow/admin
```

## Publisher

| Property          | Mandatory |
|-------------------|-----------|
| Name              | YES       |
| E-mail address    | no        |
| Unique identifier | no        |

```yaml
s:publisher:
  '@type': s:Organization
  s:name: Make Earth Observation Great Again
  s:email: info@meoga.com
  s:identifier: https://ror.org/9999cx000
```

## Authors & Contributor

While `s:author` is mandatory, `s:contributor` is not.

| Property       | Mandatory |
|----------------|-----------|
| Given name     | YES       |
| Family name    | YES       |
| E-mail address | YES       |
| URI            | no        |
| Affiliation    | YES       |

### Affiliations

| Property          | Mandatory |
|-------------------|-----------|
| Name              | YES       |
| E-mail address    | no        |
| Unique identifier | no        |

```yaml
s:author:
- '@type': s:Person
  s:givenName: Lex
  s:familyName: Luthor
  s:email: lex.luthor@luthorcorp.com
  s:identifier: https://orcid.org/0000-9999-0000-9999
  s:affiliation:
    '@type': s:Organization
    s:name: Luthor Corp
    s:identifier: https://ror.org/0000cx000

s:contributor:
- '@type': s:Person
  s:givenName: Clark
  s:familyName: Kent
  s:email: clark.kent@dailyplanet.com
  s:identifier: https://orcid.org/0000-9999-0000-9999
  s:affiliation:
    '@type': s:Organization
    s:name: Daily Planet
    s:identifier: https://ror.org/0000cx000
```
