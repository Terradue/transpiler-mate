# Schema Docs

- [1. Property `root > data`](#data)
  - [1.1. Property `root > data > id`](#data_id)
  - [1.2. Property `root > data > type`](#data_type)
  - [1.3. Property `root > data > attributes`](#data_attributes)
    - [1.3.1. Property `root > data > attributes > doi`](#data_attributes_doi)
    - [1.3.2. Property `root > data > attributes > prefix`](#data_attributes_prefix)
    - [1.3.3. Property `root > data > attributes > suffix`](#data_attributes_suffix)
    - [1.3.4. Property `root > data > attributes > event`](#data_attributes_event)
    - [1.3.5. Property `root > data > attributes > identifiers`](#data_attributes_identifiers)
      - [1.3.5.1. root > data > attributes > identifiers > Identifier](#data_attributes_identifiers_items)
        - [1.3.5.1.1. Property `root > data > attributes > identifiers > identifiers items > identifierType`](#data_attributes_identifiers_items_identifierType)
        - [1.3.5.1.2. Property `root > data > attributes > identifiers > identifiers items > identifier`](#data_attributes_identifiers_items_identifier)
    - [1.3.6. Property `root > data > attributes > creators`](#data_attributes_creators)
      - [1.3.6.1. root > data > attributes > creators > Creator](#data_attributes_creators_items)
        - [1.3.6.1.1. Property `root > data > attributes > creators > creators items > name`](#data_attributes_creators_items_name)
        - [1.3.6.1.2. Property `root > data > attributes > creators > creators items > nameType`](#data_attributes_creators_items_nameType)
        - [1.3.6.1.3. Property `root > data > attributes > creators > creators items > givenName`](#data_attributes_creators_items_givenName)
        - [1.3.6.1.4. Property `root > data > attributes > creators > creators items > familyName`](#data_attributes_creators_items_familyName)
        - [1.3.6.1.5. Property `root > data > attributes > creators > creators items > nameIdentifiers`](#data_attributes_creators_items_nameIdentifiers)
          - [1.3.6.1.5.1. root > data > attributes > creators > creators items > nameIdentifiers > NameIdentifier](#data_attributes_creators_items_nameIdentifiers_items)
            - [1.3.6.1.5.1.1. Property `root > data > attributes > creators > creators items > nameIdentifiers > nameIdentifiers items > nameIdentifier`](#data_attributes_creators_items_nameIdentifiers_items_nameIdentifier)
            - [1.3.6.1.5.1.2. Property `root > data > attributes > creators > creators items > nameIdentifiers > nameIdentifiers items > nameIdentifierScheme`](#data_attributes_creators_items_nameIdentifiers_items_nameIdentifierScheme)
            - [1.3.6.1.5.1.3. Property `root > data > attributes > creators > creators items > nameIdentifiers > nameIdentifiers items > schemeURI`](#data_attributes_creators_items_nameIdentifiers_items_schemeURI)
        - [1.3.6.1.6. Property `root > data > attributes > creators > creators items > affiliation`](#data_attributes_creators_items_affiliation)
          - [1.3.6.1.6.1. root > data > attributes > creators > creators items > affiliation > Affiliation](#data_attributes_creators_items_affiliation_items)
            - [1.3.6.1.6.1.1. Property `root > data > attributes > creators > creators items > affiliation > affiliation items > affiliationIdentifier`](#data_attributes_creators_items_affiliation_items_affiliationIdentifier)
            - [1.3.6.1.6.1.2. Property `root > data > attributes > creators > creators items > affiliation > affiliation items > affiliationIdentifierScheme`](#data_attributes_creators_items_affiliation_items_affiliationIdentifierScheme)
            - [1.3.6.1.6.1.3. Property `root > data > attributes > creators > creators items > affiliation > affiliation items > schemeURI`](#data_attributes_creators_items_affiliation_items_schemeURI)
    - [1.3.7. Property `root > data > attributes > titles`](#data_attributes_titles)
      - [1.3.7.1. root > data > attributes > titles > Title](#data_attributes_titles_items)
        - [1.3.7.1.1. Property `root > data > attributes > titles > titles items > title`](#data_attributes_titles_items_title)
        - [1.3.7.1.2. Property `root > data > attributes > titles > titles items > lang`](#data_attributes_titles_items_lang)
        - [1.3.7.1.3. Property `root > data > attributes > titles > titles items > titleType`](#data_attributes_titles_items_titleType)
    - [1.3.8. Property `root > data > attributes > publisher`](#data_attributes_publisher)
      - [1.3.8.1. Property `root > data > attributes > publisher > name`](#data_attributes_publisher_name)
      - [1.3.8.2. Property `root > data > attributes > publisher > publisherIdentifier`](#data_attributes_publisher_publisherIdentifier)
      - [1.3.8.3. Property `root > data > attributes > publisher > publisherIdentifierScheme`](#data_attributes_publisher_publisherIdentifierScheme)
      - [1.3.8.4. Property `root > data > attributes > publisher > schemeURI`](#data_attributes_publisher_schemeURI)
      - [1.3.8.5. Property `root > data > attributes > publisher > lang`](#data_attributes_publisher_lang)
    - [1.3.9. Property `root > data > attributes > publicationYear`](#data_attributes_publicationYear)
      - [1.3.9.1. Property `root > data > attributes > publicationYear > oneOf > item 0`](#data_attributes_publicationYear_oneOf_i0)
      - [1.3.9.2. Property `root > data > attributes > publicationYear > oneOf > item 1`](#data_attributes_publicationYear_oneOf_i1)
    - [1.3.10. Property `root > data > attributes > subjects`](#data_attributes_subjects)
      - [1.3.10.1. root > data > attributes > subjects > Subject](#data_attributes_subjects_items)
        - [1.3.10.1.1. Property `root > data > attributes > subjects > subjects items > subject`](#data_attributes_subjects_items_subject)
        - [1.3.10.1.2. Property `root > data > attributes > subjects > subjects items > subjectScheme`](#data_attributes_subjects_items_subjectScheme)
        - [1.3.10.1.3. Property `root > data > attributes > subjects > subjects items > schemeURI`](#data_attributes_subjects_items_schemeURI)
        - [1.3.10.1.4. Property `root > data > attributes > subjects > subjects items > valueURI`](#data_attributes_subjects_items_valueURI)
        - [1.3.10.1.5. Property `root > data > attributes > subjects > subjects items > classificationCode`](#data_attributes_subjects_items_classificationCode)
        - [1.3.10.1.6. Property `root > data > attributes > subjects > subjects items > lang`](#data_attributes_subjects_items_lang)
    - [1.3.11. Property `root > data > attributes > contributors`](#data_attributes_contributors)
      - [1.3.11.1. root > data > attributes > contributors > Contributor](#data_attributes_contributors_items)
        - [1.3.11.1.1. Property `root > data > attributes > contributors > contributors items > allOf > Creator`](#data_attributes_contributors_items_allOf_i0)
        - [1.3.11.1.2. Property `root > data > attributes > contributors > contributors items > allOf > item 1`](#data_attributes_contributors_items_allOf_i1)
          - [1.3.11.1.2.1. Property `root > data > attributes > contributors > contributors items > allOf > item 1 > contributorType`](#data_attributes_contributors_items_allOf_i1_contributorType)
    - [1.3.12. Property `root > data > attributes > dates`](#data_attributes_dates)
      - [1.3.12.1. root > data > attributes > dates > Date](#data_attributes_dates_items)
        - [1.3.12.1.1. Property `root > data > attributes > dates > dates items > date`](#data_attributes_dates_items_date)
        - [1.3.12.1.2. Property `root > data > attributes > dates > dates items > dateType`](#data_attributes_dates_items_dateType)
        - [1.3.12.1.3. Property `root > data > attributes > dates > dates items > dateInformation`](#data_attributes_dates_items_dateInformation)
    - [1.3.13. Property `root > data > attributes > language`](#data_attributes_language)
    - [1.3.14. Property `root > data > attributes > types`](#data_attributes_types)
      - [1.3.14.1. Property `root > data > attributes > types > resourceType`](#data_attributes_types_resourceType)
      - [1.3.14.2. Property `root > data > attributes > types > resourceTypeGeneral`](#data_attributes_types_resourceTypeGeneral)
    - [1.3.15. Property `root > data > attributes > alternateIdentifiers`](#data_attributes_alternateIdentifiers)
      - [1.3.15.1. root > data > attributes > alternateIdentifiers > AlternateIdentifier](#data_attributes_alternateIdentifiers_items)
        - [1.3.15.1.1. Property `root > data > attributes > alternateIdentifiers > alternateIdentifiers items > alternateIdentifier`](#data_attributes_alternateIdentifiers_items_alternateIdentifier)
        - [1.3.15.1.2. Property `root > data > attributes > alternateIdentifiers > alternateIdentifiers items > alternateIdentifierType`](#data_attributes_alternateIdentifiers_items_alternateIdentifierType)
    - [1.3.16. Property `root > data > attributes > relatedIdentifiers`](#data_attributes_relatedIdentifiers)
      - [1.3.16.1. root > data > attributes > relatedIdentifiers > RelatedIdentifier](#data_attributes_relatedIdentifiers_items)
        - [1.3.16.1.1. If (relationType = null)](#autogenerated_heading_2)
          - [1.3.16.1.1.1. The following properties are required](#autogenerated_heading_3)
        - [1.3.16.1.2. Else (i.e.  relationType != null)](#autogenerated_heading_4)
          - [1.3.16.1.2.1. Must **not** be](#autogenerated_heading_5)
            - [1.3.16.1.2.1.1. Property `root > data > attributes > relatedIdentifiers > relatedIdentifiers items > else > not > anyOf > item 0`](#data_attributes_relatedIdentifiers_items_else_not_anyOf_i0)
              - [1.3.16.1.2.1.1.1. The following properties are required](#autogenerated_heading_6)
            - [1.3.16.1.2.1.2. Property `root > data > attributes > relatedIdentifiers > relatedIdentifiers items > else > not > anyOf > item 1`](#data_attributes_relatedIdentifiers_items_else_not_anyOf_i1)
              - [1.3.16.1.2.1.2.1. The following properties are required](#autogenerated_heading_7)
            - [1.3.16.1.2.1.3. Property `root > data > attributes > relatedIdentifiers > relatedIdentifiers items > else > not > anyOf > item 2`](#data_attributes_relatedIdentifiers_items_else_not_anyOf_i2)
              - [1.3.16.1.2.1.3.1. The following properties are required](#autogenerated_heading_8)
        - [1.3.16.1.3. Property `root > data > attributes > relatedIdentifiers > relatedIdentifiers items > relatedIdentifier`](#data_attributes_relatedIdentifiers_items_relatedIdentifier)
        - [1.3.16.1.4. Property `root > data > attributes > relatedIdentifiers > relatedIdentifiers items > relatedIdentifierType`](#data_attributes_relatedIdentifiers_items_relatedIdentifierType)
        - [1.3.16.1.5. Property `root > data > attributes > relatedIdentifiers > relatedIdentifiers items > relationType`](#data_attributes_relatedIdentifiers_items_relationType)
        - [1.3.16.1.6. Property `root > data > attributes > relatedIdentifiers > relatedIdentifiers items > relatedMetadataScheme`](#data_attributes_relatedIdentifiers_items_relatedMetadataScheme)
        - [1.3.16.1.7. Property `root > data > attributes > relatedIdentifiers > relatedIdentifiers items > schemeURI`](#data_attributes_relatedIdentifiers_items_schemeURI)
        - [1.3.16.1.8. Property `root > data > attributes > relatedIdentifiers > relatedIdentifiers items > schemeType`](#data_attributes_relatedIdentifiers_items_schemeType)
        - [1.3.16.1.9. Property `root > data > attributes > relatedIdentifiers > relatedIdentifiers items > resourceTypeGeneral`](#data_attributes_relatedIdentifiers_items_resourceTypeGeneral)
    - [1.3.17. Property `root > data > attributes > sizes`](#data_attributes_sizes)
      - [1.3.17.1. root > data > attributes > sizes > sizes items](#data_attributes_sizes_items)
    - [1.3.18. Property `root > data > attributes > formats`](#data_attributes_formats)
      - [1.3.18.1. root > data > attributes > formats > formats items](#data_attributes_formats_items)
    - [1.3.19. Property `root > data > attributes > version`](#data_attributes_version)
    - [1.3.20. Property `root > data > attributes > rightsList`](#data_attributes_rightsList)
      - [1.3.20.1. root > data > attributes > rightsList > Right](#data_attributes_rightsList_items)
        - [1.3.20.1.1. Property `root > data > attributes > rightsList > rightsList items > rights`](#data_attributes_rightsList_items_rights)
        - [1.3.20.1.2. Property `root > data > attributes > rightsList > rightsList items > rightsURI`](#data_attributes_rightsList_items_rightsURI)
        - [1.3.20.1.3. Property `root > data > attributes > rightsList > rightsList items > rightsIdentifier`](#data_attributes_rightsList_items_rightsIdentifier)
        - [1.3.20.1.4. Property `root > data > attributes > rightsList > rightsList items > rightsIdentifierScheme`](#data_attributes_rightsList_items_rightsIdentifierScheme)
        - [1.3.20.1.5. Property `root > data > attributes > rightsList > rightsList items > schemeURI`](#data_attributes_rightsList_items_schemeURI)
    - [1.3.21. Property `root > data > attributes > descriptions`](#data_attributes_descriptions)
      - [1.3.21.1. root > data > attributes > descriptions > Description](#data_attributes_descriptions_items)
        - [1.3.21.1.1. Property `root > data > attributes > descriptions > descriptions items > description`](#data_attributes_descriptions_items_description)
        - [1.3.21.1.2. Property `root > data > attributes > descriptions > descriptions items > descriptionType`](#data_attributes_descriptions_items_descriptionType)
    - [1.3.22. Property `root > data > attributes > geoLocations`](#data_attributes_geoLocations)
      - [1.3.22.1. root > data > attributes > geoLocations > GeoLocation](#data_attributes_geoLocations_items)
        - [1.3.22.1.1. Property `root > data > attributes > geoLocations > geoLocations items > geoLocationPoint`](#data_attributes_geoLocations_items_geoLocationPoint)
          - [1.3.22.1.1.1. Property `root > data > attributes > geoLocations > geoLocations items > geoLocationPoint > pointLongitude`](#data_attributes_geoLocations_items_geoLocationPoint_pointLongitude)
          - [1.3.22.1.1.2. Property `root > data > attributes > geoLocations > geoLocations items > geoLocationPoint > pointLatitude`](#data_attributes_geoLocations_items_geoLocationPoint_pointLatitude)
        - [1.3.22.1.2. Property `root > data > attributes > geoLocations > geoLocations items > geoLocationBox`](#data_attributes_geoLocations_items_geoLocationBox)
          - [1.3.22.1.2.1. Property `root > data > attributes > geoLocations > geoLocations items > geoLocationBox > westBoundLongitude`](#data_attributes_geoLocations_items_geoLocationBox_westBoundLongitude)
          - [1.3.22.1.2.2. Property `root > data > attributes > geoLocations > geoLocations items > geoLocationBox > eastBoundLongitude`](#data_attributes_geoLocations_items_geoLocationBox_eastBoundLongitude)
          - [1.3.22.1.2.3. Property `root > data > attributes > geoLocations > geoLocations items > geoLocationBox > southBoundLatitude`](#data_attributes_geoLocations_items_geoLocationBox_southBoundLatitude)
          - [1.3.22.1.2.4. Property `root > data > attributes > geoLocations > geoLocations items > geoLocationBox > northBoundLatitude`](#data_attributes_geoLocations_items_geoLocationBox_northBoundLatitude)
        - [1.3.22.1.3. Property `root > data > attributes > geoLocations > geoLocations items > geoLocationPlace`](#data_attributes_geoLocations_items_geoLocationPlace)
        - [1.3.22.1.4. Property `root > data > attributes > geoLocations > geoLocations items > geoLocationPolygon`](#data_attributes_geoLocations_items_geoLocationPolygon)
          - [1.3.22.1.4.1. root > data > attributes > geoLocations > geoLocations items > geoLocationPolygon > GeoLocationPolygon](#data_attributes_geoLocations_items_geoLocationPolygon_items)
            - [1.3.22.1.4.1.1. Property `root > data > attributes > geoLocations > geoLocations items > geoLocationPolygon > geoLocationPolygon items > polygonPoint`](#data_attributes_geoLocations_items_geoLocationPolygon_items_polygonPoint)
            - [1.3.22.1.4.1.2. Property `root > data > attributes > geoLocations > geoLocations items > geoLocationPolygon > geoLocationPolygon items > inPolygonPoint`](#data_attributes_geoLocations_items_geoLocationPolygon_items_inPolygonPoint)
    - [1.3.23. Property `root > data > attributes > fundingReferences`](#data_attributes_fundingReferences)
      - [1.3.23.1. root > data > attributes > fundingReferences > FundingReference](#data_attributes_fundingReferences_items)
        - [1.3.23.1.1. Property `root > data > attributes > fundingReferences > fundingReferences items > funderName`](#data_attributes_fundingReferences_items_funderName)
        - [1.3.23.1.2. Property `root > data > attributes > fundingReferences > fundingReferences items > funderIdentifier`](#data_attributes_fundingReferences_items_funderIdentifier)
        - [1.3.23.1.3. Property `root > data > attributes > fundingReferences > fundingReferences items > funderIdentifierType`](#data_attributes_fundingReferences_items_funderIdentifierType)
        - [1.3.23.1.4. Property `root > data > attributes > fundingReferences > fundingReferences items > schemeURI`](#data_attributes_fundingReferences_items_schemeURI)
        - [1.3.23.1.5. Property `root > data > attributes > fundingReferences > fundingReferences items > awardNumber`](#data_attributes_fundingReferences_items_awardNumber)
        - [1.3.23.1.6. Property `root > data > attributes > fundingReferences > fundingReferences items > awardURI`](#data_attributes_fundingReferences_items_awardURI)
        - [1.3.23.1.7. Property `root > data > attributes > fundingReferences > fundingReferences items > awardTitle`](#data_attributes_fundingReferences_items_awardTitle)
    - [1.3.24. Property `root > data > attributes > relatedItems`](#data_attributes_relatedItems)
      - [1.3.24.1. root > data > attributes > relatedItems > RelatedItem](#data_attributes_relatedItems_items)
        - [1.3.24.1.1. Property `root > data > attributes > relatedItems > relatedItems items > relatedItemType`](#data_attributes_relatedItems_items_relatedItemType)
        - [1.3.24.1.2. Property `root > data > attributes > relatedItems > relatedItems items > relationType`](#data_attributes_relatedItems_items_relationType)
        - [1.3.24.1.3. Property `root > data > attributes > relatedItems > relatedItems items > relatedItemIdentifier`](#data_attributes_relatedItems_items_relatedItemIdentifier)
          - [1.3.24.1.3.1. Property `root > data > attributes > relatedItems > relatedItems items > relatedItemIdentifier > relatedItemIdentifierType`](#data_attributes_relatedItems_items_relatedItemIdentifier_relatedItemIdentifierType)
          - [1.3.24.1.3.2. Property `root > data > attributes > relatedItems > relatedItems items > relatedItemIdentifier > relatedMetadataScheme`](#data_attributes_relatedItems_items_relatedItemIdentifier_relatedMetadataScheme)
          - [1.3.24.1.3.3. Property `root > data > attributes > relatedItems > relatedItems items > relatedItemIdentifier > schemeURI`](#data_attributes_relatedItems_items_relatedItemIdentifier_schemeURI)
          - [1.3.24.1.3.4. Property `root > data > attributes > relatedItems > relatedItems items > relatedItemIdentifier > schemeType`](#data_attributes_relatedItems_items_relatedItemIdentifier_schemeType)
        - [1.3.24.1.4. Property `root > data > attributes > relatedItems > relatedItems items > creators`](#data_attributes_relatedItems_items_creators)
          - [1.3.24.1.4.1. root > data > attributes > relatedItems > relatedItems items > creators > RelatedItemCreator](#data_attributes_relatedItems_items_creators_items)
            - [1.3.24.1.4.1.1. Property `root > data > attributes > relatedItems > relatedItems items > creators > creators items > name`](#data_attributes_relatedItems_items_creators_items_name)
            - [1.3.24.1.4.1.2. Property `root > data > attributes > relatedItems > relatedItems items > creators > creators items > nameType`](#data_attributes_relatedItems_items_creators_items_nameType)
            - [1.3.24.1.4.1.3. Property `root > data > attributes > relatedItems > relatedItems items > creators > creators items > givenName`](#data_attributes_relatedItems_items_creators_items_givenName)
            - [1.3.24.1.4.1.4. Property `root > data > attributes > relatedItems > relatedItems items > creators > creators items > familyName`](#data_attributes_relatedItems_items_creators_items_familyName)
        - [1.3.24.1.5. Property `root > data > attributes > relatedItems > relatedItems items > titles`](#data_attributes_relatedItems_items_titles)
          - [1.3.24.1.5.1. root > data > attributes > relatedItems > relatedItems items > titles > RelatedItemTitle](#data_attributes_relatedItems_items_titles_items)
            - [1.3.24.1.5.1.1. Property `root > data > attributes > relatedItems > relatedItems items > titles > titles items > title`](#data_attributes_relatedItems_items_titles_items_title)
            - [1.3.24.1.5.1.2. Property `root > data > attributes > relatedItems > relatedItems items > titles > titles items > titleType`](#data_attributes_relatedItems_items_titles_items_titleType)
        - [1.3.24.1.6. Property `root > data > attributes > relatedItems > relatedItems items > publicationYear`](#data_attributes_relatedItems_items_publicationYear)
        - [1.3.24.1.7. Property `root > data > attributes > relatedItems > relatedItems items > volume`](#data_attributes_relatedItems_items_volume)
        - [1.3.24.1.8. Property `root > data > attributes > relatedItems > relatedItems items > issue`](#data_attributes_relatedItems_items_issue)
        - [1.3.24.1.9. Property `root > data > attributes > relatedItems > relatedItems items > number`](#data_attributes_relatedItems_items_number)
        - [1.3.24.1.10. Property `root > data > attributes > relatedItems > relatedItems items > numberType`](#data_attributes_relatedItems_items_numberType)
        - [1.3.24.1.11. Property `root > data > attributes > relatedItems > relatedItems items > firstPage`](#data_attributes_relatedItems_items_firstPage)
        - [1.3.24.1.12. Property `root > data > attributes > relatedItems > relatedItems items > lastPage`](#data_attributes_relatedItems_items_lastPage)
        - [1.3.24.1.13. Property `root > data > attributes > relatedItems > relatedItems items > publisher`](#data_attributes_relatedItems_items_publisher)
        - [1.3.24.1.14. Property `root > data > attributes > relatedItems > relatedItems items > edition`](#data_attributes_relatedItems_items_edition)
        - [1.3.24.1.15. Property `root > data > attributes > relatedItems > relatedItems items > contributors`](#data_attributes_relatedItems_items_contributors)
          - [1.3.24.1.15.1. root > data > attributes > relatedItems > relatedItems items > contributors > RelatedItemContributor](#data_attributes_relatedItems_items_contributors_items)
            - [1.3.24.1.15.1.1. Property `root > data > attributes > relatedItems > relatedItems items > contributors > contributors items > allOf > RelatedItemCreator`](#data_attributes_relatedItems_items_contributors_items_allOf_i0)
            - [1.3.24.1.15.1.2. Property `root > data > attributes > relatedItems > relatedItems items > contributors > contributors items > allOf > item 1`](#data_attributes_relatedItems_items_contributors_items_allOf_i1)
              - [1.3.24.1.15.1.2.1. Property `root > data > attributes > relatedItems > relatedItems items > contributors > contributors items > allOf > item 1 > contributorType`](#data_attributes_relatedItems_items_contributors_items_allOf_i1_contributorType)

|                           |                              |
| ------------------------- | ---------------------------- |
| **Type**                  | `object`                     |
| **Required**              | No                           |
| **Additional properties** | Any type allowed             |
| **Defined in**            | #/$defs/DataCiteMetadata_4_6 |

**Description:** DataCite Metadata Schema

| Property         | Pattern | Type   | Deprecated | Definition      | Title/Description |
| ---------------- | ------- | ------ | ---------- | --------------- | ----------------- |
| + [data](#data ) | No      | object | No         | In #/$defs/Data | TODO              |

## <a name="data"></a>1. Property `root > data`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | Yes              |
| **Additional properties** | Any type allowed |
| **Defined in**            | #/$defs/Data     |

**Description:** TODO

| Property                          | Pattern | Type   | Deprecated | Definition                    | Title/Description        |
| --------------------------------- | ------- | ------ | ---------- | ----------------------------- | ------------------------ |
| + [id](#data_id )                 | No      | string | No         | -                             | -                        |
| + [type](#data_type )             | No      | string | No         | -                             | -                        |
| - [attributes](#data_attributes ) | No      | object | No         | In #/$defs/DataCiteAttributes | DataCite Metadata Schema |

### <a name="data_id"></a>1.1. Property `root > data > id`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

### <a name="data_type"></a>1.2. Property `root > data > type`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |
| **Default**  | `"dois"` |

### <a name="data_attributes"></a>1.3. Property `root > data > attributes`

|                           |                            |
| ------------------------- | -------------------------- |
| **Type**                  | `object`                   |
| **Required**              | No                         |
| **Additional properties** | Any type allowed           |
| **Defined in**            | #/$defs/DataCiteAttributes |

**Description:** DataCite Metadata Schema

| Property                                                         | Pattern | Type             | Deprecated | Definition                 | Title/Description                                                                                                                                                                                                      |
| ---------------------------------------------------------------- | ------- | ---------------- | ---------- | -------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| - [doi](#data_attributes_doi )                                   | No      | string           | No         | -                          | The full DOI (prefix + suffix)                                                                                                                                                                                         |
| - [prefix](#data_attributes_prefix )                             | No      | string           | No         | -                          | The namespace prefix                                                                                                                                                                                                   |
| - [suffix](#data_attributes_suffix )                             | No      | string           | No         | -                          | The suffix portion of the DOI                                                                                                                                                                                          |
| - [event](#data_attributes_event )                               | No      | enum (of string) | No         | -                          | Indicates a state-change action for the DOI                                                                                                                                                                            |
| + [identifiers](#data_attributes_identifiers )                   | No      | array            | No         | -                          | -                                                                                                                                                                                                                      |
| + [creators](#data_attributes_creators )                         | No      | array            | No         | -                          | The main researchers involved in producing the data, or the authors of the publication, in priority order.                                                                                                             |
| + [titles](#data_attributes_titles )                             | No      | array            | No         | -                          | Names or titles by which a resource is known. May be the title of a dataset or the name of a piece of software or an instrument.                                                                                       |
| + [publisher](#data_attributes_publisher )                       | No      | object           | No         | In #/$defs/Publisher       | The name of the entity that holds, archives, publishes, prints, distributes, releases, issues, or produces the resource. This property will be used to formulate the citation, so consider the prominence of the role. |
| + [publicationYear](#data_attributes_publicationYear )           | No      | object           | No         | In #/$defs/PublicationYear | The year when the data was or will be made publicly available.                                                                                                                                                         |
| - [subjects](#data_attributes_subjects )                         | No      | array            | No         | -                          | Subjects, keywords, classification codes, or key phrases describing the resource.                                                                                                                                      |
| - [contributors](#data_attributes_contributors )                 | No      | array            | No         | -                          | The institution or person responsible for collecting, managing, distributing, or otherwise contributing to the development of the resource.                                                                            |
| - [dates](#data_attributes_dates )                               | No      | array            | No         | -                          | Different dates relevant to the work.                                                                                                                                                                                  |
| - [language](#data_attributes_language )                         | No      | string           | No         | -                          | The primary language of the resource                                                                                                                                                                                   |
| + [types](#data_attributes_types )                               | No      | object           | No         | In #/$defs/ResourceType    | A description of the resource.                                                                                                                                                                                         |
| - [alternateIdentifiers](#data_attributes_alternateIdentifiers ) | No      | array            | No         | -                          | An identifier other than the primary Identifier applied to the resource being registered.                                                                                                                              |
| - [relatedIdentifiers](#data_attributes_relatedIdentifiers )     | No      | array            | No         | -                          | Identifiers of related resources.                                                                                                                                                                                      |
| - [sizes](#data_attributes_sizes )                               | No      | array of string  | No         | -                          | Size (e.g., bytes, pages, inches, etc.) or duration (extent), e.g., hours, minutes, days, etc., of a resource.                                                                                                         |
| - [formats](#data_attributes_formats )                           | No      | array of string  | No         | -                          | Technical format of the resources.                                                                                                                                                                                     |
| - [version](#data_attributes_version )                           | No      | string           | No         | -                          | The version number of the resources.                                                                                                                                                                                   |
| - [rightsList](#data_attributes_rightsList )                     | No      | array            | No         | -                          | Any rights information for this resource                                                                                                                                                                               |
| - [descriptions](#data_attributes_descriptions )                 | No      | array            | No         | -                          | -                                                                                                                                                                                                                      |
| - [geoLocations](#data_attributes_geoLocations )                 | No      | array            | No         | -                          | Spatial regions or named places where the data was gathered or about which the data is focused.                                                                                                                        |
| - [fundingReferences](#data_attributes_fundingReferences )       | No      | array            | No         | -                          | Information about financial support (funding) for the resource being registered.                                                                                                                                       |
| - [relatedItems](#data_attributes_relatedItems )                 | No      | array            | No         | -                          | Informations about a resource related to the one being registered.                                                                                                                                                     |

#### <a name="data_attributes_doi"></a>1.3.1. Property `root > data > attributes > doi`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** The full DOI (prefix + suffix)

#### <a name="data_attributes_prefix"></a>1.3.2. Property `root > data > attributes > prefix`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** The namespace prefix

#### <a name="data_attributes_suffix"></a>1.3.3. Property `root > data > attributes > suffix`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** The suffix portion of the DOI

#### <a name="data_attributes_event"></a>1.3.4. Property `root > data > attributes > event`

|              |                    |
| ------------ | ------------------ |
| **Type**     | `enum (of string)` |
| **Required** | No                 |

**Description:** Indicates a state-change action for the DOI

Must be one of:
* "publish"
* "register"
* "hide"

#### <a name="data_attributes_identifiers"></a>1.3.5. Property `root > data > attributes > identifiers`

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | Yes     |

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | N/A                |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be                  | Description                                                   |
| ------------------------------------------------ | ------------------------------------------------------------- |
| [Identifier](#data_attributes_identifiers_items) | The Identifier is a unique string that identifies a resource. |

##### <a name="data_attributes_identifiers_items"></a>1.3.5.1. root > data > attributes > identifiers > Identifier

|                           |                    |
| ------------------------- | ------------------ |
| **Type**                  | `object`           |
| **Required**              | No                 |
| **Additional properties** | Any type allowed   |
| **Defined in**            | #/$defs/Identifier |

**Description:** The Identifier is a unique string that identifies a resource.

| Property                                                               | Pattern | Type   | Deprecated | Definition | Title/Description |
| ---------------------------------------------------------------------- | ------- | ------ | ---------- | ---------- | ----------------- |
| + [identifierType](#data_attributes_identifiers_items_identifierType ) | No      | string | No         | -          | -                 |
| + [identifier](#data_attributes_identifiers_items_identifier )         | No      | string | No         | -          | -                 |

###### <a name="data_attributes_identifiers_items_identifierType"></a>1.3.5.1.1. Property `root > data > attributes > identifiers > identifiers items > identifierType`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |
| **Default**  | `"DOI"`  |

###### <a name="data_attributes_identifiers_items_identifier"></a>1.3.5.1.2. Property `root > data > attributes > identifiers > identifiers items > identifier`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

#### <a name="data_attributes_creators"></a>1.3.6. Property `root > data > attributes > creators`

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | Yes     |

**Description:** The main researchers involved in producing the data, or the authors of the publication, in priority order.

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | 1                  |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be            | Description                                                                           |
| ------------------------------------------ | ------------------------------------------------------------------------------------- |
| [Creator](#data_attributes_creators_items) | The main researcher involved in producing the data, or the author of the publication. |

##### <a name="data_attributes_creators_items"></a>1.3.6.1. root > data > attributes > creators > Creator

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |
| **Defined in**            | #/$defs/Creator  |

**Description:** The main researcher involved in producing the data, or the author of the publication.

| Property                                                              | Pattern | Type             | Deprecated | Definition          | Title/Description                                                                |
| --------------------------------------------------------------------- | ------- | ---------------- | ---------- | ------------------- | -------------------------------------------------------------------------------- |
| + [name](#data_attributes_creators_items_name )                       | No      | string           | No         | -                   | The full name of the creator.                                                    |
| - [nameType](#data_attributes_creators_items_nameType )               | No      | enum (of string) | No         | In #/$defs/NameType | The type of name.                                                                |
| - [givenName](#data_attributes_creators_items_givenName )             | No      | string           | No         | -                   | The personal or first name of the creator.                                       |
| - [familyName](#data_attributes_creators_items_familyName )           | No      | string           | No         | -                   | The surname or last name of the creator.                                         |
| - [nameIdentifiers](#data_attributes_creators_items_nameIdentifiers ) | No      | array            | No         | -                   | Uniquely identifies an individual or legal entity, according to various schemes. |
| - [affiliation](#data_attributes_creators_items_affiliation )         | No      | array            | No         | -                   | The organizational or institutional affiliations of the creator.                 |

###### <a name="data_attributes_creators_items_name"></a>1.3.6.1.1. Property `root > data > attributes > creators > creators items > name`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** The full name of the creator.

###### <a name="data_attributes_creators_items_nameType"></a>1.3.6.1.2. Property `root > data > attributes > creators > creators items > nameType`

|                |                    |
| -------------- | ------------------ |
| **Type**       | `enum (of string)` |
| **Required**   | No                 |
| **Defined in** | #/$defs/NameType   |

**Description:** The type of name.

Must be one of:
* "Organizational"
* "Personal"

###### <a name="data_attributes_creators_items_givenName"></a>1.3.6.1.3. Property `root > data > attributes > creators > creators items > givenName`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** The personal or first name of the creator.

###### <a name="data_attributes_creators_items_familyName"></a>1.3.6.1.4. Property `root > data > attributes > creators > creators items > familyName`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** The surname or last name of the creator.

###### <a name="data_attributes_creators_items_nameIdentifiers"></a>1.3.6.1.5. Property `root > data > attributes > creators > creators items > nameIdentifiers`

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |

**Description:** Uniquely identifies an individual or legal entity, according to various schemes.

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | N/A                |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be                                         | Description                                                                      |
| ----------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| [NameIdentifier](#data_attributes_creators_items_nameIdentifiers_items) | Uniquely identifies an individual or legal entity, according to various schemes. |

###### <a name="data_attributes_creators_items_nameIdentifiers_items"></a>1.3.6.1.5.1. root > data > attributes > creators > creators items > nameIdentifiers > NameIdentifier

|                           |                        |
| ------------------------- | ---------------------- |
| **Type**                  | `object`               |
| **Required**              | No                     |
| **Additional properties** | Any type allowed       |
| **Defined in**            | #/$defs/NameIdentifier |

**Description:** Uniquely identifies an individual or legal entity, according to various schemes.

| Property                                                                                              | Pattern | Type   | Deprecated | Definition | Title/Description                                                                |
| ----------------------------------------------------------------------------------------------------- | ------- | ------ | ---------- | ---------- | -------------------------------------------------------------------------------- |
| - [nameIdentifier](#data_attributes_creators_items_nameIdentifiers_items_nameIdentifier )             | No      | string | No         | -          | Uniquely identifies an individual or legal entity, according to various schemes. |
| + [nameIdentifierScheme](#data_attributes_creators_items_nameIdentifiers_items_nameIdentifierScheme ) | No      | string | No         | -          | The name of the name identifier scheme.                                          |
| - [schemeURI](#data_attributes_creators_items_nameIdentifiers_items_schemeURI )                       | No      | string | No         | -          | The URI of the name identifier scheme.                                           |

###### <a name="data_attributes_creators_items_nameIdentifiers_items_nameIdentifier"></a>1.3.6.1.5.1.1. Property `root > data > attributes > creators > creators items > nameIdentifiers > nameIdentifiers items > nameIdentifier`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** Uniquely identifies an individual or legal entity, according to various schemes.

###### <a name="data_attributes_creators_items_nameIdentifiers_items_nameIdentifierScheme"></a>1.3.6.1.5.1.2. Property `root > data > attributes > creators > creators items > nameIdentifiers > nameIdentifiers items > nameIdentifierScheme`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** The name of the name identifier scheme.

###### <a name="data_attributes_creators_items_nameIdentifiers_items_schemeURI"></a>1.3.6.1.5.1.3. Property `root > data > attributes > creators > creators items > nameIdentifiers > nameIdentifiers items > schemeURI`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `uri`    |

**Description:** The URI of the name identifier scheme.

###### <a name="data_attributes_creators_items_affiliation"></a>1.3.6.1.6. Property `root > data > attributes > creators > creators items > affiliation`

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |

**Description:** The organizational or institutional affiliations of the creator.

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | N/A                |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be                                  | Description                                                     |
| ---------------------------------------------------------------- | --------------------------------------------------------------- |
| [Affiliation](#data_attributes_creators_items_affiliation_items) | The organizational or institutional affiliation of the creator. |

###### <a name="data_attributes_creators_items_affiliation_items"></a>1.3.6.1.6.1. root > data > attributes > creators > creators items > affiliation > Affiliation

|                           |                     |
| ------------------------- | ------------------- |
| **Type**                  | `object`            |
| **Required**              | No                  |
| **Additional properties** | Any type allowed    |
| **Defined in**            | #/$defs/Affiliation |

**Description:** The organizational or institutional affiliation of the creator.

| Property                                                                                                        | Pattern | Type   | Deprecated | Definition | Title/Description                                                  |
| --------------------------------------------------------------------------------------------------------------- | ------- | ------ | ---------- | ---------- | ------------------------------------------------------------------ |
| - [affiliationIdentifier](#data_attributes_creators_items_affiliation_items_affiliationIdentifier )             | No      | string | No         | -          | Uniquely identifies the organizational affiliation of the creator. |
| - [affiliationIdentifierScheme](#data_attributes_creators_items_affiliation_items_affiliationIdentifierScheme ) | No      | string | No         | -          | The name of the affiliation identifier scheme                      |
| - [schemeURI](#data_attributes_creators_items_affiliation_items_schemeURI )                                     | No      | string | No         | -          | The URI of the affiliation identifier scheme.                      |

###### <a name="data_attributes_creators_items_affiliation_items_affiliationIdentifier"></a>1.3.6.1.6.1.1. Property `root > data > attributes > creators > creators items > affiliation > affiliation items > affiliationIdentifier`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** Uniquely identifies the organizational affiliation of the creator.

###### <a name="data_attributes_creators_items_affiliation_items_affiliationIdentifierScheme"></a>1.3.6.1.6.1.2. Property `root > data > attributes > creators > creators items > affiliation > affiliation items > affiliationIdentifierScheme`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** The name of the affiliation identifier scheme

###### <a name="data_attributes_creators_items_affiliation_items_schemeURI"></a>1.3.6.1.6.1.3. Property `root > data > attributes > creators > creators items > affiliation > affiliation items > schemeURI`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `uri`    |

**Description:** The URI of the affiliation identifier scheme.

#### <a name="data_attributes_titles"></a>1.3.7. Property `root > data > attributes > titles`

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | Yes     |

**Description:** Names or titles by which a resource is known. May be the title of a dataset or the name of a piece of software or an instrument.

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | 1                  |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be        | Description                                                                                                                      |
| -------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| [Title](#data_attributes_titles_items) | A name or title by which a resource is known. May be the title of a dataset or the name of a piece of software or an instrument. |

##### <a name="data_attributes_titles_items"></a>1.3.7.1. root > data > attributes > titles > Title

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |
| **Defined in**            | #/$defs/Title    |

**Description:** A name or title by which a resource is known. May be the title of a dataset or the name of a piece of software or an instrument.

| Property                                                | Pattern | Type             | Deprecated | Definition | Title/Description                              |
| ------------------------------------------------------- | ------- | ---------------- | ---------- | ---------- | ---------------------------------------------- |
| + [title](#data_attributes_titles_items_title )         | No      | string           | No         | -          | A name or title by which a resource is known   |
| - [lang](#data_attributes_titles_items_lang )           | No      | string           | No         | -          | The languages of the title.                    |
| - [titleType](#data_attributes_titles_items_titleType ) | No      | enum (of string) | No         | -          | The type of Title (other than the Main Title). |

###### <a name="data_attributes_titles_items_title"></a>1.3.7.1.1. Property `root > data > attributes > titles > titles items > title`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** A name or title by which a resource is known

###### <a name="data_attributes_titles_items_lang"></a>1.3.7.1.2. Property `root > data > attributes > titles > titles items > lang`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** The languages of the title.

###### <a name="data_attributes_titles_items_titleType"></a>1.3.7.1.3. Property `root > data > attributes > titles > titles items > titleType`

|              |                    |
| ------------ | ------------------ |
| **Type**     | `enum (of string)` |
| **Required** | No                 |

**Description:** The type of Title (other than the Main Title).

Must be one of:
* "AlternativeTitle"
* "Subtitle"
* "TranslatedTitle"
* "Other"

#### <a name="data_attributes_publisher"></a>1.3.8. Property `root > data > attributes > publisher`

|                           |                   |
| ------------------------- | ----------------- |
| **Type**                  | `object`          |
| **Required**              | Yes               |
| **Additional properties** | Any type allowed  |
| **Defined in**            | #/$defs/Publisher |

**Description:** The name of the entity that holds, archives, publishes, prints, distributes, releases, issues, or produces the resource. This property will be used to formulate the citation, so consider the prominence of the role.

| Property                                                                             | Pattern | Type   | Deprecated | Definition | Title/Description                                                                                                                                                                                                      |
| ------------------------------------------------------------------------------------ | ------- | ------ | ---------- | ---------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| + [name](#data_attributes_publisher_name )                                           | No      | string | No         | -          | The name of the entity that holds, archives, publishes, prints, distributes, releases, issues, or produces the resource. This property will be used to formulate the citation, so consider the prominence of the role. |
| - [publisherIdentifier](#data_attributes_publisher_publisherIdentifier )             | No      | string | No         | -          | Uniquely identifies the publisher, according to various schemes.                                                                                                                                                       |
| - [publisherIdentifierScheme](#data_attributes_publisher_publisherIdentifierScheme ) | No      | string | No         | -          | The name of the publisher identifier scheme.                                                                                                                                                                           |
| - [schemeURI](#data_attributes_publisher_schemeURI )                                 | No      | string | No         | -          | The URI of the publisher identifier scheme.                                                                                                                                                                            |
| - [lang](#data_attributes_publisher_lang )                                           | No      | string | No         | -          | The language used by the Publisher.                                                                                                                                                                                    |

##### <a name="data_attributes_publisher_name"></a>1.3.8.1. Property `root > data > attributes > publisher > name`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** The name of the entity that holds, archives, publishes, prints, distributes, releases, issues, or produces the resource. This property will be used to formulate the citation, so consider the prominence of the role.

##### <a name="data_attributes_publisher_publisherIdentifier"></a>1.3.8.2. Property `root > data > attributes > publisher > publisherIdentifier`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** Uniquely identifies the publisher, according to various schemes.

##### <a name="data_attributes_publisher_publisherIdentifierScheme"></a>1.3.8.3. Property `root > data > attributes > publisher > publisherIdentifierScheme`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** The name of the publisher identifier scheme.

##### <a name="data_attributes_publisher_schemeURI"></a>1.3.8.4. Property `root > data > attributes > publisher > schemeURI`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `uri`    |

**Description:** The URI of the publisher identifier scheme.

##### <a name="data_attributes_publisher_lang"></a>1.3.8.5. Property `root > data > attributes > publisher > lang`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** The language used by the Publisher.

#### <a name="data_attributes_publicationYear"></a>1.3.9. Property `root > data > attributes > publicationYear`

|                           |                         |
| ------------------------- | ----------------------- |
| **Type**                  | `combining`             |
| **Required**              | Yes                     |
| **Additional properties** | Any type allowed        |
| **Defined in**            | #/$defs/PublicationYear |

**Description:** The year when the data was or will be made publicly available.

| One of(Option)                                      |
| --------------------------------------------------- |
| [item 0](#data_attributes_publicationYear_oneOf_i0) |
| [item 1](#data_attributes_publicationYear_oneOf_i1) |

##### <a name="data_attributes_publicationYear_oneOf_i0"></a>1.3.9.1. Property `root > data > attributes > publicationYear > oneOf > item 0`

|              |           |
| ------------ | --------- |
| **Type**     | `integer` |
| **Required** | No        |
| **Format**   | `int32`   |

##### <a name="data_attributes_publicationYear_oneOf_i1"></a>1.3.9.2. Property `root > data > attributes > publicationYear > oneOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

| Restrictions                      |                                                                     |
| --------------------------------- | ------------------------------------------------------------------- |
| **Must match regular expression** | ```^\d{4}$``` [Test](https://regex101.com/?regex=%5E%5Cd%7B4%7D%24) |

#### <a name="data_attributes_subjects"></a>1.3.10. Property `root > data > attributes > subjects`

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |

**Description:** Subjects, keywords, classification codes, or key phrases describing the resource.

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | N/A                |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be            | Description                                                                   |
| ------------------------------------------ | ----------------------------------------------------------------------------- |
| [Subject](#data_attributes_subjects_items) | Subject, keyword, classification code, or key phrase describing the resource. |

##### <a name="data_attributes_subjects_items"></a>1.3.10.1. root > data > attributes > subjects > Subject

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |
| **Defined in**            | #/$defs/Subject  |

**Description:** Subject, keyword, classification code, or key phrase describing the resource.

| Property                                                                    | Pattern | Type   | Deprecated | Definition | Title/Description                                                                  |
| --------------------------------------------------------------------------- | ------- | ------ | ---------- | ---------- | ---------------------------------------------------------------------------------- |
| + [subject](#data_attributes_subjects_items_subject )                       | No      | string | No         | -          | Subject, keyword, classification code, or key phrase describing the resource.      |
| - [subjectScheme](#data_attributes_subjects_items_subjectScheme )           | No      | string | No         | -          | The name of the subject scheme or classification code or authority if one is used. |
| - [schemeURI](#data_attributes_subjects_items_schemeURI )                   | No      | string | No         | -          | The URI of the subject identifier scheme.                                          |
| - [valueURI](#data_attributes_subjects_items_valueURI )                     | No      | string | No         | -          | The URI of the subject term.                                                       |
| - [classificationCode](#data_attributes_subjects_items_classificationCode ) | No      | string | No         | -          | The classification code used for the subject term in the subject schemes.          |
| - [lang](#data_attributes_subjects_items_lang )                             | No      | string | No         | -          | The language used in the Subject.                                                  |

###### <a name="data_attributes_subjects_items_subject"></a>1.3.10.1.1. Property `root > data > attributes > subjects > subjects items > subject`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** Subject, keyword, classification code, or key phrase describing the resource.

###### <a name="data_attributes_subjects_items_subjectScheme"></a>1.3.10.1.2. Property `root > data > attributes > subjects > subjects items > subjectScheme`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** The name of the subject scheme or classification code or authority if one is used.

###### <a name="data_attributes_subjects_items_schemeURI"></a>1.3.10.1.3. Property `root > data > attributes > subjects > subjects items > schemeURI`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `uri`    |

**Description:** The URI of the subject identifier scheme.

###### <a name="data_attributes_subjects_items_valueURI"></a>1.3.10.1.4. Property `root > data > attributes > subjects > subjects items > valueURI`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `uri`    |

**Description:** The URI of the subject term.

###### <a name="data_attributes_subjects_items_classificationCode"></a>1.3.10.1.5. Property `root > data > attributes > subjects > subjects items > classificationCode`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** The classification code used for the subject term in the subject schemes.

###### <a name="data_attributes_subjects_items_lang"></a>1.3.10.1.6. Property `root > data > attributes > subjects > subjects items > lang`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** The language used in the Subject.

#### <a name="data_attributes_contributors"></a>1.3.11. Property `root > data > attributes > contributors`

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |

**Description:** The institution or person responsible for collecting, managing, distributing, or otherwise contributing to the development of the resource.

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | N/A                |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be                    | Description                                                                                                                                 |
| -------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| [Contributor](#data_attributes_contributors_items) | The institution or person responsible for collecting, managing, distributing, or otherwise contributing to the development of the resource. |

##### <a name="data_attributes_contributors_items"></a>1.3.11.1. root > data > attributes > contributors > Contributor

|                           |                     |
| ------------------------- | ------------------- |
| **Type**                  | `combining`         |
| **Required**              | No                  |
| **Additional properties** | Any type allowed    |
| **Defined in**            | #/$defs/Contributor |

**Description:** The institution or person responsible for collecting, managing, distributing, or otherwise contributing to the development of the resource.

| All of(Requirement)                                     |
| ------------------------------------------------------- |
| [Creator](#data_attributes_contributors_items_allOf_i0) |
| [item 1](#data_attributes_contributors_items_allOf_i1)  |

###### <a name="data_attributes_contributors_items_allOf_i0"></a>1.3.11.1.1. Property `root > data > attributes > contributors > contributors items > allOf > Creator`

|                           |                                                                   |
| ------------------------- | ----------------------------------------------------------------- |
| **Type**                  | `object`                                                          |
| **Required**              | No                                                                |
| **Additional properties** | Any type allowed                                                  |
| **Same definition as**    | [data_attributes_creators_items](#data_attributes_creators_items) |

**Description:** The main researcher involved in producing the data, or the author of the publication.

###### <a name="data_attributes_contributors_items_allOf_i1"></a>1.3.11.1.2. Property `root > data > attributes > contributors > contributors items > allOf > item 1`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| Property                                                                           | Pattern | Type             | Deprecated | Definition                 | Title/Description                       |
| ---------------------------------------------------------------------------------- | ------- | ---------------- | ---------- | -------------------------- | --------------------------------------- |
| + [contributorType](#data_attributes_contributors_items_allOf_i1_contributorType ) | No      | enum (of string) | No         | In #/$defs/ContributorType | The type of contributor of the resource |

###### <a name="data_attributes_contributors_items_allOf_i1_contributorType"></a>1.3.11.1.2.1. Property `root > data > attributes > contributors > contributors items > allOf > item 1 > contributorType`

|                |                         |
| -------------- | ----------------------- |
| **Type**       | `enum (of string)`      |
| **Required**   | Yes                     |
| **Defined in** | #/$defs/ContributorType |

**Description:** The type of contributor of the resource

Must be one of:
* "ContactPerson"
* "DataCollector"
* "DataCurator"
* "DataManager"
* "Distributor"
* "Editor"
* "HostingInstitution"
* "Producer"
* "ProjectLeader"
* "ProjectManager"
* "ProjectMember"
* "RegistrationAgency"
* "RegistrationAuthority"
* "RelatedPerson"
* "Researcher"
* "ResearchGroup"
* "RightsHolder"
* "Sponsor"
* "Supervisor"
* "Translator"
* "WorkPackageLeader"
* "Other"

#### <a name="data_attributes_dates"></a>1.3.12. Property `root > data > attributes > dates`

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |

**Description:** Different dates relevant to the work.

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | N/A                |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be      | Description                |
| ------------------------------------ | -------------------------- |
| [Date](#data_attributes_dates_items) | Date relevant to the work. |

##### <a name="data_attributes_dates_items"></a>1.3.12.1. root > data > attributes > dates > Date

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |
| **Defined in**            | #/$defs/Date     |

**Description:** Date relevant to the work.

| Property                                                           | Pattern | Type             | Deprecated | Definition | Title/Description                                    |
| ------------------------------------------------------------------ | ------- | ---------------- | ---------- | ---------- | ---------------------------------------------------- |
| + [date](#data_attributes_dates_items_date )                       | No      | string           | No         | -          | Date relevant to the work.                           |
| + [dateType](#data_attributes_dates_items_dateType )               | No      | enum (of string) | No         | -          | The type of date                                     |
| - [dateInformation](#data_attributes_dates_items_dateInformation ) | No      | string           | No         | -          | Specific information about the date, if appropriate. |

###### <a name="data_attributes_dates_items_date"></a>1.3.12.1.1. Property `root > data > attributes > dates > dates items > date`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |
| **Format**   | `date`   |

**Description:** Date relevant to the work.

###### <a name="data_attributes_dates_items_dateType"></a>1.3.12.1.2. Property `root > data > attributes > dates > dates items > dateType`

|              |                    |
| ------------ | ------------------ |
| **Type**     | `enum (of string)` |
| **Required** | Yes                |

**Description:** The type of date

Must be one of:
* "Accepted"
* "Available"
* "Copyrighted"
* "Collected"
* "Coverage"
* "Created"
* "Issued"
* "Submitted"
* "Updated"
* "Valid"
* "Withdrawn"
* "Other"

###### <a name="data_attributes_dates_items_dateInformation"></a>1.3.12.1.3. Property `root > data > attributes > dates > dates items > dateInformation`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** Specific information about the date, if appropriate.

#### <a name="data_attributes_language"></a>1.3.13. Property `root > data > attributes > language`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** The primary language of the resource

#### <a name="data_attributes_types"></a>1.3.14. Property `root > data > attributes > types`

|                           |                      |
| ------------------------- | -------------------- |
| **Type**                  | `object`             |
| **Required**              | Yes                  |
| **Additional properties** | Any type allowed     |
| **Defined in**            | #/$defs/ResourceType |

**Description:** A description of the resource.

| Property                                                             | Pattern | Type             | Deprecated | Definition                     | Title/Description               |
| -------------------------------------------------------------------- | ------- | ---------------- | ---------- | ------------------------------ | ------------------------------- |
| + [resourceType](#data_attributes_types_resourceType )               | No      | string           | No         | -                              | A description of the resource.  |
| + [resourceTypeGeneral](#data_attributes_types_resourceTypeGeneral ) | No      | enum (of string) | No         | In #/$defs/ResourceTypeGeneral | The general type of a resource. |

##### <a name="data_attributes_types_resourceType"></a>1.3.14.1. Property `root > data > attributes > types > resourceType`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** A description of the resource.

##### <a name="data_attributes_types_resourceTypeGeneral"></a>1.3.14.2. Property `root > data > attributes > types > resourceTypeGeneral`

|                |                             |
| -------------- | --------------------------- |
| **Type**       | `enum (of string)`          |
| **Required**   | Yes                         |
| **Defined in** | #/$defs/ResourceTypeGeneral |

**Description:** The general type of a resource.

Must be one of:
* "Audiovisual"
* "Award"
* "Book"
* "BookChapter"
* "Collection"
* "ComputationalNotebook"
* "ConferencePaper"
* "ConferenceProceeding"
* "DataPaper"
* "Dataset"
* "Dissertation"
* "Event"
* "Image"
* "InteractiveResource"
* "Instrument"
* "Journal"
* "JournalArticle"
* "Model"
* "OutputManagementPlan"
* "PeerReview"
* "PhysicalObject"
* "Preprint"
* "Project"
* "Report"
* "Service"
* "Software"
* "Sound"
* "Standard"
* "StudyRegistration"
* "Text"
* "Workflow"
* "Other"

#### <a name="data_attributes_alternateIdentifiers"></a>1.3.15. Property `root > data > attributes > alternateIdentifiers`

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |

**Description:** An identifier other than the primary Identifier applied to the resource being registered.

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | N/A                |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be                                    | Description                                                                               |
| ------------------------------------------------------------------ | ----------------------------------------------------------------------------------------- |
| [AlternateIdentifier](#data_attributes_alternateIdentifiers_items) | An identifier other than the primary Identifier applied to the resource being registered. |

##### <a name="data_attributes_alternateIdentifiers_items"></a>1.3.15.1. root > data > attributes > alternateIdentifiers > AlternateIdentifier

|                           |                             |
| ------------------------- | --------------------------- |
| **Type**                  | `object`                    |
| **Required**              | No                          |
| **Additional properties** | Any type allowed            |
| **Defined in**            | #/$defs/AlternateIdentifier |

**Description:** An identifier other than the primary Identifier applied to the resource being registered.

| Property                                                                                          | Pattern | Type             | Deprecated | Definition                                                                 | Title/Description                                                                        |
| ------------------------------------------------------------------------------------------------- | ------- | ---------------- | ---------- | -------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| - [alternateIdentifier](#data_attributes_alternateIdentifiers_items_alternateIdentifier )         | No      | string           | No         | -                                                                          | An identifier other than the primary Identifier applied to the resource being registered |
| + [alternateIdentifierType](#data_attributes_alternateIdentifiers_items_alternateIdentifierType ) | No      | enum (of string) | No         | Same as [resourceTypeGeneral](#data_attributes_types_resourceTypeGeneral ) | The general type of a resource.                                                          |

###### <a name="data_attributes_alternateIdentifiers_items_alternateIdentifier"></a>1.3.15.1.1. Property `root > data > attributes > alternateIdentifiers > alternateIdentifiers items > alternateIdentifier`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** An identifier other than the primary Identifier applied to the resource being registered

###### <a name="data_attributes_alternateIdentifiers_items_alternateIdentifierType"></a>1.3.15.1.2. Property `root > data > attributes > alternateIdentifiers > alternateIdentifiers items > alternateIdentifierType`

|                        |                                                                   |
| ---------------------- | ----------------------------------------------------------------- |
| **Type**               | `enum (of string)`                                                |
| **Required**           | Yes                                                               |
| **Same definition as** | [resourceTypeGeneral](#data_attributes_types_resourceTypeGeneral) |

**Description:** The general type of a resource.

#### <a name="data_attributes_relatedIdentifiers"></a>1.3.16. Property `root > data > attributes > relatedIdentifiers`

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |

**Description:** Identifiers of related resources.

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | N/A                |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be                                | Description                      |
| -------------------------------------------------------------- | -------------------------------- |
| [RelatedIdentifier](#data_attributes_relatedIdentifiers_items) | Identifier of related resources. |

##### <a name="data_attributes_relatedIdentifiers_items"></a>1.3.16.1. root > data > attributes > relatedIdentifiers > RelatedIdentifier

|                           |                           |
| ------------------------- | ------------------------- |
| **Type**                  | `object`                  |
| **Required**              | No                        |
| **Additional properties** | Any type allowed          |
| **Defined in**            | #/$defs/RelatedIdentifier |

**Description:** Identifier of related resources.

| Property                                                                                    | Pattern | Type             | Deprecated | Definition                                                                 | Title/Description                                                                                  |
| ------------------------------------------------------------------------------------------- | ------- | ---------------- | ---------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| - [relatedIdentifier](#data_attributes_relatedIdentifiers_items_relatedIdentifier )         | No      | string           | No         | -                                                                          | Identifier of related resources.                                                                   |
| - [relatedIdentifierType](#data_attributes_relatedIdentifiers_items_relatedIdentifierType ) | No      | enum (of string) | No         | In #/$defs/RelatedIdentifierType                                           | The type of the RelatedIdentifier.                                                                 |
| - [relationType](#data_attributes_relatedIdentifiers_items_relationType )                   | No      | enum (of string) | No         | In #/$defs/RelationType                                                    | Description of the relationship of the resource being registered (A) and the related resource (B). |
| - [relatedMetadataScheme](#data_attributes_relatedIdentifiers_items_relatedMetadataScheme ) | No      | string           | No         | -                                                                          | The name of the schemes.                                                                           |
| - [schemeURI](#data_attributes_relatedIdentifiers_items_schemeURI )                         | No      | string           | No         | -                                                                          | The URI of the name identifier scheme.                                                             |
| - [schemeType](#data_attributes_relatedIdentifiers_items_schemeType )                       | No      | string           | No         | -                                                                          | The type of the relatedMetadataScheme, linked with the schemeURI                                   |
| - [resourceTypeGeneral](#data_attributes_relatedIdentifiers_items_resourceTypeGeneral )     | No      | enum (of string) | No         | Same as [resourceTypeGeneral](#data_attributes_types_resourceTypeGeneral ) | The general type of a resource.                                                                    |

###### <a name="autogenerated_heading_2"></a>1.3.16.1.1. If (relationType = null)

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

###### <a name="autogenerated_heading_3"></a>1.3.16.1.1.1. The following properties are required
* relatedMetadataScheme
* schemeURI
* schemeType

###### <a name="autogenerated_heading_4"></a>1.3.16.1.2. Else (i.e.  relationType != null)

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

###### <a name="autogenerated_heading_5"></a>1.3.16.1.2.1. Must **not** be

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| Any of(Option)                                                        |
| --------------------------------------------------------------------- |
| [item 0](#data_attributes_relatedIdentifiers_items_else_not_anyOf_i0) |
| [item 1](#data_attributes_relatedIdentifiers_items_else_not_anyOf_i1) |
| [item 2](#data_attributes_relatedIdentifiers_items_else_not_anyOf_i2) |

###### <a name="data_attributes_relatedIdentifiers_items_else_not_anyOf_i0"></a>1.3.16.1.2.1.1. Property `root > data > attributes > relatedIdentifiers > relatedIdentifiers items > else > not > anyOf > item 0`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

###### <a name="autogenerated_heading_6"></a>1.3.16.1.2.1.1.1. The following properties are required
* relatedMetadataScheme

###### <a name="data_attributes_relatedIdentifiers_items_else_not_anyOf_i1"></a>1.3.16.1.2.1.2. Property `root > data > attributes > relatedIdentifiers > relatedIdentifiers items > else > not > anyOf > item 1`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

###### <a name="autogenerated_heading_7"></a>1.3.16.1.2.1.2.1. The following properties are required
* schemeURI

###### <a name="data_attributes_relatedIdentifiers_items_else_not_anyOf_i2"></a>1.3.16.1.2.1.3. Property `root > data > attributes > relatedIdentifiers > relatedIdentifiers items > else > not > anyOf > item 2`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

###### <a name="autogenerated_heading_8"></a>1.3.16.1.2.1.3.1. The following properties are required
* schemeType

###### <a name="data_attributes_relatedIdentifiers_items_relatedIdentifier"></a>1.3.16.1.3. Property `root > data > attributes > relatedIdentifiers > relatedIdentifiers items > relatedIdentifier`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** Identifier of related resources.

###### <a name="data_attributes_relatedIdentifiers_items_relatedIdentifierType"></a>1.3.16.1.4. Property `root > data > attributes > relatedIdentifiers > relatedIdentifiers items > relatedIdentifierType`

|                |                               |
| -------------- | ----------------------------- |
| **Type**       | `enum (of string)`            |
| **Required**   | No                            |
| **Defined in** | #/$defs/RelatedIdentifierType |

**Description:** The type of the RelatedIdentifier.

Must be one of:
* "ARK"
* "arXiv"
* "bibcode"
* "CSTR"
* "DOI"
* "EAN13"
* "EISSN"
* "Handle"
* "IGSN"
* "ISBN"
* "ISSN"
* "ISTC"
* "LISSN"
* "LSID"
* "PMID"
* "PURL"
* "RRID"
* "UPC"
* "URL"
* "URN"
* "w3id"

###### <a name="data_attributes_relatedIdentifiers_items_relationType"></a>1.3.16.1.5. Property `root > data > attributes > relatedIdentifiers > relatedIdentifiers items > relationType`

|                |                      |
| -------------- | -------------------- |
| **Type**       | `enum (of string)`   |
| **Required**   | No                   |
| **Defined in** | #/$defs/RelationType |

**Description:** Description of the relationship of the resource being registered (A) and the related resource (B).

Must be one of:
* "IsCitedBy"
* "Cites"
* "IsSupplementTo"
* "IsSupplementedBy"
* "IsContinuedBy"
* "Continues"
* "IsDescribedBy"
* "Describes"
* "HasMetadata"
* "IsMetadataFor"
* "HasVersion"
* "IsVersionOf"
* "IsNewVersionOf"
* "IsPreviousVersionOf"
* "IsPartOf"
* "HasPart"
* "IsPublishedIn"
* "IsReferencedBy"
* "References"
* "IsDocumentedBy"
* "Documents"
* "IsCompiledBy"
* "Compiles"
* "IsVariantFormOf"
* "IsOriginalFormOf"
* "IsIdenticalTo"
* "IsReviewedBy"
* "Reviews"
* "IsDerivedFrom"
* "IsSourceOf"
* "IsRequiredBy"
* "Requires"
* "IsObsoletedBy"
* "Obsoletes"
* "IsCollectedBy"
* "Collects"
* "IsTranslationOf"
* "HasTranslation"

###### <a name="data_attributes_relatedIdentifiers_items_relatedMetadataScheme"></a>1.3.16.1.6. Property `root > data > attributes > relatedIdentifiers > relatedIdentifiers items > relatedMetadataScheme`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** The name of the schemes.

###### <a name="data_attributes_relatedIdentifiers_items_schemeURI"></a>1.3.16.1.7. Property `root > data > attributes > relatedIdentifiers > relatedIdentifiers items > schemeURI`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `uri`    |

**Description:** The URI of the name identifier scheme.

###### <a name="data_attributes_relatedIdentifiers_items_schemeType"></a>1.3.16.1.8. Property `root > data > attributes > relatedIdentifiers > relatedIdentifiers items > schemeType`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** The type of the relatedMetadataScheme, linked with the schemeURI

###### <a name="data_attributes_relatedIdentifiers_items_resourceTypeGeneral"></a>1.3.16.1.9. Property `root > data > attributes > relatedIdentifiers > relatedIdentifiers items > resourceTypeGeneral`

|                        |                                                                   |
| ---------------------- | ----------------------------------------------------------------- |
| **Type**               | `enum (of string)`                                                |
| **Required**           | No                                                                |
| **Same definition as** | [resourceTypeGeneral](#data_attributes_types_resourceTypeGeneral) |

**Description:** The general type of a resource.

#### <a name="data_attributes_sizes"></a>1.3.17. Property `root > data > attributes > sizes`

|              |                   |
| ------------ | ----------------- |
| **Type**     | `array of string` |
| **Required** | No                |

**Description:** Size (e.g., bytes, pages, inches, etc.) or duration (extent), e.g., hours, minutes, days, etc., of a resource.

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | N/A                |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be             | Description |
| ------------------------------------------- | ----------- |
| [sizes items](#data_attributes_sizes_items) | -           |

##### <a name="data_attributes_sizes_items"></a>1.3.17.1. root > data > attributes > sizes > sizes items

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

#### <a name="data_attributes_formats"></a>1.3.18. Property `root > data > attributes > formats`

|              |                   |
| ------------ | ----------------- |
| **Type**     | `array of string` |
| **Required** | No                |

**Description:** Technical format of the resources.

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | N/A                |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be                 | Description |
| ----------------------------------------------- | ----------- |
| [formats items](#data_attributes_formats_items) | -           |

##### <a name="data_attributes_formats_items"></a>1.3.18.1. root > data > attributes > formats > formats items

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

#### <a name="data_attributes_version"></a>1.3.19. Property `root > data > attributes > version`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** The version number of the resources.

#### <a name="data_attributes_rightsList"></a>1.3.20. Property `root > data > attributes > rightsList`

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |

**Description:** Any rights information for this resource

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | N/A                |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be            | Description                              |
| ------------------------------------------ | ---------------------------------------- |
| [Right](#data_attributes_rightsList_items) | Any right information for this resource. |

##### <a name="data_attributes_rightsList_items"></a>1.3.20.1. root > data > attributes > rightsList > Right

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |
| **Defined in**            | #/$defs/Right    |

**Description:** Any right information for this resource.

| Property                                                                              | Pattern | Type   | Deprecated | Definition | Title/Description                                  |
| ------------------------------------------------------------------------------------- | ------- | ------ | ---------- | ---------- | -------------------------------------------------- |
| + [rights](#data_attributes_rightsList_items_rights )                                 | No      | string | No         | -          | Any right information for this resource.           |
| - [rightsURI](#data_attributes_rightsList_items_rightsURI )                           | No      | string | No         | -          | The URI of the license.                            |
| - [rightsIdentifier](#data_attributes_rightsList_items_rightsIdentifier )             | No      | string | No         | -          | A short, standardized version of the license name. |
| - [rightsIdentifierScheme](#data_attributes_rightsList_items_rightsIdentifierScheme ) | No      | string | No         | -          | The name of the scheme.                            |
| - [schemeURI](#data_attributes_rightsList_items_schemeURI )                           | No      | string | No         | -          | The URI of the rightsIdentifierScheme.             |

###### <a name="data_attributes_rightsList_items_rights"></a>1.3.20.1.1. Property `root > data > attributes > rightsList > rightsList items > rights`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** Any right information for this resource.

###### <a name="data_attributes_rightsList_items_rightsURI"></a>1.3.20.1.2. Property `root > data > attributes > rightsList > rightsList items > rightsURI`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `uri`    |

**Description:** The URI of the license.

###### <a name="data_attributes_rightsList_items_rightsIdentifier"></a>1.3.20.1.3. Property `root > data > attributes > rightsList > rightsList items > rightsIdentifier`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** A short, standardized version of the license name.

###### <a name="data_attributes_rightsList_items_rightsIdentifierScheme"></a>1.3.20.1.4. Property `root > data > attributes > rightsList > rightsList items > rightsIdentifierScheme`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** The name of the scheme.

###### <a name="data_attributes_rightsList_items_schemeURI"></a>1.3.20.1.5. Property `root > data > attributes > rightsList > rightsList items > schemeURI`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `uri`    |

**Description:** The URI of the rightsIdentifierScheme.

#### <a name="data_attributes_descriptions"></a>1.3.21. Property `root > data > attributes > descriptions`

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | N/A                |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be                    | Description                                                                  |
| -------------------------------------------------- | ---------------------------------------------------------------------------- |
| [Description](#data_attributes_descriptions_items) | All additional information that does not fit in any of the other categories. |

##### <a name="data_attributes_descriptions_items"></a>1.3.21.1. root > data > attributes > descriptions > Description

|                           |                     |
| ------------------------- | ------------------- |
| **Type**                  | `object`            |
| **Required**              | No                  |
| **Additional properties** | Any type allowed    |
| **Defined in**            | #/$defs/Description |

**Description:** All additional information that does not fit in any of the other categories.

| Property                                                                  | Pattern | Type             | Deprecated | Definition | Title/Description                                                            |
| ------------------------------------------------------------------------- | ------- | ---------------- | ---------- | ---------- | ---------------------------------------------------------------------------- |
| + [description](#data_attributes_descriptions_items_description )         | No      | string           | No         | -          | All additional information that does not fit in any of the other categories. |
| + [descriptionType](#data_attributes_descriptions_items_descriptionType ) | No      | enum (of string) | No         | -          | The type of the Description.                                                 |

###### <a name="data_attributes_descriptions_items_description"></a>1.3.21.1.1. Property `root > data > attributes > descriptions > descriptions items > description`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** All additional information that does not fit in any of the other categories.

###### <a name="data_attributes_descriptions_items_descriptionType"></a>1.3.21.1.2. Property `root > data > attributes > descriptions > descriptions items > descriptionType`

|              |                    |
| ------------ | ------------------ |
| **Type**     | `enum (of string)` |
| **Required** | Yes                |

**Description:** The type of the Description.

Must be one of:
* "Abstract"
* "Methods"
* "SeriesInformation"
* "TableOfContents"
* "TechnicalInfo"
* "Other"

#### <a name="data_attributes_geoLocations"></a>1.3.22. Property `root > data > attributes > geoLocations`

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |

**Description:** Spatial regions or named places where the data was gathered or about which the data is focused.

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | N/A                |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be                    | Description                                                                                   |
| -------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| [GeoLocation](#data_attributes_geoLocations_items) | Spatial region or named place where the data was gathered or about which the data is focused. |

##### <a name="data_attributes_geoLocations_items"></a>1.3.22.1. root > data > attributes > geoLocations > GeoLocation

|                           |                     |
| ------------------------- | ------------------- |
| **Type**                  | `object`            |
| **Required**              | No                  |
| **Additional properties** | Any type allowed    |
| **Defined in**            | #/$defs/GeoLocation |

**Description:** Spatial region or named place where the data was gathered or about which the data is focused.

| Property                                                                        | Pattern | Type   | Deprecated | Definition                  | Title/Description                     |
| ------------------------------------------------------------------------------- | ------- | ------ | ---------- | --------------------------- | ------------------------------------- |
| - [geoLocationPoint](#data_attributes_geoLocations_items_geoLocationPoint )     | No      | object | No         | In #/$defs/GeoLocationPoint | A point location in space.            |
| - [geoLocationBox](#data_attributes_geoLocations_items_geoLocationBox )         | No      | object | No         | In #/$defs/GeoLocationBox   | The spatial limits of a box.          |
| - [geoLocationPlace](#data_attributes_geoLocations_items_geoLocationPlace )     | No      | string | No         | -                           | Description of a geographic location. |
| - [geoLocationPolygon](#data_attributes_geoLocations_items_geoLocationPolygon ) | No      | array  | No         | -                           | -                                     |

###### <a name="data_attributes_geoLocations_items_geoLocationPoint"></a>1.3.22.1.1. Property `root > data > attributes > geoLocations > geoLocations items > geoLocationPoint`

|                           |                          |
| ------------------------- | ------------------------ |
| **Type**                  | `object`                 |
| **Required**              | No                       |
| **Additional properties** | Any type allowed         |
| **Defined in**            | #/$defs/GeoLocationPoint |

**Description:** A point location in space.

| Property                                                                                 | Pattern | Type   | Deprecated | Definition | Title/Description                |
| ---------------------------------------------------------------------------------------- | ------- | ------ | ---------- | ---------- | -------------------------------- |
| + [pointLongitude](#data_attributes_geoLocations_items_geoLocationPoint_pointLongitude ) | No      | number | No         | -          | Longitudinal dimension of point. |
| + [pointLatitude](#data_attributes_geoLocations_items_geoLocationPoint_pointLatitude )   | No      | number | No         | -          | Latitudinal dimension of point.  |

###### <a name="data_attributes_geoLocations_items_geoLocationPoint_pointLongitude"></a>1.3.22.1.1.1. Property `root > data > attributes > geoLocations > geoLocations items > geoLocationPoint > pointLongitude`

|              |          |
| ------------ | -------- |
| **Type**     | `number` |
| **Required** | Yes      |
| **Format**   | `float`  |

**Description:** Longitudinal dimension of point.

###### <a name="data_attributes_geoLocations_items_geoLocationPoint_pointLatitude"></a>1.3.22.1.1.2. Property `root > data > attributes > geoLocations > geoLocations items > geoLocationPoint > pointLatitude`

|              |          |
| ------------ | -------- |
| **Type**     | `number` |
| **Required** | Yes      |
| **Format**   | `float`  |

**Description:** Latitudinal dimension of point.

###### <a name="data_attributes_geoLocations_items_geoLocationBox"></a>1.3.22.1.2. Property `root > data > attributes > geoLocations > geoLocations items > geoLocationBox`

|                           |                        |
| ------------------------- | ---------------------- |
| **Type**                  | `object`               |
| **Required**              | No                     |
| **Additional properties** | Any type allowed       |
| **Defined in**            | #/$defs/GeoLocationBox |

**Description:** The spatial limits of a box.

| Property                                                                                       | Pattern | Type   | Deprecated | Definition | Title/Description                      |
| ---------------------------------------------------------------------------------------------- | ------- | ------ | ---------- | ---------- | -------------------------------------- |
| + [westBoundLongitude](#data_attributes_geoLocations_items_geoLocationBox_westBoundLongitude ) | No      | number | No         | -          | Western longitudinal dimension of box. |
| + [eastBoundLongitude](#data_attributes_geoLocations_items_geoLocationBox_eastBoundLongitude ) | No      | number | No         | -          | Eastern longitudinal dimension of box. |
| + [southBoundLatitude](#data_attributes_geoLocations_items_geoLocationBox_southBoundLatitude ) | No      | number | No         | -          | Southern latitudinal dimension of box. |
| + [northBoundLatitude](#data_attributes_geoLocations_items_geoLocationBox_northBoundLatitude ) | No      | number | No         | -          | Northern latitudinal dimension of box. |

###### <a name="data_attributes_geoLocations_items_geoLocationBox_westBoundLongitude"></a>1.3.22.1.2.1. Property `root > data > attributes > geoLocations > geoLocations items > geoLocationBox > westBoundLongitude`

|              |          |
| ------------ | -------- |
| **Type**     | `number` |
| **Required** | Yes      |
| **Format**   | `float`  |

**Description:** Western longitudinal dimension of box.

###### <a name="data_attributes_geoLocations_items_geoLocationBox_eastBoundLongitude"></a>1.3.22.1.2.2. Property `root > data > attributes > geoLocations > geoLocations items > geoLocationBox > eastBoundLongitude`

|              |          |
| ------------ | -------- |
| **Type**     | `number` |
| **Required** | Yes      |
| **Format**   | `float`  |

**Description:** Eastern longitudinal dimension of box.

###### <a name="data_attributes_geoLocations_items_geoLocationBox_southBoundLatitude"></a>1.3.22.1.2.3. Property `root > data > attributes > geoLocations > geoLocations items > geoLocationBox > southBoundLatitude`

|              |          |
| ------------ | -------- |
| **Type**     | `number` |
| **Required** | Yes      |
| **Format**   | `float`  |

**Description:** Southern latitudinal dimension of box.

###### <a name="data_attributes_geoLocations_items_geoLocationBox_northBoundLatitude"></a>1.3.22.1.2.4. Property `root > data > attributes > geoLocations > geoLocations items > geoLocationBox > northBoundLatitude`

|              |          |
| ------------ | -------- |
| **Type**     | `number` |
| **Required** | Yes      |
| **Format**   | `float`  |

**Description:** Northern latitudinal dimension of box.

###### <a name="data_attributes_geoLocations_items_geoLocationPlace"></a>1.3.22.1.3. Property `root > data > attributes > geoLocations > geoLocations items > geoLocationPlace`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** Description of a geographic location.

###### <a name="data_attributes_geoLocations_items_geoLocationPolygon"></a>1.3.22.1.4. Property `root > data > attributes > geoLocations > geoLocations items > geoLocationPolygon`

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | 4                  |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be                                                    | Description                                                                                         |
| ---------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| [GeoLocationPolygon](#data_attributes_geoLocations_items_geoLocationPolygon_items) | A drawn polygon area, defined by a set of points and lines connecting the points in a closed chain. |

###### <a name="data_attributes_geoLocations_items_geoLocationPolygon_items"></a>1.3.22.1.4.1. root > data > attributes > geoLocations > geoLocations items > geoLocationPolygon > GeoLocationPolygon

|                           |                            |
| ------------------------- | -------------------------- |
| **Type**                  | `object`                   |
| **Required**              | No                         |
| **Additional properties** | Any type allowed           |
| **Defined in**            | #/$defs/GeoLocationPolygon |

**Description:** A drawn polygon area, defined by a set of points and lines connecting the points in a closed chain.

| Property                                                                                         | Pattern | Type   | Deprecated | Definition                                                                        | Title/Description          |
| ------------------------------------------------------------------------------------------------ | ------- | ------ | ---------- | --------------------------------------------------------------------------------- | -------------------------- |
| - [polygonPoint](#data_attributes_geoLocations_items_geoLocationPolygon_items_polygonPoint )     | No      | object | No         | Same as [geoLocationPoint](#data_attributes_geoLocations_items_geoLocationPoint ) | A point location in space. |
| - [inPolygonPoint](#data_attributes_geoLocations_items_geoLocationPolygon_items_inPolygonPoint ) | No      | object | No         | Same as [geoLocationPoint](#data_attributes_geoLocations_items_geoLocationPoint ) | A point location in space. |

###### <a name="data_attributes_geoLocations_items_geoLocationPolygon_items_polygonPoint"></a>1.3.22.1.4.1.1. Property `root > data > attributes > geoLocations > geoLocations items > geoLocationPolygon > geoLocationPolygon items > polygonPoint`

|                           |                                                                          |
| ------------------------- | ------------------------------------------------------------------------ |
| **Type**                  | `object`                                                                 |
| **Required**              | No                                                                       |
| **Additional properties** | Any type allowed                                                         |
| **Same definition as**    | [geoLocationPoint](#data_attributes_geoLocations_items_geoLocationPoint) |

**Description:** A point location in space.

###### <a name="data_attributes_geoLocations_items_geoLocationPolygon_items_inPolygonPoint"></a>1.3.22.1.4.1.2. Property `root > data > attributes > geoLocations > geoLocations items > geoLocationPolygon > geoLocationPolygon items > inPolygonPoint`

|                           |                                                                          |
| ------------------------- | ------------------------------------------------------------------------ |
| **Type**                  | `object`                                                                 |
| **Required**              | No                                                                       |
| **Additional properties** | Any type allowed                                                         |
| **Same definition as**    | [geoLocationPoint](#data_attributes_geoLocations_items_geoLocationPoint) |

**Description:** A point location in space.

#### <a name="data_attributes_fundingReferences"></a>1.3.23. Property `root > data > attributes > fundingReferences`

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |

**Description:** Information about financial support (funding) for the resource being registered.

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | N/A                |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be                              | Description                                                                      |
| ------------------------------------------------------------ | -------------------------------------------------------------------------------- |
| [FundingReference](#data_attributes_fundingReferences_items) | Information about financial support (funding) for the resource being registered. |

##### <a name="data_attributes_fundingReferences_items"></a>1.3.23.1. root > data > attributes > fundingReferences > FundingReference

|                           |                          |
| ------------------------- | ------------------------ |
| **Type**                  | `object`                 |
| **Required**              | No                       |
| **Additional properties** | Any type allowed         |
| **Defined in**            | #/$defs/FundingReference |

**Description:** Information about financial support (funding) for the resource being registered.

| Property                                                                                 | Pattern | Type             | Deprecated | Definition | Title/Description                                                                              |
| ---------------------------------------------------------------------------------------- | ------- | ---------------- | ---------- | ---------- | ---------------------------------------------------------------------------------------------- |
| + [funderName](#data_attributes_fundingReferences_items_funderName )                     | No      | string           | No         | -          | Name of the funding provider.                                                                  |
| - [funderIdentifier](#data_attributes_fundingReferences_items_funderIdentifier )         | No      | string           | No         | -          | Uniquely identifies a funding entity, according to various types                               |
| + [funderIdentifierType](#data_attributes_fundingReferences_items_funderIdentifierType ) | No      | enum (of string) | No         | -          | The type of the funderIdentifier.                                                              |
| - [schemeURI](#data_attributes_fundingReferences_items_schemeURI )                       | No      | string           | No         | -          | The URI of the funder identifier scheme.                                                       |
| - [awardNumber](#data_attributes_fundingReferences_items_awardNumber )                   | No      | string           | No         | -          | The code assigned by the funder to a sponsored award (grant).                                  |
| - [awardURI](#data_attributes_fundingReferences_items_awardURI )                         | No      | string           | No         | -          | The URI leading to a page provided by the funder for more information about the award (grant). |
| - [awardTitle](#data_attributes_fundingReferences_items_awardTitle )                     | No      | string           | No         | -          | The human readable title or name of the award (grant).                                         |

###### <a name="data_attributes_fundingReferences_items_funderName"></a>1.3.23.1.1. Property `root > data > attributes > fundingReferences > fundingReferences items > funderName`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** Name of the funding provider.

###### <a name="data_attributes_fundingReferences_items_funderIdentifier"></a>1.3.23.1.2. Property `root > data > attributes > fundingReferences > fundingReferences items > funderIdentifier`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** Uniquely identifies a funding entity, according to various types

###### <a name="data_attributes_fundingReferences_items_funderIdentifierType"></a>1.3.23.1.3. Property `root > data > attributes > fundingReferences > fundingReferences items > funderIdentifierType`

|              |                    |
| ------------ | ------------------ |
| **Type**     | `enum (of string)` |
| **Required** | Yes                |

**Description:** The type of the funderIdentifier.

Must be one of:
* "Crossref Funder ID"
* "GRID"
* "ISNI"
* "ROR"
* "Other"

###### <a name="data_attributes_fundingReferences_items_schemeURI"></a>1.3.23.1.4. Property `root > data > attributes > fundingReferences > fundingReferences items > schemeURI`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `uri`    |

**Description:** The URI of the funder identifier scheme.

###### <a name="data_attributes_fundingReferences_items_awardNumber"></a>1.3.23.1.5. Property `root > data > attributes > fundingReferences > fundingReferences items > awardNumber`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** The code assigned by the funder to a sponsored award (grant).

###### <a name="data_attributes_fundingReferences_items_awardURI"></a>1.3.23.1.6. Property `root > data > attributes > fundingReferences > fundingReferences items > awardURI`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `uri`    |

**Description:** The URI leading to a page provided by the funder for more information about the award (grant).

###### <a name="data_attributes_fundingReferences_items_awardTitle"></a>1.3.23.1.7. Property `root > data > attributes > fundingReferences > fundingReferences items > awardTitle`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** The human readable title or name of the award (grant).

#### <a name="data_attributes_relatedItems"></a>1.3.24. Property `root > data > attributes > relatedItems`

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |

**Description:** Informations about a resource related to the one being registered.

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | N/A                |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be                    | Description                                                       |
| -------------------------------------------------- | ----------------------------------------------------------------- |
| [RelatedItem](#data_attributes_relatedItems_items) | Information about a resource related to the one being registered. |

##### <a name="data_attributes_relatedItems_items"></a>1.3.24.1. root > data > attributes > relatedItems > RelatedItem

|                           |                     |
| ------------------------- | ------------------- |
| **Type**                  | `object`            |
| **Required**              | No                  |
| **Additional properties** | Any type allowed    |
| **Defined in**            | #/$defs/RelatedItem |

**Description:** Information about a resource related to the one being registered.

| Property                                                                              | Pattern | Type             | Deprecated | Definition                                                                 | Title/Description                                                                                                       |
| ------------------------------------------------------------------------------------- | ------- | ---------------- | ---------- | -------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| + [relatedItemType](#data_attributes_relatedItems_items_relatedItemType )             | No      | enum (of string) | No         | Same as [resourceTypeGeneral](#data_attributes_types_resourceTypeGeneral ) | The general type of a resource.                                                                                         |
| + [relationType](#data_attributes_relatedItems_items_relationType )                   | No      | enum (of string) | No         | Same as [resourceTypeGeneral](#data_attributes_types_resourceTypeGeneral ) | The general type of a resource.                                                                                         |
| - [relatedItemIdentifier](#data_attributes_relatedItems_items_relatedItemIdentifier ) | No      | object           | No         | In #/$defs/RelatedItemIdentifier                                           | The identifier for the related item.                                                                                    |
| - [creators](#data_attributes_relatedItems_items_creators )                           | No      | array            | No         | -                                                                          | The institution or person responsible for creating the related resource.                                                |
| + [titles](#data_attributes_relatedItems_items_titles )                               | No      | array            | No         | -                                                                          | Title of the related item                                                                                               |
| - [publicationYear](#data_attributes_relatedItems_items_publicationYear )             | No      | object           | No         | Same as [publicationYear](#data_attributes_publicationYear )               | The year when the data was or will be made publicly available.                                                          |
| - [volume](#data_attributes_relatedItems_items_volume )                               | No      | string           | No         | -                                                                          | Volume of the related item.                                                                                             |
| - [issue](#data_attributes_relatedItems_items_issue )                                 | No      | string           | No         | -                                                                          | Issue number or name of the related item.                                                                               |
| - [number](#data_attributes_relatedItems_items_number )                               | No      | string           | No         | -                                                                          | Number of the resource within the related item, e.g., report number or article number.                                  |
| - [numberType](#data_attributes_relatedItems_items_numberType )                       | No      | enum (of string) | No         | -                                                                          | Type of the related item’s number, e.g., report number or article number.                                               |
| - [firstPage](#data_attributes_relatedItems_items_firstPage )                         | No      | string           | No         | -                                                                          | First page of the resource within the related item, e.g., of the chapter, article, or conference paper in proceedings.  |
| - [lastPage](#data_attributes_relatedItems_items_lastPage )                           | No      | string           | No         | -                                                                          | Last page of the resource within the related item, e.g., of the chapter, article, or conference paper in proceedings.   |
| - [publisher](#data_attributes_relatedItems_items_publisher )                         | No      | string           | No         | -                                                                          | The name of the entity that holds, archives, publishes prints, distributes, releases, issues, or produces the resource. |
| - [edition](#data_attributes_relatedItems_items_edition )                             | No      | string           | No         | -                                                                          | Edition or version of the related item.                                                                                 |
| - [contributors](#data_attributes_relatedItems_items_contributors )                   | No      | array            | No         | -                                                                          | An institution or person identified as contributing to the development of the resource                                  |

###### <a name="data_attributes_relatedItems_items_relatedItemType"></a>1.3.24.1.1. Property `root > data > attributes > relatedItems > relatedItems items > relatedItemType`

|                        |                                                                   |
| ---------------------- | ----------------------------------------------------------------- |
| **Type**               | `enum (of string)`                                                |
| **Required**           | Yes                                                               |
| **Same definition as** | [resourceTypeGeneral](#data_attributes_types_resourceTypeGeneral) |

**Description:** The general type of a resource.

###### <a name="data_attributes_relatedItems_items_relationType"></a>1.3.24.1.2. Property `root > data > attributes > relatedItems > relatedItems items > relationType`

|                        |                                                                   |
| ---------------------- | ----------------------------------------------------------------- |
| **Type**               | `enum (of string)`                                                |
| **Required**           | Yes                                                               |
| **Same definition as** | [resourceTypeGeneral](#data_attributes_types_resourceTypeGeneral) |

**Description:** The general type of a resource.

###### <a name="data_attributes_relatedItems_items_relatedItemIdentifier"></a>1.3.24.1.3. Property `root > data > attributes > relatedItems > relatedItems items > relatedItemIdentifier`

|                           |                               |
| ------------------------- | ----------------------------- |
| **Type**                  | `object`                      |
| **Required**              | No                            |
| **Additional properties** | Any type allowed              |
| **Defined in**            | #/$defs/RelatedItemIdentifier |

**Description:** The identifier for the related item.

| Property                                                                                                            | Pattern | Type             | Deprecated | Definition                                                                                        | Title/Description                                                |
| ------------------------------------------------------------------------------------------------------------------- | ------- | ---------------- | ---------- | ------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------- |
| - [relatedItemIdentifierType](#data_attributes_relatedItems_items_relatedItemIdentifier_relatedItemIdentifierType ) | No      | enum (of string) | No         | Same as [relatedIdentifierType](#data_attributes_relatedIdentifiers_items_relatedIdentifierType ) | The type of the RelatedIdentifier.                               |
| - [relatedMetadataScheme](#data_attributes_relatedItems_items_relatedItemIdentifier_relatedMetadataScheme )         | No      | string           | No         | -                                                                                                 | The name of the schemes.                                         |
| - [schemeURI](#data_attributes_relatedItems_items_relatedItemIdentifier_schemeURI )                                 | No      | string           | No         | -                                                                                                 | The URI of the name identifier scheme.                           |
| - [schemeType](#data_attributes_relatedItems_items_relatedItemIdentifier_schemeType )                               | No      | string           | No         | -                                                                                                 | The type of the relatedMetadataScheme, linked with the schemeURI |

###### <a name="data_attributes_relatedItems_items_relatedItemIdentifier_relatedItemIdentifierType"></a>1.3.24.1.3.1. Property `root > data > attributes > relatedItems > relatedItems items > relatedItemIdentifier > relatedItemIdentifierType`

|                        |                                                                                          |
| ---------------------- | ---------------------------------------------------------------------------------------- |
| **Type**               | `enum (of string)`                                                                       |
| **Required**           | No                                                                                       |
| **Same definition as** | [relatedIdentifierType](#data_attributes_relatedIdentifiers_items_relatedIdentifierType) |

**Description:** The type of the RelatedIdentifier.

###### <a name="data_attributes_relatedItems_items_relatedItemIdentifier_relatedMetadataScheme"></a>1.3.24.1.3.2. Property `root > data > attributes > relatedItems > relatedItems items > relatedItemIdentifier > relatedMetadataScheme`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** The name of the schemes.

###### <a name="data_attributes_relatedItems_items_relatedItemIdentifier_schemeURI"></a>1.3.24.1.3.3. Property `root > data > attributes > relatedItems > relatedItems items > relatedItemIdentifier > schemeURI`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `uri`    |

**Description:** The URI of the name identifier scheme.

###### <a name="data_attributes_relatedItems_items_relatedItemIdentifier_schemeType"></a>1.3.24.1.3.4. Property `root > data > attributes > relatedItems > relatedItems items > relatedItemIdentifier > schemeType`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** The type of the relatedMetadataScheme, linked with the schemeURI

###### <a name="data_attributes_relatedItems_items_creators"></a>1.3.24.1.4. Property `root > data > attributes > relatedItems > relatedItems items > creators`

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |

**Description:** The institution or person responsible for creating the related resource.

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | N/A                |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be                                          | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| [RelatedItemCreator](#data_attributes_relatedItems_items_creators_items) | The institution or person responsible for creating the related resource. |

###### <a name="data_attributes_relatedItems_items_creators_items"></a>1.3.24.1.4.1. root > data > attributes > relatedItems > relatedItems items > creators > RelatedItemCreator

|                           |                            |
| ------------------------- | -------------------------- |
| **Type**                  | `object`                   |
| **Required**              | No                         |
| **Additional properties** | Any type allowed           |
| **Defined in**            | #/$defs/RelatedItemCreator |

**Description:** The institution or person responsible for creating the related resource.

| Property                                                                       | Pattern | Type             | Deprecated | Definition                                                    | Title/Description                          |
| ------------------------------------------------------------------------------ | ------- | ---------------- | ---------- | ------------------------------------------------------------- | ------------------------------------------ |
| + [name](#data_attributes_relatedItems_items_creators_items_name )             | No      | string           | No         | -                                                             | The full name of the related item creator  |
| - [nameType](#data_attributes_relatedItems_items_creators_items_nameType )     | No      | enum (of string) | No         | Same as [nameType](#data_attributes_creators_items_nameType ) | The type of name.                          |
| - [givenName](#data_attributes_relatedItems_items_creators_items_givenName )   | No      | string           | No         | -                                                             | The personal or first name of the creator. |
| - [familyName](#data_attributes_relatedItems_items_creators_items_familyName ) | No      | string           | No         | -                                                             | The surname or last name of the creator.   |

###### <a name="data_attributes_relatedItems_items_creators_items_name"></a>1.3.24.1.4.1.1. Property `root > data > attributes > relatedItems > relatedItems items > creators > creators items > name`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** The full name of the related item creator

###### <a name="data_attributes_relatedItems_items_creators_items_nameType"></a>1.3.24.1.4.1.2. Property `root > data > attributes > relatedItems > relatedItems items > creators > creators items > nameType`

|                        |                                                      |
| ---------------------- | ---------------------------------------------------- |
| **Type**               | `enum (of string)`                                   |
| **Required**           | No                                                   |
| **Same definition as** | [nameType](#data_attributes_creators_items_nameType) |

**Description:** The type of name.

###### <a name="data_attributes_relatedItems_items_creators_items_givenName"></a>1.3.24.1.4.1.3. Property `root > data > attributes > relatedItems > relatedItems items > creators > creators items > givenName`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** The personal or first name of the creator.

###### <a name="data_attributes_relatedItems_items_creators_items_familyName"></a>1.3.24.1.4.1.4. Property `root > data > attributes > relatedItems > relatedItems items > creators > creators items > familyName`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** The surname or last name of the creator.

###### <a name="data_attributes_relatedItems_items_titles"></a>1.3.24.1.5. Property `root > data > attributes > relatedItems > relatedItems items > titles`

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | Yes     |

**Description:** Title of the related item

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | 1                  |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be                                      | Description                |
| -------------------------------------------------------------------- | -------------------------- |
| [RelatedItemTitle](#data_attributes_relatedItems_items_titles_items) | Title of the related item. |

###### <a name="data_attributes_relatedItems_items_titles_items"></a>1.3.24.1.5.1. root > data > attributes > relatedItems > relatedItems items > titles > RelatedItemTitle

|                           |                          |
| ------------------------- | ------------------------ |
| **Type**                  | `object`                 |
| **Required**              | No                       |
| **Additional properties** | Any type allowed         |
| **Defined in**            | #/$defs/RelatedItemTitle |

**Description:** Title of the related item.

| Property                                                                   | Pattern | Type   | Deprecated | Definition | Title/Description               |
| -------------------------------------------------------------------------- | ------- | ------ | ---------- | ---------- | ------------------------------- |
| + [title](#data_attributes_relatedItems_items_titles_items_title )         | No      | string | No         | -          | Title of the related item.      |
| - [titleType](#data_attributes_relatedItems_items_titles_items_titleType ) | No      | string | No         | -          | Type of the related item title. |

###### <a name="data_attributes_relatedItems_items_titles_items_title"></a>1.3.24.1.5.1.1. Property `root > data > attributes > relatedItems > relatedItems items > titles > titles items > title`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** Title of the related item.

###### <a name="data_attributes_relatedItems_items_titles_items_titleType"></a>1.3.24.1.5.1.2. Property `root > data > attributes > relatedItems > relatedItems items > titles > titles items > titleType`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** Type of the related item title.

###### <a name="data_attributes_relatedItems_items_publicationYear"></a>1.3.24.1.6. Property `root > data > attributes > relatedItems > relatedItems items > publicationYear`

|                           |                                                     |
| ------------------------- | --------------------------------------------------- |
| **Type**                  | `combining`                                         |
| **Required**              | No                                                  |
| **Additional properties** | Any type allowed                                    |
| **Same definition as**    | [publicationYear](#data_attributes_publicationYear) |

**Description:** The year when the data was or will be made publicly available.

###### <a name="data_attributes_relatedItems_items_volume"></a>1.3.24.1.7. Property `root > data > attributes > relatedItems > relatedItems items > volume`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** Volume of the related item.

###### <a name="data_attributes_relatedItems_items_issue"></a>1.3.24.1.8. Property `root > data > attributes > relatedItems > relatedItems items > issue`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** Issue number or name of the related item.

###### <a name="data_attributes_relatedItems_items_number"></a>1.3.24.1.9. Property `root > data > attributes > relatedItems > relatedItems items > number`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** Number of the resource within the related item, e.g., report number or article number.

###### <a name="data_attributes_relatedItems_items_numberType"></a>1.3.24.1.10. Property `root > data > attributes > relatedItems > relatedItems items > numberType`

|              |                    |
| ------------ | ------------------ |
| **Type**     | `enum (of string)` |
| **Required** | No                 |

**Description:** Type of the related item’s number, e.g., report number or article number.

Must be one of:
* "Article"
* "Chapter"
* "Report"
* "Other"

###### <a name="data_attributes_relatedItems_items_firstPage"></a>1.3.24.1.11. Property `root > data > attributes > relatedItems > relatedItems items > firstPage`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** First page of the resource within the related item, e.g., of the chapter, article, or conference paper in proceedings.

###### <a name="data_attributes_relatedItems_items_lastPage"></a>1.3.24.1.12. Property `root > data > attributes > relatedItems > relatedItems items > lastPage`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** Last page of the resource within the related item, e.g., of the chapter, article, or conference paper in proceedings.

###### <a name="data_attributes_relatedItems_items_publisher"></a>1.3.24.1.13. Property `root > data > attributes > relatedItems > relatedItems items > publisher`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** The name of the entity that holds, archives, publishes prints, distributes, releases, issues, or produces the resource.

###### <a name="data_attributes_relatedItems_items_edition"></a>1.3.24.1.14. Property `root > data > attributes > relatedItems > relatedItems items > edition`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** Edition or version of the related item.

###### <a name="data_attributes_relatedItems_items_contributors"></a>1.3.24.1.15. Property `root > data > attributes > relatedItems > relatedItems items > contributors`

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |

**Description:** An institution or person identified as contributing to the development of the resource

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | N/A                |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be                                                  | Description                                                                             |
| -------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| [RelatedItemContributor](#data_attributes_relatedItems_items_contributors_items) | An institution or person identified as contributing to the development of the resource. |

###### <a name="data_attributes_relatedItems_items_contributors_items"></a>1.3.24.1.15.1. root > data > attributes > relatedItems > relatedItems items > contributors > RelatedItemContributor

|                           |                                |
| ------------------------- | ------------------------------ |
| **Type**                  | `combining`                    |
| **Required**              | No                             |
| **Additional properties** | Any type allowed               |
| **Defined in**            | #/$defs/RelatedItemContributor |

**Description:** An institution or person identified as contributing to the development of the resource.

| All of(Requirement)                                                                   |
| ------------------------------------------------------------------------------------- |
| [RelatedItemCreator](#data_attributes_relatedItems_items_contributors_items_allOf_i0) |
| [item 1](#data_attributes_relatedItems_items_contributors_items_allOf_i1)             |

###### <a name="data_attributes_relatedItems_items_contributors_items_allOf_i0"></a>1.3.24.1.15.1.1. Property `root > data > attributes > relatedItems > relatedItems items > contributors > contributors items > allOf > RelatedItemCreator`

|                           |                                                                                                         |
| ------------------------- | ------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                |
| **Required**              | No                                                                                                      |
| **Additional properties** | Any type allowed                                                                                        |
| **Same definition as**    | [data_attributes_relatedItems_items_creators_items](#data_attributes_relatedItems_items_creators_items) |

**Description:** The institution or person responsible for creating the related resource.

###### <a name="data_attributes_relatedItems_items_contributors_items_allOf_i1"></a>1.3.24.1.15.1.2. Property `root > data > attributes > relatedItems > relatedItems items > contributors > contributors items > allOf > item 1`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| Property                                                                                              | Pattern | Type             | Deprecated | Definition                                                                               | Title/Description                       |
| ----------------------------------------------------------------------------------------------------- | ------- | ---------------- | ---------- | ---------------------------------------------------------------------------------------- | --------------------------------------- |
| + [contributorType](#data_attributes_relatedItems_items_contributors_items_allOf_i1_contributorType ) | No      | enum (of string) | No         | Same as [contributorType](#data_attributes_contributors_items_allOf_i1_contributorType ) | The type of contributor of the resource |

###### <a name="data_attributes_relatedItems_items_contributors_items_allOf_i1_contributorType"></a>1.3.24.1.15.1.2.1. Property `root > data > attributes > relatedItems > relatedItems items > contributors > contributors items > allOf > item 1 > contributorType`

|                        |                                                                                 |
| ---------------------- | ------------------------------------------------------------------------------- |
| **Type**               | `enum (of string)`                                                              |
| **Required**           | Yes                                                                             |
| **Same definition as** | [contributorType](#data_attributes_contributors_items_allOf_i1_contributorType) |

**Description:** The type of contributor of the resource

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans) on 2025-11-02 at 00:11:30 +0100
