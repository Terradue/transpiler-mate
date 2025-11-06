# Schema Docs

- [1. Property `root > @type`](#@type)
- [2. Property `root > name`](#name)
- [3. Property `root > description`](#description)
- [4. Property `root > dateCreated`](#dateCreated)
  - [4.1. Property `root > dateCreated > oneOf > item 0`](#dateCreated_oneOf_i0)
  - [4.2. Property `root > dateCreated > oneOf > item 1`](#dateCreated_oneOf_i1)
- [5. Property `root > license`](#license)
  - [5.1. Property `root > license > oneOf > CreativeWork`](#license_oneOf_i0)
    - [5.1.1. Property `root > license > oneOf > item 0 > @type`](#license_oneOf_i0_@type)
    - [5.1.2. Property `root > license > oneOf > item 0 > name`](#license_oneOf_i0_name)
    - [5.1.3. Property `root > license > oneOf > item 0 > url`](#license_oneOf_i0_url)
    - [5.1.4. Property `root > license > oneOf > item 0 > identifier`](#license_oneOf_i0_identifier)
      - [5.1.4.1. Property `root > license > oneOf > item 0 > identifier > oneOf > item 0`](#license_oneOf_i0_identifier_oneOf_i0)
      - [5.1.4.2. Property `root > license > oneOf > item 0 > identifier > oneOf > item 1`](#license_oneOf_i0_identifier_oneOf_i1)
  - [5.2. Property `root > license > oneOf > item 1`](#license_oneOf_i1)
  - [5.3. Property `root > license > oneOf > item 2`](#license_oneOf_i2)
    - [5.3.1. root > license > oneOf > item 2 > item 2 items](#license_oneOf_i2_items)
      - [5.3.1.1. Property `root > license > oneOf > item 2 > item 2 items > oneOf > CreativeWork`](#license_oneOf_i2_items_oneOf_i0)
      - [5.3.1.2. Property `root > license > oneOf > item 2 > item 2 items > oneOf > item 1`](#license_oneOf_i2_items_oneOf_i1)
- [6. Property `root > identifier`](#identifier)
- [7. Property `root > sameAs`](#sameAs)
  - [7.1. Property `root > sameAs > oneOf > item 0`](#sameAs_oneOf_i0)
  - [7.2. Property `root > sameAs > oneOf > item 1`](#sameAs_oneOf_i1)
    - [7.2.1. root > sameAs > oneOf > item 1 > item 1 items](#sameAs_oneOf_i1_items)
- [8. Property `root > keywords`](#keywords)
  - [8.1. Property `root > keywords > oneOf > item 0`](#keywords_oneOf_i0)
  - [8.2. Property `root > keywords > oneOf > item 1`](#keywords_oneOf_i1)
  - [8.3. Property `root > keywords > oneOf > DefinedTerm`](#keywords_oneOf_i2)
    - [8.3.1. Property `root > keywords > oneOf > item 2 > @type`](#keywords_oneOf_i2_@type)
    - [8.3.2. Property `root > keywords > oneOf > item 2 > name`](#keywords_oneOf_i2_name)
    - [8.3.3. Property `root > keywords > oneOf > item 2 > description`](#keywords_oneOf_i2_description)
    - [8.3.4. Property `root > keywords > oneOf > item 2 > termCode`](#keywords_oneOf_i2_termCode)
    - [8.3.5. Property `root > keywords > oneOf > item 2 > inDefinedTermSet`](#keywords_oneOf_i2_inDefinedTermSet)
  - [8.4. Property `root > keywords > oneOf > item 3`](#keywords_oneOf_i3)
    - [8.4.1. root > keywords > oneOf > item 3 > item 3 items](#keywords_oneOf_i3_items)
      - [8.4.1.1. Property `root > keywords > oneOf > item 3 > item 3 items > oneOf > item 0`](#keywords_oneOf_i3_items_oneOf_i0)
      - [8.4.1.2. Property `root > keywords > oneOf > item 3 > item 3 items > oneOf > item 1`](#keywords_oneOf_i3_items_oneOf_i1)
      - [8.4.1.3. Property `root > keywords > oneOf > item 3 > item 3 items > oneOf > DefinedTerm`](#keywords_oneOf_i3_items_oneOf_i2)
- [9. Property `root > operatingSystem`](#operatingSystem)
  - [9.1. Property `root > operatingSystem > oneOf > item 0`](#operatingSystem_oneOf_i0)
  - [9.2. Property `root > operatingSystem > oneOf > item 1`](#operatingSystem_oneOf_i1)
    - [9.2.1. root > operatingSystem > oneOf > item 1 > item 1 items](#operatingSystem_oneOf_i1_items)
- [10. Property `root > softwareRequirements`](#softwareRequirements)
  - [10.1. Property `root > softwareRequirements > oneOf > item 0`](#softwareRequirements_oneOf_i0)
  - [10.2. Property `root > softwareRequirements > oneOf > item 1`](#softwareRequirements_oneOf_i1)
  - [10.3. Property `root > softwareRequirements > oneOf > item 2`](#softwareRequirements_oneOf_i2)
    - [10.3.1. root > softwareRequirements > oneOf > item 2 > item 2 items](#softwareRequirements_oneOf_i2_items)
      - [10.3.1.1. Property `root > softwareRequirements > oneOf > item 2 > item 2 items > oneOf > item 0`](#softwareRequirements_oneOf_i2_items_oneOf_i0)
      - [10.3.1.2. Property `root > softwareRequirements > oneOf > item 2 > item 2 items > oneOf > item 1`](#softwareRequirements_oneOf_i2_items_oneOf_i1)
- [11. Property `root > softwareVersion`](#softwareVersion)
- [12. Property `root > softwareHelp`](#softwareHelp)
  - [12.1. Property `root > softwareHelp > oneOf > CreativeWork`](#softwareHelp_oneOf_i0)
  - [12.2. Property `root > softwareHelp > oneOf > item 1`](#softwareHelp_oneOf_i1)
    - [12.2.1. root > softwareHelp > oneOf > item 1 > CreativeWork](#softwareHelp_oneOf_i1_items)
- [13. Property `root > publisher`](#publisher)
  - [13.1. Property `root > publisher > @type`](#publisher_@type)
  - [13.2. Property `root > publisher > name`](#publisher_name)
  - [13.3. Property `root > publisher > email`](#publisher_email)
    - [13.3.1. Property `root > publisher > email > oneOf > item 0`](#publisher_email_oneOf_i0)
    - [13.3.2. Property `root > publisher > email > oneOf > item 1`](#publisher_email_oneOf_i1)
      - [13.3.2.1. root > publisher > email > oneOf > item 1 > item 1 items](#publisher_email_oneOf_i1_items)
  - [13.4. Property `root > publisher > identifier`](#publisher_identifier)
- [14. Property `root > author`](#author)
  - [14.1. Property `root > author > oneOf > AuthorRole`](#author_oneOf_i0)
    - [14.1.1. Property `root > author > oneOf > item 0 > allOf > Role`](#author_oneOf_i0_allOf_i0)
      - [14.1.1.1. Property `root > author > oneOf > item 0 > allOf > item 0 > @type`](#author_oneOf_i0_allOf_i0_@type)
      - [14.1.1.2. Property `root > author > oneOf > item 0 > allOf > item 0 > roleName`](#author_oneOf_i0_allOf_i0_roleName)
      - [14.1.1.3. Property `root > author > oneOf > item 0 > allOf > item 0 > startDate`](#author_oneOf_i0_allOf_i0_startDate)
      - [14.1.1.4. Property `root > author > oneOf > item 0 > allOf > item 0 > endDate`](#author_oneOf_i0_allOf_i0_endDate)
      - [14.1.1.5. Property `root > author > oneOf > item 0 > allOf > item 0 > additionalType`](#author_oneOf_i0_allOf_i0_additionalType)
    - [14.1.2. Property `root > author > oneOf > item 0 > allOf > item 1`](#author_oneOf_i0_allOf_i1)
      - [14.1.2.1. Property `root > author > oneOf > item 0 > allOf > item 1 > author`](#author_oneOf_i0_allOf_i1_author)
        - [14.1.2.1.1. Property `root > author > oneOf > item 0 > allOf > item 1 > author > @type`](#author_oneOf_i0_allOf_i1_author_@type)
        - [14.1.2.1.2. Property `root > author > oneOf > item 0 > allOf > item 1 > author > givenName`](#author_oneOf_i0_allOf_i1_author_givenName)
        - [14.1.2.1.3. Property `root > author > oneOf > item 0 > allOf > item 1 > author > familyName`](#author_oneOf_i0_allOf_i1_author_familyName)
        - [14.1.2.1.4. Property `root > author > oneOf > item 0 > allOf > item 1 > author > email`](#author_oneOf_i0_allOf_i1_author_email)
        - [14.1.2.1.5. Property `root > author > oneOf > item 0 > allOf > item 1 > author > identifier`](#author_oneOf_i0_allOf_i1_author_identifier)
        - [14.1.2.1.6. Property `root > author > oneOf > item 0 > allOf > item 1 > author > affiliation`](#author_oneOf_i0_allOf_i1_author_affiliation)
          - [14.1.2.1.6.1. Property `root > author > oneOf > item 0 > allOf > item 1 > author > affiliation > oneOf > Organization`](#author_oneOf_i0_allOf_i1_author_affiliation_oneOf_i0)
          - [14.1.2.1.6.2. Property `root > author > oneOf > item 0 > allOf > item 1 > author > affiliation > oneOf > item 1`](#author_oneOf_i0_allOf_i1_author_affiliation_oneOf_i1)
            - [14.1.2.1.6.2.1. root > author > oneOf > item 0 > allOf > item 1 > author > affiliation > oneOf > item 1 > Organization](#author_oneOf_i0_allOf_i1_author_affiliation_oneOf_i1_items)
  - [14.2. Property `root > author > oneOf > Person`](#author_oneOf_i1)
  - [14.3. Property `root > author > oneOf > item 2`](#author_oneOf_i2)
    - [14.3.1. root > author > oneOf > item 2 > item 2 items](#author_oneOf_i2_items)
      - [14.3.1.1. Property `root > author > oneOf > item 2 > item 2 items > oneOf > AuthorRole`](#author_oneOf_i2_items_oneOf_i0)
      - [14.3.1.2. Property `root > author > oneOf > item 2 > item 2 items > oneOf > Person`](#author_oneOf_i2_items_oneOf_i1)
- [15. Property `root > contributor`](#contributor)
  - [15.1. Property `root > contributor > oneOf > ContributorRole`](#contributor_oneOf_i0)
    - [15.1.1. Property `root > contributor > oneOf > item 0 > allOf > Role`](#contributor_oneOf_i0_allOf_i0)
    - [15.1.2. Property `root > contributor > oneOf > item 0 > allOf > item 1`](#contributor_oneOf_i0_allOf_i1)
      - [15.1.2.1. Property `root > contributor > oneOf > item 0 > allOf > item 1 > contributor`](#contributor_oneOf_i0_allOf_i1_contributor)
  - [15.2. Property `root > contributor > oneOf > Person`](#contributor_oneOf_i1)
  - [15.3. Property `root > contributor > oneOf > item 2`](#contributor_oneOf_i2)
    - [15.3.1. root > contributor > oneOf > item 2 > item 2 items](#contributor_oneOf_i2_items)
      - [15.3.1.1. Property `root > contributor > oneOf > item 2 > item 2 items > oneOf > ContributorRole`](#contributor_oneOf_i2_items_oneOf_i0)
      - [15.3.1.2. Property `root > contributor > oneOf > item 2 > item 2 items > oneOf > Person`](#contributor_oneOf_i2_items_oneOf_i1)

|                           |                             |
| ------------------------- | --------------------------- |
| **Type**                  | `object`                    |
| **Required**              | No                          |
| **Additional properties** | Any type allowed            |
| **Defined in**            | #/$defs/SoftwareApplication |

**Description:** A software application.

| Property                                         | Pattern | Type        | Deprecated | Definition                                          | Title/Description                                                                                                                                                                                                                                                                                                                              |
| ------------------------------------------------ | ------- | ----------- | ---------- | --------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| - [@type](#@type )                               | No      | const       | No         | -                                                   | -                                                                                                                                                                                                                                                                                                                                              |
| + [name](#name )                                 | No      | string      | No         | -                                                   | The name of the item.                                                                                                                                                                                                                                                                                                                          |
| + [description](#description )                   | No      | string      | No         | -                                                   | A description of the item.                                                                                                                                                                                                                                                                                                                     |
| + [dateCreated](#dateCreated )                   | No      | Combination | No         | -                                                   | The date on which the CreativeWork was created or the item was added to a DataFeed.                                                                                                                                                                                                                                                            |
| + [license](#license )                           | No      | Combination | No         | -                                                   | A license document that applies to this content, typically indicated by URL.                                                                                                                                                                                                                                                                   |
| - [identifier](#identifier )                     | No      | object      | No         | Same as [identifier](#license_oneOf_i0_identifier ) | The identifier property represents any kind of identifier for any kind of [[Thing]], such as ISBNs, GTIN codes, UUIDs etc. Schema.org provides dedicated properties for representing many of these, either as textual strings or as URL (URI) links. See [background notes](/docs/datamodel.html#identifierBg) for more details.<br />         |
| - [sameAs](#sameAs )                             | No      | object      | No         | In #/$defs/URI                                      | URL of a reference Web page that unambiguously indicates the item's identity. E.g. the URL of the item's Wikipedia page, Wikidata entry, or official website.                                                                                                                                                                                  |
| - [keywords](#keywords )                         | No      | Combination | No         | -                                                   | Keywords or tags used to describe some item. Multiple textual entries in a keywords list are typically delimited by commas, or by repeating the property.                                                                                                                                                                                      |
| - [operatingSystem](#operatingSystem )           | No      | Combination | No         | -                                                   | Operating systems supported (Windows 7, OS X 10.6, Android 1.6).                                                                                                                                                                                                                                                                               |
| - [softwareRequirements](#softwareRequirements ) | No      | Combination | No         | -                                                   | Component dependency requirements for application. This includes runtime environments and shared libraries that are not included in the application distribution package, but required to run the application (examples: DirectX, Java or .NET runtime).                                                                                       |
| + [softwareVersion](#softwareVersion )           | No      | string      | No         | -                                                   | Version of the software instance.                                                                                                                                                                                                                                                                                                              |
| + [softwareHelp](#softwareHelp )                 | No      | Combination | No         | -                                                   | Software application help.                                                                                                                                                                                                                                                                                                                     |
| + [publisher](#publisher )                       | No      | object      | No         | In #/$defs/Organization                             | The publisher of the article in question.                                                                                                                                                                                                                                                                                                      |
| + [author](#author )                             | No      | Combination | No         | -                                                   | The author of this content or rating. Please note that author is special in that HTML 5 provides a special mechanism for indicating authorship via the rel tag. That is equivalent to this and may be used interchangeably.                                                                                                                    |
| - [contributor](#contributor )                   | No      | Combination | No         | -                                                   | A secondary contributor to the CreativeWork or Event.                                                                                                                                                                                                                                                                                          |

## <a name="@type"></a>1. Property `root > @type`

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | No      |

Specific value: `"https://schema.org/SoftwareApplication"`

## <a name="name"></a>2. Property `root > name`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** The name of the item.

## <a name="description"></a>3. Property `root > description`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** A description of the item.

## <a name="dateCreated"></a>4. Property `root > dateCreated`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | Yes              |
| **Additional properties** | Any type allowed |

**Description:** The date on which the CreativeWork was created or the item was added to a DataFeed.

| One of(Option)                  |
| ------------------------------- |
| [item 0](#dateCreated_oneOf_i0) |
| [item 1](#dateCreated_oneOf_i1) |

### <a name="dateCreated_oneOf_i0"></a>4.1. Property `root > dateCreated > oneOf > item 0`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `date`   |

### <a name="dateCreated_oneOf_i1"></a>4.2. Property `root > dateCreated > oneOf > item 1`

|              |             |
| ------------ | ----------- |
| **Type**     | `string`    |
| **Required** | No          |
| **Format**   | `date-time` |

## <a name="license"></a>5. Property `root > license`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | Yes              |
| **Additional properties** | Any type allowed |

**Description:** A license document that applies to this content, typically indicated by URL.

| One of(Option)                    |
| --------------------------------- |
| [CreativeWork](#license_oneOf_i0) |
| [item 1](#license_oneOf_i1)       |
| [item 2](#license_oneOf_i2)       |

### <a name="license_oneOf_i0"></a>5.1. Property `root > license > oneOf > CreativeWork`

|                           |                      |
| ------------------------- | -------------------- |
| **Type**                  | `object`             |
| **Required**              | No                   |
| **Additional properties** | Any type allowed     |
| **Defined in**            | #/$defs/CreativeWork |

**Description:** The most generic kind of creative work, including books, movies, photographs, software programs, etc.

| Property                                      | Pattern | Type   | Deprecated | Definition            | Title/Description                                                                                                                                                                                                                                                                                                                              |
| --------------------------------------------- | ------- | ------ | ---------- | --------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| - [@type](#license_oneOf_i0_@type )           | No      | const  | No         | -                     | -                                                                                                                                                                                                                                                                                                                                              |
| - [name](#license_oneOf_i0_name )             | No      | string | No         | -                     | The name of the item.                                                                                                                                                                                                                                                                                                                          |
| - [url](#license_oneOf_i0_url )               | No      | string | No         | -                     | URL of the item.                                                                                                                                                                                                                                                                                                                               |
| - [identifier](#license_oneOf_i0_identifier ) | No      | object | No         | In #/$defs/Identifier | The identifier property represents any kind of identifier for any kind of [[Thing]], such as ISBNs, GTIN codes, UUIDs etc. Schema.org provides dedicated properties for representing many of these, either as textual strings or as URL (URI) links. See [background notes](/docs/datamodel.html#identifierBg) for more details.<br />         |

#### <a name="license_oneOf_i0_@type"></a>5.1.1. Property `root > license > oneOf > item 0 > @type`

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | No      |

Specific value: `"https://schema.org/CreativeWork"`

#### <a name="license_oneOf_i0_name"></a>5.1.2. Property `root > license > oneOf > item 0 > name`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** The name of the item.

#### <a name="license_oneOf_i0_url"></a>5.1.3. Property `root > license > oneOf > item 0 > url`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `uri`    |

**Description:** URL of the item.

#### <a name="license_oneOf_i0_identifier"></a>5.1.4. Property `root > license > oneOf > item 0 > identifier`

|                           |                    |
| ------------------------- | ------------------ |
| **Type**                  | `combining`        |
| **Required**              | No                 |
| **Additional properties** | Any type allowed   |
| **Defined in**            | #/$defs/Identifier |

**Description:** The identifier property represents any kind of identifier for any kind of [[Thing]], such as ISBNs, GTIN codes, UUIDs etc. Schema.org provides dedicated properties for representing many of these, either as textual strings or as URL (URI) links. See [background notes](/docs/datamodel.html#identifierBg) for more details.

| One of(Option)                                  |
| ----------------------------------------------- |
| [item 0](#license_oneOf_i0_identifier_oneOf_i0) |
| [item 1](#license_oneOf_i0_identifier_oneOf_i1) |

##### <a name="license_oneOf_i0_identifier_oneOf_i0"></a>5.1.4.1. Property `root > license > oneOf > item 0 > identifier > oneOf > item 0`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `uri`    |

##### <a name="license_oneOf_i0_identifier_oneOf_i1"></a>5.1.4.2. Property `root > license > oneOf > item 0 > identifier > oneOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

### <a name="license_oneOf_i1"></a>5.2. Property `root > license > oneOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `uri`    |

### <a name="license_oneOf_i2"></a>5.3. Property `root > license > oneOf > item 2`

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

| Each item of this array must be         | Description |
| --------------------------------------- | ----------- |
| [item 2 items](#license_oneOf_i2_items) | -           |

#### <a name="license_oneOf_i2_items"></a>5.3.1. root > license > oneOf > item 2 > item 2 items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| One of(Option)                                   |
| ------------------------------------------------ |
| [CreativeWork](#license_oneOf_i2_items_oneOf_i0) |
| [item 1](#license_oneOf_i2_items_oneOf_i1)       |

##### <a name="license_oneOf_i2_items_oneOf_i0"></a>5.3.1.1. Property `root > license > oneOf > item 2 > item 2 items > oneOf > CreativeWork`

|                           |                                       |
| ------------------------- | ------------------------------------- |
| **Type**                  | `object`                              |
| **Required**              | No                                    |
| **Additional properties** | Any type allowed                      |
| **Same definition as**    | [license_oneOf_i0](#license_oneOf_i0) |

**Description:** The most generic kind of creative work, including books, movies, photographs, software programs, etc.

##### <a name="license_oneOf_i2_items_oneOf_i1"></a>5.3.1.2. Property `root > license > oneOf > item 2 > item 2 items > oneOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `uri`    |

## <a name="identifier"></a>6. Property `root > identifier`

|                           |                                            |
| ------------------------- | ------------------------------------------ |
| **Type**                  | `combining`                                |
| **Required**              | No                                         |
| **Additional properties** | Any type allowed                           |
| **Same definition as**    | [identifier](#license_oneOf_i0_identifier) |

**Description:** The identifier property represents any kind of identifier for any kind of [[Thing]], such as ISBNs, GTIN codes, UUIDs etc. Schema.org provides dedicated properties for representing many of these, either as textual strings or as URL (URI) links. See [background notes](/docs/datamodel.html#identifierBg) for more details.

## <a name="sameAs"></a>7. Property `root > sameAs`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |
| **Defined in**            | #/$defs/URI      |

**Description:** URL of a reference Web page that unambiguously indicates the item's identity. E.g. the URL of the item's Wikipedia page, Wikidata entry, or official website.

| One of(Option)             |
| -------------------------- |
| [item 0](#sameAs_oneOf_i0) |
| [item 1](#sameAs_oneOf_i1) |

### <a name="sameAs_oneOf_i0"></a>7.1. Property `root > sameAs > oneOf > item 0`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `uri`    |

### <a name="sameAs_oneOf_i1"></a>7.2. Property `root > sameAs > oneOf > item 1`

|              |                   |
| ------------ | ----------------- |
| **Type**     | `array of string` |
| **Required** | No                |

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | N/A                |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be        | Description |
| -------------------------------------- | ----------- |
| [item 1 items](#sameAs_oneOf_i1_items) | -           |

#### <a name="sameAs_oneOf_i1_items"></a>7.2.1. root > sameAs > oneOf > item 1 > item 1 items

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `uri`    |

## <a name="keywords"></a>8. Property `root > keywords`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** Keywords or tags used to describe some item. Multiple textual entries in a keywords list are typically delimited by commas, or by repeating the property.

| One of(Option)                    |
| --------------------------------- |
| [item 0](#keywords_oneOf_i0)      |
| [item 1](#keywords_oneOf_i1)      |
| [DefinedTerm](#keywords_oneOf_i2) |
| [item 3](#keywords_oneOf_i3)      |

### <a name="keywords_oneOf_i0"></a>8.1. Property `root > keywords > oneOf > item 0`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

### <a name="keywords_oneOf_i1"></a>8.2. Property `root > keywords > oneOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `uri`    |

### <a name="keywords_oneOf_i2"></a>8.3. Property `root > keywords > oneOf > DefinedTerm`

|                           |                     |
| ------------------------- | ------------------- |
| **Type**                  | `object`            |
| **Required**              | No                  |
| **Additional properties** | Any type allowed    |
| **Defined in**            | #/$defs/DefinedTerm |

**Description:** A word, name, acronym, phrase, etc. with a formal definition. Often used in the context of category or subject classification, glossaries or dictionaries, product or creative work types, etc. Use the name property for the term being defined, use termCode if the term has an alpha-numeric code allocated, use description to provide the definition of the term.

| Property                                                   | Pattern | Type   | Deprecated | Definition | Title/Description                                                        |
| ---------------------------------------------------------- | ------- | ------ | ---------- | ---------- | ------------------------------------------------------------------------ |
| - [@type](#keywords_oneOf_i2_@type )                       | No      | const  | No         | -          | -                                                                        |
| - [name](#keywords_oneOf_i2_name )                         | No      | string | No         | -          | The name of the item.                                                    |
| - [description](#keywords_oneOf_i2_description )           | No      | string | No         | -          | A description of the item.                                               |
| - [termCode](#keywords_oneOf_i2_termCode )                 | No      | string | No         | -          | A code that identifies this [[DefinedTerm]] within a [[DefinedTermSet]]. |
| - [inDefinedTermSet](#keywords_oneOf_i2_inDefinedTermSet ) | No      | string | No         | -          | A [[DefinedTermSet]] that contains this term.                            |

#### <a name="keywords_oneOf_i2_@type"></a>8.3.1. Property `root > keywords > oneOf > item 2 > @type`

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | No      |

Specific value: `"https://schema.org/DefinedTerm"`

#### <a name="keywords_oneOf_i2_name"></a>8.3.2. Property `root > keywords > oneOf > item 2 > name`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** The name of the item.

#### <a name="keywords_oneOf_i2_description"></a>8.3.3. Property `root > keywords > oneOf > item 2 > description`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** A description of the item.

#### <a name="keywords_oneOf_i2_termCode"></a>8.3.4. Property `root > keywords > oneOf > item 2 > termCode`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** A code that identifies this [[DefinedTerm]] within a [[DefinedTermSet]].

#### <a name="keywords_oneOf_i2_inDefinedTermSet"></a>8.3.5. Property `root > keywords > oneOf > item 2 > inDefinedTermSet`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `uri`    |

**Description:** A [[DefinedTermSet]] that contains this term.

### <a name="keywords_oneOf_i3"></a>8.4. Property `root > keywords > oneOf > item 3`

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

| Each item of this array must be          | Description |
| ---------------------------------------- | ----------- |
| [item 3 items](#keywords_oneOf_i3_items) | -           |

#### <a name="keywords_oneOf_i3_items"></a>8.4.1. root > keywords > oneOf > item 3 > item 3 items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| One of(Option)                                   |
| ------------------------------------------------ |
| [item 0](#keywords_oneOf_i3_items_oneOf_i0)      |
| [item 1](#keywords_oneOf_i3_items_oneOf_i1)      |
| [DefinedTerm](#keywords_oneOf_i3_items_oneOf_i2) |

##### <a name="keywords_oneOf_i3_items_oneOf_i0"></a>8.4.1.1. Property `root > keywords > oneOf > item 3 > item 3 items > oneOf > item 0`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

##### <a name="keywords_oneOf_i3_items_oneOf_i1"></a>8.4.1.2. Property `root > keywords > oneOf > item 3 > item 3 items > oneOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `uri`    |

##### <a name="keywords_oneOf_i3_items_oneOf_i2"></a>8.4.1.3. Property `root > keywords > oneOf > item 3 > item 3 items > oneOf > DefinedTerm`

|                           |                                         |
| ------------------------- | --------------------------------------- |
| **Type**                  | `object`                                |
| **Required**              | No                                      |
| **Additional properties** | Any type allowed                        |
| **Same definition as**    | [keywords_oneOf_i2](#keywords_oneOf_i2) |

**Description:** A word, name, acronym, phrase, etc. with a formal definition. Often used in the context of category or subject classification, glossaries or dictionaries, product or creative work types, etc. Use the name property for the term being defined, use termCode if the term has an alpha-numeric code allocated, use description to provide the definition of the term.

## <a name="operatingSystem"></a>9. Property `root > operatingSystem`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** Operating systems supported (Windows 7, OS X 10.6, Android 1.6).

| One of(Option)                      |
| ----------------------------------- |
| [item 0](#operatingSystem_oneOf_i0) |
| [item 1](#operatingSystem_oneOf_i1) |

### <a name="operatingSystem_oneOf_i0"></a>9.1. Property `root > operatingSystem > oneOf > item 0`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

### <a name="operatingSystem_oneOf_i1"></a>9.2. Property `root > operatingSystem > oneOf > item 1`

|              |                   |
| ------------ | ----------------- |
| **Type**     | `array of string` |
| **Required** | No                |

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | N/A                |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be                 | Description |
| ----------------------------------------------- | ----------- |
| [item 1 items](#operatingSystem_oneOf_i1_items) | -           |

#### <a name="operatingSystem_oneOf_i1_items"></a>9.2.1. root > operatingSystem > oneOf > item 1 > item 1 items

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

## <a name="softwareRequirements"></a>10. Property `root > softwareRequirements`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** Component dependency requirements for application. This includes runtime environments and shared libraries that are not included in the application distribution package, but required to run the application (examples: DirectX, Java or .NET runtime).

| One of(Option)                           |
| ---------------------------------------- |
| [item 0](#softwareRequirements_oneOf_i0) |
| [item 1](#softwareRequirements_oneOf_i1) |
| [item 2](#softwareRequirements_oneOf_i2) |

### <a name="softwareRequirements_oneOf_i0"></a>10.1. Property `root > softwareRequirements > oneOf > item 0`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

### <a name="softwareRequirements_oneOf_i1"></a>10.2. Property `root > softwareRequirements > oneOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `uri`    |

### <a name="softwareRequirements_oneOf_i2"></a>10.3. Property `root > softwareRequirements > oneOf > item 2`

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

| Each item of this array must be                      | Description |
| ---------------------------------------------------- | ----------- |
| [item 2 items](#softwareRequirements_oneOf_i2_items) | -           |

#### <a name="softwareRequirements_oneOf_i2_items"></a>10.3.1. root > softwareRequirements > oneOf > item 2 > item 2 items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| One of(Option)                                          |
| ------------------------------------------------------- |
| [item 0](#softwareRequirements_oneOf_i2_items_oneOf_i0) |
| [item 1](#softwareRequirements_oneOf_i2_items_oneOf_i1) |

##### <a name="softwareRequirements_oneOf_i2_items_oneOf_i0"></a>10.3.1.1. Property `root > softwareRequirements > oneOf > item 2 > item 2 items > oneOf > item 0`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

##### <a name="softwareRequirements_oneOf_i2_items_oneOf_i1"></a>10.3.1.2. Property `root > softwareRequirements > oneOf > item 2 > item 2 items > oneOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `uri`    |

## <a name="softwareVersion"></a>11. Property `root > softwareVersion`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** Version of the software instance.

## <a name="softwareHelp"></a>12. Property `root > softwareHelp`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | Yes              |
| **Additional properties** | Any type allowed |

**Description:** Software application help.

| One of(Option)                         |
| -------------------------------------- |
| [CreativeWork](#softwareHelp_oneOf_i0) |
| [item 1](#softwareHelp_oneOf_i1)       |

### <a name="softwareHelp_oneOf_i0"></a>12.1. Property `root > softwareHelp > oneOf > CreativeWork`

|                           |                                       |
| ------------------------- | ------------------------------------- |
| **Type**                  | `object`                              |
| **Required**              | No                                    |
| **Additional properties** | Any type allowed                      |
| **Same definition as**    | [license_oneOf_i0](#license_oneOf_i0) |

**Description:** The most generic kind of creative work, including books, movies, photographs, software programs, etc.

### <a name="softwareHelp_oneOf_i1"></a>12.2. Property `root > softwareHelp > oneOf > item 1`

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

| Each item of this array must be              | Description                                                                                           |
| -------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| [CreativeWork](#softwareHelp_oneOf_i1_items) | The most generic kind of creative work, including books, movies, photographs, software programs, etc. |

#### <a name="softwareHelp_oneOf_i1_items"></a>12.2.1. root > softwareHelp > oneOf > item 1 > CreativeWork

|                           |                                       |
| ------------------------- | ------------------------------------- |
| **Type**                  | `object`                              |
| **Required**              | No                                    |
| **Additional properties** | Any type allowed                      |
| **Same definition as**    | [license_oneOf_i0](#license_oneOf_i0) |

**Description:** The most generic kind of creative work, including books, movies, photographs, software programs, etc.

## <a name="publisher"></a>13. Property `root > publisher`

|                           |                      |
| ------------------------- | -------------------- |
| **Type**                  | `object`             |
| **Required**              | Yes                  |
| **Additional properties** | Any type allowed     |
| **Defined in**            | #/$defs/Organization |

**Description:** The publisher of the article in question.

| Property                               | Pattern | Type   | Deprecated | Definition                                          | Title/Description                                                                                                                                                                                                                                                                                                                              |
| -------------------------------------- | ------- | ------ | ---------- | --------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| - [@type](#publisher_@type )           | No      | const  | No         | -                                                   | -                                                                                                                                                                                                                                                                                                                                              |
| + [name](#publisher_name )             | No      | string | No         | -                                                   | The name of the item.                                                                                                                                                                                                                                                                                                                          |
| - [email](#publisher_email )           | No      | object | No         | In #/$defs/Email                                    | Email address.                                                                                                                                                                                                                                                                                                                                 |
| - [identifier](#publisher_identifier ) | No      | object | No         | Same as [identifier](#license_oneOf_i0_identifier ) | The identifier property represents any kind of identifier for any kind of [[Thing]], such as ISBNs, GTIN codes, UUIDs etc. Schema.org provides dedicated properties for representing many of these, either as textual strings or as URL (URI) links. See [background notes](/docs/datamodel.html#identifierBg) for more details.<br />         |

### <a name="publisher_@type"></a>13.1. Property `root > publisher > @type`

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | No      |

Specific value: `"https://schema.org/Organization"`

### <a name="publisher_name"></a>13.2. Property `root > publisher > name`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** The name of the item.

### <a name="publisher_email"></a>13.3. Property `root > publisher > email`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |
| **Defined in**            | #/$defs/Email    |

**Description:** Email address.

| One of(Option)                      |
| ----------------------------------- |
| [item 0](#publisher_email_oneOf_i0) |
| [item 1](#publisher_email_oneOf_i1) |

#### <a name="publisher_email_oneOf_i0"></a>13.3.1. Property `root > publisher > email > oneOf > item 0`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `email`  |

#### <a name="publisher_email_oneOf_i1"></a>13.3.2. Property `root > publisher > email > oneOf > item 1`

|              |                   |
| ------------ | ----------------- |
| **Type**     | `array of string` |
| **Required** | No                |

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | N/A                |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be                 | Description |
| ----------------------------------------------- | ----------- |
| [item 1 items](#publisher_email_oneOf_i1_items) | -           |

##### <a name="publisher_email_oneOf_i1_items"></a>13.3.2.1. root > publisher > email > oneOf > item 1 > item 1 items

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `email`  |

### <a name="publisher_identifier"></a>13.4. Property `root > publisher > identifier`

|                           |                                            |
| ------------------------- | ------------------------------------------ |
| **Type**                  | `combining`                                |
| **Required**              | No                                         |
| **Additional properties** | Any type allowed                           |
| **Same definition as**    | [identifier](#license_oneOf_i0_identifier) |

**Description:** The identifier property represents any kind of identifier for any kind of [[Thing]], such as ISBNs, GTIN codes, UUIDs etc. Schema.org provides dedicated properties for representing many of these, either as textual strings or as URL (URI) links. See [background notes](/docs/datamodel.html#identifierBg) for more details.

## <a name="author"></a>14. Property `root > author`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | Yes              |
| **Additional properties** | Any type allowed |

**Description:** The author of this content or rating. Please note that author is special in that HTML 5 provides a special mechanism for indicating authorship via the rel tag. That is equivalent to this and may be used interchangeably.

| One of(Option)                 |
| ------------------------------ |
| [AuthorRole](#author_oneOf_i0) |
| [Person](#author_oneOf_i1)     |
| [item 2](#author_oneOf_i2)     |

### <a name="author_oneOf_i0"></a>14.1. Property `root > author > oneOf > AuthorRole`

|                           |                    |
| ------------------------- | ------------------ |
| **Type**                  | `combining`        |
| **Required**              | No                 |
| **Additional properties** | Any type allowed   |
| **Defined in**            | #/$defs/AuthorRole |

| All of(Requirement)                 |
| ----------------------------------- |
| [Role](#author_oneOf_i0_allOf_i0)   |
| [item 1](#author_oneOf_i0_allOf_i1) |

#### <a name="author_oneOf_i0_allOf_i0"></a>14.1.1. Property `root > author > oneOf > item 0 > allOf > Role`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |
| **Defined in**            | #/$defs/Role     |

**Description:** Represents additional information about a relationship or property.

| Property                                                      | Pattern | Type   | Deprecated | Definition | Title/Description                                                                                                              |
| ------------------------------------------------------------- | ------- | ------ | ---------- | ---------- | ------------------------------------------------------------------------------------------------------------------------------ |
| - [@type](#author_oneOf_i0_allOf_i0_@type )                   | No      | const  | No         | -          | -                                                                                                                              |
| + [roleName](#author_oneOf_i0_allOf_i0_roleName )             | No      | string | No         | -          | A role played, performed or filled by a person or organization.                                                                |
| - [startDate](#author_oneOf_i0_allOf_i0_startDate )           | No      | string | No         | -          | The start date and time of the item                                                                                            |
| - [endDate](#author_oneOf_i0_allOf_i0_endDate )               | No      | string | No         | -          | The end date and time of the item                                                                                              |
| - [additionalType](#author_oneOf_i0_allOf_i0_additionalType ) | No      | string | No         | -          | An additional type for the item, typically used for adding more specific types from external vocabularies in microdata syntax. |

##### <a name="author_oneOf_i0_allOf_i0_@type"></a>14.1.1.1. Property `root > author > oneOf > item 0 > allOf > item 0 > @type`

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | No      |

Specific value: `"https://schema.org/Role"`

##### <a name="author_oneOf_i0_allOf_i0_roleName"></a>14.1.1.2. Property `root > author > oneOf > item 0 > allOf > item 0 > roleName`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** A role played, performed or filled by a person or organization.

##### <a name="author_oneOf_i0_allOf_i0_startDate"></a>14.1.1.3. Property `root > author > oneOf > item 0 > allOf > item 0 > startDate`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `date`   |

**Description:** The start date and time of the item

##### <a name="author_oneOf_i0_allOf_i0_endDate"></a>14.1.1.4. Property `root > author > oneOf > item 0 > allOf > item 0 > endDate`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `date`   |

**Description:** The end date and time of the item

##### <a name="author_oneOf_i0_allOf_i0_additionalType"></a>14.1.1.5. Property `root > author > oneOf > item 0 > allOf > item 0 > additionalType`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `uri`    |

**Description:** An additional type for the item, typically used for adding more specific types from external vocabularies in microdata syntax.

#### <a name="author_oneOf_i0_allOf_i1"></a>14.1.2. Property `root > author > oneOf > item 0 > allOf > item 1`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| Property                                      | Pattern | Type   | Deprecated | Definition        | Title/Description                             |
| --------------------------------------------- | ------- | ------ | ---------- | ----------------- | --------------------------------------------- |
| + [author](#author_oneOf_i0_allOf_i1_author ) | No      | object | No         | In #/$defs/Person | A person (alive, dead, undead, or fictional). |

##### <a name="author_oneOf_i0_allOf_i1_author"></a>14.1.2.1. Property `root > author > oneOf > item 0 > allOf > item 1 > author`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | Yes              |
| **Additional properties** | Any type allowed |
| **Defined in**            | #/$defs/Person   |

**Description:** A person (alive, dead, undead, or fictional).

| Property                                                       | Pattern | Type        | Deprecated | Definition                                          | Title/Description                                                                                                                                                                                                                                                                                                                              |
| -------------------------------------------------------------- | ------- | ----------- | ---------- | --------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| - [@type](#author_oneOf_i0_allOf_i1_author_@type )             | No      | const       | No         | -                                                   | -                                                                                                                                                                                                                                                                                                                                              |
| + [givenName](#author_oneOf_i0_allOf_i1_author_givenName )     | No      | string      | No         | -                                                   | Given name. In the U.S., the first name of a Person.                                                                                                                                                                                                                                                                                           |
| + [familyName](#author_oneOf_i0_allOf_i1_author_familyName )   | No      | string      | No         | -                                                   | Family name. In the U.S., the last name of a Person.                                                                                                                                                                                                                                                                                           |
| + [email](#author_oneOf_i0_allOf_i1_author_email )             | No      | object      | No         | Same as [email](#publisher_email )                  | Email address.                                                                                                                                                                                                                                                                                                                                 |
| - [identifier](#author_oneOf_i0_allOf_i1_author_identifier )   | No      | object      | No         | Same as [identifier](#license_oneOf_i0_identifier ) | The identifier property represents any kind of identifier for any kind of [[Thing]], such as ISBNs, GTIN codes, UUIDs etc. Schema.org provides dedicated properties for representing many of these, either as textual strings or as URL (URI) links. See [background notes](/docs/datamodel.html#identifierBg) for more details.<br />         |
| + [affiliation](#author_oneOf_i0_allOf_i1_author_affiliation ) | No      | Combination | No         | -                                                   | An organization that this person is affiliated with. For example, a school/university, a club, or a team.                                                                                                                                                                                                                                      |

###### <a name="author_oneOf_i0_allOf_i1_author_@type"></a>14.1.2.1.1. Property `root > author > oneOf > item 0 > allOf > item 1 > author > @type`

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | No      |

Specific value: `"https://schema.org/Person"`

###### <a name="author_oneOf_i0_allOf_i1_author_givenName"></a>14.1.2.1.2. Property `root > author > oneOf > item 0 > allOf > item 1 > author > givenName`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** Given name. In the U.S., the first name of a Person.

###### <a name="author_oneOf_i0_allOf_i1_author_familyName"></a>14.1.2.1.3. Property `root > author > oneOf > item 0 > allOf > item 1 > author > familyName`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** Family name. In the U.S., the last name of a Person.

###### <a name="author_oneOf_i0_allOf_i1_author_email"></a>14.1.2.1.4. Property `root > author > oneOf > item 0 > allOf > item 1 > author > email`

|                           |                           |
| ------------------------- | ------------------------- |
| **Type**                  | `combining`               |
| **Required**              | Yes                       |
| **Additional properties** | Any type allowed          |
| **Same definition as**    | [email](#publisher_email) |

**Description:** Email address.

###### <a name="author_oneOf_i0_allOf_i1_author_identifier"></a>14.1.2.1.5. Property `root > author > oneOf > item 0 > allOf > item 1 > author > identifier`

|                           |                                            |
| ------------------------- | ------------------------------------------ |
| **Type**                  | `combining`                                |
| **Required**              | No                                         |
| **Additional properties** | Any type allowed                           |
| **Same definition as**    | [identifier](#license_oneOf_i0_identifier) |

**Description:** The identifier property represents any kind of identifier for any kind of [[Thing]], such as ISBNs, GTIN codes, UUIDs etc. Schema.org provides dedicated properties for representing many of these, either as textual strings or as URL (URI) links. See [background notes](/docs/datamodel.html#identifierBg) for more details.

###### <a name="author_oneOf_i0_allOf_i1_author_affiliation"></a>14.1.2.1.6. Property `root > author > oneOf > item 0 > allOf > item 1 > author > affiliation`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | Yes              |
| **Additional properties** | Any type allowed |

**Description:** An organization that this person is affiliated with. For example, a school/university, a club, or a team.

| One of(Option)                                                        |
| --------------------------------------------------------------------- |
| [Organization](#author_oneOf_i0_allOf_i1_author_affiliation_oneOf_i0) |
| [item 1](#author_oneOf_i0_allOf_i1_author_affiliation_oneOf_i1)       |

###### <a name="author_oneOf_i0_allOf_i1_author_affiliation_oneOf_i0"></a>14.1.2.1.6.1. Property `root > author > oneOf > item 0 > allOf > item 1 > author > affiliation > oneOf > Organization`

|                           |                         |
| ------------------------- | ----------------------- |
| **Type**                  | `object`                |
| **Required**              | No                      |
| **Additional properties** | Any type allowed        |
| **Same definition as**    | [publisher](#publisher) |

**Description:** An organization such as a school, NGO, corporation, club, etc.

###### <a name="author_oneOf_i0_allOf_i1_author_affiliation_oneOf_i1"></a>14.1.2.1.6.2. Property `root > author > oneOf > item 0 > allOf > item 1 > author > affiliation > oneOf > item 1`

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

| Each item of this array must be                                             | Description                                                    |
| --------------------------------------------------------------------------- | -------------------------------------------------------------- |
| [Organization](#author_oneOf_i0_allOf_i1_author_affiliation_oneOf_i1_items) | An organization such as a school, NGO, corporation, club, etc. |

###### <a name="author_oneOf_i0_allOf_i1_author_affiliation_oneOf_i1_items"></a>14.1.2.1.6.2.1. root > author > oneOf > item 0 > allOf > item 1 > author > affiliation > oneOf > item 1 > Organization

|                           |                         |
| ------------------------- | ----------------------- |
| **Type**                  | `object`                |
| **Required**              | No                      |
| **Additional properties** | Any type allowed        |
| **Same definition as**    | [publisher](#publisher) |

**Description:** An organization such as a school, NGO, corporation, club, etc.

### <a name="author_oneOf_i1"></a>14.2. Property `root > author > oneOf > Person`

|                           |                                            |
| ------------------------- | ------------------------------------------ |
| **Type**                  | `object`                                   |
| **Required**              | No                                         |
| **Additional properties** | Any type allowed                           |
| **Same definition as**    | [author](#author_oneOf_i0_allOf_i1_author) |

**Description:** A person (alive, dead, undead, or fictional).

### <a name="author_oneOf_i2"></a>14.3. Property `root > author > oneOf > item 2`

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

| Each item of this array must be        | Description |
| -------------------------------------- | ----------- |
| [item 2 items](#author_oneOf_i2_items) | -           |

#### <a name="author_oneOf_i2_items"></a>14.3.1. root > author > oneOf > item 2 > item 2 items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| One of(Option)                                |
| --------------------------------------------- |
| [AuthorRole](#author_oneOf_i2_items_oneOf_i0) |
| [Person](#author_oneOf_i2_items_oneOf_i1)     |

##### <a name="author_oneOf_i2_items_oneOf_i0"></a>14.3.1.1. Property `root > author > oneOf > item 2 > item 2 items > oneOf > AuthorRole`

|                           |                                     |
| ------------------------- | ----------------------------------- |
| **Type**                  | `combining`                         |
| **Required**              | No                                  |
| **Additional properties** | Any type allowed                    |
| **Same definition as**    | [author_oneOf_i0](#author_oneOf_i0) |

##### <a name="author_oneOf_i2_items_oneOf_i1"></a>14.3.1.2. Property `root > author > oneOf > item 2 > item 2 items > oneOf > Person`

|                           |                                            |
| ------------------------- | ------------------------------------------ |
| **Type**                  | `object`                                   |
| **Required**              | No                                         |
| **Additional properties** | Any type allowed                           |
| **Same definition as**    | [author](#author_oneOf_i0_allOf_i1_author) |

**Description:** A person (alive, dead, undead, or fictional).

## <a name="contributor"></a>15. Property `root > contributor`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A secondary contributor to the CreativeWork or Event.

| One of(Option)                           |
| ---------------------------------------- |
| [ContributorRole](#contributor_oneOf_i0) |
| [Person](#contributor_oneOf_i1)          |
| [item 2](#contributor_oneOf_i2)          |

### <a name="contributor_oneOf_i0"></a>15.1. Property `root > contributor > oneOf > ContributorRole`

|                           |                         |
| ------------------------- | ----------------------- |
| **Type**                  | `combining`             |
| **Required**              | No                      |
| **Additional properties** | Any type allowed        |
| **Defined in**            | #/$defs/ContributorRole |

| All of(Requirement)                      |
| ---------------------------------------- |
| [Role](#contributor_oneOf_i0_allOf_i0)   |
| [item 1](#contributor_oneOf_i0_allOf_i1) |

#### <a name="contributor_oneOf_i0_allOf_i0"></a>15.1.1. Property `root > contributor > oneOf > item 0 > allOf > Role`

|                           |                                                       |
| ------------------------- | ----------------------------------------------------- |
| **Type**                  | `object`                                              |
| **Required**              | No                                                    |
| **Additional properties** | Any type allowed                                      |
| **Same definition as**    | [author_oneOf_i0_allOf_i0](#author_oneOf_i0_allOf_i0) |

**Description:** Represents additional information about a relationship or property.

#### <a name="contributor_oneOf_i0_allOf_i1"></a>15.1.2. Property `root > contributor > oneOf > item 0 > allOf > item 1`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| Property                                                     | Pattern | Type   | Deprecated | Definition                                          | Title/Description                             |
| ------------------------------------------------------------ | ------- | ------ | ---------- | --------------------------------------------------- | --------------------------------------------- |
| + [contributor](#contributor_oneOf_i0_allOf_i1_contributor ) | No      | object | No         | Same as [author](#author_oneOf_i0_allOf_i1_author ) | A person (alive, dead, undead, or fictional). |

##### <a name="contributor_oneOf_i0_allOf_i1_contributor"></a>15.1.2.1. Property `root > contributor > oneOf > item 0 > allOf > item 1 > contributor`

|                           |                                            |
| ------------------------- | ------------------------------------------ |
| **Type**                  | `object`                                   |
| **Required**              | Yes                                        |
| **Additional properties** | Any type allowed                           |
| **Same definition as**    | [author](#author_oneOf_i0_allOf_i1_author) |

**Description:** A person (alive, dead, undead, or fictional).

### <a name="contributor_oneOf_i1"></a>15.2. Property `root > contributor > oneOf > Person`

|                           |                                            |
| ------------------------- | ------------------------------------------ |
| **Type**                  | `object`                                   |
| **Required**              | No                                         |
| **Additional properties** | Any type allowed                           |
| **Same definition as**    | [author](#author_oneOf_i0_allOf_i1_author) |

**Description:** A person (alive, dead, undead, or fictional).

### <a name="contributor_oneOf_i2"></a>15.3. Property `root > contributor > oneOf > item 2`

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

| Each item of this array must be             | Description |
| ------------------------------------------- | ----------- |
| [item 2 items](#contributor_oneOf_i2_items) | -           |

#### <a name="contributor_oneOf_i2_items"></a>15.3.1. root > contributor > oneOf > item 2 > item 2 items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| One of(Option)                                          |
| ------------------------------------------------------- |
| [ContributorRole](#contributor_oneOf_i2_items_oneOf_i0) |
| [Person](#contributor_oneOf_i2_items_oneOf_i1)          |

##### <a name="contributor_oneOf_i2_items_oneOf_i0"></a>15.3.1.1. Property `root > contributor > oneOf > item 2 > item 2 items > oneOf > ContributorRole`

|                           |                                               |
| ------------------------- | --------------------------------------------- |
| **Type**                  | `combining`                                   |
| **Required**              | No                                            |
| **Additional properties** | Any type allowed                              |
| **Same definition as**    | [contributor_oneOf_i0](#contributor_oneOf_i0) |

##### <a name="contributor_oneOf_i2_items_oneOf_i1"></a>15.3.1.2. Property `root > contributor > oneOf > item 2 > item 2 items > oneOf > Person`

|                           |                                            |
| ------------------------- | ------------------------------------------ |
| **Type**                  | `object`                                   |
| **Required**              | No                                         |
| **Additional properties** | Any type allowed                           |
| **Same definition as**    | [author](#author_oneOf_i0_allOf_i1_author) |

**Description:** A person (alive, dead, undead, or fictional).

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans) on 2025-11-07 at 00:41:11 +0100
