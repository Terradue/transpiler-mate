# https://schema.org/SoftwareApplication Crosswalk for OGC API - Records

The [OGC API - Records](https://ogcapi.ogc.org/records/) spec defines discovery of geospatial resources by standardizing the way collections of descriptive information about the resources (metadata) are exposed.

## Root properties:

```
RecordGeoJSONProperties
```

| Schema.org                                | CodeMeta                |
|-------------------------------------------|-------------------------|
| https://schema.org/softwareVersion        | N/A                     |
| https://schema.org/description            | description             |
| https://schema.org/applicationCategory    | N/A                     |
| https://schema.org/applicationSubCategory | N/A                     |
| https://schema.org/copyrightYear          | N/A                     |
| https://schema.org/dateCreated            | created                 |
| https://schema.org/name                   | title                   |
| https://schema.org/operatingSystem        | N/A                     |
| https://schema.org/keywords               | [keywords](#keywords)   |
| https://schema.org/softwareRequirements   | N/A                     |
| https://schema.org/author                 | N/A                     |
| https://schema.org/license                | [license](#license)     |
| https://schema.org/publisher              | [publisher](#publisher) |
| https://schema.org/softwareHelp           | N/A                     |

## <a id="keywords"></a> Keywords

### String keywords

Each `str` instance will be part of the `keywords` property of `RecordGeoJSONProperties`.

### https://schema.org/DefinedTerm keywords

Each `https://schema.org/DefinedTerm` keyword will be transpiled as item of the `themes.concepts` property of `RecordGeoJSONProperties` if:

- `https://schema.org/inDefinedTermSet` will points to https://gcmd.earthdata.nasa.gov/kms/concepts/concept_scheme/sciencekeywords;
- `https://schema.org/termCode` is a valid concept UUID that points to an existing `https://cmr.earthdata.nasa.gov/kms/concept/{UUID}`.

i.e. given an input keyword like the one below:

```yaml
s:keywords:
- '@type': s:DefinedTerm
  s:inDefinedTermSet: https://gcmd.earthdata.nasa.gov/kms/concepts/concept_scheme/sciencekeywords
  s:termCode: 959f1861-a776-41b1-ba6b-d23c71d4d1eb
```

Resulting as an element like the one below:

```json
"themes": [
    {
        "concepts": [
            {
                "id": "EARTH SCIENCE",
                "description": "EARTH SCIENCE",
                "url": "https://cmr.earthdata.nasa.gov/kms/concept/959f1861-a776-41b1-ba6b-d23c71d4d1eb"
            },
            {
                "id": "TERRESTRIAL HYDROSPHERE",
                "description": "EARTH SCIENCE > TERRESTRIAL HYDROSPHERE",
                "url": "https://cmr.earthdata.nasa.gov/kms/concept/959f1861-a776-41b1-ba6b-d23c71d4d1eb"
            },
            {
                "id": "SURFACE WATER",
                "description": "EARTH SCIENCE > TERRESTRIAL HYDROSPHERE > SURFACE WATER",
                "url": "https://cmr.earthdata.nasa.gov/kms/concept/959f1861-a776-41b1-ba6b-d23c71d4d1eb"
            },
            {
                "id": "SURFACE WATER FEATURES",
                "description": "EARTH SCIENCE > TERRESTRIAL HYDROSPHERE > SURFACE WATER > SURFACE WATER FEATURES",
                "url": "https://cmr.earthdata.nasa.gov/kms/concept/959f1861-a776-41b1-ba6b-d23c71d4d1eb"
            }
        ],
        "scheme": "https://gcmd.earthdata.nasa.gov/kms/concepts/concept_scheme/sciencekeywords"
    }
]
```

## <a id="license"></a> License

the `license` field is a root property of `RecordGeoJSONProperties`.

| Schema.org                    | CodeMeta   |
|-------------------------------|------------|
| https://schema.org/identifier | N/A        |
| https://schema.org/name       | N/A        |
| https://schema.org/url        | url        |

## <a id="publisher"></a> Publisher

the `contacts` field is a root property of `RecordGeoJSONProperties`.

| Schema.org                    | CodeMeta   |
|-------------------------------|------------|
| https://schema.org/email      | email      |
| https://schema.org/identifier | N/A        |
| https://schema.org/name       | N/A        |
