# Schema Docs

- [1. Property `root > id`](#id)
- [2. Property `root > type`](#type)
- [3. Property `root > time`](#time)
  - [3.1. Property `root > time > oneOf > item 0`](#time_oneOf_i0)
  - [3.2. Property `root > time > oneOf > time`](#time_oneOf_i1)
    - [3.2.1. Property `root > time > oneOf > item 1 > date`](#time_oneOf_i1_date)
    - [3.2.2. Property `root > time > oneOf > item 1 > timestamp`](#time_oneOf_i1_timestamp)
    - [3.2.3. Property `root > time > oneOf > item 1 > interval`](#time_oneOf_i1_interval)
      - [3.2.3.1. root > time > oneOf > item 1 > interval > interval items](#time_oneOf_i1_interval_items)
        - [3.2.3.1.1. Property `root > time > oneOf > item 1 > interval > interval items > oneOf > item 0`](#time_oneOf_i1_interval_items_oneOf_i0)
        - [3.2.3.1.2. Property `root > time > oneOf > item 1 > interval > interval items > oneOf > item 1`](#time_oneOf_i1_interval_items_oneOf_i1)
        - [3.2.3.1.3. Property `root > time > oneOf > item 1 > interval > interval items > oneOf > item 2`](#time_oneOf_i1_interval_items_oneOf_i2)
    - [3.2.4. Property `root > time > oneOf > item 1 > resolution`](#time_oneOf_i1_resolution)
- [4. Property `root > geometry`](#geometry)
  - [4.1. Property `root > geometry > oneOf > item 0`](#geometry_oneOf_i0)
  - [4.2. Property `root > geometry > oneOf > geometryGeoJSON`](#geometry_oneOf_i1)
    - [4.2.1. Property `root > geometry > oneOf > item 1 > oneOf > pointGeoJSON`](#geometry_oneOf_i1_oneOf_i0)
      - [4.2.1.1. Property `root > geometry > oneOf > item 1 > oneOf > item 0 > type`](#geometry_oneOf_i1_oneOf_i0_type)
      - [4.2.1.2. Property `root > geometry > oneOf > item 1 > oneOf > item 0 > coordinates`](#geometry_oneOf_i1_oneOf_i0_coordinates)
        - [4.2.1.2.1. root > geometry > oneOf > item 1 > oneOf > item 0 > coordinates > coordinates items](#geometry_oneOf_i1_oneOf_i0_coordinates_items)
    - [4.2.2. Property `root > geometry > oneOf > item 1 > oneOf > multipointGeoJSON`](#geometry_oneOf_i1_oneOf_i1)
      - [4.2.2.1. Property `root > geometry > oneOf > item 1 > oneOf > item 1 > type`](#geometry_oneOf_i1_oneOf_i1_type)
      - [4.2.2.2. Property `root > geometry > oneOf > item 1 > oneOf > item 1 > coordinates`](#geometry_oneOf_i1_oneOf_i1_coordinates)
        - [4.2.2.2.1. root > geometry > oneOf > item 1 > oneOf > item 1 > coordinates > coordinates items](#geometry_oneOf_i1_oneOf_i1_coordinates_items)
          - [4.2.2.2.1.1. root > geometry > oneOf > item 1 > oneOf > item 1 > coordinates > coordinates items > coordinates items items](#geometry_oneOf_i1_oneOf_i1_coordinates_items_items)
    - [4.2.3. Property `root > geometry > oneOf > item 1 > oneOf > linestringGeoJSON`](#geometry_oneOf_i1_oneOf_i2)
      - [4.2.3.1. Property `root > geometry > oneOf > item 1 > oneOf > item 2 > type`](#geometry_oneOf_i1_oneOf_i2_type)
      - [4.2.3.2. Property `root > geometry > oneOf > item 1 > oneOf > item 2 > coordinates`](#geometry_oneOf_i1_oneOf_i2_coordinates)
        - [4.2.3.2.1. root > geometry > oneOf > item 1 > oneOf > item 2 > coordinates > coordinates items](#geometry_oneOf_i1_oneOf_i2_coordinates_items)
          - [4.2.3.2.1.1. root > geometry > oneOf > item 1 > oneOf > item 2 > coordinates > coordinates items > coordinates items items](#geometry_oneOf_i1_oneOf_i2_coordinates_items_items)
    - [4.2.4. Property `root > geometry > oneOf > item 1 > oneOf > multilinestringGeoJSON`](#geometry_oneOf_i1_oneOf_i3)
      - [4.2.4.1. Property `root > geometry > oneOf > item 1 > oneOf > item 3 > type`](#geometry_oneOf_i1_oneOf_i3_type)
      - [4.2.4.2. Property `root > geometry > oneOf > item 1 > oneOf > item 3 > coordinates`](#geometry_oneOf_i1_oneOf_i3_coordinates)
        - [4.2.4.2.1. root > geometry > oneOf > item 1 > oneOf > item 3 > coordinates > coordinates items](#geometry_oneOf_i1_oneOf_i3_coordinates_items)
          - [4.2.4.2.1.1. root > geometry > oneOf > item 1 > oneOf > item 3 > coordinates > coordinates items > coordinates items items](#geometry_oneOf_i1_oneOf_i3_coordinates_items_items)
            - [4.2.4.2.1.1.1. root > geometry > oneOf > item 1 > oneOf > item 3 > coordinates > coordinates items > coordinates items items > coordinates items items items](#geometry_oneOf_i1_oneOf_i3_coordinates_items_items_items)
    - [4.2.5. Property `root > geometry > oneOf > item 1 > oneOf > polygonGeoJSON`](#geometry_oneOf_i1_oneOf_i4)
      - [4.2.5.1. Property `root > geometry > oneOf > item 1 > oneOf > item 4 > type`](#geometry_oneOf_i1_oneOf_i4_type)
      - [4.2.5.2. Property `root > geometry > oneOf > item 1 > oneOf > item 4 > coordinates`](#geometry_oneOf_i1_oneOf_i4_coordinates)
        - [4.2.5.2.1. root > geometry > oneOf > item 1 > oneOf > item 4 > coordinates > coordinates items](#geometry_oneOf_i1_oneOf_i4_coordinates_items)
          - [4.2.5.2.1.1. root > geometry > oneOf > item 1 > oneOf > item 4 > coordinates > coordinates items > coordinates items items](#geometry_oneOf_i1_oneOf_i4_coordinates_items_items)
            - [4.2.5.2.1.1.1. root > geometry > oneOf > item 1 > oneOf > item 4 > coordinates > coordinates items > coordinates items items > coordinates items items items](#geometry_oneOf_i1_oneOf_i4_coordinates_items_items_items)
    - [4.2.6. Property `root > geometry > oneOf > item 1 > oneOf > multipolygonGeoJSON`](#geometry_oneOf_i1_oneOf_i5)
      - [4.2.6.1. Property `root > geometry > oneOf > item 1 > oneOf > item 5 > type`](#geometry_oneOf_i1_oneOf_i5_type)
      - [4.2.6.2. Property `root > geometry > oneOf > item 1 > oneOf > item 5 > coordinates`](#geometry_oneOf_i1_oneOf_i5_coordinates)
        - [4.2.6.2.1. root > geometry > oneOf > item 1 > oneOf > item 5 > coordinates > coordinates items](#geometry_oneOf_i1_oneOf_i5_coordinates_items)
          - [4.2.6.2.1.1. root > geometry > oneOf > item 1 > oneOf > item 5 > coordinates > coordinates items > coordinates items items](#geometry_oneOf_i1_oneOf_i5_coordinates_items_items)
    - [4.2.7. Property `root > geometry > oneOf > item 1 > oneOf > geometrycollectionGeoJSON`](#geometry_oneOf_i1_oneOf_i6)
      - [4.2.7.1. Property `root > geometry > oneOf > item 1 > oneOf > item 6 > type`](#geometry_oneOf_i1_oneOf_i6_type)
      - [4.2.7.2. Property `root > geometry > oneOf > item 1 > oneOf > item 6 > geometries`](#geometry_oneOf_i1_oneOf_i6_geometries)
        - [4.2.7.2.1. root > geometry > oneOf > item 1 > oneOf > item 6 > geometries > geometryGeoJSON](#geometry_oneOf_i1_oneOf_i6_geometries_items)
- [5. Property `root > conformsTo`](#conformsTo)
  - [5.1. root > conformsTo > conformsTo items](#conformsTo_items)
- [6. Property `root > properties`](#properties)
  - [6.1. Property `root > properties > allOf > recordCommonProperties`](#properties_allOf_i0)
    - [6.1.1. Property `root > properties > allOf > item 0 > created`](#properties_allOf_i0_created)
    - [6.1.2. Property `root > properties > allOf > item 0 > updated`](#properties_allOf_i0_updated)
    - [6.1.3. Property `root > properties > allOf > item 0 > type`](#properties_allOf_i0_type)
    - [6.1.4. Property `root > properties > allOf > item 0 > title`](#properties_allOf_i0_title)
    - [6.1.5. Property `root > properties > allOf > item 0 > description`](#properties_allOf_i0_description)
    - [6.1.6. Property `root > properties > allOf > item 0 > keywords`](#properties_allOf_i0_keywords)
      - [6.1.6.1. root > properties > allOf > item 0 > keywords > keywords items](#properties_allOf_i0_keywords_items)
    - [6.1.7. Property `root > properties > allOf > item 0 > themes`](#properties_allOf_i0_themes)
      - [6.1.7.1. root > properties > allOf > item 0 > themes > theme](#properties_allOf_i0_themes_items)
        - [6.1.7.1.1. Property `root > properties > allOf > item 0 > themes > themes items > concepts`](#properties_allOf_i0_themes_items_concepts)
          - [6.1.7.1.1.1. root > properties > allOf > item 0 > themes > themes items > concepts > concepts items](#properties_allOf_i0_themes_items_concepts_items)
            - [6.1.7.1.1.1.1. Property `root > properties > allOf > item 0 > themes > themes items > concepts > concepts items > id`](#properties_allOf_i0_themes_items_concepts_items_id)
            - [6.1.7.1.1.1.2. Property `root > properties > allOf > item 0 > themes > themes items > concepts > concepts items > title`](#properties_allOf_i0_themes_items_concepts_items_title)
            - [6.1.7.1.1.1.3. Property `root > properties > allOf > item 0 > themes > themes items > concepts > concepts items > description`](#properties_allOf_i0_themes_items_concepts_items_description)
            - [6.1.7.1.1.1.4. Property `root > properties > allOf > item 0 > themes > themes items > concepts > concepts items > url`](#properties_allOf_i0_themes_items_concepts_items_url)
        - [6.1.7.1.2. Property `root > properties > allOf > item 0 > themes > themes items > scheme`](#properties_allOf_i0_themes_items_scheme)
    - [6.1.8. Property `root > properties > allOf > item 0 > language`](#properties_allOf_i0_language)
      - [6.1.8.1. Property `root > properties > allOf > item 0 > language > code`](#properties_allOf_i0_language_code)
      - [6.1.8.2. Property `root > properties > allOf > item 0 > language > name`](#properties_allOf_i0_language_name)
      - [6.1.8.3. Property `root > properties > allOf > item 0 > language > alternate`](#properties_allOf_i0_language_alternate)
      - [6.1.8.4. Property `root > properties > allOf > item 0 > language > dir`](#properties_allOf_i0_language_dir)
    - [6.1.9. Property `root > properties > allOf > item 0 > languages`](#properties_allOf_i0_languages)
      - [6.1.9.1. root > properties > allOf > item 0 > languages > language](#properties_allOf_i0_languages_items)
    - [6.1.10. Property `root > properties > allOf > item 0 > resourceLanguages`](#properties_allOf_i0_resourceLanguages)
      - [6.1.10.1. root > properties > allOf > item 0 > resourceLanguages > language](#properties_allOf_i0_resourceLanguages_items)
    - [6.1.11. Property `root > properties > allOf > item 0 > externalIds`](#properties_allOf_i0_externalIds)
      - [6.1.11.1. root > properties > allOf > item 0 > externalIds > externalIds items](#properties_allOf_i0_externalIds_items)
        - [6.1.11.1.1. Property `root > properties > allOf > item 0 > externalIds > externalIds items > scheme`](#properties_allOf_i0_externalIds_items_scheme)
        - [6.1.11.1.2. Property `root > properties > allOf > item 0 > externalIds > externalIds items > value`](#properties_allOf_i0_externalIds_items_value)
    - [6.1.12. Property `root > properties > allOf > item 0 > formats`](#properties_allOf_i0_formats)
      - [6.1.12.1. root > properties > allOf > item 0 > formats > format](#properties_allOf_i0_formats_items)
        - [6.1.12.1.1. Property `root > properties > allOf > item 0 > formats > formats items > anyOf > item 0`](#properties_allOf_i0_formats_items_anyOf_i0)
          - [6.1.12.1.1.1. The following properties are required](#autogenerated_heading_2)
        - [6.1.12.1.2. Property `root > properties > allOf > item 0 > formats > formats items > anyOf > item 1`](#properties_allOf_i0_formats_items_anyOf_i1)
          - [6.1.12.1.2.1. The following properties are required](#autogenerated_heading_3)
        - [6.1.12.1.3. Property `root > properties > allOf > item 0 > formats > formats items > name`](#properties_allOf_i0_formats_items_name)
        - [6.1.12.1.4. Property `root > properties > allOf > item 0 > formats > formats items > mediaType`](#properties_allOf_i0_formats_items_mediaType)
    - [6.1.13. Property `root > properties > allOf > item 0 > contacts`](#properties_allOf_i0_contacts)
      - [6.1.13.1. root > properties > allOf > item 0 > contacts > contact](#properties_allOf_i0_contacts_items)
        - [6.1.13.1.1. Property `root > properties > allOf > item 0 > contacts > contacts items > anyOf > item 0`](#properties_allOf_i0_contacts_items_anyOf_i0)
          - [6.1.13.1.1.1. The following properties are required](#autogenerated_heading_4)
        - [6.1.13.1.2. Property `root > properties > allOf > item 0 > contacts > contacts items > anyOf > item 1`](#properties_allOf_i0_contacts_items_anyOf_i1)
          - [6.1.13.1.2.1. The following properties are required](#autogenerated_heading_5)
        - [6.1.13.1.3. Property `root > properties > allOf > item 0 > contacts > contacts items > identifier`](#properties_allOf_i0_contacts_items_identifier)
        - [6.1.13.1.4. Property `root > properties > allOf > item 0 > contacts > contacts items > name`](#properties_allOf_i0_contacts_items_name)
        - [6.1.13.1.5. Property `root > properties > allOf > item 0 > contacts > contacts items > position`](#properties_allOf_i0_contacts_items_position)
        - [6.1.13.1.6. Property `root > properties > allOf > item 0 > contacts > contacts items > organization`](#properties_allOf_i0_contacts_items_organization)
        - [6.1.13.1.7. Property `root > properties > allOf > item 0 > contacts > contacts items > logo`](#properties_allOf_i0_contacts_items_logo)
          - [6.1.13.1.7.1. Property `root > properties > allOf > item 0 > contacts > contacts items > logo > allOf > link`](#properties_allOf_i0_contacts_items_logo_allOf_i0)
            - [6.1.13.1.7.1.1. Property `root > properties > allOf > item 0 > contacts > contacts items > logo > allOf > item 0 > allOf > linkBase`](#properties_allOf_i0_contacts_items_logo_allOf_i0_allOf_i0)
              - [6.1.13.1.7.1.1.1. Property `root > properties > allOf > item 0 > contacts > contacts items > logo > allOf > item 0 > allOf > item 0 > rel`](#properties_allOf_i0_contacts_items_logo_allOf_i0_allOf_i0_rel)
              - [6.1.13.1.7.1.1.2. Property `root > properties > allOf > item 0 > contacts > contacts items > logo > allOf > item 0 > allOf > item 0 > type`](#properties_allOf_i0_contacts_items_logo_allOf_i0_allOf_i0_type)
              - [6.1.13.1.7.1.1.3. Property `root > properties > allOf > item 0 > contacts > contacts items > logo > allOf > item 0 > allOf > item 0 > hreflang`](#properties_allOf_i0_contacts_items_logo_allOf_i0_allOf_i0_hreflang)
              - [6.1.13.1.7.1.1.4. Property `root > properties > allOf > item 0 > contacts > contacts items > logo > allOf > item 0 > allOf > item 0 > title`](#properties_allOf_i0_contacts_items_logo_allOf_i0_allOf_i0_title)
              - [6.1.13.1.7.1.1.5. Property `root > properties > allOf > item 0 > contacts > contacts items > logo > allOf > item 0 > allOf > item 0 > length`](#properties_allOf_i0_contacts_items_logo_allOf_i0_allOf_i0_length)
              - [6.1.13.1.7.1.1.6. Property `root > properties > allOf > item 0 > contacts > contacts items > logo > allOf > item 0 > allOf > item 0 > created`](#properties_allOf_i0_contacts_items_logo_allOf_i0_allOf_i0_created)
              - [6.1.13.1.7.1.1.7. Property `root > properties > allOf > item 0 > contacts > contacts items > logo > allOf > item 0 > allOf > item 0 > updated`](#properties_allOf_i0_contacts_items_logo_allOf_i0_allOf_i0_updated)
            - [6.1.13.1.7.1.2. Property `root > properties > allOf > item 0 > contacts > contacts items > logo > allOf > item 0 > allOf > item 1`](#properties_allOf_i0_contacts_items_logo_allOf_i0_allOf_i1)
              - [6.1.13.1.7.1.2.1. Property `root > properties > allOf > item 0 > contacts > contacts items > logo > allOf > item 0 > allOf > item 1 > href`](#properties_allOf_i0_contacts_items_logo_allOf_i0_allOf_i1_href)
          - [6.1.13.1.7.2. Property `root > properties > allOf > item 0 > contacts > contacts items > logo > allOf > item 1`](#properties_allOf_i0_contacts_items_logo_allOf_i1)
            - [6.1.13.1.7.2.1. The following properties are required](#autogenerated_heading_6)
            - [6.1.13.1.7.2.2. Property `root > properties > allOf > item 0 > contacts > contacts items > logo > allOf > item 1 > rel`](#properties_allOf_i0_contacts_items_logo_allOf_i1_rel)
        - [6.1.13.1.8. Property `root > properties > allOf > item 0 > contacts > contacts items > phones`](#properties_allOf_i0_contacts_items_phones)
          - [6.1.13.1.8.1. root > properties > allOf > item 0 > contacts > contacts items > phones > phones items](#properties_allOf_i0_contacts_items_phones_items)
            - [6.1.13.1.8.1.1. Property `root > properties > allOf > item 0 > contacts > contacts items > phones > phones items > value`](#properties_allOf_i0_contacts_items_phones_items_value)
            - [6.1.13.1.8.1.2. Property `root > properties > allOf > item 0 > contacts > contacts items > phones > phones items > roles`](#properties_allOf_i0_contacts_items_phones_items_roles)
              - [6.1.13.1.8.1.2.1. root > properties > allOf > item 0 > contacts > contacts items > phones > phones items > roles > roles items](#properties_allOf_i0_contacts_items_phones_items_roles_items)
        - [6.1.13.1.9. Property `root > properties > allOf > item 0 > contacts > contacts items > emails`](#properties_allOf_i0_contacts_items_emails)
          - [6.1.13.1.9.1. root > properties > allOf > item 0 > contacts > contacts items > emails > emails items](#properties_allOf_i0_contacts_items_emails_items)
            - [6.1.13.1.9.1.1. Property `root > properties > allOf > item 0 > contacts > contacts items > emails > emails items > value`](#properties_allOf_i0_contacts_items_emails_items_value)
            - [6.1.13.1.9.1.2. Property `root > properties > allOf > item 0 > contacts > contacts items > emails > emails items > roles`](#properties_allOf_i0_contacts_items_emails_items_roles)
        - [6.1.13.1.10. Property `root > properties > allOf > item 0 > contacts > contacts items > addresses`](#properties_allOf_i0_contacts_items_addresses)
          - [6.1.13.1.10.1. root > properties > allOf > item 0 > contacts > contacts items > addresses > addresses items](#properties_allOf_i0_contacts_items_addresses_items)
            - [6.1.13.1.10.1.1. Property `root > properties > allOf > item 0 > contacts > contacts items > addresses > addresses items > deliveryPoint`](#properties_allOf_i0_contacts_items_addresses_items_deliveryPoint)
              - [6.1.13.1.10.1.1.1. root > properties > allOf > item 0 > contacts > contacts items > addresses > addresses items > deliveryPoint > deliveryPoint items](#properties_allOf_i0_contacts_items_addresses_items_deliveryPoint_items)
            - [6.1.13.1.10.1.2. Property `root > properties > allOf > item 0 > contacts > contacts items > addresses > addresses items > city`](#properties_allOf_i0_contacts_items_addresses_items_city)
            - [6.1.13.1.10.1.3. Property `root > properties > allOf > item 0 > contacts > contacts items > addresses > addresses items > administrativeArea`](#properties_allOf_i0_contacts_items_addresses_items_administrativeArea)
            - [6.1.13.1.10.1.4. Property `root > properties > allOf > item 0 > contacts > contacts items > addresses > addresses items > postalCode`](#properties_allOf_i0_contacts_items_addresses_items_postalCode)
            - [6.1.13.1.10.1.5. Property `root > properties > allOf > item 0 > contacts > contacts items > addresses > addresses items > country`](#properties_allOf_i0_contacts_items_addresses_items_country)
            - [6.1.13.1.10.1.6. Property `root > properties > allOf > item 0 > contacts > contacts items > addresses > addresses items > roles`](#properties_allOf_i0_contacts_items_addresses_items_roles)
        - [6.1.13.1.11. Property `root > properties > allOf > item 0 > contacts > contacts items > links`](#properties_allOf_i0_contacts_items_links)
          - [6.1.13.1.11.1. root > properties > allOf > item 0 > contacts > contacts items > links > links items](#properties_allOf_i0_contacts_items_links_items)
            - [6.1.13.1.11.1.1. Property `root > properties > allOf > item 0 > contacts > contacts items > links > links items > allOf > link`](#properties_allOf_i0_contacts_items_links_items_allOf_i0)
            - [6.1.13.1.11.1.2. Property `root > properties > allOf > item 0 > contacts > contacts items > links > links items > allOf > item 1`](#properties_allOf_i0_contacts_items_links_items_allOf_i1)
              - [6.1.13.1.11.1.2.1. The following properties are required](#autogenerated_heading_7)
        - [6.1.13.1.12. Property `root > properties > allOf > item 0 > contacts > contacts items > hoursOfService`](#properties_allOf_i0_contacts_items_hoursOfService)
        - [6.1.13.1.13. Property `root > properties > allOf > item 0 > contacts > contacts items > contactInstructions`](#properties_allOf_i0_contacts_items_contactInstructions)
        - [6.1.13.1.14. Property `root > properties > allOf > item 0 > contacts > contacts items > roles`](#properties_allOf_i0_contacts_items_roles)
    - [6.1.14. Property `root > properties > allOf > item 0 > license`](#properties_allOf_i0_license)
    - [6.1.15. Property `root > properties > allOf > item 0 > rights`](#properties_allOf_i0_rights)
  - [6.2. Property `root > properties > allOf > item 1`](#properties_allOf_i1)
- [7. Property `root > links`](#links)
  - [7.1. root > links > link](#links_items)
- [8. Property `root > linkTemplates`](#linkTemplates)
  - [8.1. root > linkTemplates > linkTemplate](#linkTemplates_items)
    - [8.1.1. Property `root > linkTemplates > linkTemplates items > allOf > linkBase`](#linkTemplates_items_allOf_i0)
    - [8.1.2. Property `root > linkTemplates > linkTemplates items > allOf > item 1`](#linkTemplates_items_allOf_i1)
      - [8.1.2.1. Property `root > linkTemplates > linkTemplates items > allOf > item 1 > uriTemplate`](#linkTemplates_items_allOf_i1_uriTemplate)
      - [8.1.2.2. Property `root > linkTemplates > linkTemplates items > allOf > item 1 > varBase`](#linkTemplates_items_allOf_i1_varBase)
      - [8.1.2.3. Property `root > linkTemplates > linkTemplates items > allOf > item 1 > variables`](#linkTemplates_items_allOf_i1_variables)

|                           |                       |
| ------------------------- | --------------------- |
| **Type**                  | `object`              |
| **Required**              | No                    |
| **Additional properties** | Any type allowed      |
| **Defined in**            | #/$defs/recordGeoJSON |

| Property                           | Pattern | Type             | Deprecated | Definition | Title/Description                                       |
| ---------------------------------- | ------- | ---------------- | ---------- | ---------- | ------------------------------------------------------- |
| + [id](#id )                       | No      | string           | No         | -          | A unique identifier of the catalog record.              |
| + [type](#type )                   | No      | enum (of string) | No         | -          | -                                                       |
| - [time](#time )                   | No      | Combination      | No         | -          | -                                                       |
| + [geometry](#geometry )           | No      | Combination      | No         | -          | -                                                       |
| - [conformsTo](#conformsTo )       | No      | array of string  | No         | -          | The extensions/conformance classes used in this record. |
| + [properties](#properties )       | No      | Combination      | No         | -          | -                                                       |
| - [links](#links )                 | No      | array            | No         | -          | -                                                       |
| - [linkTemplates](#linkTemplates ) | No      | array            | No         | -          | -                                                       |

## <a name="id"></a>1. Property `root > id`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** A unique identifier of the catalog record.

## <a name="type"></a>2. Property `root > type`

|              |                    |
| ------------ | ------------------ |
| **Type**     | `enum (of string)` |
| **Required** | Yes                |

Must be one of:
* "Feature"

## <a name="time"></a>3. Property `root > time`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| One of(Option)           |
| ------------------------ |
| [item 0](#time_oneOf_i0) |
| [time](#time_oneOf_i1)   |

### <a name="time_oneOf_i0"></a>3.1. Property `root > time > oneOf > item 0`

|              |                  |
| ------------ | ---------------- |
| **Type**     | `enum (of null)` |
| **Required** | No               |

Must be one of:
* null

### <a name="time_oneOf_i1"></a>3.2. Property `root > time > oneOf > time`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |
| **Defined in**            | #/$defs/time     |

| Property                                   | Pattern | Type   | Deprecated | Definition | Title/Description                                                       |
| ------------------------------------------ | ------- | ------ | ---------- | ---------- | ----------------------------------------------------------------------- |
| - [date](#time_oneOf_i1_date )             | No      | string | No         | -          | -                                                                       |
| - [timestamp](#time_oneOf_i1_timestamp )   | No      | string | No         | -          | -                                                                       |
| - [interval](#time_oneOf_i1_interval )     | No      | array  | No         | -          | -                                                                       |
| - [resolution](#time_oneOf_i1_resolution ) | No      | string | No         | -          | Minimum time period resolvable in the dataset, as an ISO 8601 duration. |

#### <a name="time_oneOf_i1_date"></a>3.2.1. Property `root > time > oneOf > item 1 > date`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

| Restrictions                      |                                                                                                         |
| --------------------------------- | ------------------------------------------------------------------------------------------------------- |
| **Must match regular expression** | ```^\d{4}-\d{2}-\d{2}$``` [Test](https://regex101.com/?regex=%5E%5Cd%7B4%7D-%5Cd%7B2%7D-%5Cd%7B2%7D%24) |

#### <a name="time_oneOf_i1_timestamp"></a>3.2.2. Property `root > time > oneOf > item 1 > timestamp`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

| Restrictions                      |                                                                                                                                                                                                         |
| --------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Must match regular expression** | ```^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d+)?Z$``` [Test](https://regex101.com/?regex=%5E%5Cd%7B4%7D-%5Cd%7B2%7D-%5Cd%7B2%7DT%5Cd%7B2%7D%3A%5Cd%7B2%7D%3A%5Cd%7B2%7D%28%3F%3A%5C.%5Cd%2B%29%3FZ%24) |

#### <a name="time_oneOf_i1_interval"></a>3.2.3. Property `root > time > oneOf > item 1 > interval`

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | 2                  |
| **Max items**        | 2                  |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be                 | Description |
| ----------------------------------------------- | ----------- |
| [interval items](#time_oneOf_i1_interval_items) | -           |

##### <a name="time_oneOf_i1_interval_items"></a>3.2.3.1. root > time > oneOf > item 1 > interval > interval items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| One of(Option)                                   |
| ------------------------------------------------ |
| [item 0](#time_oneOf_i1_interval_items_oneOf_i0) |
| [item 1](#time_oneOf_i1_interval_items_oneOf_i1) |
| [item 2](#time_oneOf_i1_interval_items_oneOf_i2) |

###### <a name="time_oneOf_i1_interval_items_oneOf_i0"></a>3.2.3.1.1. Property `root > time > oneOf > item 1 > interval > interval items > oneOf > item 0`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

| Restrictions                      |                                                                                                         |
| --------------------------------- | ------------------------------------------------------------------------------------------------------- |
| **Must match regular expression** | ```^\d{4}-\d{2}-\d{2}$``` [Test](https://regex101.com/?regex=%5E%5Cd%7B4%7D-%5Cd%7B2%7D-%5Cd%7B2%7D%24) |

###### <a name="time_oneOf_i1_interval_items_oneOf_i1"></a>3.2.3.1.2. Property `root > time > oneOf > item 1 > interval > interval items > oneOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

| Restrictions                      |                                                                                                                                                                                                         |
| --------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Must match regular expression** | ```^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d+)?Z$``` [Test](https://regex101.com/?regex=%5E%5Cd%7B4%7D-%5Cd%7B2%7D-%5Cd%7B2%7DT%5Cd%7B2%7D%3A%5Cd%7B2%7D%3A%5Cd%7B2%7D%28%3F%3A%5C.%5Cd%2B%29%3FZ%24) |

###### <a name="time_oneOf_i1_interval_items_oneOf_i2"></a>3.2.3.1.3. Property `root > time > oneOf > item 1 > interval > interval items > oneOf > item 2`

|              |                    |
| ------------ | ------------------ |
| **Type**     | `enum (of string)` |
| **Required** | No                 |

Must be one of:
* ".."

#### <a name="time_oneOf_i1_resolution"></a>3.2.4. Property `root > time > oneOf > item 1 > resolution`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** Minimum time period resolvable in the dataset, as an ISO 8601 duration.

## <a name="geometry"></a>4. Property `root > geometry`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | Yes              |
| **Additional properties** | Any type allowed |

| One of(Option)                        |
| ------------------------------------- |
| [item 0](#geometry_oneOf_i0)          |
| [geometryGeoJSON](#geometry_oneOf_i1) |

### <a name="geometry_oneOf_i0"></a>4.1. Property `root > geometry > oneOf > item 0`

|              |                  |
| ------------ | ---------------- |
| **Type**     | `enum (of null)` |
| **Required** | No               |

Must be one of:
* null

### <a name="geometry_oneOf_i1"></a>4.2. Property `root > geometry > oneOf > geometryGeoJSON`

|                           |                         |
| ------------------------- | ----------------------- |
| **Type**                  | `combining`             |
| **Required**              | No                      |
| **Additional properties** | Any type allowed        |
| **Defined in**            | #/$defs/geometryGeoJSON |

| One of(Option)                                           |
| -------------------------------------------------------- |
| [pointGeoJSON](#geometry_oneOf_i1_oneOf_i0)              |
| [multipointGeoJSON](#geometry_oneOf_i1_oneOf_i1)         |
| [linestringGeoJSON](#geometry_oneOf_i1_oneOf_i2)         |
| [multilinestringGeoJSON](#geometry_oneOf_i1_oneOf_i3)    |
| [polygonGeoJSON](#geometry_oneOf_i1_oneOf_i4)            |
| [multipolygonGeoJSON](#geometry_oneOf_i1_oneOf_i5)       |
| [geometrycollectionGeoJSON](#geometry_oneOf_i1_oneOf_i6) |

#### <a name="geometry_oneOf_i1_oneOf_i0"></a>4.2.1. Property `root > geometry > oneOf > item 1 > oneOf > pointGeoJSON`

|                           |                      |
| ------------------------- | -------------------- |
| **Type**                  | `object`             |
| **Required**              | No                   |
| **Additional properties** | Any type allowed     |
| **Defined in**            | #/$defs/pointGeoJSON |

| Property                                                  | Pattern | Type             | Deprecated | Definition | Title/Description |
| --------------------------------------------------------- | ------- | ---------------- | ---------- | ---------- | ----------------- |
| + [type](#geometry_oneOf_i1_oneOf_i0_type )               | No      | enum (of string) | No         | -          | -                 |
| + [coordinates](#geometry_oneOf_i1_oneOf_i0_coordinates ) | No      | array of number  | No         | -          | -                 |

##### <a name="geometry_oneOf_i1_oneOf_i0_type"></a>4.2.1.1. Property `root > geometry > oneOf > item 1 > oneOf > item 0 > type`

|              |                    |
| ------------ | ------------------ |
| **Type**     | `enum (of string)` |
| **Required** | Yes                |

Must be one of:
* "Point"

##### <a name="geometry_oneOf_i1_oneOf_i0_coordinates"></a>4.2.1.2. Property `root > geometry > oneOf > item 1 > oneOf > item 0 > coordinates`

|              |                   |
| ------------ | ----------------- |
| **Type**     | `array of number` |
| **Required** | Yes               |

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | 2                  |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be                                    | Description |
| ------------------------------------------------------------------ | ----------- |
| [coordinates items](#geometry_oneOf_i1_oneOf_i0_coordinates_items) | -           |

###### <a name="geometry_oneOf_i1_oneOf_i0_coordinates_items"></a>4.2.1.2.1. root > geometry > oneOf > item 1 > oneOf > item 0 > coordinates > coordinates items

|              |          |
| ------------ | -------- |
| **Type**     | `number` |
| **Required** | No       |

#### <a name="geometry_oneOf_i1_oneOf_i1"></a>4.2.2. Property `root > geometry > oneOf > item 1 > oneOf > multipointGeoJSON`

|                           |                           |
| ------------------------- | ------------------------- |
| **Type**                  | `object`                  |
| **Required**              | No                        |
| **Additional properties** | Any type allowed          |
| **Defined in**            | #/$defs/multipointGeoJSON |

| Property                                                  | Pattern | Type             | Deprecated | Definition | Title/Description |
| --------------------------------------------------------- | ------- | ---------------- | ---------- | ---------- | ----------------- |
| + [type](#geometry_oneOf_i1_oneOf_i1_type )               | No      | enum (of string) | No         | -          | -                 |
| + [coordinates](#geometry_oneOf_i1_oneOf_i1_coordinates ) | No      | array of array   | No         | -          | -                 |

##### <a name="geometry_oneOf_i1_oneOf_i1_type"></a>4.2.2.1. Property `root > geometry > oneOf > item 1 > oneOf > item 1 > type`

|              |                    |
| ------------ | ------------------ |
| **Type**     | `enum (of string)` |
| **Required** | Yes                |

Must be one of:
* "MultiPoint"

##### <a name="geometry_oneOf_i1_oneOf_i1_coordinates"></a>4.2.2.2. Property `root > geometry > oneOf > item 1 > oneOf > item 1 > coordinates`

|              |                  |
| ------------ | ---------------- |
| **Type**     | `array of array` |
| **Required** | Yes              |

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | N/A                |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be                                    | Description |
| ------------------------------------------------------------------ | ----------- |
| [coordinates items](#geometry_oneOf_i1_oneOf_i1_coordinates_items) | -           |

###### <a name="geometry_oneOf_i1_oneOf_i1_coordinates_items"></a>4.2.2.2.1. root > geometry > oneOf > item 1 > oneOf > item 1 > coordinates > coordinates items

|              |                   |
| ------------ | ----------------- |
| **Type**     | `array of number` |
| **Required** | No                |

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | 2                  |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be                                                | Description |
| ------------------------------------------------------------------------------ | ----------- |
| [coordinates items items](#geometry_oneOf_i1_oneOf_i1_coordinates_items_items) | -           |

###### <a name="geometry_oneOf_i1_oneOf_i1_coordinates_items_items"></a>4.2.2.2.1.1. root > geometry > oneOf > item 1 > oneOf > item 1 > coordinates > coordinates items > coordinates items items

|              |          |
| ------------ | -------- |
| **Type**     | `number` |
| **Required** | No       |

#### <a name="geometry_oneOf_i1_oneOf_i2"></a>4.2.3. Property `root > geometry > oneOf > item 1 > oneOf > linestringGeoJSON`

|                           |                           |
| ------------------------- | ------------------------- |
| **Type**                  | `object`                  |
| **Required**              | No                        |
| **Additional properties** | Any type allowed          |
| **Defined in**            | #/$defs/linestringGeoJSON |

| Property                                                  | Pattern | Type             | Deprecated | Definition | Title/Description |
| --------------------------------------------------------- | ------- | ---------------- | ---------- | ---------- | ----------------- |
| + [type](#geometry_oneOf_i1_oneOf_i2_type )               | No      | enum (of string) | No         | -          | -                 |
| + [coordinates](#geometry_oneOf_i1_oneOf_i2_coordinates ) | No      | array of array   | No         | -          | -                 |

##### <a name="geometry_oneOf_i1_oneOf_i2_type"></a>4.2.3.1. Property `root > geometry > oneOf > item 1 > oneOf > item 2 > type`

|              |                    |
| ------------ | ------------------ |
| **Type**     | `enum (of string)` |
| **Required** | Yes                |

Must be one of:
* "LineString"

##### <a name="geometry_oneOf_i1_oneOf_i2_coordinates"></a>4.2.3.2. Property `root > geometry > oneOf > item 1 > oneOf > item 2 > coordinates`

|              |                  |
| ------------ | ---------------- |
| **Type**     | `array of array` |
| **Required** | Yes              |

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | 2                  |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be                                    | Description |
| ------------------------------------------------------------------ | ----------- |
| [coordinates items](#geometry_oneOf_i1_oneOf_i2_coordinates_items) | -           |

###### <a name="geometry_oneOf_i1_oneOf_i2_coordinates_items"></a>4.2.3.2.1. root > geometry > oneOf > item 1 > oneOf > item 2 > coordinates > coordinates items

|              |                   |
| ------------ | ----------------- |
| **Type**     | `array of number` |
| **Required** | No                |

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | 2                  |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be                                                | Description |
| ------------------------------------------------------------------------------ | ----------- |
| [coordinates items items](#geometry_oneOf_i1_oneOf_i2_coordinates_items_items) | -           |

###### <a name="geometry_oneOf_i1_oneOf_i2_coordinates_items_items"></a>4.2.3.2.1.1. root > geometry > oneOf > item 1 > oneOf > item 2 > coordinates > coordinates items > coordinates items items

|              |          |
| ------------ | -------- |
| **Type**     | `number` |
| **Required** | No       |

#### <a name="geometry_oneOf_i1_oneOf_i3"></a>4.2.4. Property `root > geometry > oneOf > item 1 > oneOf > multilinestringGeoJSON`

|                           |                                |
| ------------------------- | ------------------------------ |
| **Type**                  | `object`                       |
| **Required**              | No                             |
| **Additional properties** | Any type allowed               |
| **Defined in**            | #/$defs/multilinestringGeoJSON |

| Property                                                  | Pattern | Type             | Deprecated | Definition | Title/Description |
| --------------------------------------------------------- | ------- | ---------------- | ---------- | ---------- | ----------------- |
| + [type](#geometry_oneOf_i1_oneOf_i3_type )               | No      | enum (of string) | No         | -          | -                 |
| + [coordinates](#geometry_oneOf_i1_oneOf_i3_coordinates ) | No      | array of array   | No         | -          | -                 |

##### <a name="geometry_oneOf_i1_oneOf_i3_type"></a>4.2.4.1. Property `root > geometry > oneOf > item 1 > oneOf > item 3 > type`

|              |                    |
| ------------ | ------------------ |
| **Type**     | `enum (of string)` |
| **Required** | Yes                |

Must be one of:
* "MultiLineString"

##### <a name="geometry_oneOf_i1_oneOf_i3_coordinates"></a>4.2.4.2. Property `root > geometry > oneOf > item 1 > oneOf > item 3 > coordinates`

|              |                  |
| ------------ | ---------------- |
| **Type**     | `array of array` |
| **Required** | Yes              |

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | N/A                |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be                                    | Description |
| ------------------------------------------------------------------ | ----------- |
| [coordinates items](#geometry_oneOf_i1_oneOf_i3_coordinates_items) | -           |

###### <a name="geometry_oneOf_i1_oneOf_i3_coordinates_items"></a>4.2.4.2.1. root > geometry > oneOf > item 1 > oneOf > item 3 > coordinates > coordinates items

|              |                  |
| ------------ | ---------------- |
| **Type**     | `array of array` |
| **Required** | No               |

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | 2                  |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be                                                | Description |
| ------------------------------------------------------------------------------ | ----------- |
| [coordinates items items](#geometry_oneOf_i1_oneOf_i3_coordinates_items_items) | -           |

###### <a name="geometry_oneOf_i1_oneOf_i3_coordinates_items_items"></a>4.2.4.2.1.1. root > geometry > oneOf > item 1 > oneOf > item 3 > coordinates > coordinates items > coordinates items items

|              |                   |
| ------------ | ----------------- |
| **Type**     | `array of number` |
| **Required** | No                |

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | 2                  |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be                                                            | Description |
| ------------------------------------------------------------------------------------------ | ----------- |
| [coordinates items items items](#geometry_oneOf_i1_oneOf_i3_coordinates_items_items_items) | -           |

###### <a name="geometry_oneOf_i1_oneOf_i3_coordinates_items_items_items"></a>4.2.4.2.1.1.1. root > geometry > oneOf > item 1 > oneOf > item 3 > coordinates > coordinates items > coordinates items items > coordinates items items items

|              |          |
| ------------ | -------- |
| **Type**     | `number` |
| **Required** | No       |

#### <a name="geometry_oneOf_i1_oneOf_i4"></a>4.2.5. Property `root > geometry > oneOf > item 1 > oneOf > polygonGeoJSON`

|                           |                        |
| ------------------------- | ---------------------- |
| **Type**                  | `object`               |
| **Required**              | No                     |
| **Additional properties** | Any type allowed       |
| **Defined in**            | #/$defs/polygonGeoJSON |

| Property                                                  | Pattern | Type             | Deprecated | Definition | Title/Description |
| --------------------------------------------------------- | ------- | ---------------- | ---------- | ---------- | ----------------- |
| + [type](#geometry_oneOf_i1_oneOf_i4_type )               | No      | enum (of string) | No         | -          | -                 |
| + [coordinates](#geometry_oneOf_i1_oneOf_i4_coordinates ) | No      | array of array   | No         | -          | -                 |

##### <a name="geometry_oneOf_i1_oneOf_i4_type"></a>4.2.5.1. Property `root > geometry > oneOf > item 1 > oneOf > item 4 > type`

|              |                    |
| ------------ | ------------------ |
| **Type**     | `enum (of string)` |
| **Required** | Yes                |

Must be one of:
* "Polygon"

##### <a name="geometry_oneOf_i1_oneOf_i4_coordinates"></a>4.2.5.2. Property `root > geometry > oneOf > item 1 > oneOf > item 4 > coordinates`

|              |                  |
| ------------ | ---------------- |
| **Type**     | `array of array` |
| **Required** | Yes              |

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | N/A                |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be                                    | Description |
| ------------------------------------------------------------------ | ----------- |
| [coordinates items](#geometry_oneOf_i1_oneOf_i4_coordinates_items) | -           |

###### <a name="geometry_oneOf_i1_oneOf_i4_coordinates_items"></a>4.2.5.2.1. root > geometry > oneOf > item 1 > oneOf > item 4 > coordinates > coordinates items

|              |                  |
| ------------ | ---------------- |
| **Type**     | `array of array` |
| **Required** | No               |

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | 4                  |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be                                                | Description |
| ------------------------------------------------------------------------------ | ----------- |
| [coordinates items items](#geometry_oneOf_i1_oneOf_i4_coordinates_items_items) | -           |

###### <a name="geometry_oneOf_i1_oneOf_i4_coordinates_items_items"></a>4.2.5.2.1.1. root > geometry > oneOf > item 1 > oneOf > item 4 > coordinates > coordinates items > coordinates items items

|              |                   |
| ------------ | ----------------- |
| **Type**     | `array of number` |
| **Required** | No                |

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | 2                  |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be                                                            | Description |
| ------------------------------------------------------------------------------------------ | ----------- |
| [coordinates items items items](#geometry_oneOf_i1_oneOf_i4_coordinates_items_items_items) | -           |

###### <a name="geometry_oneOf_i1_oneOf_i4_coordinates_items_items_items"></a>4.2.5.2.1.1.1. root > geometry > oneOf > item 1 > oneOf > item 4 > coordinates > coordinates items > coordinates items items > coordinates items items items

|              |          |
| ------------ | -------- |
| **Type**     | `number` |
| **Required** | No       |

#### <a name="geometry_oneOf_i1_oneOf_i5"></a>4.2.6. Property `root > geometry > oneOf > item 1 > oneOf > multipolygonGeoJSON`

|                           |                             |
| ------------------------- | --------------------------- |
| **Type**                  | `object`                    |
| **Required**              | No                          |
| **Additional properties** | Any type allowed            |
| **Defined in**            | #/$defs/multipolygonGeoJSON |

| Property                                                  | Pattern | Type             | Deprecated | Definition | Title/Description |
| --------------------------------------------------------- | ------- | ---------------- | ---------- | ---------- | ----------------- |
| + [type](#geometry_oneOf_i1_oneOf_i5_type )               | No      | enum (of string) | No         | -          | -                 |
| + [coordinates](#geometry_oneOf_i1_oneOf_i5_coordinates ) | No      | array of array   | No         | -          | -                 |

##### <a name="geometry_oneOf_i1_oneOf_i5_type"></a>4.2.6.1. Property `root > geometry > oneOf > item 1 > oneOf > item 5 > type`

|              |                    |
| ------------ | ------------------ |
| **Type**     | `enum (of string)` |
| **Required** | Yes                |

Must be one of:
* "MultiPoint"

##### <a name="geometry_oneOf_i1_oneOf_i5_coordinates"></a>4.2.6.2. Property `root > geometry > oneOf > item 1 > oneOf > item 5 > coordinates`

|              |                  |
| ------------ | ---------------- |
| **Type**     | `array of array` |
| **Required** | Yes              |

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | N/A                |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be                                    | Description |
| ------------------------------------------------------------------ | ----------- |
| [coordinates items](#geometry_oneOf_i1_oneOf_i5_coordinates_items) | -           |

###### <a name="geometry_oneOf_i1_oneOf_i5_coordinates_items"></a>4.2.6.2.1. root > geometry > oneOf > item 1 > oneOf > item 5 > coordinates > coordinates items

|              |                   |
| ------------ | ----------------- |
| **Type**     | `array of number` |
| **Required** | No                |

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | 2                  |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be                                                | Description |
| ------------------------------------------------------------------------------ | ----------- |
| [coordinates items items](#geometry_oneOf_i1_oneOf_i5_coordinates_items_items) | -           |

###### <a name="geometry_oneOf_i1_oneOf_i5_coordinates_items_items"></a>4.2.6.2.1.1. root > geometry > oneOf > item 1 > oneOf > item 5 > coordinates > coordinates items > coordinates items items

|              |          |
| ------------ | -------- |
| **Type**     | `number` |
| **Required** | No       |

#### <a name="geometry_oneOf_i1_oneOf_i6"></a>4.2.7. Property `root > geometry > oneOf > item 1 > oneOf > geometrycollectionGeoJSON`

|                           |                                   |
| ------------------------- | --------------------------------- |
| **Type**                  | `object`                          |
| **Required**              | No                                |
| **Additional properties** | Any type allowed                  |
| **Defined in**            | #/$defs/geometrycollectionGeoJSON |

| Property                                                | Pattern | Type             | Deprecated | Definition | Title/Description |
| ------------------------------------------------------- | ------- | ---------------- | ---------- | ---------- | ----------------- |
| + [type](#geometry_oneOf_i1_oneOf_i6_type )             | No      | enum (of string) | No         | -          | -                 |
| + [geometries](#geometry_oneOf_i1_oneOf_i6_geometries ) | No      | array            | No         | -          | -                 |

##### <a name="geometry_oneOf_i1_oneOf_i6_type"></a>4.2.7.1. Property `root > geometry > oneOf > item 1 > oneOf > item 6 > type`

|              |                    |
| ------------ | ------------------ |
| **Type**     | `enum (of string)` |
| **Required** | Yes                |

Must be one of:
* "GeometryCollection"

##### <a name="geometry_oneOf_i1_oneOf_i6_geometries"></a>4.2.7.2. Property `root > geometry > oneOf > item 1 > oneOf > item 6 > geometries`

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

| Each item of this array must be                                 | Description |
| --------------------------------------------------------------- | ----------- |
| [geometryGeoJSON](#geometry_oneOf_i1_oneOf_i6_geometries_items) | -           |

###### <a name="geometry_oneOf_i1_oneOf_i6_geometries_items"></a>4.2.7.2.1. root > geometry > oneOf > item 1 > oneOf > item 6 > geometries > geometryGeoJSON

|                           |                                         |
| ------------------------- | --------------------------------------- |
| **Type**                  | `combining`                             |
| **Required**              | No                                      |
| **Additional properties** | Any type allowed                        |
| **Same definition as**    | [geometry_oneOf_i1](#geometry_oneOf_i1) |

## <a name="conformsTo"></a>5. Property `root > conformsTo`

|              |                   |
| ------------ | ----------------- |
| **Type**     | `array of string` |
| **Required** | No                |

**Description:** The extensions/conformance classes used in this record.

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | N/A                |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be       | Description |
| ------------------------------------- | ----------- |
| [conformsTo items](#conformsTo_items) | -           |

### <a name="conformsTo_items"></a>5.1. root > conformsTo > conformsTo items

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

## <a name="properties"></a>6. Property `root > properties`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | Yes              |
| **Additional properties** | Any type allowed |

| All of(Requirement)                            |
| ---------------------------------------------- |
| [recordCommonProperties](#properties_allOf_i0) |
| [item 1](#properties_allOf_i1)                 |

### <a name="properties_allOf_i0"></a>6.1. Property `root > properties > allOf > recordCommonProperties`

|                           |                                |
| ------------------------- | ------------------------------ |
| **Type**                  | `object`                       |
| **Required**              | No                             |
| **Additional properties** | Any type allowed               |
| **Defined in**            | #/$defs/recordCommonProperties |

| Property                                                       | Pattern | Type            | Deprecated | Definition          | Title/Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| -------------------------------------------------------------- | ------- | --------------- | ---------- | ------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| - [created](#properties_allOf_i0_created )                     | No      | string          | No         | -                   | The date this record was created in the server.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| - [updated](#properties_allOf_i0_updated )                     | No      | string          | No         | -                   | The most recent date on which the record was changed.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| - [type](#properties_allOf_i0_type )                           | No      | string          | No         | -                   | The nature or genre of the resource. The value should be a code, convenient for filtering records. Where available, a link to the canonical URI of the record type resource will be added to the 'links' property.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| - [title](#properties_allOf_i0_title )                         | No      | string          | No         | -                   | A human-readable name given to the resource.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| - [description](#properties_allOf_i0_description )             | No      | string          | No         | -                   | A free-text account of the resource.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| - [keywords](#properties_allOf_i0_keywords )                   | No      | array of string | No         | -                   | The topic or topics of the resource. Typically represented using free-form keywords, tags, key phrases, or classification codes.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| - [themes](#properties_allOf_i0_themes )                       | No      | array           | No         | -                   | A knowledge organization system used to classify the resource.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| - [language](#properties_allOf_i0_language )                   | No      | object          | No         | In #/$defs/language | The language used for textual values in this record representation.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| - [languages](#properties_allOf_i0_languages )                 | No      | array           | No         | -                   | This list of languages in which this record is available.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| - [resourceLanguages](#properties_allOf_i0_resourceLanguages ) | No      | array           | No         | -                   | The list of languages in which the resource described by this record is available.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| - [externalIds](#properties_allOf_i0_externalIds )             | No      | array of object | No         | -                   | An identifier for the resource assigned by an external (to the catalog) entity.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| - [formats](#properties_allOf_i0_formats )                     | No      | array           | No         | -                   | A list of available distributions of the resource.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| - [contacts](#properties_allOf_i0_contacts )                   | No      | array           | No         | -                   | A list of contacts qualified by their role(s) in association to the record or the resource described by the record.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| - [license](#properties_allOf_i0_license )                     | No      | string          | No         | In #/$defs/license  | A legal document under which the resource is made available. If the resource is being made available under a common license then use an SPDX license id (https://spdx.org/licenses/). If the resource is being made available under multiple common licenses then use an SPDX license expression v2.3 string (https://spdx.github.io/spdx-spec/v2.3/SPDX-license-expressions/) If the resource is being made available under one or more licenses that haven't been assigned an SPDX identifier or one or more custom licenses then use a string value of 'other' and include one or more links (rel="license") in the \`link\` section of the record to the file(s) that contains the text of the license(s). There is also the case of a resource that is private or unpublished and is thus unlicensed; in this case do not register such a resource in the catalog in the first place since there is no point in making such a resource discoverable. |
| - [rights](#properties_allOf_i0_rights )                       | No      | string          | No         | -                   | A statement that concerns all rights not addressed by the license such as a copyright statement.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |

#### <a name="properties_allOf_i0_created"></a>6.1.1. Property `root > properties > allOf > item 0 > created`

|              |             |
| ------------ | ----------- |
| **Type**     | `string`    |
| **Required** | No          |
| **Format**   | `date-time` |

**Description:** The date this record was created in the server.

#### <a name="properties_allOf_i0_updated"></a>6.1.2. Property `root > properties > allOf > item 0 > updated`

|              |             |
| ------------ | ----------- |
| **Type**     | `string`    |
| **Required** | No          |
| **Format**   | `date-time` |

**Description:** The most recent date on which the record was changed.

#### <a name="properties_allOf_i0_type"></a>6.1.3. Property `root > properties > allOf > item 0 > type`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** The nature or genre of the resource. The value should be a code, convenient for filtering records. Where available, a link to the canonical URI of the record type resource will be added to the 'links' property.

#### <a name="properties_allOf_i0_title"></a>6.1.4. Property `root > properties > allOf > item 0 > title`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** A human-readable name given to the resource.

#### <a name="properties_allOf_i0_description"></a>6.1.5. Property `root > properties > allOf > item 0 > description`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** A free-text account of the resource.

#### <a name="properties_allOf_i0_keywords"></a>6.1.6. Property `root > properties > allOf > item 0 > keywords`

|              |                   |
| ------------ | ----------------- |
| **Type**     | `array of string` |
| **Required** | No                |

**Description:** The topic or topics of the resource. Typically represented using free-form keywords, tags, key phrases, or classification codes.

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | N/A                |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be                       | Description |
| ----------------------------------------------------- | ----------- |
| [keywords items](#properties_allOf_i0_keywords_items) | -           |

##### <a name="properties_allOf_i0_keywords_items"></a>6.1.6.1. root > properties > allOf > item 0 > keywords > keywords items

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

#### <a name="properties_allOf_i0_themes"></a>6.1.7. Property `root > properties > allOf > item 0 > themes`

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |

**Description:** A knowledge organization system used to classify the resource.

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | 1                  |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be            | Description |
| ------------------------------------------ | ----------- |
| [theme](#properties_allOf_i0_themes_items) | -           |

##### <a name="properties_allOf_i0_themes_items"></a>6.1.7.1. root > properties > allOf > item 0 > themes > theme

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |
| **Defined in**            | #/$defs/theme    |

| Property                                                  | Pattern | Type            | Deprecated | Definition | Title/Description                                                                                                                                                                                                                                                                                                                                                                                                           |
| --------------------------------------------------------- | ------- | --------------- | ---------- | ---------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| + [concepts](#properties_allOf_i0_themes_items_concepts ) | No      | array of object | No         | -          | One or more entity/concept identifiers from this knowledge system. it is recommended that a resolvable URI be used for each entity/concept identifier.                                                                                                                                                                                                                                                                      |
| + [scheme](#properties_allOf_i0_themes_items_scheme )     | No      | string          | No         | -          | An identifier for the knowledge organization system used to classify the resource.  It is recommended that the identifier be a resolvable URI.  The list of schemes used in a searchable catalog can be determined by inspecting the server's OpenAPI document or, if the server implements CQL2, by exposing a queryable (e.g. named \`scheme\`) and enumerating the list of schemes in the queryable's schema definition. |

###### <a name="properties_allOf_i0_themes_items_concepts"></a>6.1.7.1.1. Property `root > properties > allOf > item 0 > themes > themes items > concepts`

|              |                   |
| ------------ | ----------------- |
| **Type**     | `array of object` |
| **Required** | Yes               |

**Description:** One or more entity/concept identifiers from this knowledge system. it is recommended that a resolvable URI be used for each entity/concept identifier.

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | 1                  |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be                                    | Description |
| ------------------------------------------------------------------ | ----------- |
| [concepts items](#properties_allOf_i0_themes_items_concepts_items) | -           |

###### <a name="properties_allOf_i0_themes_items_concepts_items"></a>6.1.7.1.1.1. root > properties > allOf > item 0 > themes > themes items > concepts > concepts items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| Property                                                                       | Pattern | Type   | Deprecated | Definition | Title/Description                                   |
| ------------------------------------------------------------------------------ | ------- | ------ | ---------- | ---------- | --------------------------------------------------- |
| + [id](#properties_allOf_i0_themes_items_concepts_items_id )                   | No      | string | No         | -          | An identifier for the concept.                      |
| - [title](#properties_allOf_i0_themes_items_concepts_items_title )             | No      | string | No         | -          | A human readable title for the concept.             |
| - [description](#properties_allOf_i0_themes_items_concepts_items_description ) | No      | string | No         | -          | A human readable description for the concept.       |
| - [url](#properties_allOf_i0_themes_items_concepts_items_url )                 | No      | string | No         | -          | A URI providing further description of the concept. |

###### <a name="properties_allOf_i0_themes_items_concepts_items_id"></a>6.1.7.1.1.1.1. Property `root > properties > allOf > item 0 > themes > themes items > concepts > concepts items > id`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** An identifier for the concept.

###### <a name="properties_allOf_i0_themes_items_concepts_items_title"></a>6.1.7.1.1.1.2. Property `root > properties > allOf > item 0 > themes > themes items > concepts > concepts items > title`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** A human readable title for the concept.

###### <a name="properties_allOf_i0_themes_items_concepts_items_description"></a>6.1.7.1.1.1.3. Property `root > properties > allOf > item 0 > themes > themes items > concepts > concepts items > description`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** A human readable description for the concept.

###### <a name="properties_allOf_i0_themes_items_concepts_items_url"></a>6.1.7.1.1.1.4. Property `root > properties > allOf > item 0 > themes > themes items > concepts > concepts items > url`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `uri`    |

**Description:** A URI providing further description of the concept.

###### <a name="properties_allOf_i0_themes_items_scheme"></a>6.1.7.1.2. Property `root > properties > allOf > item 0 > themes > themes items > scheme`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** An identifier for the knowledge organization system used to classify the resource.  It is recommended that the identifier be a resolvable URI.  The list of schemes used in a searchable catalog can be determined by inspecting the server's OpenAPI document or, if the server implements CQL2, by exposing a queryable (e.g. named `scheme`) and enumerating the list of schemes in the queryable's schema definition.

#### <a name="properties_allOf_i0_language"></a>6.1.8. Property `root > properties > allOf > item 0 > language`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |
| **Defined in**            | #/$defs/language |

**Description:** The language used for textual values in this record representation.

| Property                                                | Pattern | Type             | Deprecated | Definition | Title/Description                                                                                                                                                                                                                                                                                                                                |
| ------------------------------------------------------- | ------- | ---------------- | ---------- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| + [code](#properties_allOf_i0_language_code )           | No      | string           | No         | -          | The language tag as per RFC-5646.                                                                                                                                                                                                                                                                                                                |
| - [name](#properties_allOf_i0_language_name )           | No      | string           | No         | -          | The untranslated name of the language.                                                                                                                                                                                                                                                                                                           |
| - [alternate](#properties_allOf_i0_language_alternate ) | No      | string           | No         | -          | The name of the language in another well-understood language, usually English.                                                                                                                                                                                                                                                                   |
| - [dir](#properties_allOf_i0_language_dir )             | No      | enum (of string) | No         | -          | The direction for text in this language. The default, \`ltr\` (left-to-right), represents the most common situation. However, care should be taken to set the value of \`dir\` appropriately if the language direction is not \`ltr\`. Other values supported are \`rtl\` (right-to-left), \`ttb\` (top-to-bottom), and \`btt\` (bottom-to-top). |

##### <a name="properties_allOf_i0_language_code"></a>6.1.8.1. Property `root > properties > allOf > item 0 > language > code`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** The language tag as per RFC-5646.

##### <a name="properties_allOf_i0_language_name"></a>6.1.8.2. Property `root > properties > allOf > item 0 > language > name`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** The untranslated name of the language.

| Restrictions   |   |
| -------------- | - |
| **Min length** | 1 |

##### <a name="properties_allOf_i0_language_alternate"></a>6.1.8.3. Property `root > properties > allOf > item 0 > language > alternate`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** The name of the language in another well-understood language, usually English.

##### <a name="properties_allOf_i0_language_dir"></a>6.1.8.4. Property `root > properties > allOf > item 0 > language > dir`

|              |                    |
| ------------ | ------------------ |
| **Type**     | `enum (of string)` |
| **Required** | No                 |
| **Default**  | `"ltr"`            |

**Description:** The direction for text in this language. The default, `ltr` (left-to-right), represents the most common situation. However, care should be taken to set the value of `dir` appropriately if the language direction is not `ltr`. Other values supported are `rtl` (right-to-left), `ttb` (top-to-bottom), and `btt` (bottom-to-top).

Must be one of:
* "ltr"
* "rtl"
* "ttb"
* "btt"

#### <a name="properties_allOf_i0_languages"></a>6.1.9. Property `root > properties > allOf > item 0 > languages`

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |

**Description:** This list of languages in which this record is available.

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | N/A                |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be                  | Description                                          |
| ------------------------------------------------ | ---------------------------------------------------- |
| [language](#properties_allOf_i0_languages_items) | The language used for textual values in this record. |

##### <a name="properties_allOf_i0_languages_items"></a>6.1.9.1. root > properties > allOf > item 0 > languages > language

|                           |                                           |
| ------------------------- | ----------------------------------------- |
| **Type**                  | `object`                                  |
| **Required**              | No                                        |
| **Additional properties** | Any type allowed                          |
| **Same definition as**    | [language](#properties_allOf_i0_language) |

**Description:** The language used for textual values in this record.

#### <a name="properties_allOf_i0_resourceLanguages"></a>6.1.10. Property `root > properties > allOf > item 0 > resourceLanguages`

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |

**Description:** The list of languages in which the resource described by this record is available.

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | N/A                |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be                          | Description                                          |
| -------------------------------------------------------- | ---------------------------------------------------- |
| [language](#properties_allOf_i0_resourceLanguages_items) | The language used for textual values in this record. |

##### <a name="properties_allOf_i0_resourceLanguages_items"></a>6.1.10.1. root > properties > allOf > item 0 > resourceLanguages > language

|                           |                                           |
| ------------------------- | ----------------------------------------- |
| **Type**                  | `object`                                  |
| **Required**              | No                                        |
| **Additional properties** | Any type allowed                          |
| **Same definition as**    | [language](#properties_allOf_i0_language) |

**Description:** The language used for textual values in this record.

#### <a name="properties_allOf_i0_externalIds"></a>6.1.11. Property `root > properties > allOf > item 0 > externalIds`

|              |                   |
| ------------ | ----------------- |
| **Type**     | `array of object` |
| **Required** | No                |

**Description:** An identifier for the resource assigned by an external (to the catalog) entity.

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | N/A                |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be                             | Description |
| ----------------------------------------------------------- | ----------- |
| [externalIds items](#properties_allOf_i0_externalIds_items) | -           |

##### <a name="properties_allOf_i0_externalIds_items"></a>6.1.11.1. root > properties > allOf > item 0 > externalIds > externalIds items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| Property                                                   | Pattern | Type   | Deprecated | Definition | Title/Description                                                                                                                                                                         |
| ---------------------------------------------------------- | ------- | ------ | ---------- | ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| - [scheme](#properties_allOf_i0_externalIds_items_scheme ) | No      | string | No         | -          | A reference to an authority or identifier for a knowledge organization system from which the external identifier was obtained. It is recommended that the identifier be a resolvable URI. |
| + [value](#properties_allOf_i0_externalIds_items_value )   | No      | string | No         | -          | The value of the identifier.                                                                                                                                                              |

###### <a name="properties_allOf_i0_externalIds_items_scheme"></a>6.1.11.1.1. Property `root > properties > allOf > item 0 > externalIds > externalIds items > scheme`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** A reference to an authority or identifier for a knowledge organization system from which the external identifier was obtained. It is recommended that the identifier be a resolvable URI.

###### <a name="properties_allOf_i0_externalIds_items_value"></a>6.1.11.1.2. Property `root > properties > allOf > item 0 > externalIds > externalIds items > value`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** The value of the identifier.

#### <a name="properties_allOf_i0_formats"></a>6.1.12. Property `root > properties > allOf > item 0 > formats`

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |

**Description:** A list of available distributions of the resource.

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | N/A                |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be              | Description |
| -------------------------------------------- | ----------- |
| [format](#properties_allOf_i0_formats_items) | -           |

##### <a name="properties_allOf_i0_formats_items"></a>6.1.12.1. root > properties > allOf > item 0 > formats > format

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |
| **Defined in**            | #/$defs/format   |

| Property                                                     | Pattern | Type   | Deprecated | Definition | Title/Description |
| ------------------------------------------------------------ | ------- | ------ | ---------- | ---------- | ----------------- |
| - [name](#properties_allOf_i0_formats_items_name )           | No      | string | No         | -          | -                 |
| - [mediaType](#properties_allOf_i0_formats_items_mediaType ) | No      | string | No         | -          | -                 |

| Any of(Option)                                        |
| ----------------------------------------------------- |
| [item 0](#properties_allOf_i0_formats_items_anyOf_i0) |
| [item 1](#properties_allOf_i0_formats_items_anyOf_i1) |

###### <a name="properties_allOf_i0_formats_items_anyOf_i0"></a>6.1.12.1.1. Property `root > properties > allOf > item 0 > formats > formats items > anyOf > item 0`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

###### <a name="autogenerated_heading_2"></a>6.1.12.1.1.1. The following properties are required
* name

###### <a name="properties_allOf_i0_formats_items_anyOf_i1"></a>6.1.12.1.2. Property `root > properties > allOf > item 0 > formats > formats items > anyOf > item 1`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

###### <a name="autogenerated_heading_3"></a>6.1.12.1.2.1. The following properties are required
* mediaType

###### <a name="properties_allOf_i0_formats_items_name"></a>6.1.12.1.3. Property `root > properties > allOf > item 0 > formats > formats items > name`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

###### <a name="properties_allOf_i0_formats_items_mediaType"></a>6.1.12.1.4. Property `root > properties > allOf > item 0 > formats > formats items > mediaType`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

#### <a name="properties_allOf_i0_contacts"></a>6.1.13. Property `root > properties > allOf > item 0 > contacts`

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |

**Description:** A list of contacts qualified by their role(s) in association to the record or the resource described by the record.

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | N/A                |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be                | Description                                                                |
| ---------------------------------------------- | -------------------------------------------------------------------------- |
| [contact](#properties_allOf_i0_contacts_items) | Identification of, and means of communication with, person responsible ... |

##### <a name="properties_allOf_i0_contacts_items"></a>6.1.13.1. root > properties > allOf > item 0 > contacts > contact

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |
| **Defined in**            | #/$defs/contact  |

**Description:** Identification of, and means of communication with, person responsible
for the resource.

| Property                                                                          | Pattern | Type            | Deprecated | Definition                                                               | Title/Description                                                                                                                                                                                                                                                   |
| --------------------------------------------------------------------------------- | ------- | --------------- | ---------- | ------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| - [identifier](#properties_allOf_i0_contacts_items_identifier )                   | No      | string          | No         | -                                                                        | A value uniquely identifying a contact.                                                                                                                                                                                                                             |
| - [name](#properties_allOf_i0_contacts_items_name )                               | No      | string          | No         | -                                                                        | The name of the responsible person.                                                                                                                                                                                                                                 |
| - [position](#properties_allOf_i0_contacts_items_position )                       | No      | string          | No         | -                                                                        | The name of the role or position of the responsible person taken from the organization's formal organizational hierarchy or chart.                                                                                                                                  |
| - [organization](#properties_allOf_i0_contacts_items_organization )               | No      | string          | No         | -                                                                        | Organization/affiliation of the contact.                                                                                                                                                                                                                            |
| - [logo](#properties_allOf_i0_contacts_items_logo )                               | No      | Combination     | No         | -                                                                        | Graphic identifying a contact. The link relation should be \`icon\` and the media type should be an image media type.                                                                                                                                               |
| - [phones](#properties_allOf_i0_contacts_items_phones )                           | No      | array of object | No         | -                                                                        | Telephone numbers at which contact can be made.  The type of<br />phone number is indicated using the roles property.                                                                                                                                               |
| - [emails](#properties_allOf_i0_contacts_items_emails )                           | No      | array of object | No         | -                                                                        | Email addresses at which contact can be made.  The type of <br />email address is indicated using the roles property.                                                                                                                                               |
| - [addresses](#properties_allOf_i0_contacts_items_addresses )                     | No      | array of object | No         | -                                                                        | Physical location at which contact can be made.  The type of<br />address is indicated using the roles property.                                                                                                                                                    |
| - [links](#properties_allOf_i0_contacts_items_links )                             | No      | array           | No         | -                                                                        | On-line information about the contact.                                                                                                                                                                                                                              |
| - [hoursOfService](#properties_allOf_i0_contacts_items_hoursOfService )           | No      | string          | No         | -                                                                        | Time period when the contact can be contacted.                                                                                                                                                                                                                      |
| - [contactInstructions](#properties_allOf_i0_contacts_items_contactInstructions ) | No      | string          | No         | -                                                                        | Supplemental instructions on how or when to contact the<br />responsible party. The roles property is used to associate<br />a set of named duties, job functions and/or permissions<br />associated with this contact. (e.g. developer,<br />administrator, etc.). |
| - [roles](#properties_allOf_i0_contacts_items_roles )                             | No      | array of string | No         | Same as [roles](#properties_allOf_i0_contacts_items_phones_items_roles ) | The list of duties, job functions or permissions assigned by the system and associated with the context of this member.                                                                                                                                             |

| Any of(Option)                                         |
| ------------------------------------------------------ |
| [item 0](#properties_allOf_i0_contacts_items_anyOf_i0) |
| [item 1](#properties_allOf_i0_contacts_items_anyOf_i1) |

###### <a name="properties_allOf_i0_contacts_items_anyOf_i0"></a>6.1.13.1.1. Property `root > properties > allOf > item 0 > contacts > contacts items > anyOf > item 0`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

###### <a name="autogenerated_heading_4"></a>6.1.13.1.1.1. The following properties are required
* name

###### <a name="properties_allOf_i0_contacts_items_anyOf_i1"></a>6.1.13.1.2. Property `root > properties > allOf > item 0 > contacts > contacts items > anyOf > item 1`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

###### <a name="autogenerated_heading_5"></a>6.1.13.1.2.1. The following properties are required
* organization

###### <a name="properties_allOf_i0_contacts_items_identifier"></a>6.1.13.1.3. Property `root > properties > allOf > item 0 > contacts > contacts items > identifier`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** A value uniquely identifying a contact.

###### <a name="properties_allOf_i0_contacts_items_name"></a>6.1.13.1.4. Property `root > properties > allOf > item 0 > contacts > contacts items > name`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** The name of the responsible person.

###### <a name="properties_allOf_i0_contacts_items_position"></a>6.1.13.1.5. Property `root > properties > allOf > item 0 > contacts > contacts items > position`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** The name of the role or position of the responsible person taken from the organization's formal organizational hierarchy or chart.

###### <a name="properties_allOf_i0_contacts_items_organization"></a>6.1.13.1.6. Property `root > properties > allOf > item 0 > contacts > contacts items > organization`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** Organization/affiliation of the contact.

###### <a name="properties_allOf_i0_contacts_items_logo"></a>6.1.13.1.7. Property `root > properties > allOf > item 0 > contacts > contacts items > logo`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** Graphic identifying a contact. The link relation should be `icon` and the media type should be an image media type.

| All of(Requirement)                                         |
| ----------------------------------------------------------- |
| [link](#properties_allOf_i0_contacts_items_logo_allOf_i0)   |
| [item 1](#properties_allOf_i0_contacts_items_logo_allOf_i1) |

###### <a name="properties_allOf_i0_contacts_items_logo_allOf_i0"></a>6.1.13.1.7.1. Property `root > properties > allOf > item 0 > contacts > contacts items > logo > allOf > link`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |
| **Defined in**            | #/$defs/link     |

| All of(Requirement)                                                    |
| ---------------------------------------------------------------------- |
| [linkBase](#properties_allOf_i0_contacts_items_logo_allOf_i0_allOf_i0) |
| [item 1](#properties_allOf_i0_contacts_items_logo_allOf_i0_allOf_i1)   |

###### <a name="properties_allOf_i0_contacts_items_logo_allOf_i0_allOf_i0"></a>6.1.13.1.7.1.1. Property `root > properties > allOf > item 0 > contacts > contacts items > logo > allOf > item 0 > allOf > linkBase`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |
| **Defined in**            | #/$defs/linkBase |

| Property                                                                           | Pattern | Type    | Deprecated | Definition | Title/Description                                                                                |
| ---------------------------------------------------------------------------------- | ------- | ------- | ---------- | ---------- | ------------------------------------------------------------------------------------------------ |
| - [rel](#properties_allOf_i0_contacts_items_logo_allOf_i0_allOf_i0_rel )           | No      | string  | No         | -          | The type or semantics of the relation.                                                           |
| - [type](#properties_allOf_i0_contacts_items_logo_allOf_i0_allOf_i0_type )         | No      | string  | No         | -          | A hint indicating what the media type of the result of dereferencing the link should be.         |
| - [hreflang](#properties_allOf_i0_contacts_items_logo_allOf_i0_allOf_i0_hreflang ) | No      | string  | No         | -          | A hint indicating what the language of the result of dereferencing the link should be.           |
| - [title](#properties_allOf_i0_contacts_items_logo_allOf_i0_allOf_i0_title )       | No      | string  | No         | -          | Used to label the destination of a link such that it can be used as a human-readable identifier. |
| - [length](#properties_allOf_i0_contacts_items_logo_allOf_i0_allOf_i0_length )     | No      | integer | No         | -          | -                                                                                                |
| - [created](#properties_allOf_i0_contacts_items_logo_allOf_i0_allOf_i0_created )   | No      | string  | No         | -          | Date of creation of the resource pointed to by the link.                                         |
| - [updated](#properties_allOf_i0_contacts_items_logo_allOf_i0_allOf_i0_updated )   | No      | string  | No         | -          | Most recent date on which the resource pointed to by the link was changed.                       |

###### <a name="properties_allOf_i0_contacts_items_logo_allOf_i0_allOf_i0_rel"></a>6.1.13.1.7.1.1.1. Property `root > properties > allOf > item 0 > contacts > contacts items > logo > allOf > item 0 > allOf > item 0 > rel`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** The type or semantics of the relation.

###### <a name="properties_allOf_i0_contacts_items_logo_allOf_i0_allOf_i0_type"></a>6.1.13.1.7.1.1.2. Property `root > properties > allOf > item 0 > contacts > contacts items > logo > allOf > item 0 > allOf > item 0 > type`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** A hint indicating what the media type of the result of dereferencing the link should be.

###### <a name="properties_allOf_i0_contacts_items_logo_allOf_i0_allOf_i0_hreflang"></a>6.1.13.1.7.1.1.3. Property `root > properties > allOf > item 0 > contacts > contacts items > logo > allOf > item 0 > allOf > item 0 > hreflang`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** A hint indicating what the language of the result of dereferencing the link should be.

###### <a name="properties_allOf_i0_contacts_items_logo_allOf_i0_allOf_i0_title"></a>6.1.13.1.7.1.1.4. Property `root > properties > allOf > item 0 > contacts > contacts items > logo > allOf > item 0 > allOf > item 0 > title`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** Used to label the destination of a link such that it can be used as a human-readable identifier.

###### <a name="properties_allOf_i0_contacts_items_logo_allOf_i0_allOf_i0_length"></a>6.1.13.1.7.1.1.5. Property `root > properties > allOf > item 0 > contacts > contacts items > logo > allOf > item 0 > allOf > item 0 > length`

|              |           |
| ------------ | --------- |
| **Type**     | `integer` |
| **Required** | No        |

###### <a name="properties_allOf_i0_contacts_items_logo_allOf_i0_allOf_i0_created"></a>6.1.13.1.7.1.1.6. Property `root > properties > allOf > item 0 > contacts > contacts items > logo > allOf > item 0 > allOf > item 0 > created`

|              |             |
| ------------ | ----------- |
| **Type**     | `string`    |
| **Required** | No          |
| **Format**   | `date-time` |

**Description:** Date of creation of the resource pointed to by the link.

###### <a name="properties_allOf_i0_contacts_items_logo_allOf_i0_allOf_i0_updated"></a>6.1.13.1.7.1.1.7. Property `root > properties > allOf > item 0 > contacts > contacts items > logo > allOf > item 0 > allOf > item 0 > updated`

|              |             |
| ------------ | ----------- |
| **Type**     | `string`    |
| **Required** | No          |
| **Format**   | `date-time` |

**Description:** Most recent date on which the resource pointed to by the link was changed.

###### <a name="properties_allOf_i0_contacts_items_logo_allOf_i0_allOf_i1"></a>6.1.13.1.7.1.2. Property `root > properties > allOf > item 0 > contacts > contacts items > logo > allOf > item 0 > allOf > item 1`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| Property                                                                   | Pattern | Type   | Deprecated | Definition | Title/Description |
| -------------------------------------------------------------------------- | ------- | ------ | ---------- | ---------- | ----------------- |
| + [href](#properties_allOf_i0_contacts_items_logo_allOf_i0_allOf_i1_href ) | No      | string | No         | -          | -                 |

###### <a name="properties_allOf_i0_contacts_items_logo_allOf_i0_allOf_i1_href"></a>6.1.13.1.7.1.2.1. Property `root > properties > allOf > item 0 > contacts > contacts items > logo > allOf > item 0 > allOf > item 1 > href`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |
| **Format**   | `uri`    |

###### <a name="properties_allOf_i0_contacts_items_logo_allOf_i1"></a>6.1.13.1.7.2. Property `root > properties > allOf > item 0 > contacts > contacts items > logo > allOf > item 1`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| Property                                                        | Pattern | Type             | Deprecated | Definition | Title/Description |
| --------------------------------------------------------------- | ------- | ---------------- | ---------- | ---------- | ----------------- |
| + [rel](#properties_allOf_i0_contacts_items_logo_allOf_i1_rel ) | No      | enum (of string) | No         | -          | -                 |

###### <a name="autogenerated_heading_6"></a>6.1.13.1.7.2.1. The following properties are required
* type

###### <a name="properties_allOf_i0_contacts_items_logo_allOf_i1_rel"></a>6.1.13.1.7.2.2. Property `root > properties > allOf > item 0 > contacts > contacts items > logo > allOf > item 1 > rel`

|              |                    |
| ------------ | ------------------ |
| **Type**     | `enum (of string)` |
| **Required** | Yes                |

Must be one of:
* "icon"

###### <a name="properties_allOf_i0_contacts_items_phones"></a>6.1.13.1.8. Property `root > properties > allOf > item 0 > contacts > contacts items > phones`

|              |                   |
| ------------ | ----------------- |
| **Type**     | `array of object` |
| **Required** | No                |

**Description:** Telephone numbers at which contact can be made.  The type of
phone number is indicated using the roles property.

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | N/A                |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be                                  | Description |
| ---------------------------------------------------------------- | ----------- |
| [phones items](#properties_allOf_i0_contacts_items_phones_items) | -           |

###### <a name="properties_allOf_i0_contacts_items_phones_items"></a>6.1.13.1.8.1. root > properties > allOf > item 0 > contacts > contacts items > phones > phones items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| Property                                                           | Pattern | Type            | Deprecated | Definition       | Title/Description                                                                                                       |
| ------------------------------------------------------------------ | ------- | --------------- | ---------- | ---------------- | ----------------------------------------------------------------------------------------------------------------------- |
| + [value](#properties_allOf_i0_contacts_items_phones_items_value ) | No      | string          | No         | -                | The value is the phone number itself.                                                                                   |
| - [roles](#properties_allOf_i0_contacts_items_phones_items_roles ) | No      | array of string | No         | In #/$defs/roles | The list of duties, job functions or permissions assigned by the system and associated with the context of this member. |

###### <a name="properties_allOf_i0_contacts_items_phones_items_value"></a>6.1.13.1.8.1.1. Property `root > properties > allOf > item 0 > contacts > contacts items > phones > phones items > value`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** The value is the phone number itself.

| Restrictions                      |                                                                                                                     |
| --------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| **Must match regular expression** | ```^\+[1-9]{1}[0-9]{3,14}$``` [Test](https://regex101.com/?regex=%5E%5C%2B%5B1-9%5D%7B1%7D%5B0-9%5D%7B3%2C14%7D%24) |

###### <a name="properties_allOf_i0_contacts_items_phones_items_roles"></a>6.1.13.1.8.1.2. Property `root > properties > allOf > item 0 > contacts > contacts items > phones > phones items > roles`

|                |                   |
| -------------- | ----------------- |
| **Type**       | `array of string` |
| **Required**   | No                |
| **Defined in** | #/$defs/roles     |

**Description:** The list of duties, job functions or permissions assigned by the system and associated with the context of this member.

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | 1                  |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be                                             | Description |
| --------------------------------------------------------------------------- | ----------- |
| [roles items](#properties_allOf_i0_contacts_items_phones_items_roles_items) | -           |

###### <a name="properties_allOf_i0_contacts_items_phones_items_roles_items"></a>6.1.13.1.8.1.2.1. root > properties > allOf > item 0 > contacts > contacts items > phones > phones items > roles > roles items

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

###### <a name="properties_allOf_i0_contacts_items_emails"></a>6.1.13.1.9. Property `root > properties > allOf > item 0 > contacts > contacts items > emails`

|              |                   |
| ------------ | ----------------- |
| **Type**     | `array of object` |
| **Required** | No                |

**Description:** Email addresses at which contact can be made.  The type of 
email address is indicated using the roles property.

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | N/A                |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be                                  | Description |
| ---------------------------------------------------------------- | ----------- |
| [emails items](#properties_allOf_i0_contacts_items_emails_items) | -           |

###### <a name="properties_allOf_i0_contacts_items_emails_items"></a>6.1.13.1.9.1. root > properties > allOf > item 0 > contacts > contacts items > emails > emails items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| Property                                                           | Pattern | Type            | Deprecated | Definition                                                               | Title/Description                                                                                                       |
| ------------------------------------------------------------------ | ------- | --------------- | ---------- | ------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------- |
| + [value](#properties_allOf_i0_contacts_items_emails_items_value ) | No      | string          | No         | -                                                                        | The value is the email number itself.                                                                                   |
| - [roles](#properties_allOf_i0_contacts_items_emails_items_roles ) | No      | array of string | No         | Same as [roles](#properties_allOf_i0_contacts_items_phones_items_roles ) | The list of duties, job functions or permissions assigned by the system and associated with the context of this member. |

###### <a name="properties_allOf_i0_contacts_items_emails_items_value"></a>6.1.13.1.9.1.1. Property `root > properties > allOf > item 0 > contacts > contacts items > emails > emails items > value`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |
| **Format**   | `email`  |

**Description:** The value is the email number itself.

###### <a name="properties_allOf_i0_contacts_items_emails_items_roles"></a>6.1.13.1.9.1.2. Property `root > properties > allOf > item 0 > contacts > contacts items > emails > emails items > roles`

|                        |                                                                 |
| ---------------------- | --------------------------------------------------------------- |
| **Type**               | `array of string`                                               |
| **Required**           | No                                                              |
| **Same definition as** | [roles](#properties_allOf_i0_contacts_items_phones_items_roles) |

**Description:** The list of duties, job functions or permissions assigned by the system and associated with the context of this member.

###### <a name="properties_allOf_i0_contacts_items_addresses"></a>6.1.13.1.10. Property `root > properties > allOf > item 0 > contacts > contacts items > addresses`

|              |                   |
| ------------ | ----------------- |
| **Type**     | `array of object` |
| **Required** | No                |

**Description:** Physical location at which contact can be made.  The type of
address is indicated using the roles property.

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | N/A                |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be                                        | Description |
| ---------------------------------------------------------------------- | ----------- |
| [addresses items](#properties_allOf_i0_contacts_items_addresses_items) | -           |

###### <a name="properties_allOf_i0_contacts_items_addresses_items"></a>6.1.13.1.10.1. root > properties > allOf > item 0 > contacts > contacts items > addresses > addresses items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| Property                                                                                        | Pattern | Type            | Deprecated | Definition                                                               | Title/Description                                                                                                       |
| ----------------------------------------------------------------------------------------------- | ------- | --------------- | ---------- | ------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------- |
| - [deliveryPoint](#properties_allOf_i0_contacts_items_addresses_items_deliveryPoint )           | No      | array of string | No         | -                                                                        | Address lines for the location.                                                                                         |
| - [city](#properties_allOf_i0_contacts_items_addresses_items_city )                             | No      | string          | No         | -                                                                        | City for the location.                                                                                                  |
| - [administrativeArea](#properties_allOf_i0_contacts_items_addresses_items_administrativeArea ) | No      | string          | No         | -                                                                        | State or province of the location.                                                                                      |
| - [postalCode](#properties_allOf_i0_contacts_items_addresses_items_postalCode )                 | No      | string          | No         | -                                                                        | ZIP or other postal code.                                                                                               |
| - [country](#properties_allOf_i0_contacts_items_addresses_items_country )                       | No      | string          | No         | -                                                                        | Country of the physical address.  ISO 3166-1 is recommended.                                                            |
| - [roles](#properties_allOf_i0_contacts_items_addresses_items_roles )                           | No      | array of string | No         | Same as [roles](#properties_allOf_i0_contacts_items_phones_items_roles ) | The list of duties, job functions or permissions assigned by the system and associated with the context of this member. |

###### <a name="properties_allOf_i0_contacts_items_addresses_items_deliveryPoint"></a>6.1.13.1.10.1.1. Property `root > properties > allOf > item 0 > contacts > contacts items > addresses > addresses items > deliveryPoint`

|              |                   |
| ------------ | ----------------- |
| **Type**     | `array of string` |
| **Required** | No                |

**Description:** Address lines for the location.

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | N/A                |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be                                                                | Description |
| ---------------------------------------------------------------------------------------------- | ----------- |
| [deliveryPoint items](#properties_allOf_i0_contacts_items_addresses_items_deliveryPoint_items) | -           |

###### <a name="properties_allOf_i0_contacts_items_addresses_items_deliveryPoint_items"></a>6.1.13.1.10.1.1.1. root > properties > allOf > item 0 > contacts > contacts items > addresses > addresses items > deliveryPoint > deliveryPoint items

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

###### <a name="properties_allOf_i0_contacts_items_addresses_items_city"></a>6.1.13.1.10.1.2. Property `root > properties > allOf > item 0 > contacts > contacts items > addresses > addresses items > city`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** City for the location.

###### <a name="properties_allOf_i0_contacts_items_addresses_items_administrativeArea"></a>6.1.13.1.10.1.3. Property `root > properties > allOf > item 0 > contacts > contacts items > addresses > addresses items > administrativeArea`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** State or province of the location.

###### <a name="properties_allOf_i0_contacts_items_addresses_items_postalCode"></a>6.1.13.1.10.1.4. Property `root > properties > allOf > item 0 > contacts > contacts items > addresses > addresses items > postalCode`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** ZIP or other postal code.

###### <a name="properties_allOf_i0_contacts_items_addresses_items_country"></a>6.1.13.1.10.1.5. Property `root > properties > allOf > item 0 > contacts > contacts items > addresses > addresses items > country`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** Country of the physical address.  ISO 3166-1 is recommended.

###### <a name="properties_allOf_i0_contacts_items_addresses_items_roles"></a>6.1.13.1.10.1.6. Property `root > properties > allOf > item 0 > contacts > contacts items > addresses > addresses items > roles`

|                        |                                                                 |
| ---------------------- | --------------------------------------------------------------- |
| **Type**               | `array of string`                                               |
| **Required**           | No                                                              |
| **Same definition as** | [roles](#properties_allOf_i0_contacts_items_phones_items_roles) |

**Description:** The list of duties, job functions or permissions assigned by the system and associated with the context of this member.

###### <a name="properties_allOf_i0_contacts_items_links"></a>6.1.13.1.11. Property `root > properties > allOf > item 0 > contacts > contacts items > links`

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |

**Description:** On-line information about the contact.

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | N/A                |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be                                | Description |
| -------------------------------------------------------------- | ----------- |
| [links items](#properties_allOf_i0_contacts_items_links_items) | -           |

###### <a name="properties_allOf_i0_contacts_items_links_items"></a>6.1.13.1.11.1. root > properties > allOf > item 0 > contacts > contacts items > links > links items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| All of(Requirement)                                                |
| ------------------------------------------------------------------ |
| [link](#properties_allOf_i0_contacts_items_links_items_allOf_i0)   |
| [item 1](#properties_allOf_i0_contacts_items_links_items_allOf_i1) |

###### <a name="properties_allOf_i0_contacts_items_links_items_allOf_i0"></a>6.1.13.1.11.1.1. Property `root > properties > allOf > item 0 > contacts > contacts items > links > links items > allOf > link`

|                           |                                                                                                       |
| ------------------------- | ----------------------------------------------------------------------------------------------------- |
| **Type**                  | `combining`                                                                                           |
| **Required**              | No                                                                                                    |
| **Additional properties** | Any type allowed                                                                                      |
| **Same definition as**    | [properties_allOf_i0_contacts_items_logo_allOf_i0](#properties_allOf_i0_contacts_items_logo_allOf_i0) |

###### <a name="properties_allOf_i0_contacts_items_links_items_allOf_i1"></a>6.1.13.1.11.1.2. Property `root > properties > allOf > item 0 > contacts > contacts items > links > links items > allOf > item 1`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

###### <a name="autogenerated_heading_7"></a>6.1.13.1.11.1.2.1. The following properties are required
* type

###### <a name="properties_allOf_i0_contacts_items_hoursOfService"></a>6.1.13.1.12. Property `root > properties > allOf > item 0 > contacts > contacts items > hoursOfService`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** Time period when the contact can be contacted.

###### <a name="properties_allOf_i0_contacts_items_contactInstructions"></a>6.1.13.1.13. Property `root > properties > allOf > item 0 > contacts > contacts items > contactInstructions`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** Supplemental instructions on how or when to contact the
responsible party. The roles property is used to associate
a set of named duties, job functions and/or permissions
associated with this contact. (e.g. developer,
administrator, etc.).

###### <a name="properties_allOf_i0_contacts_items_roles"></a>6.1.13.1.14. Property `root > properties > allOf > item 0 > contacts > contacts items > roles`

|                        |                                                                 |
| ---------------------- | --------------------------------------------------------------- |
| **Type**               | `array of string`                                               |
| **Required**           | No                                                              |
| **Same definition as** | [roles](#properties_allOf_i0_contacts_items_phones_items_roles) |

**Description:** The list of duties, job functions or permissions assigned by the system and associated with the context of this member.

#### <a name="properties_allOf_i0_license"></a>6.1.14. Property `root > properties > allOf > item 0 > license`

|                |                 |
| -------------- | --------------- |
| **Type**       | `string`        |
| **Required**   | No              |
| **Defined in** | #/$defs/license |

**Description:** A legal document under which the resource is made available. If the resource is being made available under a common license then use an SPDX license id (https://spdx.org/licenses/). If the resource is being made available under multiple common licenses then use an SPDX license expression v2.3 string (https://spdx.github.io/spdx-spec/v2.3/SPDX-license-expressions/) If the resource is being made available under one or more licenses that haven't been assigned an SPDX identifier or one or more custom licenses then use a string value of 'other' and include one or more links (rel="license") in the `link` section of the record to the file(s) that contains the text of the license(s). There is also the case of a resource that is private or unpublished and is thus unlicensed; in this case do not register such a resource in the catalog in the first place since there is no point in making such a resource discoverable.

#### <a name="properties_allOf_i0_rights"></a>6.1.15. Property `root > properties > allOf > item 0 > rights`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** A statement that concerns all rights not addressed by the license such as a copyright statement.

### <a name="properties_allOf_i1"></a>6.2. Property `root > properties > allOf > item 1`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

## <a name="links"></a>7. Property `root > links`

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

| Each item of this array must be | Description |
| ------------------------------- | ----------- |
| [link](#links_items)            | -           |

### <a name="links_items"></a>7.1. root > links > link

|                           |                                                                                                       |
| ------------------------- | ----------------------------------------------------------------------------------------------------- |
| **Type**                  | `combining`                                                                                           |
| **Required**              | No                                                                                                    |
| **Additional properties** | Any type allowed                                                                                      |
| **Same definition as**    | [properties_allOf_i0_contacts_items_logo_allOf_i0](#properties_allOf_i0_contacts_items_logo_allOf_i0) |

## <a name="linkTemplates"></a>8. Property `root > linkTemplates`

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

| Each item of this array must be      | Description |
| ------------------------------------ | ----------- |
| [linkTemplate](#linkTemplates_items) | -           |

### <a name="linkTemplates_items"></a>8.1. root > linkTemplates > linkTemplate

|                           |                      |
| ------------------------- | -------------------- |
| **Type**                  | `combining`          |
| **Required**              | No                   |
| **Additional properties** | Any type allowed     |
| **Defined in**            | #/$defs/linkTemplate |

| All of(Requirement)                       |
| ----------------------------------------- |
| [linkBase](#linkTemplates_items_allOf_i0) |
| [item 1](#linkTemplates_items_allOf_i1)   |

#### <a name="linkTemplates_items_allOf_i0"></a>8.1.1. Property `root > linkTemplates > linkTemplates items > allOf > linkBase`

|                           |                                                                                                                         |
| ------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                |
| **Required**              | No                                                                                                                      |
| **Additional properties** | Any type allowed                                                                                                        |
| **Same definition as**    | [properties_allOf_i0_contacts_items_logo_allOf_i0_allOf_i0](#properties_allOf_i0_contacts_items_logo_allOf_i0_allOf_i0) |

#### <a name="linkTemplates_items_allOf_i1"></a>8.1.2. Property `root > linkTemplates > linkTemplates items > allOf > item 1`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| Property                                                    | Pattern | Type   | Deprecated | Definition | Title/Description                                                                                                                                                                                                                                                                      |
| ----------------------------------------------------------- | ------- | ------ | ---------- | ---------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| + [uriTemplate](#linkTemplates_items_allOf_i1_uriTemplate ) | No      | string | No         | -          | Supplies a resolvable URI to a remote resource (or resource fragment).                                                                                                                                                                                                                 |
| - [varBase](#linkTemplates_items_allOf_i1_varBase )         | No      | string | No         | -          | The base URI to which the variable name can be appended to retrieve the definition of the variable as a JSON Schema fragment.                                                                                                                                                          |
| - [variables](#linkTemplates_items_allOf_i1_variables )     | No      | object | No         | -          | This object contains one key per substitution variable in the templated URL.  Each key defines the schema of one substitution variable using a JSON Schema fragment and can thus include things like the data type of the variable, enumerations, minimum values, maximum values, etc. |

##### <a name="linkTemplates_items_allOf_i1_uriTemplate"></a>8.1.2.1. Property `root > linkTemplates > linkTemplates items > allOf > item 1 > uriTemplate`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** Supplies a resolvable URI to a remote resource (or resource fragment).

##### <a name="linkTemplates_items_allOf_i1_varBase"></a>8.1.2.2. Property `root > linkTemplates > linkTemplates items > allOf > item 1 > varBase`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `uri`    |

**Description:** The base URI to which the variable name can be appended to retrieve the definition of the variable as a JSON Schema fragment.

##### <a name="linkTemplates_items_allOf_i1_variables"></a>8.1.2.3. Property `root > linkTemplates > linkTemplates items > allOf > item 1 > variables`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** This object contains one key per substitution variable in the templated URL.  Each key defines the schema of one substitution variable using a JSON Schema fragment and can thus include things like the data type of the variable, enumerations, minimum values, maximum values, etc.

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans) on 2025-11-07 at 00:41:11 +0100
