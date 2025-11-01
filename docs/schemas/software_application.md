# Schema Docs

- [1. Property `root > @type`](#@type)
- [2. Property `root > name`](#name)
- [3. Property `root > copyrightYear`](#copyrightYear)
- [4. Property `root > dateCreated`](#dateCreated)
  - [4.1. Property `root > dateCreated > oneOf > item 0`](#dateCreated_oneOf_i0)
  - [4.2. Property `root > dateCreated > oneOf > item 1`](#dateCreated_oneOf_i1)
- [5. Property `root > identifier`](#identifier)
  - [5.1. Property `root > identifier > oneOf > item 0`](#identifier_oneOf_i0)
  - [5.2. Property `root > identifier > oneOf > item 1`](#identifier_oneOf_i1)
- [6. Property `root > description`](#description)
- [7. Property `root > sameAs`](#sameAs)
  - [7.1. Property `root > sameAs > oneOf > item 0`](#sameAs_oneOf_i0)
  - [7.2. Property `root > sameAs > oneOf > item 1`](#sameAs_oneOf_i1)
    - [7.2.1. root > sameAs > oneOf > item 1 > item 1 items](#sameAs_oneOf_i1_items)
- [8. Property `root > author`](#author)
  - [8.1. Property `root > author > oneOf > Person`](#author_oneOf_i0)
    - [8.1.1. Property `root > author > oneOf > item 0 > @type`](#author_oneOf_i0_@type)
    - [8.1.2. Property `root > author > oneOf > item 0 > givenName`](#author_oneOf_i0_givenName)
    - [8.1.3. Property `root > author > oneOf > item 0 > familyName`](#author_oneOf_i0_familyName)
    - [8.1.4. Property `root > author > oneOf > item 0 > email`](#author_oneOf_i0_email)
      - [8.1.4.1. Property `root > author > oneOf > item 0 > email > oneOf > item 0`](#author_oneOf_i0_email_oneOf_i0)
      - [8.1.4.2. Property `root > author > oneOf > item 0 > email > oneOf > item 1`](#author_oneOf_i0_email_oneOf_i1)
        - [8.1.4.2.1. root > author > oneOf > item 0 > email > oneOf > item 1 > item 1 items](#author_oneOf_i0_email_oneOf_i1_items)
    - [8.1.5. Property `root > author > oneOf > item 0 > identifier`](#author_oneOf_i0_identifier)
    - [8.1.6. Property `root > author > oneOf > item 0 > affiliation`](#author_oneOf_i0_affiliation)
      - [8.1.6.1. Property `root > author > oneOf > item 0 > affiliation > oneOf > Organization`](#author_oneOf_i0_affiliation_oneOf_i0)
        - [8.1.6.1.1. Property `root > author > oneOf > item 0 > affiliation > oneOf > item 0 > @type`](#author_oneOf_i0_affiliation_oneOf_i0_@type)
        - [8.1.6.1.2. Property `root > author > oneOf > item 0 > affiliation > oneOf > item 0 > name`](#author_oneOf_i0_affiliation_oneOf_i0_name)
        - [8.1.6.1.3. Property `root > author > oneOf > item 0 > affiliation > oneOf > item 0 > email`](#author_oneOf_i0_affiliation_oneOf_i0_email)
        - [8.1.6.1.4. Property `root > author > oneOf > item 0 > affiliation > oneOf > item 0 > identifier`](#author_oneOf_i0_affiliation_oneOf_i0_identifier)
      - [8.1.6.2. Property `root > author > oneOf > item 0 > affiliation > oneOf > item 1`](#author_oneOf_i0_affiliation_oneOf_i1)
        - [8.1.6.2.1. root > author > oneOf > item 0 > affiliation > oneOf > item 1 > Organization](#author_oneOf_i0_affiliation_oneOf_i1_items)
  - [8.2. Property `root > author > oneOf > item 1`](#author_oneOf_i1)
    - [8.2.1. root > author > oneOf > item 1 > item 1 items](#author_oneOf_i1_items)
- [9. Property `root > license`](#license)
  - [9.1. Property `root > license > oneOf > CreativeWork`](#license_oneOf_i0)
    - [9.1.1. Property `root > license > oneOf > item 0 > @type`](#license_oneOf_i0_@type)
    - [9.1.2. Property `root > license > oneOf > item 0 > name`](#license_oneOf_i0_name)
    - [9.1.3. Property `root > license > oneOf > item 0 > url`](#license_oneOf_i0_url)
    - [9.1.4. Property `root > license > oneOf > item 0 > identifier`](#license_oneOf_i0_identifier)
  - [9.2. Property `root > license > oneOf > item 1`](#license_oneOf_i1)
  - [9.3. Property `root > license > oneOf > item 2`](#license_oneOf_i2)
    - [9.3.1. root > license > oneOf > item 2 > item 2 items](#license_oneOf_i2_items)
      - [9.3.1.1. Property `root > license > oneOf > item 2 > item 2 items > oneOf > CreativeWork`](#license_oneOf_i2_items_oneOf_i0)
      - [9.3.1.2. Property `root > license > oneOf > item 2 > item 2 items > oneOf > item 1`](#license_oneOf_i2_items_oneOf_i1)
- [10. Property `root > publisher`](#publisher)
- [11. Property `root > softwareVersion`](#softwareVersion)
- [12. Property `root > keywords`](#keywords)
  - [12.1. Property `root > keywords > oneOf > item 0`](#keywords_oneOf_i0)
  - [12.2. Property `root > keywords > oneOf > item 1`](#keywords_oneOf_i1)
  - [12.3. Property `root > keywords > oneOf > DefinedTerm`](#keywords_oneOf_i2)
    - [12.3.1. Property `root > keywords > oneOf > item 2 > @type`](#keywords_oneOf_i2_@type)
    - [12.3.2. Property `root > keywords > oneOf > item 2 > name`](#keywords_oneOf_i2_name)
    - [12.3.3. Property `root > keywords > oneOf > item 2 > description`](#keywords_oneOf_i2_description)
    - [12.3.4. Property `root > keywords > oneOf > item 2 > termCode`](#keywords_oneOf_i2_termCode)
    - [12.3.5. Property `root > keywords > oneOf > item 2 > inDefinedTermSet`](#keywords_oneOf_i2_inDefinedTermSet)
  - [12.4. Property `root > keywords > oneOf > item 3`](#keywords_oneOf_i3)
    - [12.4.1. root > keywords > oneOf > item 3 > item 3 items](#keywords_oneOf_i3_items)
      - [12.4.1.1. Property `root > keywords > oneOf > item 3 > item 3 items > oneOf > item 0`](#keywords_oneOf_i3_items_oneOf_i0)
      - [12.4.1.2. Property `root > keywords > oneOf > item 3 > item 3 items > oneOf > item 1`](#keywords_oneOf_i3_items_oneOf_i1)
      - [12.4.1.3. Property `root > keywords > oneOf > item 3 > item 3 items > oneOf > DefinedTerm`](#keywords_oneOf_i3_items_oneOf_i2)
- [13. Property `root > softwareHelp`](#softwareHelp)
  - [13.1. Property `root > softwareHelp > oneOf > CreativeWork`](#softwareHelp_oneOf_i0)
  - [13.2. Property `root > softwareHelp > oneOf > item 1`](#softwareHelp_oneOf_i1)
    - [13.2.1. root > softwareHelp > oneOf > item 1 > CreativeWork](#softwareHelp_oneOf_i1_items)
- [14. Property `root > softwareRequirements`](#softwareRequirements)
  - [14.1. Property `root > softwareRequirements > oneOf > item 0`](#softwareRequirements_oneOf_i0)
  - [14.2. Property `root > softwareRequirements > oneOf > item 1`](#softwareRequirements_oneOf_i1)
  - [14.3. Property `root > softwareRequirements > oneOf > item 2`](#softwareRequirements_oneOf_i2)
    - [14.3.1. root > softwareRequirements > oneOf > item 2 > item 2 items](#softwareRequirements_oneOf_i2_items)
      - [14.3.1.1. Property `root > softwareRequirements > oneOf > item 2 > item 2 items > oneOf > item 0`](#softwareRequirements_oneOf_i2_items_oneOf_i0)
      - [14.3.1.2. Property `root > softwareRequirements > oneOf > item 2 > item 2 items > oneOf > item 1`](#softwareRequirements_oneOf_i2_items_oneOf_i1)
- [15. Property `root > operatingSystem`](#operatingSystem)
  - [15.1. Property `root > operatingSystem > oneOf > item 0`](#operatingSystem_oneOf_i0)
  - [15.2. Property `root > operatingSystem > oneOf > item 1`](#operatingSystem_oneOf_i1)
    - [15.2.1. root > operatingSystem > oneOf > item 1 > item 1 items](#operatingSystem_oneOf_i1_items)

|                           |                             |
| ------------------------- | --------------------------- |
| **Type**                  | `object`                    |
| **Required**              | No                          |
| **Additional properties** | Any type allowed            |
| **Defined in**            | #/$defs/SoftwareApplication |

**Description:** A software application.

| Property                                         | Pattern | Type        | Deprecated | Definition                                                                             | Title/Description                                                                                                                                                                                                                                                                                                                              |
| ------------------------------------------------ | ------- | ----------- | ---------- | -------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| - [@type](#@type )                               | No      | const       | No         | -                                                                                      | -                                                                                                                                                                                                                                                                                                                                              |
| + [name](#name )                                 | No      | string      | No         | -                                                                                      | The name of the item.                                                                                                                                                                                                                                                                                                                          |
| + [copyrightYear](#copyrightYear )               | No      | integer     | No         | -                                                                                      | The year during which the claimed copyright for the CreativeWork was first asserted.                                                                                                                                                                                                                                                           |
| + [dateCreated](#dateCreated )                   | No      | Combination | No         | -                                                                                      | The date on which the CreativeWork was created or the item was added to a DataFeed.                                                                                                                                                                                                                                                            |
| - [identifier](#identifier )                     | No      | object      | No         | In #/$defs/Identifier                                                                  | The identifier property represents any kind of identifier for any kind of [[Thing]], such as ISBNs, GTIN codes, UUIDs etc. Schema.org provides dedicated properties for representing many of these, either as textual strings or as URL (URI) links. See [background notes](/docs/datamodel.html#identifierBg) for more details.<br />         |
| + [description](#description )                   | No      | string      | No         | -                                                                                      | A description of the item.                                                                                                                                                                                                                                                                                                                     |
| - [sameAs](#sameAs )                             | No      | object      | No         | In #/$defs/URI                                                                         | URL of a reference Web page that unambiguously indicates the item's identity. E.g. the URL of the item's Wikipedia page, Wikidata entry, or official website.                                                                                                                                                                                  |
| + [author](#author )                             | No      | Combination | No         | -                                                                                      | The author of this content or rating. Please note that author is special in that HTML 5 provides a special mechanism for indicating authorship via the rel tag. That is equivalent to this and may be used interchangeably.                                                                                                                    |
| + [license](#license )                           | No      | Combination | No         | -                                                                                      | A license document that applies to this content, typically indicated by URL.                                                                                                                                                                                                                                                                   |
| + [publisher](#publisher )                       | No      | object      | No         | Same as [author_oneOf_i0_affiliation_oneOf_i0](#author_oneOf_i0_affiliation_oneOf_i0 ) | The publisher of the article in question.                                                                                                                                                                                                                                                                                                      |
| + [softwareVersion](#softwareVersion )           | No      | string      | No         | -                                                                                      | Version of the software instance.                                                                                                                                                                                                                                                                                                              |
| - [keywords](#keywords )                         | No      | Combination | No         | -                                                                                      | Keywords or tags used to describe some item. Multiple textual entries in a keywords list are typically delimited by commas, or by repeating the property.                                                                                                                                                                                      |
| - [softwareHelp](#softwareHelp )                 | No      | Combination | No         | -                                                                                      | Software application help.                                                                                                                                                                                                                                                                                                                     |
| - [softwareRequirements](#softwareRequirements ) | No      | Combination | No         | -                                                                                      | Component dependency requirements for application. This includes runtime environments and shared libraries that are not included in the application distribution package, but required to run the application (examples: DirectX, Java or .NET runtime).                                                                                       |
| - [operatingSystem](#operatingSystem )           | No      | Combination | No         | -                                                                                      | Operating systems supported (Windows 7, OS X 10.6, Android 1.6).                                                                                                                                                                                                                                                                               |

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

## <a name="copyrightYear"></a>3. Property `root > copyrightYear`

|              |           |
| ------------ | --------- |
| **Type**     | `integer` |
| **Required** | Yes       |
| **Format**   | `int32`   |

**Description:** The year during which the claimed copyright for the CreativeWork was first asserted.

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

## <a name="identifier"></a>5. Property `root > identifier`

|                           |                    |
| ------------------------- | ------------------ |
| **Type**                  | `combining`        |
| **Required**              | No                 |
| **Additional properties** | Any type allowed   |
| **Defined in**            | #/$defs/Identifier |

**Description:** The identifier property represents any kind of identifier for any kind of [[Thing]], such as ISBNs, GTIN codes, UUIDs etc. Schema.org provides dedicated properties for representing many of these, either as textual strings or as URL (URI) links. See [background notes](/docs/datamodel.html#identifierBg) for more details.

| One of(Option)                 |
| ------------------------------ |
| [item 0](#identifier_oneOf_i0) |
| [item 1](#identifier_oneOf_i1) |

### <a name="identifier_oneOf_i0"></a>5.1. Property `root > identifier > oneOf > item 0`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `uri`    |

### <a name="identifier_oneOf_i1"></a>5.2. Property `root > identifier > oneOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

## <a name="description"></a>6. Property `root > description`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** A description of the item.

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

## <a name="author"></a>8. Property `root > author`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | Yes              |
| **Additional properties** | Any type allowed |

**Description:** The author of this content or rating. Please note that author is special in that HTML 5 provides a special mechanism for indicating authorship via the rel tag. That is equivalent to this and may be used interchangeably.

| One of(Option)             |
| -------------------------- |
| [Person](#author_oneOf_i0) |
| [item 1](#author_oneOf_i1) |

### <a name="author_oneOf_i0"></a>8.1. Property `root > author > oneOf > Person`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |
| **Defined in**            | #/$defs/Person   |

**Description:** A person (alive, dead, undead, or fictional).

| Property                                       | Pattern | Type        | Deprecated | Definition                         | Title/Description                                                                                                                                                                                                                                                                                                                              |
| ---------------------------------------------- | ------- | ----------- | ---------- | ---------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| - [@type](#author_oneOf_i0_@type )             | No      | const       | No         | -                                  | -                                                                                                                                                                                                                                                                                                                                              |
| + [givenName](#author_oneOf_i0_givenName )     | No      | string      | No         | -                                  | Given name. In the U.S., the first name of a Person.                                                                                                                                                                                                                                                                                           |
| + [familyName](#author_oneOf_i0_familyName )   | No      | string      | No         | -                                  | Family name. In the U.S., the last name of a Person.                                                                                                                                                                                                                                                                                           |
| + [email](#author_oneOf_i0_email )             | No      | object      | No         | In #/$defs/Email                   | Email address.                                                                                                                                                                                                                                                                                                                                 |
| - [identifier](#author_oneOf_i0_identifier )   | No      | object      | No         | Same as [identifier](#identifier ) | The identifier property represents any kind of identifier for any kind of [[Thing]], such as ISBNs, GTIN codes, UUIDs etc. Schema.org provides dedicated properties for representing many of these, either as textual strings or as URL (URI) links. See [background notes](/docs/datamodel.html#identifierBg) for more details.<br />         |
| + [affiliation](#author_oneOf_i0_affiliation ) | No      | Combination | No         | -                                  | An organization that this person is affiliated with. For example, a school/university, a club, or a team.                                                                                                                                                                                                                                      |

#### <a name="author_oneOf_i0_@type"></a>8.1.1. Property `root > author > oneOf > item 0 > @type`

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | No      |

Specific value: `"https://schema.org/Person"`

#### <a name="author_oneOf_i0_givenName"></a>8.1.2. Property `root > author > oneOf > item 0 > givenName`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** Given name. In the U.S., the first name of a Person.

#### <a name="author_oneOf_i0_familyName"></a>8.1.3. Property `root > author > oneOf > item 0 > familyName`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** Family name. In the U.S., the last name of a Person.

#### <a name="author_oneOf_i0_email"></a>8.1.4. Property `root > author > oneOf > item 0 > email`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | Yes              |
| **Additional properties** | Any type allowed |
| **Defined in**            | #/$defs/Email    |

**Description:** Email address.

| One of(Option)                            |
| ----------------------------------------- |
| [item 0](#author_oneOf_i0_email_oneOf_i0) |
| [item 1](#author_oneOf_i0_email_oneOf_i1) |

##### <a name="author_oneOf_i0_email_oneOf_i0"></a>8.1.4.1. Property `root > author > oneOf > item 0 > email > oneOf > item 0`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `email`  |

##### <a name="author_oneOf_i0_email_oneOf_i1"></a>8.1.4.2. Property `root > author > oneOf > item 0 > email > oneOf > item 1`

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

| Each item of this array must be                       | Description |
| ----------------------------------------------------- | ----------- |
| [item 1 items](#author_oneOf_i0_email_oneOf_i1_items) | -           |

###### <a name="author_oneOf_i0_email_oneOf_i1_items"></a>8.1.4.2.1. root > author > oneOf > item 0 > email > oneOf > item 1 > item 1 items

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `email`  |

#### <a name="author_oneOf_i0_identifier"></a>8.1.5. Property `root > author > oneOf > item 0 > identifier`

|                           |                           |
| ------------------------- | ------------------------- |
| **Type**                  | `combining`               |
| **Required**              | No                        |
| **Additional properties** | Any type allowed          |
| **Same definition as**    | [identifier](#identifier) |

**Description:** The identifier property represents any kind of identifier for any kind of [[Thing]], such as ISBNs, GTIN codes, UUIDs etc. Schema.org provides dedicated properties for representing many of these, either as textual strings or as URL (URI) links. See [background notes](/docs/datamodel.html#identifierBg) for more details.

#### <a name="author_oneOf_i0_affiliation"></a>8.1.6. Property `root > author > oneOf > item 0 > affiliation`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | Yes              |
| **Additional properties** | Any type allowed |

**Description:** An organization that this person is affiliated with. For example, a school/university, a club, or a team.

| One of(Option)                                        |
| ----------------------------------------------------- |
| [Organization](#author_oneOf_i0_affiliation_oneOf_i0) |
| [item 1](#author_oneOf_i0_affiliation_oneOf_i1)       |

##### <a name="author_oneOf_i0_affiliation_oneOf_i0"></a>8.1.6.1. Property `root > author > oneOf > item 0 > affiliation > oneOf > Organization`

|                           |                      |
| ------------------------- | -------------------- |
| **Type**                  | `object`             |
| **Required**              | No                   |
| **Additional properties** | Any type allowed     |
| **Defined in**            | #/$defs/Organization |

**Description:** An organization such as a school, NGO, corporation, club, etc.

| Property                                                          | Pattern | Type   | Deprecated | Definition                               | Title/Description                                                                                                                                                                                                                                                                                                                              |
| ----------------------------------------------------------------- | ------- | ------ | ---------- | ---------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| - [@type](#author_oneOf_i0_affiliation_oneOf_i0_@type )           | No      | const  | No         | -                                        | -                                                                                                                                                                                                                                                                                                                                              |
| + [name](#author_oneOf_i0_affiliation_oneOf_i0_name )             | No      | string | No         | -                                        | The name of the item.                                                                                                                                                                                                                                                                                                                          |
| - [email](#author_oneOf_i0_affiliation_oneOf_i0_email )           | No      | object | No         | Same as [email](#author_oneOf_i0_email ) | Email address.                                                                                                                                                                                                                                                                                                                                 |
| - [identifier](#author_oneOf_i0_affiliation_oneOf_i0_identifier ) | No      | object | No         | Same as [identifier](#identifier )       | The identifier property represents any kind of identifier for any kind of [[Thing]], such as ISBNs, GTIN codes, UUIDs etc. Schema.org provides dedicated properties for representing many of these, either as textual strings or as URL (URI) links. See [background notes](/docs/datamodel.html#identifierBg) for more details.<br />         |

###### <a name="author_oneOf_i0_affiliation_oneOf_i0_@type"></a>8.1.6.1.1. Property `root > author > oneOf > item 0 > affiliation > oneOf > item 0 > @type`

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | No      |

Specific value: `"https://schema.org/Organization"`

###### <a name="author_oneOf_i0_affiliation_oneOf_i0_name"></a>8.1.6.1.2. Property `root > author > oneOf > item 0 > affiliation > oneOf > item 0 > name`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** The name of the item.

###### <a name="author_oneOf_i0_affiliation_oneOf_i0_email"></a>8.1.6.1.3. Property `root > author > oneOf > item 0 > affiliation > oneOf > item 0 > email`

|                           |                                 |
| ------------------------- | ------------------------------- |
| **Type**                  | `combining`                     |
| **Required**              | No                              |
| **Additional properties** | Any type allowed                |
| **Same definition as**    | [email](#author_oneOf_i0_email) |

**Description:** Email address.

###### <a name="author_oneOf_i0_affiliation_oneOf_i0_identifier"></a>8.1.6.1.4. Property `root > author > oneOf > item 0 > affiliation > oneOf > item 0 > identifier`

|                           |                           |
| ------------------------- | ------------------------- |
| **Type**                  | `combining`               |
| **Required**              | No                        |
| **Additional properties** | Any type allowed          |
| **Same definition as**    | [identifier](#identifier) |

**Description:** The identifier property represents any kind of identifier for any kind of [[Thing]], such as ISBNs, GTIN codes, UUIDs etc. Schema.org provides dedicated properties for representing many of these, either as textual strings or as URL (URI) links. See [background notes](/docs/datamodel.html#identifierBg) for more details.

##### <a name="author_oneOf_i0_affiliation_oneOf_i1"></a>8.1.6.2. Property `root > author > oneOf > item 0 > affiliation > oneOf > item 1`

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

| Each item of this array must be                             | Description                                                    |
| ----------------------------------------------------------- | -------------------------------------------------------------- |
| [Organization](#author_oneOf_i0_affiliation_oneOf_i1_items) | An organization such as a school, NGO, corporation, club, etc. |

###### <a name="author_oneOf_i0_affiliation_oneOf_i1_items"></a>8.1.6.2.1. root > author > oneOf > item 0 > affiliation > oneOf > item 1 > Organization

|                           |                                                                               |
| ------------------------- | ----------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                      |
| **Required**              | No                                                                            |
| **Additional properties** | Any type allowed                                                              |
| **Same definition as**    | [author_oneOf_i0_affiliation_oneOf_i0](#author_oneOf_i0_affiliation_oneOf_i0) |

**Description:** An organization such as a school, NGO, corporation, club, etc.

### <a name="author_oneOf_i1"></a>8.2. Property `root > author > oneOf > item 1`

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

| Each item of this array must be        | Description                                   |
| -------------------------------------- | --------------------------------------------- |
| [item 1 items](#author_oneOf_i1_items) | A person (alive, dead, undead, or fictional). |

#### <a name="author_oneOf_i1_items"></a>8.2.1. root > author > oneOf > item 1 > item 1 items

|                           |                                     |
| ------------------------- | ----------------------------------- |
| **Type**                  | `object`                            |
| **Required**              | No                                  |
| **Additional properties** | Any type allowed                    |
| **Same definition as**    | [author_oneOf_i0](#author_oneOf_i0) |

**Description:** A person (alive, dead, undead, or fictional).

## <a name="license"></a>9. Property `root > license`

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

### <a name="license_oneOf_i0"></a>9.1. Property `root > license > oneOf > CreativeWork`

|                           |                      |
| ------------------------- | -------------------- |
| **Type**                  | `object`             |
| **Required**              | No                   |
| **Additional properties** | Any type allowed     |
| **Defined in**            | #/$defs/CreativeWork |

**Description:** The most generic kind of creative work, including books, movies, photographs, software programs, etc.

| Property                                      | Pattern | Type   | Deprecated | Definition                         | Title/Description                                                                                                                                                                                                                                                                                                                              |
| --------------------------------------------- | ------- | ------ | ---------- | ---------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| - [@type](#license_oneOf_i0_@type )           | No      | const  | No         | -                                  | -                                                                                                                                                                                                                                                                                                                                              |
| - [name](#license_oneOf_i0_name )             | No      | string | No         | -                                  | The name of the item.                                                                                                                                                                                                                                                                                                                          |
| - [url](#license_oneOf_i0_url )               | No      | string | No         | -                                  | URL of the item.                                                                                                                                                                                                                                                                                                                               |
| - [identifier](#license_oneOf_i0_identifier ) | No      | object | No         | Same as [identifier](#identifier ) | The identifier property represents any kind of identifier for any kind of [[Thing]], such as ISBNs, GTIN codes, UUIDs etc. Schema.org provides dedicated properties for representing many of these, either as textual strings or as URL (URI) links. See [background notes](/docs/datamodel.html#identifierBg) for more details.<br />         |

#### <a name="license_oneOf_i0_@type"></a>9.1.1. Property `root > license > oneOf > item 0 > @type`

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | No      |

Specific value: `"https://schema.org/CreativeWork"`

#### <a name="license_oneOf_i0_name"></a>9.1.2. Property `root > license > oneOf > item 0 > name`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** The name of the item.

#### <a name="license_oneOf_i0_url"></a>9.1.3. Property `root > license > oneOf > item 0 > url`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `uri`    |

**Description:** URL of the item.

#### <a name="license_oneOf_i0_identifier"></a>9.1.4. Property `root > license > oneOf > item 0 > identifier`

|                           |                           |
| ------------------------- | ------------------------- |
| **Type**                  | `combining`               |
| **Required**              | No                        |
| **Additional properties** | Any type allowed          |
| **Same definition as**    | [identifier](#identifier) |

**Description:** The identifier property represents any kind of identifier for any kind of [[Thing]], such as ISBNs, GTIN codes, UUIDs etc. Schema.org provides dedicated properties for representing many of these, either as textual strings or as URL (URI) links. See [background notes](/docs/datamodel.html#identifierBg) for more details.

### <a name="license_oneOf_i1"></a>9.2. Property `root > license > oneOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `uri`    |

### <a name="license_oneOf_i2"></a>9.3. Property `root > license > oneOf > item 2`

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

#### <a name="license_oneOf_i2_items"></a>9.3.1. root > license > oneOf > item 2 > item 2 items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| One of(Option)                                   |
| ------------------------------------------------ |
| [CreativeWork](#license_oneOf_i2_items_oneOf_i0) |
| [item 1](#license_oneOf_i2_items_oneOf_i1)       |

##### <a name="license_oneOf_i2_items_oneOf_i0"></a>9.3.1.1. Property `root > license > oneOf > item 2 > item 2 items > oneOf > CreativeWork`

|                           |                                       |
| ------------------------- | ------------------------------------- |
| **Type**                  | `object`                              |
| **Required**              | No                                    |
| **Additional properties** | Any type allowed                      |
| **Same definition as**    | [license_oneOf_i0](#license_oneOf_i0) |

**Description:** The most generic kind of creative work, including books, movies, photographs, software programs, etc.

##### <a name="license_oneOf_i2_items_oneOf_i1"></a>9.3.1.2. Property `root > license > oneOf > item 2 > item 2 items > oneOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `uri`    |

## <a name="publisher"></a>10. Property `root > publisher`

|                           |                                                                               |
| ------------------------- | ----------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                      |
| **Required**              | Yes                                                                           |
| **Additional properties** | Any type allowed                                                              |
| **Same definition as**    | [author_oneOf_i0_affiliation_oneOf_i0](#author_oneOf_i0_affiliation_oneOf_i0) |

**Description:** The publisher of the article in question.

## <a name="softwareVersion"></a>11. Property `root > softwareVersion`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** Version of the software instance.

## <a name="keywords"></a>12. Property `root > keywords`

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

### <a name="keywords_oneOf_i0"></a>12.1. Property `root > keywords > oneOf > item 0`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

### <a name="keywords_oneOf_i1"></a>12.2. Property `root > keywords > oneOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `uri`    |

### <a name="keywords_oneOf_i2"></a>12.3. Property `root > keywords > oneOf > DefinedTerm`

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

#### <a name="keywords_oneOf_i2_@type"></a>12.3.1. Property `root > keywords > oneOf > item 2 > @type`

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | No      |

Specific value: `"https://schema.org/DefinedTerm"`

#### <a name="keywords_oneOf_i2_name"></a>12.3.2. Property `root > keywords > oneOf > item 2 > name`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** The name of the item.

#### <a name="keywords_oneOf_i2_description"></a>12.3.3. Property `root > keywords > oneOf > item 2 > description`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** A description of the item.

#### <a name="keywords_oneOf_i2_termCode"></a>12.3.4. Property `root > keywords > oneOf > item 2 > termCode`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** A code that identifies this [[DefinedTerm]] within a [[DefinedTermSet]].

#### <a name="keywords_oneOf_i2_inDefinedTermSet"></a>12.3.5. Property `root > keywords > oneOf > item 2 > inDefinedTermSet`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `uri`    |

**Description:** A [[DefinedTermSet]] that contains this term.

### <a name="keywords_oneOf_i3"></a>12.4. Property `root > keywords > oneOf > item 3`

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

#### <a name="keywords_oneOf_i3_items"></a>12.4.1. root > keywords > oneOf > item 3 > item 3 items

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

##### <a name="keywords_oneOf_i3_items_oneOf_i0"></a>12.4.1.1. Property `root > keywords > oneOf > item 3 > item 3 items > oneOf > item 0`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

##### <a name="keywords_oneOf_i3_items_oneOf_i1"></a>12.4.1.2. Property `root > keywords > oneOf > item 3 > item 3 items > oneOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `uri`    |

##### <a name="keywords_oneOf_i3_items_oneOf_i2"></a>12.4.1.3. Property `root > keywords > oneOf > item 3 > item 3 items > oneOf > DefinedTerm`

|                           |                                         |
| ------------------------- | --------------------------------------- |
| **Type**                  | `object`                                |
| **Required**              | No                                      |
| **Additional properties** | Any type allowed                        |
| **Same definition as**    | [keywords_oneOf_i2](#keywords_oneOf_i2) |

**Description:** A word, name, acronym, phrase, etc. with a formal definition. Often used in the context of category or subject classification, glossaries or dictionaries, product or creative work types, etc. Use the name property for the term being defined, use termCode if the term has an alpha-numeric code allocated, use description to provide the definition of the term.

## <a name="softwareHelp"></a>13. Property `root > softwareHelp`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** Software application help.

| One of(Option)                         |
| -------------------------------------- |
| [CreativeWork](#softwareHelp_oneOf_i0) |
| [item 1](#softwareHelp_oneOf_i1)       |

### <a name="softwareHelp_oneOf_i0"></a>13.1. Property `root > softwareHelp > oneOf > CreativeWork`

|                           |                                       |
| ------------------------- | ------------------------------------- |
| **Type**                  | `object`                              |
| **Required**              | No                                    |
| **Additional properties** | Any type allowed                      |
| **Same definition as**    | [license_oneOf_i0](#license_oneOf_i0) |

**Description:** The most generic kind of creative work, including books, movies, photographs, software programs, etc.

### <a name="softwareHelp_oneOf_i1"></a>13.2. Property `root > softwareHelp > oneOf > item 1`

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

#### <a name="softwareHelp_oneOf_i1_items"></a>13.2.1. root > softwareHelp > oneOf > item 1 > CreativeWork

|                           |                                       |
| ------------------------- | ------------------------------------- |
| **Type**                  | `object`                              |
| **Required**              | No                                    |
| **Additional properties** | Any type allowed                      |
| **Same definition as**    | [license_oneOf_i0](#license_oneOf_i0) |

**Description:** The most generic kind of creative work, including books, movies, photographs, software programs, etc.

## <a name="softwareRequirements"></a>14. Property `root > softwareRequirements`

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

### <a name="softwareRequirements_oneOf_i0"></a>14.1. Property `root > softwareRequirements > oneOf > item 0`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

### <a name="softwareRequirements_oneOf_i1"></a>14.2. Property `root > softwareRequirements > oneOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `uri`    |

### <a name="softwareRequirements_oneOf_i2"></a>14.3. Property `root > softwareRequirements > oneOf > item 2`

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

#### <a name="softwareRequirements_oneOf_i2_items"></a>14.3.1. root > softwareRequirements > oneOf > item 2 > item 2 items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| One of(Option)                                          |
| ------------------------------------------------------- |
| [item 0](#softwareRequirements_oneOf_i2_items_oneOf_i0) |
| [item 1](#softwareRequirements_oneOf_i2_items_oneOf_i1) |

##### <a name="softwareRequirements_oneOf_i2_items_oneOf_i0"></a>14.3.1.1. Property `root > softwareRequirements > oneOf > item 2 > item 2 items > oneOf > item 0`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

##### <a name="softwareRequirements_oneOf_i2_items_oneOf_i1"></a>14.3.1.2. Property `root > softwareRequirements > oneOf > item 2 > item 2 items > oneOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `uri`    |

## <a name="operatingSystem"></a>15. Property `root > operatingSystem`

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

### <a name="operatingSystem_oneOf_i0"></a>15.1. Property `root > operatingSystem > oneOf > item 0`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

### <a name="operatingSystem_oneOf_i1"></a>15.2. Property `root > operatingSystem > oneOf > item 1`

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

#### <a name="operatingSystem_oneOf_i1_items"></a>15.2.1. root > operatingSystem > oneOf > item 1 > item 1 items

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans) on 2025-11-02 at 00:11:30 +0100
