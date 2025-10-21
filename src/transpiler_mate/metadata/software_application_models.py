# Transpiler Mate (c) 2025
# 
# Transpiler Mate is licensed under
# Creative Commons Attribution-ShareAlike 4.0 International.
# 
# You should have received a copy of the license along with this work.
# If not, see <https://creativecommons.org/licenses/by-sa/4.0/>.

from __future__ import annotations

from .. import TranspilerBaseModel
from datetime import (
    date,
    time
)
from pydantic import (
    AliasChoices,
    AnyUrl,
    AwareDatetime,
    Field,
    RootModel
)
from typing import (
    Any,
    List,
    Literal,
    Optional,
    Union
)


class Text(RootModel[Any]):
    root: Any


class CssSelectorType(TranspilerBaseModel):
    field_type: Literal['https://schema.org/CssSelectorType'] = Field(
        'https://schema.org/CssSelectorType', alias='@type'
    )


class Thing(TranspilerBaseModel):
    """
    The most generic type of item.
    """

    field_type: Literal['https://schema.org/Thing'] = Field(
        'https://schema.org/Thing', alias='@type'
    )
    additional_type: Optional[Union[str, AnyUrl, List[Union[str, AnyUrl]]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'additionalType', 'https://schema.org/additionalType'
        ),
        serialization_alias='https://schema.org/additionalType',
    )
    identifier: Optional[
        Union[AnyUrl, str, PropertyValue, List[Union[AnyUrl, str, PropertyValue]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('identifier', 'https://schema.org/identifier'),
        serialization_alias='https://schema.org/identifier',
    )
    image: Optional[
        Union[ImageObject, AnyUrl, List[Union[ImageObject, AnyUrl]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('image', 'https://schema.org/image'),
        serialization_alias='https://schema.org/image',
    )
    url: Optional[Union[AnyUrl, List[AnyUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices('url', 'https://schema.org/url'),
        serialization_alias='https://schema.org/url',
    )
    disambiguating_description: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'disambiguatingDescription', 'https://schema.org/disambiguatingDescription'
        ),
        serialization_alias='https://schema.org/disambiguatingDescription',
    )
    description: Optional[Union[str, TextObject, List[Union[str, TextObject]]]] = Field(
        default=None,
        validation_alias=AliasChoices('description', 'https://schema.org/description'),
        serialization_alias='https://schema.org/description',
    )
    main_entity_of_page: Optional[
        Union[CreativeWork, AnyUrl, List[Union[CreativeWork, AnyUrl]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'mainEntityOfPage', 'https://schema.org/mainEntityOfPage'
        ),
        serialization_alias='https://schema.org/mainEntityOfPage',
    )
    same_as: Optional[Union[AnyUrl, List[AnyUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices('sameAs', 'https://schema.org/sameAs'),
        serialization_alias='https://schema.org/sameAs',
    )
    name: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices('name', 'https://schema.org/name'),
        serialization_alias='https://schema.org/name',
    )
    subject_of: Optional[
        Union[Event, CreativeWork, List[Union[Event, CreativeWork]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('subjectOf', 'https://schema.org/subjectOf'),
        serialization_alias='https://schema.org/subjectOf',
    )
    alternate_name: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'alternateName', 'https://schema.org/alternateName'
        ),
        serialization_alias='https://schema.org/alternateName',
    )
    potential_action: Optional[Union[Action, List[Action]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'potentialAction', 'https://schema.org/potentialAction'
        ),
        serialization_alias='https://schema.org/potentialAction',
    )


class Intangible(Thing):
    field_type: Literal['https://schema.org/Intangible'] = Field(
        'https://schema.org/Intangible', alias='@type'
    )


class CreativeWork(Thing):
    field_type: Literal['https://schema.org/CreativeWork'] = Field(
        'https://schema.org/CreativeWork', alias='@type'
    )
    educational_use: Optional[
        Union[DefinedTerm, str, List[Union[DefinedTerm, str]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'educationalUse', 'https://schema.org/educationalUse'
        ),
        serialization_alias='https://schema.org/educationalUse',
    )
    access_mode: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices('accessMode', 'https://schema.org/accessMode'),
        serialization_alias='https://schema.org/accessMode',
    )
    sd_license: Optional[
        Union[CreativeWork, AnyUrl, List[Union[CreativeWork, AnyUrl]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('sdLicense', 'https://schema.org/sdLicense'),
        serialization_alias='https://schema.org/sdLicense',
    )
    is_accessible_for_free: Optional[Union[bool, List[bool]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'isAccessibleForFree', 'https://schema.org/isAccessibleForFree'
        ),
        serialization_alias='https://schema.org/isAccessibleForFree',
    )
    learning_resource_type: Optional[
        Union[DefinedTerm, str, List[Union[DefinedTerm, str]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'learningResourceType', 'https://schema.org/learningResourceType'
        ),
        serialization_alias='https://schema.org/learningResourceType',
    )
    creator: Optional[
        Union[Person, Organization, List[Union[Person, Organization]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('creator', 'https://schema.org/creator'),
        serialization_alias='https://schema.org/creator',
    )
    country_of_origin: Optional[Union[Country, List[Country]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'countryOfOrigin', 'https://schema.org/countryOfOrigin'
        ),
        serialization_alias='https://schema.org/countryOfOrigin',
    )
    assesses: Optional[Union[DefinedTerm, str, List[Union[DefinedTerm, str]]]] = Field(
        default=None,
        validation_alias=AliasChoices('assesses', 'https://schema.org/assesses'),
        serialization_alias='https://schema.org/assesses',
    )
    interpreted_as_claim: Optional[Union[Claim, List[Claim]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'interpretedAsClaim', 'https://schema.org/interpretedAsClaim'
        ),
        serialization_alias='https://schema.org/interpretedAsClaim',
    )
    comment_count: Optional[Union[int, List[int]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'commentCount', 'https://schema.org/commentCount'
        ),
        serialization_alias='https://schema.org/commentCount',
    )
    audio: Optional[
        Union[
            AudioObject,
            MusicRecording,
            Clip,
            List[Union[AudioObject, MusicRecording, Clip]],
        ]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('audio', 'https://schema.org/audio'),
        serialization_alias='https://schema.org/audio',
    )
    reviews: Optional[Union[Review, List[Review]]] = Field(
        default=None,
        validation_alias=AliasChoices('reviews', 'https://schema.org/reviews'),
        serialization_alias='https://schema.org/reviews',
    )
    content_location: Optional[Union[Place, List[Place]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'contentLocation', 'https://schema.org/contentLocation'
        ),
        serialization_alias='https://schema.org/contentLocation',
    )
    publication: Optional[Union[PublicationEvent, List[PublicationEvent]]] = Field(
        default=None,
        validation_alias=AliasChoices('publication', 'https://schema.org/publication'),
        serialization_alias='https://schema.org/publication',
    )
    license: Optional[
        Union[CreativeWork, AnyUrl, List[Union[CreativeWork, AnyUrl]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('license', 'https://schema.org/license'),
        serialization_alias='https://schema.org/license',
    )
    position: Optional[Union[int, str, List[Union[int, str]]]] = Field(
        default=None,
        validation_alias=AliasChoices('position', 'https://schema.org/position'),
        serialization_alias='https://schema.org/position',
    )
    content_rating: Optional[Union[Rating, str, List[Union[Rating, str]]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'contentRating', 'https://schema.org/contentRating'
        ),
        serialization_alias='https://schema.org/contentRating',
    )
    word_count: Optional[Union[int, List[int]]] = Field(
        default=None,
        validation_alias=AliasChoices('wordCount', 'https://schema.org/wordCount'),
        serialization_alias='https://schema.org/wordCount',
    )
    interaction_statistic: Optional[
        Union[InteractionCounter, List[InteractionCounter]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'interactionStatistic', 'https://schema.org/interactionStatistic'
        ),
        serialization_alias='https://schema.org/interactionStatistic',
    )
    pattern: Optional[Union[DefinedTerm, str, List[Union[DefinedTerm, str]]]] = Field(
        default=None,
        validation_alias=AliasChoices('pattern', 'https://schema.org/pattern'),
        serialization_alias='https://schema.org/pattern',
    )
    accessibility_api: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'accessibilityAPI', 'https://schema.org/accessibilityAPI'
        ),
        serialization_alias='https://schema.org/accessibilityAPI',
    )
    usage_info: Optional[
        Union[CreativeWork, AnyUrl, List[Union[CreativeWork, AnyUrl]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('usageInfo', 'https://schema.org/usageInfo'),
        serialization_alias='https://schema.org/usageInfo',
    )
    credit_text: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices('creditText', 'https://schema.org/creditText'),
        serialization_alias='https://schema.org/creditText',
    )
    work_translation: Optional[Union[CreativeWork, List[CreativeWork]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'workTranslation', 'https://schema.org/workTranslation'
        ),
        serialization_alias='https://schema.org/workTranslation',
    )
    in_language: Optional[Union[str, Language, List[Union[str, Language]]]] = Field(
        default=None,
        validation_alias=AliasChoices('inLanguage', 'https://schema.org/inLanguage'),
        serialization_alias='https://schema.org/inLanguage',
    )
    sponsor: Optional[
        Union[Organization, Person, List[Union[Organization, Person]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('sponsor', 'https://schema.org/sponsor'),
        serialization_alias='https://schema.org/sponsor',
    )
    awards: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices('awards', 'https://schema.org/awards'),
        serialization_alias='https://schema.org/awards',
    )
    discussion_url: Optional[Union[AnyUrl, List[AnyUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'discussionUrl', 'https://schema.org/discussionUrl'
        ),
        serialization_alias='https://schema.org/discussionUrl',
    )
    accountable_person: Optional[Union[Person, List[Person]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'accountablePerson', 'https://schema.org/accountablePerson'
        ),
        serialization_alias='https://schema.org/accountablePerson',
    )
    conditions_of_access: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'conditionsOfAccess', 'https://schema.org/conditionsOfAccess'
        ),
        serialization_alias='https://schema.org/conditionsOfAccess',
    )
    encoding_format: Optional[Union[AnyUrl, str, List[Union[AnyUrl, str]]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'encodingFormat', 'https://schema.org/encodingFormat'
        ),
        serialization_alias='https://schema.org/encodingFormat',
    )
    publisher_imprint: Optional[Union[Organization, List[Organization]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'publisherImprint', 'https://schema.org/publisherImprint'
        ),
        serialization_alias='https://schema.org/publisherImprint',
    )
    accessibility_summary: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'accessibilitySummary', 'https://schema.org/accessibilitySummary'
        ),
        serialization_alias='https://schema.org/accessibilitySummary',
    )
    access_mode_sufficient: Optional[Union[ItemList, List[ItemList]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'accessModeSufficient', 'https://schema.org/accessModeSufficient'
        ),
        serialization_alias='https://schema.org/accessModeSufficient',
    )
    sd_date_published: Optional[Union[date, List[date]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'sdDatePublished', 'https://schema.org/sdDatePublished'
        ),
        serialization_alias='https://schema.org/sdDatePublished',
    )
    temporal_coverage: Optional[
        Union[AwareDatetime, str, AnyUrl, List[Union[AwareDatetime, str, AnyUrl]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'temporalCoverage', 'https://schema.org/temporalCoverage'
        ),
        serialization_alias='https://schema.org/temporalCoverage',
    )
    is_family_friendly: Optional[Union[bool, List[bool]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'isFamilyFriendly', 'https://schema.org/isFamilyFriendly'
        ),
        serialization_alias='https://schema.org/isFamilyFriendly',
    )
    acquire_license_page: Optional[
        Union[AnyUrl, CreativeWork, List[Union[AnyUrl, CreativeWork]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'acquireLicensePage', 'https://schema.org/acquireLicensePage'
        ),
        serialization_alias='https://schema.org/acquireLicensePage',
    )
    headline: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices('headline', 'https://schema.org/headline'),
        serialization_alias='https://schema.org/headline',
    )
    aggregate_rating: Optional[Union[AggregateRating, List[AggregateRating]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'aggregateRating', 'https://schema.org/aggregateRating'
        ),
        serialization_alias='https://schema.org/aggregateRating',
    )
    edit_eidr: Optional[Union[str, AnyUrl, List[Union[str, AnyUrl]]]] = Field(
        default=None,
        validation_alias=AliasChoices('editEIDR', 'https://schema.org/editEIDR'),
        serialization_alias='https://schema.org/editEIDR',
    )
    correction: Optional[
        Union[
            CorrectionComment, str, AnyUrl, List[Union[CorrectionComment, str, AnyUrl]]
        ]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('correction', 'https://schema.org/correction'),
        serialization_alias='https://schema.org/correction',
    )
    alternative_headline: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'alternativeHeadline', 'https://schema.org/alternativeHeadline'
        ),
        serialization_alias='https://schema.org/alternativeHeadline',
    )
    is_part_of: Optional[
        Union[AnyUrl, CreativeWork, List[Union[AnyUrl, CreativeWork]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('isPartOf', 'https://schema.org/isPartOf'),
        serialization_alias='https://schema.org/isPartOf',
    )
    version: Optional[Union[str, float, List[Union[str, float]]]] = Field(
        default=None,
        validation_alias=AliasChoices('version', 'https://schema.org/version'),
        serialization_alias='https://schema.org/version',
    )
    translation_of_work: Optional[Union[CreativeWork, List[CreativeWork]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'translationOfWork', 'https://schema.org/translationOfWork'
        ),
        serialization_alias='https://schema.org/translationOfWork',
    )
    copyright_holder: Optional[
        Union[Person, Organization, List[Union[Person, Organization]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'copyrightHolder', 'https://schema.org/copyrightHolder'
        ),
        serialization_alias='https://schema.org/copyrightHolder',
    )
    has_part: Optional[Union[CreativeWork, List[CreativeWork]]] = Field(
        default=None,
        validation_alias=AliasChoices('hasPart', 'https://schema.org/hasPart'),
        serialization_alias='https://schema.org/hasPart',
    )
    source_organization: Optional[Union[Organization, List[Organization]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'sourceOrganization', 'https://schema.org/sourceOrganization'
        ),
        serialization_alias='https://schema.org/sourceOrganization',
    )
    thumbnail: Optional[Union[ImageObject, List[ImageObject]]] = Field(
        default=None,
        validation_alias=AliasChoices('thumbnail', 'https://schema.org/thumbnail'),
        serialization_alias='https://schema.org/thumbnail',
    )
    about: Optional[Union[Thing, List[Thing]]] = Field(
        default=None,
        validation_alias=AliasChoices('about', 'https://schema.org/about'),
        serialization_alias='https://schema.org/about',
    )
    accessibility_control: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'accessibilityControl', 'https://schema.org/accessibilityControl'
        ),
        serialization_alias='https://schema.org/accessibilityControl',
    )
    mentions: Optional[Union[Thing, List[Thing]]] = Field(
        default=None,
        validation_alias=AliasChoices('mentions', 'https://schema.org/mentions'),
        serialization_alias='https://schema.org/mentions',
    )
    archived_at: Optional[Union[AnyUrl, WebPage, List[Union[AnyUrl, WebPage]]]] = Field(
        default=None,
        validation_alias=AliasChoices('archivedAt', 'https://schema.org/archivedAt'),
        serialization_alias='https://schema.org/archivedAt',
    )
    genre: Optional[Union[AnyUrl, str, List[Union[AnyUrl, str]]]] = Field(
        default=None,
        validation_alias=AliasChoices('genre', 'https://schema.org/genre'),
        serialization_alias='https://schema.org/genre',
    )
    copyright_year: Optional[Union[int, List[int]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'copyrightYear', 'https://schema.org/copyrightYear'
        ),
        serialization_alias='https://schema.org/copyrightYear',
    )
    funder: Optional[
        Union[Organization, Person, List[Union[Organization, Person]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('funder', 'https://schema.org/funder'),
        serialization_alias='https://schema.org/funder',
    )
    time_required: Optional[Union[Duration, List[Duration]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'timeRequired', 'https://schema.org/timeRequired'
        ),
        serialization_alias='https://schema.org/timeRequired',
    )
    publisher: Optional[
        Union[Person, Organization, List[Union[Person, Organization]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('publisher', 'https://schema.org/publisher'),
        serialization_alias='https://schema.org/publisher',
    )
    video: Optional[Union[VideoObject, Clip, List[Union[VideoObject, Clip]]]] = Field(
        default=None,
        validation_alias=AliasChoices('video', 'https://schema.org/video'),
        serialization_alias='https://schema.org/video',
    )
    accessibility_feature: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'accessibilityFeature', 'https://schema.org/accessibilityFeature'
        ),
        serialization_alias='https://schema.org/accessibilityFeature',
    )
    keywords: Optional[
        Union[str, AnyUrl, DefinedTerm, List[Union[str, AnyUrl, DefinedTerm]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('keywords', 'https://schema.org/keywords'),
        serialization_alias='https://schema.org/keywords',
    )
    award: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices('award', 'https://schema.org/award'),
        serialization_alias='https://schema.org/award',
    )
    translator: Optional[
        Union[Person, Organization, List[Union[Person, Organization]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('translator', 'https://schema.org/translator'),
        serialization_alias='https://schema.org/translator',
    )
    creative_work_status: Optional[
        Union[DefinedTerm, str, List[Union[DefinedTerm, str]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'creativeWorkStatus', 'https://schema.org/creativeWorkStatus'
        ),
        serialization_alias='https://schema.org/creativeWorkStatus',
    )
    expires: Optional[
        Union[date, AwareDatetime, List[Union[date, AwareDatetime]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('expires', 'https://schema.org/expires'),
        serialization_alias='https://schema.org/expires',
    )
    abstract: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices('abstract', 'https://schema.org/abstract'),
        serialization_alias='https://schema.org/abstract',
    )
    spatial_coverage: Optional[Union[Place, List[Place]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'spatialCoverage', 'https://schema.org/spatialCoverage'
        ),
        serialization_alias='https://schema.org/spatialCoverage',
    )
    material_extent: Optional[
        Union[str, QuantitativeValue, List[Union[str, QuantitativeValue]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'materialExtent', 'https://schema.org/materialExtent'
        ),
        serialization_alias='https://schema.org/materialExtent',
    )
    accessibility_hazard: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'accessibilityHazard', 'https://schema.org/accessibilityHazard'
        ),
        serialization_alias='https://schema.org/accessibilityHazard',
    )
    associated_media: Optional[Union[MediaObject, List[MediaObject]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'associatedMedia', 'https://schema.org/associatedMedia'
        ),
        serialization_alias='https://schema.org/associatedMedia',
    )
    content_reference_time: Optional[Union[AwareDatetime, List[AwareDatetime]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'contentReferenceTime', 'https://schema.org/contentReferenceTime'
        ),
        serialization_alias='https://schema.org/contentReferenceTime',
    )
    offers: Optional[Union[Demand, Offer, List[Union[Demand, Offer]]]] = Field(
        default=None,
        validation_alias=AliasChoices('offers', 'https://schema.org/offers'),
        serialization_alias='https://schema.org/offers',
    )
    producer: Optional[
        Union[Person, Organization, List[Union[Person, Organization]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('producer', 'https://schema.org/producer'),
        serialization_alias='https://schema.org/producer',
    )
    audience: Optional[Union[Audience, List[Audience]]] = Field(
        default=None,
        validation_alias=AliasChoices('audience', 'https://schema.org/audience'),
        serialization_alias='https://schema.org/audience',
    )
    date_created: Optional[
        Union[date, AwareDatetime, List[Union[date, AwareDatetime]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('dateCreated', 'https://schema.org/dateCreated'),
        serialization_alias='https://schema.org/dateCreated',
    )
    funding: Optional[Union[Grant, List[Grant]]] = Field(
        default=None,
        validation_alias=AliasChoices('funding', 'https://schema.org/funding'),
        serialization_alias='https://schema.org/funding',
    )
    is_based_on: Optional[
        Union[Product, CreativeWork, AnyUrl, List[Union[Product, CreativeWork, AnyUrl]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('isBasedOn', 'https://schema.org/isBasedOn'),
        serialization_alias='https://schema.org/isBasedOn',
    )
    educational_level: Optional[
        Union[str, AnyUrl, DefinedTerm, List[Union[str, AnyUrl, DefinedTerm]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'educationalLevel', 'https://schema.org/educationalLevel'
        ),
        serialization_alias='https://schema.org/educationalLevel',
    )
    main_entity: Optional[Union[Thing, List[Thing]]] = Field(
        default=None,
        validation_alias=AliasChoices('mainEntity', 'https://schema.org/mainEntity'),
        serialization_alias='https://schema.org/mainEntity',
    )
    thumbnail_url: Optional[Union[AnyUrl, List[AnyUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'thumbnailUrl', 'https://schema.org/thumbnailUrl'
        ),
        serialization_alias='https://schema.org/thumbnailUrl',
    )
    author: Optional[
        Union[Person, Organization, List[Union[Person, Organization]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('author', 'https://schema.org/author'),
        serialization_alias='https://schema.org/author',
    )
    released_event: Optional[Union[PublicationEvent, List[PublicationEvent]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'releasedEvent', 'https://schema.org/releasedEvent'
        ),
        serialization_alias='https://schema.org/releasedEvent',
    )
    recorded_at: Optional[Union[Event, List[Event]]] = Field(
        default=None,
        validation_alias=AliasChoices('recordedAt', 'https://schema.org/recordedAt'),
        serialization_alias='https://schema.org/recordedAt',
    )
    schema_version: Optional[Union[str, AnyUrl, List[Union[str, AnyUrl]]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'schemaVersion', 'https://schema.org/schemaVersion'
        ),
        serialization_alias='https://schema.org/schemaVersion',
    )
    material: Optional[
        Union[str, Product, AnyUrl, List[Union[str, Product, AnyUrl]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('material', 'https://schema.org/material'),
        serialization_alias='https://schema.org/material',
    )
    digital_source_type: Optional[
        Union[IPTCDigitalSourceEnumeration, List[IPTCDigitalSourceEnumeration]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'digitalSourceType', 'https://schema.org/digitalSourceType'
        ),
        serialization_alias='https://schema.org/digitalSourceType',
    )
    example_of_work: Optional[Union[CreativeWork, List[CreativeWork]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'exampleOfWork', 'https://schema.org/exampleOfWork'
        ),
        serialization_alias='https://schema.org/exampleOfWork',
    )
    publishing_principles: Optional[
        Union[CreativeWork, AnyUrl, List[Union[CreativeWork, AnyUrl]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'publishingPrinciples', 'https://schema.org/publishingPrinciples'
        ),
        serialization_alias='https://schema.org/publishingPrinciples',
    )
    date_published: Optional[
        Union[date, AwareDatetime, List[Union[date, AwareDatetime]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'datePublished', 'https://schema.org/datePublished'
        ),
        serialization_alias='https://schema.org/datePublished',
    )
    temporal: Optional[
        Union[str, AwareDatetime, List[Union[str, AwareDatetime]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('temporal', 'https://schema.org/temporal'),
        serialization_alias='https://schema.org/temporal',
    )
    interactivity_type: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'interactivityType', 'https://schema.org/interactivityType'
        ),
        serialization_alias='https://schema.org/interactivityType',
    )
    contributor: Optional[
        Union[Organization, Person, List[Union[Organization, Person]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('contributor', 'https://schema.org/contributor'),
        serialization_alias='https://schema.org/contributor',
    )
    file_format: Optional[Union[str, AnyUrl, List[Union[str, AnyUrl]]]] = Field(
        default=None,
        validation_alias=AliasChoices('fileFormat', 'https://schema.org/fileFormat'),
        serialization_alias='https://schema.org/fileFormat',
    )
    size: Optional[
        Union[
            DefinedTerm,
            str,
            SizeSpecification,
            QuantitativeValue,
            List[Union[DefinedTerm, str, SizeSpecification, QuantitativeValue]],
        ]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('size', 'https://schema.org/size'),
        serialization_alias='https://schema.org/size',
    )
    sd_publisher: Optional[
        Union[Person, Organization, List[Union[Person, Organization]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('sdPublisher', 'https://schema.org/sdPublisher'),
        serialization_alias='https://schema.org/sdPublisher',
    )
    character: Optional[Union[Person, List[Person]]] = Field(
        default=None,
        validation_alias=AliasChoices('character', 'https://schema.org/character'),
        serialization_alias='https://schema.org/character',
    )
    text: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices('text', 'https://schema.org/text'),
        serialization_alias='https://schema.org/text',
    )
    educational_alignment: Optional[
        Union[AlignmentObject, List[AlignmentObject]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'educationalAlignment', 'https://schema.org/educationalAlignment'
        ),
        serialization_alias='https://schema.org/educationalAlignment',
    )
    spatial: Optional[Union[Place, List[Place]]] = Field(
        default=None,
        validation_alias=AliasChoices('spatial', 'https://schema.org/spatial'),
        serialization_alias='https://schema.org/spatial',
    )
    work_example: Optional[Union[CreativeWork, List[CreativeWork]]] = Field(
        default=None,
        validation_alias=AliasChoices('workExample', 'https://schema.org/workExample'),
        serialization_alias='https://schema.org/workExample',
    )
    citation: Optional[
        Union[str, CreativeWork, List[Union[str, CreativeWork]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('citation', 'https://schema.org/citation'),
        serialization_alias='https://schema.org/citation',
    )
    review: Optional[Union[Review, List[Review]]] = Field(
        default=None,
        validation_alias=AliasChoices('review', 'https://schema.org/review'),
        serialization_alias='https://schema.org/review',
    )
    maintainer: Optional[
        Union[Person, Organization, List[Union[Person, Organization]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('maintainer', 'https://schema.org/maintainer'),
        serialization_alias='https://schema.org/maintainer',
    )
    teaches: Optional[Union[DefinedTerm, str, List[Union[DefinedTerm, str]]]] = Field(
        default=None,
        validation_alias=AliasChoices('teaches', 'https://schema.org/teaches'),
        serialization_alias='https://schema.org/teaches',
    )
    typical_age_range: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'typicalAgeRange', 'https://schema.org/typicalAgeRange'
        ),
        serialization_alias='https://schema.org/typicalAgeRange',
    )
    editor: Optional[Union[Person, List[Person]]] = Field(
        default=None,
        validation_alias=AliasChoices('editor', 'https://schema.org/editor'),
        serialization_alias='https://schema.org/editor',
    )
    encoding: Optional[Union[MediaObject, List[MediaObject]]] = Field(
        default=None,
        validation_alias=AliasChoices('encoding', 'https://schema.org/encoding'),
        serialization_alias='https://schema.org/encoding',
    )
    encodings: Optional[Union[MediaObject, List[MediaObject]]] = Field(
        default=None,
        validation_alias=AliasChoices('encodings', 'https://schema.org/encodings'),
        serialization_alias='https://schema.org/encodings',
    )
    comment: Optional[Union[Comment, List[Comment]]] = Field(
        default=None,
        validation_alias=AliasChoices('comment', 'https://schema.org/comment'),
        serialization_alias='https://schema.org/comment',
    )
    copyright_notice: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'copyrightNotice', 'https://schema.org/copyrightNotice'
        ),
        serialization_alias='https://schema.org/copyrightNotice',
    )
    date_modified: Optional[
        Union[AwareDatetime, date, List[Union[AwareDatetime, date]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'dateModified', 'https://schema.org/dateModified'
        ),
        serialization_alias='https://schema.org/dateModified',
    )
    location_created: Optional[Union[Place, List[Place]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'locationCreated', 'https://schema.org/locationCreated'
        ),
        serialization_alias='https://schema.org/locationCreated',
    )
    provider: Optional[
        Union[Person, Organization, List[Union[Person, Organization]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('provider', 'https://schema.org/provider'),
        serialization_alias='https://schema.org/provider',
    )
    is_based_on_url: Optional[
        Union[Product, CreativeWork, AnyUrl, List[Union[Product, CreativeWork, AnyUrl]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'isBasedOnUrl', 'https://schema.org/isBasedOnUrl'
        ),
        serialization_alias='https://schema.org/isBasedOnUrl',
    )


class Person(Thing):
    field_type: Literal['https://schema.org/Person'] = Field(
        'https://schema.org/Person', alias='@type'
    )
    knows_language: Optional[Union[str, Language, List[Union[str, Language]]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'knowsLanguage', 'https://schema.org/knowsLanguage'
        ),
        serialization_alias='https://schema.org/knowsLanguage',
    )
    gender: Optional[Union[GenderType, str, List[Union[GenderType, str]]]] = Field(
        default=None,
        validation_alias=AliasChoices('gender', 'https://schema.org/gender'),
        serialization_alias='https://schema.org/gender',
    )
    fax_number: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices('faxNumber', 'https://schema.org/faxNumber'),
        serialization_alias='https://schema.org/faxNumber',
    )
    global_location_number: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'globalLocationNumber', 'https://schema.org/globalLocationNumber'
        ),
        serialization_alias='https://schema.org/globalLocationNumber',
    )
    sponsor: Optional[
        Union[Organization, Person, List[Union[Organization, Person]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('sponsor', 'https://schema.org/sponsor'),
        serialization_alias='https://schema.org/sponsor',
    )
    death_place: Optional[Union[Place, List[Place]]] = Field(
        default=None,
        validation_alias=AliasChoices('deathPlace', 'https://schema.org/deathPlace'),
        serialization_alias='https://schema.org/deathPlace',
    )
    follows: Optional[Union[Person, List[Person]]] = Field(
        default=None,
        validation_alias=AliasChoices('follows', 'https://schema.org/follows'),
        serialization_alias='https://schema.org/follows',
    )
    sibling: Optional[Union[Person, List[Person]]] = Field(
        default=None,
        validation_alias=AliasChoices('sibling', 'https://schema.org/sibling'),
        serialization_alias='https://schema.org/sibling',
    )
    has_offer_catalog: Optional[Union[OfferCatalog, List[OfferCatalog]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'hasOfferCatalog', 'https://schema.org/hasOfferCatalog'
        ),
        serialization_alias='https://schema.org/hasOfferCatalog',
    )
    has_certification: Optional[Union[Certification, List[Certification]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'hasCertification', 'https://schema.org/hasCertification'
        ),
        serialization_alias='https://schema.org/hasCertification',
    )
    home_location: Optional[
        Union[Place, ContactPoint, List[Union[Place, ContactPoint]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'homeLocation', 'https://schema.org/homeLocation'
        ),
        serialization_alias='https://schema.org/homeLocation',
    )
    alumni_of: Optional[
        Union[
            Organization,
            EducationalOrganization,
            List[Union[Organization, EducationalOrganization]],
        ]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('alumniOf', 'https://schema.org/alumniOf'),
        serialization_alias='https://schema.org/alumniOf',
    )
    family_name: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices('familyName', 'https://schema.org/familyName'),
        serialization_alias='https://schema.org/familyName',
    )
    birth_date: Optional[Union[date, List[date]]] = Field(
        default=None,
        validation_alias=AliasChoices('birthDate', 'https://schema.org/birthDate'),
        serialization_alias='https://schema.org/birthDate',
    )
    owns: Optional[
        Union[Product, OwnershipInfo, List[Union[Product, OwnershipInfo]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('owns', 'https://schema.org/owns'),
        serialization_alias='https://schema.org/owns',
    )
    member_of: Optional[
        Union[
            Organization,
            MemberProgramTier,
            ProgramMembership,
            List[Union[Organization, MemberProgramTier, ProgramMembership]],
        ]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('memberOf', 'https://schema.org/memberOf'),
        serialization_alias='https://schema.org/memberOf',
    )
    interaction_statistic: Optional[
        Union[InteractionCounter, List[InteractionCounter]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'interactionStatistic', 'https://schema.org/interactionStatistic'
        ),
        serialization_alias='https://schema.org/interactionStatistic',
    )
    vat_id: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices('vatID', 'https://schema.org/vatID'),
        serialization_alias='https://schema.org/vatID',
    )
    awards: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices('awards', 'https://schema.org/awards'),
        serialization_alias='https://schema.org/awards',
    )
    job_title: Optional[Union[DefinedTerm, str, List[Union[DefinedTerm, str]]]] = Field(
        default=None,
        validation_alias=AliasChoices('jobTitle', 'https://schema.org/jobTitle'),
        serialization_alias='https://schema.org/jobTitle',
    )
    funder: Optional[
        Union[Organization, Person, List[Union[Organization, Person]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('funder', 'https://schema.org/funder'),
        serialization_alias='https://schema.org/funder',
    )
    death_date: Optional[Union[date, List[date]]] = Field(
        default=None,
        validation_alias=AliasChoices('deathDate', 'https://schema.org/deathDate'),
        serialization_alias='https://schema.org/deathDate',
    )
    spouse: Optional[Union[Person, List[Person]]] = Field(
        default=None,
        validation_alias=AliasChoices('spouse', 'https://schema.org/spouse'),
        serialization_alias='https://schema.org/spouse',
    )
    honorific_prefix: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'honorificPrefix', 'https://schema.org/honorificPrefix'
        ),
        serialization_alias='https://schema.org/honorificPrefix',
    )
    email: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices('email', 'https://schema.org/email'),
        serialization_alias='https://schema.org/email',
    )
    net_worth: Optional[
        Union[
            PriceSpecification,
            MonetaryAmount,
            List[Union[PriceSpecification, MonetaryAmount]],
        ]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('netWorth', 'https://schema.org/netWorth'),
        serialization_alias='https://schema.org/netWorth',
    )
    siblings: Optional[Union[Person, List[Person]]] = Field(
        default=None,
        validation_alias=AliasChoices('siblings', 'https://schema.org/siblings'),
        serialization_alias='https://schema.org/siblings',
    )
    colleagues: Optional[Union[Person, List[Person]]] = Field(
        default=None,
        validation_alias=AliasChoices('colleagues', 'https://schema.org/colleagues'),
        serialization_alias='https://schema.org/colleagues',
    )
    seeks: Optional[Union[Demand, List[Demand]]] = Field(
        default=None,
        validation_alias=AliasChoices('seeks', 'https://schema.org/seeks'),
        serialization_alias='https://schema.org/seeks',
    )
    nationality: Optional[Union[Country, List[Country]]] = Field(
        default=None,
        validation_alias=AliasChoices('nationality', 'https://schema.org/nationality'),
        serialization_alias='https://schema.org/nationality',
    )
    has_credential: Optional[
        Union[
            EducationalOccupationalCredential, List[EducationalOccupationalCredential]
        ]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'hasCredential', 'https://schema.org/hasCredential'
        ),
        serialization_alias='https://schema.org/hasCredential',
    )
    funding: Optional[Union[Grant, List[Grant]]] = Field(
        default=None,
        validation_alias=AliasChoices('funding', 'https://schema.org/funding'),
        serialization_alias='https://schema.org/funding',
    )
    agent_interaction_statistic: Optional[
        Union[InteractionCounter, List[InteractionCounter]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'agentInteractionStatistic', 'https://schema.org/agentInteractionStatistic'
        ),
        serialization_alias='https://schema.org/agentInteractionStatistic',
    )
    naics: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices('naics', 'https://schema.org/naics'),
        serialization_alias='https://schema.org/naics',
    )
    colleague: Optional[Union[Person, AnyUrl, List[Union[Person, AnyUrl]]]] = Field(
        default=None,
        validation_alias=AliasChoices('colleague', 'https://schema.org/colleague'),
        serialization_alias='https://schema.org/colleague',
    )
    given_name: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices('givenName', 'https://schema.org/givenName'),
        serialization_alias='https://schema.org/givenName',
    )
    works_for: Optional[Union[Organization, List[Organization]]] = Field(
        default=None,
        validation_alias=AliasChoices('worksFor', 'https://schema.org/worksFor'),
        serialization_alias='https://schema.org/worksFor',
    )
    additional_name: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'additionalName', 'https://schema.org/additionalName'
        ),
        serialization_alias='https://schema.org/additionalName',
    )
    has_occupation: Optional[Union[Occupation, List[Occupation]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'hasOccupation', 'https://schema.org/hasOccupation'
        ),
        serialization_alias='https://schema.org/hasOccupation',
    )
    knows: Optional[Union[Person, List[Person]]] = Field(
        default=None,
        validation_alias=AliasChoices('knows', 'https://schema.org/knows'),
        serialization_alias='https://schema.org/knows',
    )
    award: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices('award', 'https://schema.org/award'),
        serialization_alias='https://schema.org/award',
    )
    parents: Optional[Union[Person, List[Person]]] = Field(
        default=None,
        validation_alias=AliasChoices('parents', 'https://schema.org/parents'),
        serialization_alias='https://schema.org/parents',
    )
    address: Optional[
        Union[str, PostalAddress, List[Union[str, PostalAddress]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('address', 'https://schema.org/address'),
        serialization_alias='https://schema.org/address',
    )
    height: Optional[
        Union[Distance, QuantitativeValue, List[Union[Distance, QuantitativeValue]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('height', 'https://schema.org/height'),
        serialization_alias='https://schema.org/height',
    )
    tax_id: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices('taxID', 'https://schema.org/taxID'),
        serialization_alias='https://schema.org/taxID',
    )
    weight: Optional[
        Union[QuantitativeValue, Mass, List[Union[QuantitativeValue, Mass]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('weight', 'https://schema.org/weight'),
        serialization_alias='https://schema.org/weight',
    )
    children: Optional[Union[Person, List[Person]]] = Field(
        default=None,
        validation_alias=AliasChoices('children', 'https://schema.org/children'),
        serialization_alias='https://schema.org/children',
    )
    performer_in: Optional[Union[Event, List[Event]]] = Field(
        default=None,
        validation_alias=AliasChoices('performerIn', 'https://schema.org/performerIn'),
        serialization_alias='https://schema.org/performerIn',
    )
    pronouns: Optional[
        Union[
            str,
            StructuredValue,
            DefinedTerm,
            List[Union[str, StructuredValue, DefinedTerm]],
        ]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('pronouns', 'https://schema.org/pronouns'),
        serialization_alias='https://schema.org/pronouns',
    )
    knows_about: Optional[
        Union[str, Thing, AnyUrl, List[Union[str, Thing, AnyUrl]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('knowsAbout', 'https://schema.org/knowsAbout'),
        serialization_alias='https://schema.org/knowsAbout',
    )
    telephone: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices('telephone', 'https://schema.org/telephone'),
        serialization_alias='https://schema.org/telephone',
    )
    call_sign: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices('callSign', 'https://schema.org/callSign'),
        serialization_alias='https://schema.org/callSign',
    )
    brand: Optional[
        Union[Organization, Brand, List[Union[Organization, Brand]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('brand', 'https://schema.org/brand'),
        serialization_alias='https://schema.org/brand',
    )
    contact_points: Optional[Union[ContactPoint, List[ContactPoint]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'contactPoints', 'https://schema.org/contactPoints'
        ),
        serialization_alias='https://schema.org/contactPoints',
    )
    work_location: Optional[
        Union[ContactPoint, Place, List[Union[ContactPoint, Place]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'workLocation', 'https://schema.org/workLocation'
        ),
        serialization_alias='https://schema.org/workLocation',
    )
    makes_offer: Optional[Union[Offer, List[Offer]]] = Field(
        default=None,
        validation_alias=AliasChoices('makesOffer', 'https://schema.org/makesOffer'),
        serialization_alias='https://schema.org/makesOffer',
    )
    birth_place: Optional[Union[Place, List[Place]]] = Field(
        default=None,
        validation_alias=AliasChoices('birthPlace', 'https://schema.org/birthPlace'),
        serialization_alias='https://schema.org/birthPlace',
    )
    publishing_principles: Optional[
        Union[CreativeWork, AnyUrl, List[Union[CreativeWork, AnyUrl]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'publishingPrinciples', 'https://schema.org/publishingPrinciples'
        ),
        serialization_alias='https://schema.org/publishingPrinciples',
    )
    isic_v4: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices('isicV4', 'https://schema.org/isicV4'),
        serialization_alias='https://schema.org/isicV4',
    )
    honorific_suffix: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'honorificSuffix', 'https://schema.org/honorificSuffix'
        ),
        serialization_alias='https://schema.org/honorificSuffix',
    )
    duns: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices('duns', 'https://schema.org/duns'),
        serialization_alias='https://schema.org/duns',
    )
    has_pos: Optional[Union[Place, List[Place]]] = Field(
        default=None,
        validation_alias=AliasChoices('hasPOS', 'https://schema.org/hasPOS'),
        serialization_alias='https://schema.org/hasPOS',
    )
    skills: Optional[Union[DefinedTerm, str, List[Union[DefinedTerm, str]]]] = Field(
        default=None,
        validation_alias=AliasChoices('skills', 'https://schema.org/skills'),
        serialization_alias='https://schema.org/skills',
    )
    related_to: Optional[Union[Person, List[Person]]] = Field(
        default=None,
        validation_alias=AliasChoices('relatedTo', 'https://schema.org/relatedTo'),
        serialization_alias='https://schema.org/relatedTo',
    )
    contact_point: Optional[Union[ContactPoint, List[ContactPoint]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'contactPoint', 'https://schema.org/contactPoint'
        ),
        serialization_alias='https://schema.org/contactPoint',
    )
    affiliation: Optional[Union[Organization, List[Organization]]] = Field(
        default=None,
        validation_alias=AliasChoices('affiliation', 'https://schema.org/affiliation'),
        serialization_alias='https://schema.org/affiliation',
    )
    parent: Optional[Union[Person, List[Person]]] = Field(
        default=None,
        validation_alias=AliasChoices('parent', 'https://schema.org/parent'),
        serialization_alias='https://schema.org/parent',
    )


class Organization(Thing):
    field_type: Literal['https://schema.org/Organization'] = Field(
        'https://schema.org/Organization', alias='@type'
    )
    knows_about: Optional[
        Union[str, Thing, AnyUrl, List[Union[str, Thing, AnyUrl]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('knowsAbout', 'https://schema.org/knowsAbout'),
        serialization_alias='https://schema.org/knowsAbout',
    )
    employees: Optional[Union[Person, List[Person]]] = Field(
        default=None,
        validation_alias=AliasChoices('employees', 'https://schema.org/employees'),
        serialization_alias='https://schema.org/employees',
    )
    iso6523_code: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices('iso6523Code', 'https://schema.org/iso6523Code'),
        serialization_alias='https://schema.org/iso6523Code',
    )
    telephone: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices('telephone', 'https://schema.org/telephone'),
        serialization_alias='https://schema.org/telephone',
    )
    accepted_payment_method: Optional[
        Union[
            str,
            PaymentMethod,
            LoanOrCredit,
            List[Union[str, PaymentMethod, LoanOrCredit]],
        ]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'acceptedPaymentMethod', 'https://schema.org/acceptedPaymentMethod'
        ),
        serialization_alias='https://schema.org/acceptedPaymentMethod',
    )
    brand: Optional[
        Union[Organization, Brand, List[Union[Organization, Brand]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('brand', 'https://schema.org/brand'),
        serialization_alias='https://schema.org/brand',
    )
    member: Optional[
        Union[Person, Organization, List[Union[Person, Organization]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('member', 'https://schema.org/member'),
        serialization_alias='https://schema.org/member',
    )
    contact_points: Optional[Union[ContactPoint, List[ContactPoint]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'contactPoints', 'https://schema.org/contactPoints'
        ),
        serialization_alias='https://schema.org/contactPoints',
    )
    review: Optional[Union[Review, List[Review]]] = Field(
        default=None,
        validation_alias=AliasChoices('review', 'https://schema.org/review'),
        serialization_alias='https://schema.org/review',
    )
    has_member_program: Optional[Union[MemberProgram, List[MemberProgram]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'hasMemberProgram', 'https://schema.org/hasMemberProgram'
        ),
        serialization_alias='https://schema.org/hasMemberProgram',
    )
    has_shipping_service: Optional[
        Union[ShippingService, List[ShippingService]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'hasShippingService', 'https://schema.org/hasShippingService'
        ),
        serialization_alias='https://schema.org/hasShippingService',
    )
    publishing_principles: Optional[
        Union[CreativeWork, AnyUrl, List[Union[CreativeWork, AnyUrl]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'publishingPrinciples', 'https://schema.org/publishingPrinciples'
        ),
        serialization_alias='https://schema.org/publishingPrinciples',
    )
    department: Optional[Union[Organization, List[Organization]]] = Field(
        default=None,
        validation_alias=AliasChoices('department', 'https://schema.org/department'),
        serialization_alias='https://schema.org/department',
    )
    isic_v4: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices('isicV4', 'https://schema.org/isicV4'),
        serialization_alias='https://schema.org/isicV4',
    )
    duns: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices('duns', 'https://schema.org/duns'),
        serialization_alias='https://schema.org/duns',
    )
    has_pos: Optional[Union[Place, List[Place]]] = Field(
        default=None,
        validation_alias=AliasChoices('hasPOS', 'https://schema.org/hasPOS'),
        serialization_alias='https://schema.org/hasPOS',
    )
    skills: Optional[Union[DefinedTerm, str, List[Union[DefinedTerm, str]]]] = Field(
        default=None,
        validation_alias=AliasChoices('skills', 'https://schema.org/skills'),
        serialization_alias='https://schema.org/skills',
    )
    sub_organization: Optional[Union[Organization, List[Organization]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'subOrganization', 'https://schema.org/subOrganization'
        ),
        serialization_alias='https://schema.org/subOrganization',
    )
    has_merchant_return_policy: Optional[
        Union[MerchantReturnPolicy, List[MerchantReturnPolicy]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'hasMerchantReturnPolicy', 'https://schema.org/hasMerchantReturnPolicy'
        ),
        serialization_alias='https://schema.org/hasMerchantReturnPolicy',
    )
    ownership_funding_info: Optional[
        Union[
            str,
            CreativeWork,
            AnyUrl,
            AboutPage,
            List[Union[str, CreativeWork, AnyUrl, AboutPage]],
        ]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'ownershipFundingInfo', 'https://schema.org/ownershipFundingInfo'
        ),
        serialization_alias='https://schema.org/ownershipFundingInfo',
    )
    knows_language: Optional[Union[str, Language, List[Union[str, Language]]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'knowsLanguage', 'https://schema.org/knowsLanguage'
        ),
        serialization_alias='https://schema.org/knowsLanguage',
    )
    makes_offer: Optional[Union[Offer, List[Offer]]] = Field(
        default=None,
        validation_alias=AliasChoices('makesOffer', 'https://schema.org/makesOffer'),
        serialization_alias='https://schema.org/makesOffer',
    )
    fax_number: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices('faxNumber', 'https://schema.org/faxNumber'),
        serialization_alias='https://schema.org/faxNumber',
    )
    ethics_policy: Optional[
        Union[CreativeWork, AnyUrl, List[Union[CreativeWork, AnyUrl]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'ethicsPolicy', 'https://schema.org/ethicsPolicy'
        ),
        serialization_alias='https://schema.org/ethicsPolicy',
    )
    global_location_number: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'globalLocationNumber', 'https://schema.org/globalLocationNumber'
        ),
        serialization_alias='https://schema.org/globalLocationNumber',
    )
    sponsor: Optional[
        Union[Organization, Person, List[Union[Organization, Person]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('sponsor', 'https://schema.org/sponsor'),
        serialization_alias='https://schema.org/sponsor',
    )
    event: Optional[Union[Event, List[Event]]] = Field(
        default=None,
        validation_alias=AliasChoices('event', 'https://schema.org/event'),
        serialization_alias='https://schema.org/event',
    )
    owns: Optional[
        Union[Product, OwnershipInfo, List[Union[Product, OwnershipInfo]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('owns', 'https://schema.org/owns'),
        serialization_alias='https://schema.org/owns',
    )
    reviews: Optional[Union[Review, List[Review]]] = Field(
        default=None,
        validation_alias=AliasChoices('reviews', 'https://schema.org/reviews'),
        serialization_alias='https://schema.org/reviews',
    )
    nonprofit_status: Optional[Union[NonprofitType, List[NonprofitType]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'nonprofitStatus', 'https://schema.org/nonprofitStatus'
        ),
        serialization_alias='https://schema.org/nonprofitStatus',
    )
    aggregate_rating: Optional[Union[AggregateRating, List[AggregateRating]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'aggregateRating', 'https://schema.org/aggregateRating'
        ),
        serialization_alias='https://schema.org/aggregateRating',
    )
    dissolution_date: Optional[Union[date, List[date]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'dissolutionDate', 'https://schema.org/dissolutionDate'
        ),
        serialization_alias='https://schema.org/dissolutionDate',
    )
    area_served: Optional[
        Union[
            GeoShape,
            str,
            AdministrativeArea,
            Place,
            List[Union[GeoShape, str, AdministrativeArea, Place]],
        ]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('areaServed', 'https://schema.org/areaServed'),
        serialization_alias='https://schema.org/areaServed',
    )
    member_of: Optional[
        Union[
            Organization,
            MemberProgramTier,
            ProgramMembership,
            List[Union[Organization, MemberProgramTier, ProgramMembership]],
        ]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('memberOf', 'https://schema.org/memberOf'),
        serialization_alias='https://schema.org/memberOf',
    )
    contact_point: Optional[Union[ContactPoint, List[ContactPoint]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'contactPoint', 'https://schema.org/contactPoint'
        ),
        serialization_alias='https://schema.org/contactPoint',
    )
    founder: Optional[
        Union[Organization, Person, List[Union[Organization, Person]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('founder', 'https://schema.org/founder'),
        serialization_alias='https://schema.org/founder',
    )
    interaction_statistic: Optional[
        Union[InteractionCounter, List[InteractionCounter]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'interactionStatistic', 'https://schema.org/interactionStatistic'
        ),
        serialization_alias='https://schema.org/interactionStatistic',
    )
    legal_address: Optional[Union[PostalAddress, List[PostalAddress]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'legalAddress', 'https://schema.org/legalAddress'
        ),
        serialization_alias='https://schema.org/legalAddress',
    )
    vat_id: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices('vatID', 'https://schema.org/vatID'),
        serialization_alias='https://schema.org/vatID',
    )
    parent_organization: Optional[Union[Organization, List[Organization]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'parentOrganization', 'https://schema.org/parentOrganization'
        ),
        serialization_alias='https://schema.org/parentOrganization',
    )
    awards: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices('awards', 'https://schema.org/awards'),
        serialization_alias='https://schema.org/awards',
    )
    location: Optional[
        Union[
            VirtualLocation,
            PostalAddress,
            str,
            Place,
            List[Union[VirtualLocation, PostalAddress, str, Place]],
        ]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('location', 'https://schema.org/location'),
        serialization_alias='https://schema.org/location',
    )
    actionable_feedback_policy: Optional[
        Union[CreativeWork, AnyUrl, List[Union[CreativeWork, AnyUrl]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'actionableFeedbackPolicy', 'https://schema.org/actionableFeedbackPolicy'
        ),
        serialization_alias='https://schema.org/actionableFeedbackPolicy',
    )
    legal_representative: Optional[Union[Person, List[Person]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'legalRepresentative', 'https://schema.org/legalRepresentative'
        ),
        serialization_alias='https://schema.org/legalRepresentative',
    )
    service_area: Optional[
        Union[
            AdministrativeArea,
            GeoShape,
            Place,
            List[Union[AdministrativeArea, GeoShape, Place]],
        ]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('serviceArea', 'https://schema.org/serviceArea'),
        serialization_alias='https://schema.org/serviceArea',
    )
    has_offer_catalog: Optional[Union[OfferCatalog, List[OfferCatalog]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'hasOfferCatalog', 'https://schema.org/hasOfferCatalog'
        ),
        serialization_alias='https://schema.org/hasOfferCatalog',
    )
    has_certification: Optional[Union[Certification, List[Certification]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'hasCertification', 'https://schema.org/hasCertification'
        ),
        serialization_alias='https://schema.org/hasCertification',
    )
    corrections_policy: Optional[
        Union[AnyUrl, CreativeWork, List[Union[AnyUrl, CreativeWork]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'correctionsPolicy', 'https://schema.org/correctionsPolicy'
        ),
        serialization_alias='https://schema.org/correctionsPolicy',
    )
    members: Optional[
        Union[Organization, Person, List[Union[Organization, Person]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('members', 'https://schema.org/members'),
        serialization_alias='https://schema.org/members',
    )
    keywords: Optional[
        Union[str, AnyUrl, DefinedTerm, List[Union[str, AnyUrl, DefinedTerm]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('keywords', 'https://schema.org/keywords'),
        serialization_alias='https://schema.org/keywords',
    )
    has_product_return_policy: Optional[
        Union[ProductReturnPolicy, List[ProductReturnPolicy]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'hasProductReturnPolicy', 'https://schema.org/hasProductReturnPolicy'
        ),
        serialization_alias='https://schema.org/hasProductReturnPolicy',
    )
    logo: Optional[
        Union[AnyUrl, ImageObject, List[Union[AnyUrl, ImageObject]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('logo', 'https://schema.org/logo'),
        serialization_alias='https://schema.org/logo',
    )
    number_of_employees: Optional[
        Union[QuantitativeValue, List[QuantitativeValue]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'numberOfEmployees', 'https://schema.org/numberOfEmployees'
        ),
        serialization_alias='https://schema.org/numberOfEmployees',
    )
    email: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices('email', 'https://schema.org/email'),
        serialization_alias='https://schema.org/email',
    )
    seeks: Optional[Union[Demand, List[Demand]]] = Field(
        default=None,
        validation_alias=AliasChoices('seeks', 'https://schema.org/seeks'),
        serialization_alias='https://schema.org/seeks',
    )
    legal_name: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices('legalName', 'https://schema.org/legalName'),
        serialization_alias='https://schema.org/legalName',
    )
    has_credential: Optional[
        Union[
            EducationalOccupationalCredential, List[EducationalOccupationalCredential]
        ]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'hasCredential', 'https://schema.org/hasCredential'
        ),
        serialization_alias='https://schema.org/hasCredential',
    )
    alumni: Optional[Union[Person, List[Person]]] = Field(
        default=None,
        validation_alias=AliasChoices('alumni', 'https://schema.org/alumni'),
        serialization_alias='https://schema.org/alumni',
    )
    funding: Optional[Union[Grant, List[Grant]]] = Field(
        default=None,
        validation_alias=AliasChoices('funding', 'https://schema.org/funding'),
        serialization_alias='https://schema.org/funding',
    )
    funder: Optional[
        Union[Organization, Person, List[Union[Organization, Person]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('funder', 'https://schema.org/funder'),
        serialization_alias='https://schema.org/funder',
    )
    agent_interaction_statistic: Optional[
        Union[InteractionCounter, List[InteractionCounter]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'agentInteractionStatistic', 'https://schema.org/agentInteractionStatistic'
        ),
        serialization_alias='https://schema.org/agentInteractionStatistic',
    )
    naics: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices('naics', 'https://schema.org/naics'),
        serialization_alias='https://schema.org/naics',
    )
    slogan: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices('slogan', 'https://schema.org/slogan'),
        serialization_alias='https://schema.org/slogan',
    )
    founding_date: Optional[Union[date, List[date]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'foundingDate', 'https://schema.org/foundingDate'
        ),
        serialization_alias='https://schema.org/foundingDate',
    )
    diversity_policy: Optional[
        Union[CreativeWork, AnyUrl, List[Union[CreativeWork, AnyUrl]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'diversityPolicy', 'https://schema.org/diversityPolicy'
        ),
        serialization_alias='https://schema.org/diversityPolicy',
    )
    founders: Optional[Union[Person, List[Person]]] = Field(
        default=None,
        validation_alias=AliasChoices('founders', 'https://schema.org/founders'),
        serialization_alias='https://schema.org/founders',
    )
    award: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices('award', 'https://schema.org/award'),
        serialization_alias='https://schema.org/award',
    )
    founding_location: Optional[Union[Place, List[Place]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'foundingLocation', 'https://schema.org/foundingLocation'
        ),
        serialization_alias='https://schema.org/foundingLocation',
    )
    unnamed_sources_policy: Optional[
        Union[CreativeWork, AnyUrl, List[Union[CreativeWork, AnyUrl]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'unnamedSourcesPolicy', 'https://schema.org/unnamedSourcesPolicy'
        ),
        serialization_alias='https://schema.org/unnamedSourcesPolicy',
    )
    lei_code: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices('leiCode', 'https://schema.org/leiCode'),
        serialization_alias='https://schema.org/leiCode',
    )
    address: Optional[
        Union[str, PostalAddress, List[Union[str, PostalAddress]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('address', 'https://schema.org/address'),
        serialization_alias='https://schema.org/address',
    )
    events: Optional[Union[Event, List[Event]]] = Field(
        default=None,
        validation_alias=AliasChoices('events', 'https://schema.org/events'),
        serialization_alias='https://schema.org/events',
    )
    employee: Optional[Union[Person, List[Person]]] = Field(
        default=None,
        validation_alias=AliasChoices('employee', 'https://schema.org/employee'),
        serialization_alias='https://schema.org/employee',
    )
    tax_id: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices('taxID', 'https://schema.org/taxID'),
        serialization_alias='https://schema.org/taxID',
    )
    has_gs1_digital_link: Optional[Union[AnyUrl, List[AnyUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'hasGS1DigitalLink', 'https://schema.org/hasGS1DigitalLink'
        ),
        serialization_alias='https://schema.org/hasGS1DigitalLink',
    )
    diversity_staffing_report: Optional[
        Union[Article, AnyUrl, List[Union[Article, AnyUrl]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'diversityStaffingReport', 'https://schema.org/diversityStaffingReport'
        ),
        serialization_alias='https://schema.org/diversityStaffingReport',
    )
    company_registration: Optional[Union[Certification, List[Certification]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'companyRegistration', 'https://schema.org/companyRegistration'
        ),
        serialization_alias='https://schema.org/companyRegistration',
    )


class Place(Thing):
    field_type: Literal['https://schema.org/Place'] = Field(
        'https://schema.org/Place', alias='@type'
    )
    fax_number: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices('faxNumber', 'https://schema.org/faxNumber'),
        serialization_alias='https://schema.org/faxNumber',
    )
    global_location_number: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'globalLocationNumber', 'https://schema.org/globalLocationNumber'
        ),
        serialization_alias='https://schema.org/globalLocationNumber',
    )
    event: Optional[Union[Event, List[Event]]] = Field(
        default=None,
        validation_alias=AliasChoices('event', 'https://schema.org/event'),
        serialization_alias='https://schema.org/event',
    )
    has_certification: Optional[Union[Certification, List[Certification]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'hasCertification', 'https://schema.org/hasCertification'
        ),
        serialization_alias='https://schema.org/hasCertification',
    )
    is_accessible_for_free: Optional[Union[bool, List[bool]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'isAccessibleForFree', 'https://schema.org/isAccessibleForFree'
        ),
        serialization_alias='https://schema.org/isAccessibleForFree',
    )
    geo_intersects: Optional[
        Union[Place, GeospatialGeometry, List[Union[Place, GeospatialGeometry]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'geoIntersects', 'https://schema.org/geoIntersects'
        ),
        serialization_alias='https://schema.org/geoIntersects',
    )
    geo_covered_by: Optional[
        Union[GeospatialGeometry, Place, List[Union[GeospatialGeometry, Place]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'geoCoveredBy', 'https://schema.org/geoCoveredBy'
        ),
        serialization_alias='https://schema.org/geoCoveredBy',
    )
    reviews: Optional[Union[Review, List[Review]]] = Field(
        default=None,
        validation_alias=AliasChoices('reviews', 'https://schema.org/reviews'),
        serialization_alias='https://schema.org/reviews',
    )
    aggregate_rating: Optional[Union[AggregateRating, List[AggregateRating]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'aggregateRating', 'https://schema.org/aggregateRating'
        ),
        serialization_alias='https://schema.org/aggregateRating',
    )
    has_map: Optional[Union[AnyUrl, Map, List[Union[AnyUrl, Map]]]] = Field(
        default=None,
        validation_alias=AliasChoices('hasMap', 'https://schema.org/hasMap'),
        serialization_alias='https://schema.org/hasMap',
    )
    longitude: Optional[Union[float, str, List[Union[float, str]]]] = Field(
        default=None,
        validation_alias=AliasChoices('longitude', 'https://schema.org/longitude'),
        serialization_alias='https://schema.org/longitude',
    )
    photos: Optional[
        Union[Photograph, ImageObject, List[Union[Photograph, ImageObject]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('photos', 'https://schema.org/photos'),
        serialization_alias='https://schema.org/photos',
    )
    photo: Optional[
        Union[Photograph, ImageObject, List[Union[Photograph, ImageObject]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('photo', 'https://schema.org/photo'),
        serialization_alias='https://schema.org/photo',
    )
    geo_equals: Optional[
        Union[Place, GeospatialGeometry, List[Union[Place, GeospatialGeometry]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('geoEquals', 'https://schema.org/geoEquals'),
        serialization_alias='https://schema.org/geoEquals',
    )
    has_drive_through_service: Optional[Union[bool, List[bool]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'hasDriveThroughService', 'https://schema.org/hasDriveThroughService'
        ),
        serialization_alias='https://schema.org/hasDriveThroughService',
    )
    geo_covers: Optional[
        Union[Place, GeospatialGeometry, List[Union[Place, GeospatialGeometry]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('geoCovers', 'https://schema.org/geoCovers'),
        serialization_alias='https://schema.org/geoCovers',
    )
    slogan: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices('slogan', 'https://schema.org/slogan'),
        serialization_alias='https://schema.org/slogan',
    )
    amenity_feature: Optional[
        Union[LocationFeatureSpecification, List[LocationFeatureSpecification]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'amenityFeature', 'https://schema.org/amenityFeature'
        ),
        serialization_alias='https://schema.org/amenityFeature',
    )
    keywords: Optional[
        Union[str, AnyUrl, DefinedTerm, List[Union[str, AnyUrl, DefinedTerm]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('keywords', 'https://schema.org/keywords'),
        serialization_alias='https://schema.org/keywords',
    )
    logo: Optional[
        Union[AnyUrl, ImageObject, List[Union[AnyUrl, ImageObject]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('logo', 'https://schema.org/logo'),
        serialization_alias='https://schema.org/logo',
    )
    map: Optional[Union[AnyUrl, List[AnyUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices('map', 'https://schema.org/map'),
        serialization_alias='https://schema.org/map',
    )
    geo: Optional[
        Union[GeoShape, GeoCoordinates, List[Union[GeoShape, GeoCoordinates]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('geo', 'https://schema.org/geo'),
        serialization_alias='https://schema.org/geo',
    )
    tour_booking_page: Optional[Union[AnyUrl, List[AnyUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'tourBookingPage', 'https://schema.org/tourBookingPage'
        ),
        serialization_alias='https://schema.org/tourBookingPage',
    )
    latitude: Optional[Union[str, float, List[Union[str, float]]]] = Field(
        default=None,
        validation_alias=AliasChoices('latitude', 'https://schema.org/latitude'),
        serialization_alias='https://schema.org/latitude',
    )
    public_access: Optional[Union[bool, List[bool]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'publicAccess', 'https://schema.org/publicAccess'
        ),
        serialization_alias='https://schema.org/publicAccess',
    )
    maps: Optional[Union[AnyUrl, List[AnyUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices('maps', 'https://schema.org/maps'),
        serialization_alias='https://schema.org/maps',
    )
    branch_code: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices('branchCode', 'https://schema.org/branchCode'),
        serialization_alias='https://schema.org/branchCode',
    )
    address: Optional[
        Union[str, PostalAddress, List[Union[str, PostalAddress]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('address', 'https://schema.org/address'),
        serialization_alias='https://schema.org/address',
    )
    additional_property: Optional[Union[PropertyValue, List[PropertyValue]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'additionalProperty', 'https://schema.org/additionalProperty'
        ),
        serialization_alias='https://schema.org/additionalProperty',
    )
    events: Optional[Union[Event, List[Event]]] = Field(
        default=None,
        validation_alias=AliasChoices('events', 'https://schema.org/events'),
        serialization_alias='https://schema.org/events',
    )
    opening_hours_specification: Optional[
        Union[OpeningHoursSpecification, List[OpeningHoursSpecification]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'openingHoursSpecification', 'https://schema.org/openingHoursSpecification'
        ),
        serialization_alias='https://schema.org/openingHoursSpecification',
    )
    has_gs1_digital_link: Optional[Union[AnyUrl, List[AnyUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'hasGS1DigitalLink', 'https://schema.org/hasGS1DigitalLink'
        ),
        serialization_alias='https://schema.org/hasGS1DigitalLink',
    )
    geo_contains: Optional[
        Union[Place, GeospatialGeometry, List[Union[Place, GeospatialGeometry]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('geoContains', 'https://schema.org/geoContains'),
        serialization_alias='https://schema.org/geoContains',
    )
    telephone: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices('telephone', 'https://schema.org/telephone'),
        serialization_alias='https://schema.org/telephone',
    )
    smoking_allowed: Optional[Union[bool, List[bool]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'smokingAllowed', 'https://schema.org/smokingAllowed'
        ),
        serialization_alias='https://schema.org/smokingAllowed',
    )
    geo_disjoint: Optional[
        Union[GeospatialGeometry, Place, List[Union[GeospatialGeometry, Place]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('geoDisjoint', 'https://schema.org/geoDisjoint'),
        serialization_alias='https://schema.org/geoDisjoint',
    )
    contained_in_place: Optional[Union[Place, List[Place]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'containedInPlace', 'https://schema.org/containedInPlace'
        ),
        serialization_alias='https://schema.org/containedInPlace',
    )
    geo_overlaps: Optional[
        Union[Place, GeospatialGeometry, List[Union[Place, GeospatialGeometry]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('geoOverlaps', 'https://schema.org/geoOverlaps'),
        serialization_alias='https://schema.org/geoOverlaps',
    )
    review: Optional[Union[Review, List[Review]]] = Field(
        default=None,
        validation_alias=AliasChoices('review', 'https://schema.org/review'),
        serialization_alias='https://schema.org/review',
    )
    contained_in: Optional[Union[Place, List[Place]]] = Field(
        default=None,
        validation_alias=AliasChoices('containedIn', 'https://schema.org/containedIn'),
        serialization_alias='https://schema.org/containedIn',
    )
    special_opening_hours_specification: Optional[
        Union[OpeningHoursSpecification, List[OpeningHoursSpecification]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'specialOpeningHoursSpecification',
            'https://schema.org/specialOpeningHoursSpecification',
        ),
        serialization_alias='https://schema.org/specialOpeningHoursSpecification',
    )
    geo_touches: Optional[
        Union[Place, GeospatialGeometry, List[Union[Place, GeospatialGeometry]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('geoTouches', 'https://schema.org/geoTouches'),
        serialization_alias='https://schema.org/geoTouches',
    )
    contains_place: Optional[Union[Place, List[Place]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'containsPlace', 'https://schema.org/containsPlace'
        ),
        serialization_alias='https://schema.org/containsPlace',
    )
    isic_v4: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices('isicV4', 'https://schema.org/isicV4'),
        serialization_alias='https://schema.org/isicV4',
    )
    geo_crosses: Optional[
        Union[Place, GeospatialGeometry, List[Union[Place, GeospatialGeometry]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('geoCrosses', 'https://schema.org/geoCrosses'),
        serialization_alias='https://schema.org/geoCrosses',
    )
    maximum_attendee_capacity: Optional[Union[int, List[int]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'maximumAttendeeCapacity', 'https://schema.org/maximumAttendeeCapacity'
        ),
        serialization_alias='https://schema.org/maximumAttendeeCapacity',
    )
    geo_within: Optional[
        Union[GeospatialGeometry, Place, List[Union[GeospatialGeometry, Place]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('geoWithin', 'https://schema.org/geoWithin'),
        serialization_alias='https://schema.org/geoWithin',
    )


class Event(Thing):
    field_type: Literal['https://schema.org/Event'] = Field(
        'https://schema.org/Event', alias='@type'
    )
    recorded_in: Optional[Union[CreativeWork, List[CreativeWork]]] = Field(
        default=None,
        validation_alias=AliasChoices('recordedIn', 'https://schema.org/recordedIn'),
        serialization_alias='https://schema.org/recordedIn',
    )
    is_accessible_for_free: Optional[Union[bool, List[bool]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'isAccessibleForFree', 'https://schema.org/isAccessibleForFree'
        ),
        serialization_alias='https://schema.org/isAccessibleForFree',
    )
    aggregate_rating: Optional[Union[AggregateRating, List[AggregateRating]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'aggregateRating', 'https://schema.org/aggregateRating'
        ),
        serialization_alias='https://schema.org/aggregateRating',
    )
    event_schedule: Optional[Union[Schedule, List[Schedule]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'eventSchedule', 'https://schema.org/eventSchedule'
        ),
        serialization_alias='https://schema.org/eventSchedule',
    )
    director: Optional[Union[Person, List[Person]]] = Field(
        default=None,
        validation_alias=AliasChoices('director', 'https://schema.org/director'),
        serialization_alias='https://schema.org/director',
    )
    remaining_attendee_capacity: Optional[Union[int, List[int]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'remainingAttendeeCapacity', 'https://schema.org/remainingAttendeeCapacity'
        ),
        serialization_alias='https://schema.org/remainingAttendeeCapacity',
    )
    about: Optional[Union[Thing, List[Thing]]] = Field(
        default=None,
        validation_alias=AliasChoices('about', 'https://schema.org/about'),
        serialization_alias='https://schema.org/about',
    )
    sub_event: Optional[Union[Event, List[Event]]] = Field(
        default=None,
        validation_alias=AliasChoices('subEvent', 'https://schema.org/subEvent'),
        serialization_alias='https://schema.org/subEvent',
    )
    maximum_physical_attendee_capacity: Optional[Union[int, List[int]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'maximumPhysicalAttendeeCapacity',
            'https://schema.org/maximumPhysicalAttendeeCapacity',
        ),
        serialization_alias='https://schema.org/maximumPhysicalAttendeeCapacity',
    )
    work_featured: Optional[Union[CreativeWork, List[CreativeWork]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'workFeatured', 'https://schema.org/workFeatured'
        ),
        serialization_alias='https://schema.org/workFeatured',
    )
    location: Optional[
        Union[
            VirtualLocation,
            PostalAddress,
            str,
            Place,
            List[Union[VirtualLocation, PostalAddress, str, Place]],
        ]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('location', 'https://schema.org/location'),
        serialization_alias='https://schema.org/location',
    )
    start_date: Optional[
        Union[date, AwareDatetime, List[Union[date, AwareDatetime]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('startDate', 'https://schema.org/startDate'),
        serialization_alias='https://schema.org/startDate',
    )
    previous_start_date: Optional[Union[date, List[date]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'previousStartDate', 'https://schema.org/previousStartDate'
        ),
        serialization_alias='https://schema.org/previousStartDate',
    )
    funder: Optional[
        Union[Organization, Person, List[Union[Organization, Person]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('funder', 'https://schema.org/funder'),
        serialization_alias='https://schema.org/funder',
    )
    maximum_virtual_attendee_capacity: Optional[Union[int, List[int]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'maximumVirtualAttendeeCapacity',
            'https://schema.org/maximumVirtualAttendeeCapacity',
        ),
        serialization_alias='https://schema.org/maximumVirtualAttendeeCapacity',
    )
    duration: Optional[
        Union[Duration, QuantitativeValue, List[Union[Duration, QuantitativeValue]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('duration', 'https://schema.org/duration'),
        serialization_alias='https://schema.org/duration',
    )
    keywords: Optional[
        Union[str, AnyUrl, DefinedTerm, List[Union[str, AnyUrl, DefinedTerm]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('keywords', 'https://schema.org/keywords'),
        serialization_alias='https://schema.org/keywords',
    )
    translator: Optional[
        Union[Person, Organization, List[Union[Person, Organization]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('translator', 'https://schema.org/translator'),
        serialization_alias='https://schema.org/translator',
    )
    door_time: Optional[
        Union[time, AwareDatetime, List[Union[time, AwareDatetime]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('doorTime', 'https://schema.org/doorTime'),
        serialization_alias='https://schema.org/doorTime',
    )
    attendee: Optional[
        Union[Person, Organization, List[Union[Person, Organization]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('attendee', 'https://schema.org/attendee'),
        serialization_alias='https://schema.org/attendee',
    )
    offers: Optional[Union[Demand, Offer, List[Union[Demand, Offer]]]] = Field(
        default=None,
        validation_alias=AliasChoices('offers', 'https://schema.org/offers'),
        serialization_alias='https://schema.org/offers',
    )
    audience: Optional[Union[Audience, List[Audience]]] = Field(
        default=None,
        validation_alias=AliasChoices('audience', 'https://schema.org/audience'),
        serialization_alias='https://schema.org/audience',
    )
    funding: Optional[Union[Grant, List[Grant]]] = Field(
        default=None,
        validation_alias=AliasChoices('funding', 'https://schema.org/funding'),
        serialization_alias='https://schema.org/funding',
    )
    performers: Optional[
        Union[Person, Organization, List[Union[Person, Organization]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('performers', 'https://schema.org/performers'),
        serialization_alias='https://schema.org/performers',
    )
    event_status: Optional[Union[EventStatusType, List[EventStatusType]]] = Field(
        default=None,
        validation_alias=AliasChoices('eventStatus', 'https://schema.org/eventStatus'),
        serialization_alias='https://schema.org/eventStatus',
    )
    actor: Optional[
        Union[Person, PerformingGroup, List[Union[Person, PerformingGroup]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('actor', 'https://schema.org/actor'),
        serialization_alias='https://schema.org/actor',
    )
    super_event: Optional[Union[Event, List[Event]]] = Field(
        default=None,
        validation_alias=AliasChoices('superEvent', 'https://schema.org/superEvent'),
        serialization_alias='https://schema.org/superEvent',
    )
    event_attendance_mode: Optional[
        Union[EventAttendanceModeEnumeration, List[EventAttendanceModeEnumeration]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'eventAttendanceMode', 'https://schema.org/eventAttendanceMode'
        ),
        serialization_alias='https://schema.org/eventAttendanceMode',
    )
    organizer: Optional[
        Union[Person, Organization, List[Union[Person, Organization]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('organizer', 'https://schema.org/organizer'),
        serialization_alias='https://schema.org/organizer',
    )
    attendees: Optional[
        Union[Person, Organization, List[Union[Person, Organization]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('attendees', 'https://schema.org/attendees'),
        serialization_alias='https://schema.org/attendees',
    )
    sub_events: Optional[Union[Event, List[Event]]] = Field(
        default=None,
        validation_alias=AliasChoices('subEvents', 'https://schema.org/subEvents'),
        serialization_alias='https://schema.org/subEvents',
    )
    review: Optional[Union[Review, List[Review]]] = Field(
        default=None,
        validation_alias=AliasChoices('review', 'https://schema.org/review'),
        serialization_alias='https://schema.org/review',
    )
    performer: Optional[
        Union[Person, Organization, List[Union[Person, Organization]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('performer', 'https://schema.org/performer'),
        serialization_alias='https://schema.org/performer',
    )
    typical_age_range: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'typicalAgeRange', 'https://schema.org/typicalAgeRange'
        ),
        serialization_alias='https://schema.org/typicalAgeRange',
    )
    end_date: Optional[
        Union[AwareDatetime, date, List[Union[AwareDatetime, date]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('endDate', 'https://schema.org/endDate'),
        serialization_alias='https://schema.org/endDate',
    )
    contributor: Optional[
        Union[Organization, Person, List[Union[Organization, Person]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('contributor', 'https://schema.org/contributor'),
        serialization_alias='https://schema.org/contributor',
    )
    composer: Optional[
        Union[Organization, Person, List[Union[Organization, Person]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('composer', 'https://schema.org/composer'),
        serialization_alias='https://schema.org/composer',
    )
    maximum_attendee_capacity: Optional[Union[int, List[int]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'maximumAttendeeCapacity', 'https://schema.org/maximumAttendeeCapacity'
        ),
        serialization_alias='https://schema.org/maximumAttendeeCapacity',
    )
    work_performed: Optional[Union[CreativeWork, List[CreativeWork]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'workPerformed', 'https://schema.org/workPerformed'
        ),
        serialization_alias='https://schema.org/workPerformed',
    )
    in_language: Optional[Union[str, Language, List[Union[str, Language]]]] = Field(
        default=None,
        validation_alias=AliasChoices('inLanguage', 'https://schema.org/inLanguage'),
        serialization_alias='https://schema.org/inLanguage',
    )
    sponsor: Optional[
        Union[Organization, Person, List[Union[Organization, Person]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('sponsor', 'https://schema.org/sponsor'),
        serialization_alias='https://schema.org/sponsor',
    )


class Product(Thing):
    field_type: Literal['https://schema.org/Product'] = Field(
        'https://schema.org/Product', alias='@type'
    )
    reviews: Optional[Union[Review, List[Review]]] = Field(
        default=None,
        validation_alias=AliasChoices('reviews', 'https://schema.org/reviews'),
        serialization_alias='https://schema.org/reviews',
    )
    in_product_group_with_id: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'inProductGroupWithID', 'https://schema.org/inProductGroupWithID'
        ),
        serialization_alias='https://schema.org/inProductGroupWithID',
    )
    gtin: Optional[Union[str, AnyUrl, List[Union[str, AnyUrl]]]] = Field(
        default=None,
        validation_alias=AliasChoices('gtin', 'https://schema.org/gtin'),
        serialization_alias='https://schema.org/gtin',
    )
    gtin8: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices('gtin8', 'https://schema.org/gtin8'),
        serialization_alias='https://schema.org/gtin8',
    )
    is_related_to: Optional[
        Union[Service, Product, List[Union[Service, Product]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('isRelatedTo', 'https://schema.org/isRelatedTo'),
        serialization_alias='https://schema.org/isRelatedTo',
    )
    color_swatch: Optional[
        Union[ImageObject, AnyUrl, List[Union[ImageObject, AnyUrl]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('colorSwatch', 'https://schema.org/colorSwatch'),
        serialization_alias='https://schema.org/colorSwatch',
    )
    asin: Optional[Union[AnyUrl, str, List[Union[AnyUrl, str]]]] = Field(
        default=None,
        validation_alias=AliasChoices('asin', 'https://schema.org/asin'),
        serialization_alias='https://schema.org/asin',
    )
    pattern: Optional[Union[DefinedTerm, str, List[Union[DefinedTerm, str]]]] = Field(
        default=None,
        validation_alias=AliasChoices('pattern', 'https://schema.org/pattern'),
        serialization_alias='https://schema.org/pattern',
    )
    awards: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices('awards', 'https://schema.org/awards'),
        serialization_alias='https://schema.org/awards',
    )
    production_date: Optional[Union[date, List[date]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'productionDate', 'https://schema.org/productionDate'
        ),
        serialization_alias='https://schema.org/productionDate',
    )
    model: Optional[Union[ProductModel, str, List[Union[ProductModel, str]]]] = Field(
        default=None,
        validation_alias=AliasChoices('model', 'https://schema.org/model'),
        serialization_alias='https://schema.org/model',
    )
    has_certification: Optional[Union[Certification, List[Certification]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'hasCertification', 'https://schema.org/hasCertification'
        ),
        serialization_alias='https://schema.org/hasCertification',
    )
    is_variant_of: Optional[
        Union[ProductModel, ProductGroup, List[Union[ProductModel, ProductGroup]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('isVariantOf', 'https://schema.org/isVariantOf'),
        serialization_alias='https://schema.org/isVariantOf',
    )
    is_family_friendly: Optional[Union[bool, List[bool]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'isFamilyFriendly', 'https://schema.org/isFamilyFriendly'
        ),
        serialization_alias='https://schema.org/isFamilyFriendly',
    )
    logo: Optional[
        Union[AnyUrl, ImageObject, List[Union[AnyUrl, ImageObject]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('logo', 'https://schema.org/logo'),
        serialization_alias='https://schema.org/logo',
    )
    aggregate_rating: Optional[Union[AggregateRating, List[AggregateRating]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'aggregateRating', 'https://schema.org/aggregateRating'
        ),
        serialization_alias='https://schema.org/aggregateRating',
    )
    sku: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices('sku', 'https://schema.org/sku'),
        serialization_alias='https://schema.org/sku',
    )
    negative_notes: Optional[
        Union[
            ListItem,
            WebContent,
            ItemList,
            str,
            List[Union[ListItem, WebContent, ItemList, str]],
        ]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'negativeNotes', 'https://schema.org/negativeNotes'
        ),
        serialization_alias='https://schema.org/negativeNotes',
    )
    width: Optional[
        Union[QuantitativeValue, Distance, List[Union[QuantitativeValue, Distance]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('width', 'https://schema.org/width'),
        serialization_alias='https://schema.org/width',
    )
    color: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices('color', 'https://schema.org/color'),
        serialization_alias='https://schema.org/color',
    )
    has_adult_consideration: Optional[
        Union[AdultOrientedEnumeration, List[AdultOrientedEnumeration]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'hasAdultConsideration', 'https://schema.org/hasAdultConsideration'
        ),
        serialization_alias='https://schema.org/hasAdultConsideration',
    )
    purchase_date: Optional[Union[date, List[date]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'purchaseDate', 'https://schema.org/purchaseDate'
        ),
        serialization_alias='https://schema.org/purchaseDate',
    )
    country_of_assembly: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'countryOfAssembly', 'https://schema.org/countryOfAssembly'
        ),
        serialization_alias='https://schema.org/countryOfAssembly',
    )
    slogan: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices('slogan', 'https://schema.org/slogan'),
        serialization_alias='https://schema.org/slogan',
    )
    mobile_url: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices('mobileUrl', 'https://schema.org/mobileUrl'),
        serialization_alias='https://schema.org/mobileUrl',
    )
    keywords: Optional[
        Union[str, AnyUrl, DefinedTerm, List[Union[str, AnyUrl, DefinedTerm]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('keywords', 'https://schema.org/keywords'),
        serialization_alias='https://schema.org/keywords',
    )
    has_product_return_policy: Optional[
        Union[ProductReturnPolicy, List[ProductReturnPolicy]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'hasProductReturnPolicy', 'https://schema.org/hasProductReturnPolicy'
        ),
        serialization_alias='https://schema.org/hasProductReturnPolicy',
    )
    award: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices('award', 'https://schema.org/award'),
        serialization_alias='https://schema.org/award',
    )
    is_similar_to: Optional[
        Union[Service, Product, List[Union[Service, Product]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('isSimilarTo', 'https://schema.org/isSimilarTo'),
        serialization_alias='https://schema.org/isSimilarTo',
    )
    additional_property: Optional[Union[PropertyValue, List[PropertyValue]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'additionalProperty', 'https://schema.org/additionalProperty'
        ),
        serialization_alias='https://schema.org/additionalProperty',
    )
    product_id: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices('productID', 'https://schema.org/productID'),
        serialization_alias='https://schema.org/productID',
    )
    gtin13: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices('gtin13', 'https://schema.org/gtin13'),
        serialization_alias='https://schema.org/gtin13',
    )
    offers: Optional[Union[Demand, Offer, List[Union[Demand, Offer]]]] = Field(
        default=None,
        validation_alias=AliasChoices('offers', 'https://schema.org/offers'),
        serialization_alias='https://schema.org/offers',
    )
    audience: Optional[Union[Audience, List[Audience]]] = Field(
        default=None,
        validation_alias=AliasChoices('audience', 'https://schema.org/audience'),
        serialization_alias='https://schema.org/audience',
    )
    has_gs1_digital_link: Optional[Union[AnyUrl, List[AnyUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'hasGS1DigitalLink', 'https://schema.org/hasGS1DigitalLink'
        ),
        serialization_alias='https://schema.org/hasGS1DigitalLink',
    )
    is_consumable_for: Optional[Union[Product, List[Product]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'isConsumableFor', 'https://schema.org/isConsumableFor'
        ),
        serialization_alias='https://schema.org/isConsumableFor',
    )
    funding: Optional[Union[Grant, List[Grant]]] = Field(
        default=None,
        validation_alias=AliasChoices('funding', 'https://schema.org/funding'),
        serialization_alias='https://schema.org/funding',
    )
    has_measurement: Optional[
        Union[QuantitativeValue, List[QuantitativeValue]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'hasMeasurement', 'https://schema.org/hasMeasurement'
        ),
        serialization_alias='https://schema.org/hasMeasurement',
    )
    has_energy_consumption_details: Optional[
        Union[EnergyConsumptionDetails, List[EnergyConsumptionDetails]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'hasEnergyConsumptionDetails',
            'https://schema.org/hasEnergyConsumptionDetails',
        ),
        serialization_alias='https://schema.org/hasEnergyConsumptionDetails',
    )
    brand: Optional[
        Union[Organization, Brand, List[Union[Organization, Brand]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('brand', 'https://schema.org/brand'),
        serialization_alias='https://schema.org/brand',
    )
    country_of_last_processing: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'countryOfLastProcessing', 'https://schema.org/countryOfLastProcessing'
        ),
        serialization_alias='https://schema.org/countryOfLastProcessing',
    )
    item_condition: Optional[
        Union[OfferItemCondition, List[OfferItemCondition]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'itemCondition', 'https://schema.org/itemCondition'
        ),
        serialization_alias='https://schema.org/itemCondition',
    )
    material: Optional[
        Union[str, Product, AnyUrl, List[Union[str, Product, AnyUrl]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('material', 'https://schema.org/material'),
        serialization_alias='https://schema.org/material',
    )
    mpn: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices('mpn', 'https://schema.org/mpn'),
        serialization_alias='https://schema.org/mpn',
    )
    height: Optional[
        Union[Distance, QuantitativeValue, List[Union[Distance, QuantitativeValue]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('height', 'https://schema.org/height'),
        serialization_alias='https://schema.org/height',
    )
    release_date: Optional[Union[date, List[date]]] = Field(
        default=None,
        validation_alias=AliasChoices('releaseDate', 'https://schema.org/releaseDate'),
        serialization_alias='https://schema.org/releaseDate',
    )
    size: Optional[
        Union[
            DefinedTerm,
            str,
            SizeSpecification,
            QuantitativeValue,
            List[Union[DefinedTerm, str, SizeSpecification, QuantitativeValue]],
        ]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('size', 'https://schema.org/size'),
        serialization_alias='https://schema.org/size',
    )
    category: Optional[
        Union[
            PhysicalActivityCategory,
            CategoryCode,
            str,
            Thing,
            AnyUrl,
            List[Union[PhysicalActivityCategory, CategoryCode, str, Thing, AnyUrl]],
        ]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('category', 'https://schema.org/category'),
        serialization_alias='https://schema.org/category',
    )
    weight: Optional[
        Union[QuantitativeValue, Mass, List[Union[QuantitativeValue, Mass]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('weight', 'https://schema.org/weight'),
        serialization_alias='https://schema.org/weight',
    )
    has_merchant_return_policy: Optional[
        Union[MerchantReturnPolicy, List[MerchantReturnPolicy]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'hasMerchantReturnPolicy', 'https://schema.org/hasMerchantReturnPolicy'
        ),
        serialization_alias='https://schema.org/hasMerchantReturnPolicy',
    )
    nsn: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices('nsn', 'https://schema.org/nsn'),
        serialization_alias='https://schema.org/nsn',
    )
    gtin14: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices('gtin14', 'https://schema.org/gtin14'),
        serialization_alias='https://schema.org/gtin14',
    )
    gtin12: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices('gtin12', 'https://schema.org/gtin12'),
        serialization_alias='https://schema.org/gtin12',
    )
    manufacturer: Optional[Union[Organization, List[Organization]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'manufacturer', 'https://schema.org/manufacturer'
        ),
        serialization_alias='https://schema.org/manufacturer',
    )
    review: Optional[Union[Review, List[Review]]] = Field(
        default=None,
        validation_alias=AliasChoices('review', 'https://schema.org/review'),
        serialization_alias='https://schema.org/review',
    )
    depth: Optional[
        Union[Distance, QuantitativeValue, List[Union[Distance, QuantitativeValue]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('depth', 'https://schema.org/depth'),
        serialization_alias='https://schema.org/depth',
    )
    positive_notes: Optional[
        Union[
            WebContent,
            ItemList,
            str,
            ListItem,
            List[Union[WebContent, ItemList, str, ListItem]],
        ]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'positiveNotes', 'https://schema.org/positiveNotes'
        ),
        serialization_alias='https://schema.org/positiveNotes',
    )
    country_of_origin: Optional[Union[Country, List[Country]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'countryOfOrigin', 'https://schema.org/countryOfOrigin'
        ),
        serialization_alias='https://schema.org/countryOfOrigin',
    )
    is_accessory_or_spare_part_for: Optional[Union[Product, List[Product]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'isAccessoryOrSparePartFor', 'https://schema.org/isAccessoryOrSparePartFor'
        ),
        serialization_alias='https://schema.org/isAccessoryOrSparePartFor',
    )


class MedicalEntity(Thing):
    field_type: Literal['https://schema.org/MedicalEntity'] = Field(
        'https://schema.org/MedicalEntity', alias='@type'
    )
    code: Optional[Union[MedicalCode, List[MedicalCode]]] = Field(
        default=None,
        validation_alias=AliasChoices('code', 'https://schema.org/code'),
        serialization_alias='https://schema.org/code',
    )
    guideline: Optional[Union[MedicalGuideline, List[MedicalGuideline]]] = Field(
        default=None,
        validation_alias=AliasChoices('guideline', 'https://schema.org/guideline'),
        serialization_alias='https://schema.org/guideline',
    )
    legal_status: Optional[
        Union[
            DrugLegalStatus,
            MedicalEnumeration,
            str,
            List[Union[DrugLegalStatus, MedicalEnumeration, str]],
        ]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('legalStatus', 'https://schema.org/legalStatus'),
        serialization_alias='https://schema.org/legalStatus',
    )
    recognizing_authority: Optional[Union[Organization, List[Organization]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'recognizingAuthority', 'https://schema.org/recognizingAuthority'
        ),
        serialization_alias='https://schema.org/recognizingAuthority',
    )
    medicine_system: Optional[Union[MedicineSystem, List[MedicineSystem]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'medicineSystem', 'https://schema.org/medicineSystem'
        ),
        serialization_alias='https://schema.org/medicineSystem',
    )
    funding: Optional[Union[Grant, List[Grant]]] = Field(
        default=None,
        validation_alias=AliasChoices('funding', 'https://schema.org/funding'),
        serialization_alias='https://schema.org/funding',
    )
    relevant_specialty: Optional[
        Union[MedicalSpecialty, List[MedicalSpecialty]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'relevantSpecialty', 'https://schema.org/relevantSpecialty'
        ),
        serialization_alias='https://schema.org/relevantSpecialty',
    )
    study: Optional[Union[MedicalStudy, List[MedicalStudy]]] = Field(
        default=None,
        validation_alias=AliasChoices('study', 'https://schema.org/study'),
        serialization_alias='https://schema.org/study',
    )


class BioChemEntity(Thing):
    field_type: Literal['https://schema.org/BioChemEntity'] = Field(
        'https://schema.org/BioChemEntity', alias='@type'
    )
    taxonomic_range: Optional[
        Union[
            Taxon,
            DefinedTerm,
            str,
            AnyUrl,
            List[Union[Taxon, DefinedTerm, str, AnyUrl]],
        ]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'taxonomicRange', 'https://schema.org/taxonomicRange'
        ),
        serialization_alias='https://schema.org/taxonomicRange',
    )
    is_involved_in_biological_process: Optional[
        Union[
            PropertyValue,
            AnyUrl,
            DefinedTerm,
            List[Union[PropertyValue, AnyUrl, DefinedTerm]],
        ]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'isInvolvedInBiologicalProcess',
            'https://schema.org/isInvolvedInBiologicalProcess',
        ),
        serialization_alias='https://schema.org/isInvolvedInBiologicalProcess',
    )
    has_bio_chem_entity_part: Optional[
        Union[BioChemEntity, List[BioChemEntity]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'hasBioChemEntityPart', 'https://schema.org/hasBioChemEntityPart'
        ),
        serialization_alias='https://schema.org/hasBioChemEntityPart',
    )
    bio_chem_similarity: Optional[Union[BioChemEntity, List[BioChemEntity]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'bioChemSimilarity', 'https://schema.org/bioChemSimilarity'
        ),
        serialization_alias='https://schema.org/bioChemSimilarity',
    )
    has_representation: Optional[
        Union[PropertyValue, AnyUrl, str, List[Union[PropertyValue, AnyUrl, str]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'hasRepresentation', 'https://schema.org/hasRepresentation'
        ),
        serialization_alias='https://schema.org/hasRepresentation',
    )
    biological_role: Optional[Union[DefinedTerm, List[DefinedTerm]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'biologicalRole', 'https://schema.org/biologicalRole'
        ),
        serialization_alias='https://schema.org/biologicalRole',
    )
    has_molecular_function: Optional[
        Union[
            PropertyValue,
            AnyUrl,
            DefinedTerm,
            List[Union[PropertyValue, AnyUrl, DefinedTerm]],
        ]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'hasMolecularFunction', 'https://schema.org/hasMolecularFunction'
        ),
        serialization_alias='https://schema.org/hasMolecularFunction',
    )
    bio_chem_interaction: Optional[Union[BioChemEntity, List[BioChemEntity]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'bioChemInteraction', 'https://schema.org/bioChemInteraction'
        ),
        serialization_alias='https://schema.org/bioChemInteraction',
    )
    is_located_in_subcellular_location: Optional[
        Union[
            AnyUrl,
            PropertyValue,
            DefinedTerm,
            List[Union[AnyUrl, PropertyValue, DefinedTerm]],
        ]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'isLocatedInSubcellularLocation',
            'https://schema.org/isLocatedInSubcellularLocation',
        ),
        serialization_alias='https://schema.org/isLocatedInSubcellularLocation',
    )
    funding: Optional[Union[Grant, List[Grant]]] = Field(
        default=None,
        validation_alias=AliasChoices('funding', 'https://schema.org/funding'),
        serialization_alias='https://schema.org/funding',
    )
    is_part_of_bio_chem_entity: Optional[
        Union[BioChemEntity, List[BioChemEntity]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'isPartOfBioChemEntity', 'https://schema.org/isPartOfBioChemEntity'
        ),
        serialization_alias='https://schema.org/isPartOfBioChemEntity',
    )
    is_encoded_by_bio_chem_entity: Optional[Union[Gene, List[Gene]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'isEncodedByBioChemEntity', 'https://schema.org/isEncodedByBioChemEntity'
        ),
        serialization_alias='https://schema.org/isEncodedByBioChemEntity',
    )
    associated_disease: Optional[
        Union[
            MedicalCondition,
            PropertyValue,
            AnyUrl,
            List[Union[MedicalCondition, PropertyValue, AnyUrl]],
        ]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'associatedDisease', 'https://schema.org/associatedDisease'
        ),
        serialization_alias='https://schema.org/associatedDisease',
    )


class Taxon(Thing):
    field_type: Literal['https://schema.org/Taxon'] = Field(
        'https://schema.org/Taxon', alias='@type'
    )
    has_defined_term: Optional[Union[DefinedTerm, List[DefinedTerm]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'hasDefinedTerm', 'https://schema.org/hasDefinedTerm'
        ),
        serialization_alias='https://schema.org/hasDefinedTerm',
    )
    taxon_rank: Optional[
        Union[str, PropertyValue, AnyUrl, List[Union[str, PropertyValue, AnyUrl]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('taxonRank', 'https://schema.org/taxonRank'),
        serialization_alias='https://schema.org/taxonRank',
    )
    parent_taxon: Optional[
        Union[str, AnyUrl, Taxon, List[Union[str, AnyUrl, Taxon]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('parentTaxon', 'https://schema.org/parentTaxon'),
        serialization_alias='https://schema.org/parentTaxon',
    )
    child_taxon: Optional[
        Union[Taxon, str, AnyUrl, List[Union[Taxon, str, AnyUrl]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('childTaxon', 'https://schema.org/childTaxon'),
        serialization_alias='https://schema.org/childTaxon',
    )


class Action(Thing):
    field_type: Literal['https://schema.org/Action'] = Field(
        'https://schema.org/Action', alias='@type'
    )
    action_status: Optional[Union[ActionStatusType, List[ActionStatusType]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'actionStatus', 'https://schema.org/actionStatus'
        ),
        serialization_alias='https://schema.org/actionStatus',
    )
    target: Optional[
        Union[AnyUrl, EntryPoint, List[Union[AnyUrl, EntryPoint]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('target', 'https://schema.org/target'),
        serialization_alias='https://schema.org/target',
    )
    instrument: Optional[Union[Thing, List[Thing]]] = Field(
        default=None,
        validation_alias=AliasChoices('instrument', 'https://schema.org/instrument'),
        serialization_alias='https://schema.org/instrument',
    )
    provider: Optional[
        Union[Person, Organization, List[Union[Person, Organization]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('provider', 'https://schema.org/provider'),
        serialization_alias='https://schema.org/provider',
    )
    action_process: Optional[Union[HowTo, List[HowTo]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'actionProcess', 'https://schema.org/actionProcess'
        ),
        serialization_alias='https://schema.org/actionProcess',
    )
    agent: Optional[
        Union[Person, Organization, List[Union[Person, Organization]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('agent', 'https://schema.org/agent'),
        serialization_alias='https://schema.org/agent',
    )
    participant: Optional[
        Union[Organization, Person, List[Union[Organization, Person]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('participant', 'https://schema.org/participant'),
        serialization_alias='https://schema.org/participant',
    )
    end_time: Optional[
        Union[time, AwareDatetime, List[Union[time, AwareDatetime]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('endTime', 'https://schema.org/endTime'),
        serialization_alias='https://schema.org/endTime',
    )
    error: Optional[Union[Thing, List[Thing]]] = Field(
        default=None,
        validation_alias=AliasChoices('error', 'https://schema.org/error'),
        serialization_alias='https://schema.org/error',
    )
    result: Optional[Union[Thing, List[Thing]]] = Field(
        default=None,
        validation_alias=AliasChoices('result', 'https://schema.org/result'),
        serialization_alias='https://schema.org/result',
    )
    object: Optional[Union[Thing, List[Thing]]] = Field(
        default=None,
        validation_alias=AliasChoices('object', 'https://schema.org/object'),
        serialization_alias='https://schema.org/object',
    )
    location: Optional[
        Union[
            VirtualLocation,
            PostalAddress,
            str,
            Place,
            List[Union[VirtualLocation, PostalAddress, str, Place]],
        ]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('location', 'https://schema.org/location'),
        serialization_alias='https://schema.org/location',
    )
    start_time: Optional[
        Union[time, AwareDatetime, List[Union[time, AwareDatetime]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('startTime', 'https://schema.org/startTime'),
        serialization_alias='https://schema.org/startTime',
    )


class StructuredValue(Intangible):
    field_type: Literal['https://schema.org/StructuredValue'] = Field(
        'https://schema.org/StructuredValue', alias='@type'
    )


class DefinedTerm(Intangible):
    field_type: Literal['https://schema.org/DefinedTerm'] = Field(
        'https://schema.org/DefinedTerm', alias='@type'
    )
    term_code: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices('termCode', 'https://schema.org/termCode'),
        serialization_alias='https://schema.org/termCode',
    )
    in_defined_term_set: Optional[
        Union[AnyUrl, DefinedTermSet, List[Union[AnyUrl, DefinedTermSet]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'inDefinedTermSet', 'https://schema.org/inDefinedTermSet'
        ),
        serialization_alias='https://schema.org/inDefinedTermSet',
    )


class Language(Intangible):
    field_type: Literal['https://schema.org/Language'] = Field(
        'https://schema.org/Language', alias='@type'
    )


class Enumeration(Intangible):
    field_type: Literal['https://schema.org/Enumeration'] = Field(
        'https://schema.org/Enumeration', alias='@type'
    )
    superseded_by: Optional[
        Union[Enumeration, Class, Property, List[Union[Enumeration, Class, Property]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'supersededBy', 'https://schema.org/supersededBy'
        ),
        serialization_alias='https://schema.org/supersededBy',
    )


class Class(Intangible):
    field_type: Literal['https://schema.org/Class'] = Field(
        'https://schema.org/Class', alias='@type'
    )
    superseded_by: Optional[
        Union[Enumeration, Class, Property, List[Union[Enumeration, Class, Property]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'supersededBy', 'https://schema.org/supersededBy'
        ),
        serialization_alias='https://schema.org/supersededBy',
    )


class Property(Intangible):
    field_type: Literal['https://schema.org/Property'] = Field(
        'https://schema.org/Property', alias='@type'
    )
    superseded_by: Optional[
        Union[Enumeration, Class, Property, List[Union[Enumeration, Class, Property]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'supersededBy', 'https://schema.org/supersededBy'
        ),
        serialization_alias='https://schema.org/supersededBy',
    )
    range_includes: Optional[Union[Class, List[Class]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'rangeIncludes', 'https://schema.org/rangeIncludes'
        ),
        serialization_alias='https://schema.org/rangeIncludes',
    )
    inverse_of: Optional[Union[Property, List[Property]]] = Field(
        default=None,
        validation_alias=AliasChoices('inverseOf', 'https://schema.org/inverseOf'),
        serialization_alias='https://schema.org/inverseOf',
    )
    domain_includes: Optional[Union[Class, List[Class]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'domainIncludes', 'https://schema.org/domainIncludes'
        ),
        serialization_alias='https://schema.org/domainIncludes',
    )


class PaymentMethod(Intangible):
    field_type: Literal['https://schema.org/PaymentMethod'] = Field(
        'https://schema.org/PaymentMethod', alias='@type'
    )
    payment_method_type: Optional[
        Union[PaymentMethodType, List[PaymentMethodType]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'paymentMethodType', 'https://schema.org/paymentMethodType'
        ),
        serialization_alias='https://schema.org/paymentMethodType',
    )


class Service(Intangible):
    field_type: Literal['https://schema.org/Service'] = Field(
        'https://schema.org/Service', alias='@type'
    )
    slogan: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices('slogan', 'https://schema.org/slogan'),
        serialization_alias='https://schema.org/slogan',
    )
    logo: Optional[
        Union[AnyUrl, ImageObject, List[Union[AnyUrl, ImageObject]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('logo', 'https://schema.org/logo'),
        serialization_alias='https://schema.org/logo',
    )
    audience: Optional[Union[Audience, List[Audience]]] = Field(
        default=None,
        validation_alias=AliasChoices('audience', 'https://schema.org/audience'),
        serialization_alias='https://schema.org/audience',
    )
    produces: Optional[Union[Thing, List[Thing]]] = Field(
        default=None,
        validation_alias=AliasChoices('produces', 'https://schema.org/produces'),
        serialization_alias='https://schema.org/produces',
    )
    hours_available: Optional[
        Union[OpeningHoursSpecification, List[OpeningHoursSpecification]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'hoursAvailable', 'https://schema.org/hoursAvailable'
        ),
        serialization_alias='https://schema.org/hoursAvailable',
    )
    service_audience: Optional[Union[Audience, List[Audience]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'serviceAudience', 'https://schema.org/serviceAudience'
        ),
        serialization_alias='https://schema.org/serviceAudience',
    )
    terms_of_service: Optional[Union[AnyUrl, str, List[Union[AnyUrl, str]]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'termsOfService', 'https://schema.org/termsOfService'
        ),
        serialization_alias='https://schema.org/termsOfService',
    )
    award: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices('award', 'https://schema.org/award'),
        serialization_alias='https://schema.org/award',
    )
    available_channel: Optional[Union[ServiceChannel, List[ServiceChannel]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'availableChannel', 'https://schema.org/availableChannel'
        ),
        serialization_alias='https://schema.org/availableChannel',
    )
    is_similar_to: Optional[
        Union[Service, Product, List[Union[Service, Product]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('isSimilarTo', 'https://schema.org/isSimilarTo'),
        serialization_alias='https://schema.org/isSimilarTo',
    )
    offers: Optional[Union[Demand, Offer, List[Union[Demand, Offer]]]] = Field(
        default=None,
        validation_alias=AliasChoices('offers', 'https://schema.org/offers'),
        serialization_alias='https://schema.org/offers',
    )
    provider_mobility: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'providerMobility', 'https://schema.org/providerMobility'
        ),
        serialization_alias='https://schema.org/providerMobility',
    )
    brand: Optional[
        Union[Organization, Brand, List[Union[Organization, Brand]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('brand', 'https://schema.org/brand'),
        serialization_alias='https://schema.org/brand',
    )
    review: Optional[Union[Review, List[Review]]] = Field(
        default=None,
        validation_alias=AliasChoices('review', 'https://schema.org/review'),
        serialization_alias='https://schema.org/review',
    )
    broker: Optional[
        Union[Person, Organization, List[Union[Person, Organization]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('broker', 'https://schema.org/broker'),
        serialization_alias='https://schema.org/broker',
    )
    provider: Optional[
        Union[Person, Organization, List[Union[Person, Organization]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('provider', 'https://schema.org/provider'),
        serialization_alias='https://schema.org/provider',
    )
    category: Optional[
        Union[
            PhysicalActivityCategory,
            CategoryCode,
            str,
            Thing,
            AnyUrl,
            List[Union[PhysicalActivityCategory, CategoryCode, str, Thing, AnyUrl]],
        ]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('category', 'https://schema.org/category'),
        serialization_alias='https://schema.org/category',
    )
    service_area: Optional[
        Union[
            AdministrativeArea,
            GeoShape,
            Place,
            List[Union[AdministrativeArea, GeoShape, Place]],
        ]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('serviceArea', 'https://schema.org/serviceArea'),
        serialization_alias='https://schema.org/serviceArea',
    )
    has_offer_catalog: Optional[Union[OfferCatalog, List[OfferCatalog]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'hasOfferCatalog', 'https://schema.org/hasOfferCatalog'
        ),
        serialization_alias='https://schema.org/hasOfferCatalog',
    )
    has_certification: Optional[Union[Certification, List[Certification]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'hasCertification', 'https://schema.org/hasCertification'
        ),
        serialization_alias='https://schema.org/hasCertification',
    )
    service_type: Optional[
        Union[GovernmentBenefitsType, str, List[Union[GovernmentBenefitsType, str]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('serviceType', 'https://schema.org/serviceType'),
        serialization_alias='https://schema.org/serviceType',
    )
    aggregate_rating: Optional[Union[AggregateRating, List[AggregateRating]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'aggregateRating', 'https://schema.org/aggregateRating'
        ),
        serialization_alias='https://schema.org/aggregateRating',
    )
    area_served: Optional[
        Union[
            GeoShape,
            str,
            AdministrativeArea,
            Place,
            List[Union[GeoShape, str, AdministrativeArea, Place]],
        ]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('areaServed', 'https://schema.org/areaServed'),
        serialization_alias='https://schema.org/areaServed',
    )
    is_related_to: Optional[
        Union[Service, Product, List[Union[Service, Product]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('isRelatedTo', 'https://schema.org/isRelatedTo'),
        serialization_alias='https://schema.org/isRelatedTo',
    )
    service_output: Optional[Union[Thing, List[Thing]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'serviceOutput', 'https://schema.org/serviceOutput'
        ),
        serialization_alias='https://schema.org/serviceOutput',
    )


class Quantity(Intangible):
    field_type: Literal['https://schema.org/Quantity'] = Field(
        'https://schema.org/Quantity', alias='@type'
    )


class Rating(Intangible):
    field_type: Literal['https://schema.org/Rating'] = Field(
        'https://schema.org/Rating', alias='@type'
    )
    best_rating: Optional[Union[str, float, List[Union[str, float]]]] = Field(
        default=None,
        validation_alias=AliasChoices('bestRating', 'https://schema.org/bestRating'),
        serialization_alias='https://schema.org/bestRating',
    )
    review_aspect: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'reviewAspect', 'https://schema.org/reviewAspect'
        ),
        serialization_alias='https://schema.org/reviewAspect',
    )
    author: Optional[
        Union[Person, Organization, List[Union[Person, Organization]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('author', 'https://schema.org/author'),
        serialization_alias='https://schema.org/author',
    )
    rating_value: Optional[Union[str, float, List[Union[str, float]]]] = Field(
        default=None,
        validation_alias=AliasChoices('ratingValue', 'https://schema.org/ratingValue'),
        serialization_alias='https://schema.org/ratingValue',
    )
    worst_rating: Optional[Union[str, float, List[Union[str, float]]]] = Field(
        default=None,
        validation_alias=AliasChoices('worstRating', 'https://schema.org/worstRating'),
        serialization_alias='https://schema.org/worstRating',
    )
    rating_explanation: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'ratingExplanation', 'https://schema.org/ratingExplanation'
        ),
        serialization_alias='https://schema.org/ratingExplanation',
    )


class Schedule(Intangible):
    field_type: Literal['https://schema.org/Schedule'] = Field(
        'https://schema.org/Schedule', alias='@type'
    )
    schedule_timezone: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'scheduleTimezone', 'https://schema.org/scheduleTimezone'
        ),
        serialization_alias='https://schema.org/scheduleTimezone',
    )
    repeat_frequency: Optional[
        Union[str, Duration, List[Union[str, Duration]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'repeatFrequency', 'https://schema.org/repeatFrequency'
        ),
        serialization_alias='https://schema.org/repeatFrequency',
    )
    end_date: Optional[
        Union[AwareDatetime, date, List[Union[AwareDatetime, date]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('endDate', 'https://schema.org/endDate'),
        serialization_alias='https://schema.org/endDate',
    )
    except_date: Optional[
        Union[AwareDatetime, date, List[Union[AwareDatetime, date]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('exceptDate', 'https://schema.org/exceptDate'),
        serialization_alias='https://schema.org/exceptDate',
    )
    by_day: Optional[Union[str, DayOfWeek, List[Union[str, DayOfWeek]]]] = Field(
        default=None,
        validation_alias=AliasChoices('byDay', 'https://schema.org/byDay'),
        serialization_alias='https://schema.org/byDay',
    )
    by_month_day: Optional[Union[int, List[int]]] = Field(
        default=None,
        validation_alias=AliasChoices('byMonthDay', 'https://schema.org/byMonthDay'),
        serialization_alias='https://schema.org/byMonthDay',
    )
    end_time: Optional[
        Union[time, AwareDatetime, List[Union[time, AwareDatetime]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('endTime', 'https://schema.org/endTime'),
        serialization_alias='https://schema.org/endTime',
    )
    start_date: Optional[
        Union[date, AwareDatetime, List[Union[date, AwareDatetime]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('startDate', 'https://schema.org/startDate'),
        serialization_alias='https://schema.org/startDate',
    )
    duration: Optional[
        Union[Duration, QuantitativeValue, List[Union[Duration, QuantitativeValue]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('duration', 'https://schema.org/duration'),
        serialization_alias='https://schema.org/duration',
    )
    repeat_count: Optional[Union[int, List[int]]] = Field(
        default=None,
        validation_alias=AliasChoices('repeatCount', 'https://schema.org/repeatCount'),
        serialization_alias='https://schema.org/repeatCount',
    )
    by_month_week: Optional[Union[int, List[int]]] = Field(
        default=None,
        validation_alias=AliasChoices('byMonthWeek', 'https://schema.org/byMonthWeek'),
        serialization_alias='https://schema.org/byMonthWeek',
    )
    by_month: Optional[Union[int, List[int]]] = Field(
        default=None,
        validation_alias=AliasChoices('byMonth', 'https://schema.org/byMonth'),
        serialization_alias='https://schema.org/byMonth',
    )
    start_time: Optional[
        Union[time, AwareDatetime, List[Union[time, AwareDatetime]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('startTime', 'https://schema.org/startTime'),
        serialization_alias='https://schema.org/startTime',
    )


class VirtualLocation(Intangible):
    field_type: Literal['https://schema.org/VirtualLocation'] = Field(
        'https://schema.org/VirtualLocation', alias='@type'
    )


class ItemList(Intangible):
    field_type: Literal['https://schema.org/ItemList'] = Field(
        'https://schema.org/ItemList', alias='@type'
    )
    number_of_items: Optional[Union[int, List[int]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'numberOfItems', 'https://schema.org/numberOfItems'
        ),
        serialization_alias='https://schema.org/numberOfItems',
    )
    aggregate_element: Optional[Union[Thing, List[Thing]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'aggregateElement', 'https://schema.org/aggregateElement'
        ),
        serialization_alias='https://schema.org/aggregateElement',
    )
    item_list_order: Optional[
        Union[ItemListOrderType, str, List[Union[ItemListOrderType, str]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'itemListOrder', 'https://schema.org/itemListOrder'
        ),
        serialization_alias='https://schema.org/itemListOrder',
    )
    item_list_element: Optional[
        Union[str, Thing, ListItem, List[Union[str, Thing, ListItem]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'itemListElement', 'https://schema.org/itemListElement'
        ),
        serialization_alias='https://schema.org/itemListElement',
    )


class ListItem(Intangible):
    field_type: Literal['https://schema.org/ListItem'] = Field(
        'https://schema.org/ListItem', alias='@type'
    )
    position: Optional[Union[int, str, List[Union[int, str]]]] = Field(
        default=None,
        validation_alias=AliasChoices('position', 'https://schema.org/position'),
        serialization_alias='https://schema.org/position',
    )
    next_item: Optional[Union[ListItem, List[ListItem]]] = Field(
        default=None,
        validation_alias=AliasChoices('nextItem', 'https://schema.org/nextItem'),
        serialization_alias='https://schema.org/nextItem',
    )
    item: Optional[Union[Thing, List[Thing]]] = Field(
        default=None,
        validation_alias=AliasChoices('item', 'https://schema.org/item'),
        serialization_alias='https://schema.org/item',
    )
    previous_item: Optional[Union[ListItem, List[ListItem]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'previousItem', 'https://schema.org/previousItem'
        ),
        serialization_alias='https://schema.org/previousItem',
    )


class ProductReturnPolicy(Intangible):
    field_type: Literal['https://schema.org/ProductReturnPolicy'] = Field(
        'https://schema.org/ProductReturnPolicy', alias='@type'
    )
    product_return_days: Optional[Union[int, List[int]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'productReturnDays', 'https://schema.org/productReturnDays'
        ),
        serialization_alias='https://schema.org/productReturnDays',
    )
    product_return_link: Optional[Union[AnyUrl, List[AnyUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'productReturnLink', 'https://schema.org/productReturnLink'
        ),
        serialization_alias='https://schema.org/productReturnLink',
    )


class Demand(Intangible):
    field_type: Literal['https://schema.org/Demand'] = Field(
        'https://schema.org/Demand', alias='@type'
    )
    availability_ends: Optional[
        Union[date, time, AwareDatetime, List[Union[date, time, AwareDatetime]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'availabilityEnds', 'https://schema.org/availabilityEnds'
        ),
        serialization_alias='https://schema.org/availabilityEnds',
    )
    sku: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices('sku', 'https://schema.org/sku'),
        serialization_alias='https://schema.org/sku',
    )
    eligible_transaction_volume: Optional[
        Union[PriceSpecification, List[PriceSpecification]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'eligibleTransactionVolume', 'https://schema.org/eligibleTransactionVolume'
        ),
        serialization_alias='https://schema.org/eligibleTransactionVolume',
    )
    includes_object: Optional[
        Union[TypeAndQuantityNode, List[TypeAndQuantityNode]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'includesObject', 'https://schema.org/includesObject'
        ),
        serialization_alias='https://schema.org/includesObject',
    )
    eligible_customer_type: Optional[
        Union[BusinessEntityType, List[BusinessEntityType]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'eligibleCustomerType', 'https://schema.org/eligibleCustomerType'
        ),
        serialization_alias='https://schema.org/eligibleCustomerType',
    )
    available_delivery_method: Optional[
        Union[DeliveryMethod, List[DeliveryMethod]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'availableDeliveryMethod', 'https://schema.org/availableDeliveryMethod'
        ),
        serialization_alias='https://schema.org/availableDeliveryMethod',
    )
    valid_from: Optional[
        Union[date, AwareDatetime, List[Union[date, AwareDatetime]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('validFrom', 'https://schema.org/validFrom'),
        serialization_alias='https://schema.org/validFrom',
    )
    delivery_lead_time: Optional[
        Union[QuantitativeValue, List[QuantitativeValue]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'deliveryLeadTime', 'https://schema.org/deliveryLeadTime'
        ),
        serialization_alias='https://schema.org/deliveryLeadTime',
    )
    ineligible_region: Optional[
        Union[str, Place, GeoShape, List[Union[str, Place, GeoShape]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'ineligibleRegion', 'https://schema.org/ineligibleRegion'
        ),
        serialization_alias='https://schema.org/ineligibleRegion',
    )
    gtin13: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices('gtin13', 'https://schema.org/gtin13'),
        serialization_alias='https://schema.org/gtin13',
    )
    advance_booking_requirement: Optional[
        Union[QuantitativeValue, List[QuantitativeValue]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'advanceBookingRequirement', 'https://schema.org/advanceBookingRequirement'
        ),
        serialization_alias='https://schema.org/advanceBookingRequirement',
    )
    inventory_level: Optional[
        Union[QuantitativeValue, List[QuantitativeValue]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'inventoryLevel', 'https://schema.org/inventoryLevel'
        ),
        serialization_alias='https://schema.org/inventoryLevel',
    )
    accepted_payment_method: Optional[
        Union[
            str,
            PaymentMethod,
            LoanOrCredit,
            List[Union[str, PaymentMethod, LoanOrCredit]],
        ]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'acceptedPaymentMethod', 'https://schema.org/acceptedPaymentMethod'
        ),
        serialization_alias='https://schema.org/acceptedPaymentMethod',
    )
    item_condition: Optional[
        Union[OfferItemCondition, List[OfferItemCondition]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'itemCondition', 'https://schema.org/itemCondition'
        ),
        serialization_alias='https://schema.org/itemCondition',
    )
    availability_starts: Optional[
        Union[AwareDatetime, date, time, List[Union[AwareDatetime, date, time]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'availabilityStarts', 'https://schema.org/availabilityStarts'
        ),
        serialization_alias='https://schema.org/availabilityStarts',
    )
    mpn: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices('mpn', 'https://schema.org/mpn'),
        serialization_alias='https://schema.org/mpn',
    )
    availability: Optional[Union[ItemAvailability, List[ItemAvailability]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'availability', 'https://schema.org/availability'
        ),
        serialization_alias='https://schema.org/availability',
    )
    gtin14: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices('gtin14', 'https://schema.org/gtin14'),
        serialization_alias='https://schema.org/gtin14',
    )
    serial_number: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'serialNumber', 'https://schema.org/serialNumber'
        ),
        serialization_alias='https://schema.org/serialNumber',
    )
    available_at_or_from: Optional[Union[Place, List[Place]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'availableAtOrFrom', 'https://schema.org/availableAtOrFrom'
        ),
        serialization_alias='https://schema.org/availableAtOrFrom',
    )
    gtin12: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices('gtin12', 'https://schema.org/gtin12'),
        serialization_alias='https://schema.org/gtin12',
    )
    business_function: Optional[
        Union[BusinessFunction, List[BusinessFunction]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'businessFunction', 'https://schema.org/businessFunction'
        ),
        serialization_alias='https://schema.org/businessFunction',
    )
    gtin8: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices('gtin8', 'https://schema.org/gtin8'),
        serialization_alias='https://schema.org/gtin8',
    )
    eligible_quantity: Optional[
        Union[QuantitativeValue, List[QuantitativeValue]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'eligibleQuantity', 'https://schema.org/eligibleQuantity'
        ),
        serialization_alias='https://schema.org/eligibleQuantity',
    )
    eligible_duration: Optional[
        Union[QuantitativeValue, List[QuantitativeValue]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'eligibleDuration', 'https://schema.org/eligibleDuration'
        ),
        serialization_alias='https://schema.org/eligibleDuration',
    )
    item_offered: Optional[
        Union[
            Event,
            Service,
            AggregateOffer,
            Product,
            MenuItem,
            CreativeWork,
            Trip,
            List[
                Union[
                    Event,
                    Service,
                    AggregateOffer,
                    Product,
                    MenuItem,
                    CreativeWork,
                    Trip,
                ]
            ],
        ]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('itemOffered', 'https://schema.org/itemOffered'),
        serialization_alias='https://schema.org/itemOffered',
    )
    eligible_region: Optional[
        Union[GeoShape, str, Place, List[Union[GeoShape, str, Place]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'eligibleRegion', 'https://schema.org/eligibleRegion'
        ),
        serialization_alias='https://schema.org/eligibleRegion',
    )
    price_specification: Optional[
        Union[PriceSpecification, List[PriceSpecification]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'priceSpecification', 'https://schema.org/priceSpecification'
        ),
        serialization_alias='https://schema.org/priceSpecification',
    )
    gtin: Optional[Union[str, AnyUrl, List[Union[str, AnyUrl]]]] = Field(
        default=None,
        validation_alias=AliasChoices('gtin', 'https://schema.org/gtin'),
        serialization_alias='https://schema.org/gtin',
    )
    area_served: Optional[
        Union[
            GeoShape,
            str,
            AdministrativeArea,
            Place,
            List[Union[GeoShape, str, AdministrativeArea, Place]],
        ]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('areaServed', 'https://schema.org/areaServed'),
        serialization_alias='https://schema.org/areaServed',
    )
    asin: Optional[Union[AnyUrl, str, List[Union[AnyUrl, str]]]] = Field(
        default=None,
        validation_alias=AliasChoices('asin', 'https://schema.org/asin'),
        serialization_alias='https://schema.org/asin',
    )
    seller: Optional[
        Union[Organization, Person, List[Union[Organization, Person]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('seller', 'https://schema.org/seller'),
        serialization_alias='https://schema.org/seller',
    )
    valid_through: Optional[
        Union[AwareDatetime, date, List[Union[AwareDatetime, date]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'validThrough', 'https://schema.org/validThrough'
        ),
        serialization_alias='https://schema.org/validThrough',
    )
    warranty: Optional[Union[WarrantyPromise, List[WarrantyPromise]]] = Field(
        default=None,
        validation_alias=AliasChoices('warranty', 'https://schema.org/warranty'),
        serialization_alias='https://schema.org/warranty',
    )


class MemberProgramTier(Intangible):
    field_type: Literal['https://schema.org/MemberProgramTier'] = Field(
        'https://schema.org/MemberProgramTier', alias='@type'
    )
    membership_points_earned: Optional[
        Union[QuantitativeValue, float, List[Union[QuantitativeValue, float]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'membershipPointsEarned', 'https://schema.org/membershipPointsEarned'
        ),
        serialization_alias='https://schema.org/membershipPointsEarned',
    )
    has_tier_benefit: Optional[
        Union[TierBenefitEnumeration, List[TierBenefitEnumeration]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'hasTierBenefit', 'https://schema.org/hasTierBenefit'
        ),
        serialization_alias='https://schema.org/hasTierBenefit',
    )
    is_tier_of: Optional[Union[MemberProgram, List[MemberProgram]]] = Field(
        default=None,
        validation_alias=AliasChoices('isTierOf', 'https://schema.org/isTierOf'),
        serialization_alias='https://schema.org/isTierOf',
    )
    has_tier_requirement: Optional[
        Union[
            MonetaryAmount,
            CreditCard,
            str,
            UnitPriceSpecification,
            List[Union[MonetaryAmount, CreditCard, str, UnitPriceSpecification]],
        ]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'hasTierRequirement', 'https://schema.org/hasTierRequirement'
        ),
        serialization_alias='https://schema.org/hasTierRequirement',
    )


class MemberProgram(Intangible):
    field_type: Literal['https://schema.org/MemberProgram'] = Field(
        'https://schema.org/MemberProgram', alias='@type'
    )
    hosting_organization: Optional[Union[Organization, List[Organization]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'hostingOrganization', 'https://schema.org/hostingOrganization'
        ),
        serialization_alias='https://schema.org/hostingOrganization',
    )
    has_tiers: Optional[Union[MemberProgramTier, List[MemberProgramTier]]] = Field(
        default=None,
        validation_alias=AliasChoices('hasTiers', 'https://schema.org/hasTiers'),
        serialization_alias='https://schema.org/hasTiers',
    )


class Offer(Intangible):
    field_type: Literal['https://schema.org/Offer'] = Field(
        'https://schema.org/Offer', alias='@type'
    )
    asin: Optional[Union[AnyUrl, str, List[Union[AnyUrl, str]]]] = Field(
        default=None,
        validation_alias=AliasChoices('asin', 'https://schema.org/asin'),
        serialization_alias='https://schema.org/asin',
    )
    has_adult_consideration: Optional[
        Union[AdultOrientedEnumeration, List[AdultOrientedEnumeration]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'hasAdultConsideration', 'https://schema.org/hasAdultConsideration'
        ),
        serialization_alias='https://schema.org/hasAdultConsideration',
    )
    eligible_transaction_volume: Optional[
        Union[PriceSpecification, List[PriceSpecification]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'eligibleTransactionVolume', 'https://schema.org/eligibleTransactionVolume'
        ),
        serialization_alias='https://schema.org/eligibleTransactionVolume',
    )
    includes_object: Optional[
        Union[TypeAndQuantityNode, List[TypeAndQuantityNode]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'includesObject', 'https://schema.org/includesObject'
        ),
        serialization_alias='https://schema.org/includesObject',
    )
    eligible_customer_type: Optional[
        Union[BusinessEntityType, List[BusinessEntityType]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'eligibleCustomerType', 'https://schema.org/eligibleCustomerType'
        ),
        serialization_alias='https://schema.org/eligibleCustomerType',
    )
    shipping_details: Optional[
        Union[OfferShippingDetails, List[OfferShippingDetails]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'shippingDetails', 'https://schema.org/shippingDetails'
        ),
        serialization_alias='https://schema.org/shippingDetails',
    )
    availability_ends: Optional[
        Union[date, time, AwareDatetime, List[Union[date, time, AwareDatetime]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'availabilityEnds', 'https://schema.org/availabilityEnds'
        ),
        serialization_alias='https://schema.org/availabilityEnds',
    )
    available_delivery_method: Optional[
        Union[DeliveryMethod, List[DeliveryMethod]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'availableDeliveryMethod', 'https://schema.org/availableDeliveryMethod'
        ),
        serialization_alias='https://schema.org/availableDeliveryMethod',
    )
    valid_from: Optional[
        Union[date, AwareDatetime, List[Union[date, AwareDatetime]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('validFrom', 'https://schema.org/validFrom'),
        serialization_alias='https://schema.org/validFrom',
    )
    mobile_url: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices('mobileUrl', 'https://schema.org/mobileUrl'),
        serialization_alias='https://schema.org/mobileUrl',
    )
    valid_for_member_tier: Optional[
        Union[MemberProgramTier, List[MemberProgramTier]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'validForMemberTier', 'https://schema.org/validForMemberTier'
        ),
        serialization_alias='https://schema.org/validForMemberTier',
    )
    delivery_lead_time: Optional[
        Union[QuantitativeValue, List[QuantitativeValue]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'deliveryLeadTime', 'https://schema.org/deliveryLeadTime'
        ),
        serialization_alias='https://schema.org/deliveryLeadTime',
    )
    is_family_friendly: Optional[Union[bool, List[bool]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'isFamilyFriendly', 'https://schema.org/isFamilyFriendly'
        ),
        serialization_alias='https://schema.org/isFamilyFriendly',
    )
    ineligible_region: Optional[
        Union[str, Place, GeoShape, List[Union[str, Place, GeoShape]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'ineligibleRegion', 'https://schema.org/ineligibleRegion'
        ),
        serialization_alias='https://schema.org/ineligibleRegion',
    )
    gtin13: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices('gtin13', 'https://schema.org/gtin13'),
        serialization_alias='https://schema.org/gtin13',
    )
    has_gs1_digital_link: Optional[Union[AnyUrl, List[AnyUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'hasGS1DigitalLink', 'https://schema.org/hasGS1DigitalLink'
        ),
        serialization_alias='https://schema.org/hasGS1DigitalLink',
    )
    has_measurement: Optional[
        Union[QuantitativeValue, List[QuantitativeValue]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'hasMeasurement', 'https://schema.org/hasMeasurement'
        ),
        serialization_alias='https://schema.org/hasMeasurement',
    )
    inventory_level: Optional[
        Union[QuantitativeValue, List[QuantitativeValue]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'inventoryLevel', 'https://schema.org/inventoryLevel'
        ),
        serialization_alias='https://schema.org/inventoryLevel',
    )
    item_condition: Optional[
        Union[OfferItemCondition, List[OfferItemCondition]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'itemCondition', 'https://schema.org/itemCondition'
        ),
        serialization_alias='https://schema.org/itemCondition',
    )
    price: Optional[Union[str, float, List[Union[str, float]]]] = Field(
        default=None,
        validation_alias=AliasChoices('price', 'https://schema.org/price'),
        serialization_alias='https://schema.org/price',
    )
    additional_property: Optional[Union[PropertyValue, List[PropertyValue]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'additionalProperty', 'https://schema.org/additionalProperty'
        ),
        serialization_alias='https://schema.org/additionalProperty',
    )
    checkout_page_url_template: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'checkoutPageURLTemplate', 'https://schema.org/checkoutPageURLTemplate'
        ),
        serialization_alias='https://schema.org/checkoutPageURLTemplate',
    )
    category: Optional[
        Union[
            PhysicalActivityCategory,
            CategoryCode,
            str,
            Thing,
            AnyUrl,
            List[Union[PhysicalActivityCategory, CategoryCode, str, Thing, AnyUrl]],
        ]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('category', 'https://schema.org/category'),
        serialization_alias='https://schema.org/category',
    )
    has_merchant_return_policy: Optional[
        Union[MerchantReturnPolicy, List[MerchantReturnPolicy]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'hasMerchantReturnPolicy', 'https://schema.org/hasMerchantReturnPolicy'
        ),
        serialization_alias='https://schema.org/hasMerchantReturnPolicy',
    )
    price_currency: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'priceCurrency', 'https://schema.org/priceCurrency'
        ),
        serialization_alias='https://schema.org/priceCurrency',
    )
    availability: Optional[Union[ItemAvailability, List[ItemAvailability]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'availability', 'https://schema.org/availability'
        ),
        serialization_alias='https://schema.org/availability',
    )
    gtin14: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices('gtin14', 'https://schema.org/gtin14'),
        serialization_alias='https://schema.org/gtin14',
    )
    price_valid_until: Optional[Union[date, List[date]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'priceValidUntil', 'https://schema.org/priceValidUntil'
        ),
        serialization_alias='https://schema.org/priceValidUntil',
    )
    serial_number: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'serialNumber', 'https://schema.org/serialNumber'
        ),
        serialization_alias='https://schema.org/serialNumber',
    )
    advance_booking_requirement: Optional[
        Union[QuantitativeValue, List[QuantitativeValue]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'advanceBookingRequirement', 'https://schema.org/advanceBookingRequirement'
        ),
        serialization_alias='https://schema.org/advanceBookingRequirement',
    )
    gtin12: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices('gtin12', 'https://schema.org/gtin12'),
        serialization_alias='https://schema.org/gtin12',
    )
    accepted_payment_method: Optional[
        Union[
            str,
            PaymentMethod,
            LoanOrCredit,
            List[Union[str, PaymentMethod, LoanOrCredit]],
        ]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'acceptedPaymentMethod', 'https://schema.org/acceptedPaymentMethod'
        ),
        serialization_alias='https://schema.org/acceptedPaymentMethod',
    )
    review: Optional[Union[Review, List[Review]]] = Field(
        default=None,
        validation_alias=AliasChoices('review', 'https://schema.org/review'),
        serialization_alias='https://schema.org/review',
    )
    availability_starts: Optional[
        Union[AwareDatetime, date, time, List[Union[AwareDatetime, date, time]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'availabilityStarts', 'https://schema.org/availabilityStarts'
        ),
        serialization_alias='https://schema.org/availabilityStarts',
    )
    mpn: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices('mpn', 'https://schema.org/mpn'),
        serialization_alias='https://schema.org/mpn',
    )
    lease_length: Optional[
        Union[QuantitativeValue, Duration, List[Union[QuantitativeValue, Duration]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('leaseLength', 'https://schema.org/leaseLength'),
        serialization_alias='https://schema.org/leaseLength',
    )
    price_specification: Optional[
        Union[PriceSpecification, List[PriceSpecification]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'priceSpecification', 'https://schema.org/priceSpecification'
        ),
        serialization_alias='https://schema.org/priceSpecification',
    )
    reviews: Optional[Union[Review, List[Review]]] = Field(
        default=None,
        validation_alias=AliasChoices('reviews', 'https://schema.org/reviews'),
        serialization_alias='https://schema.org/reviews',
    )
    gtin: Optional[Union[str, AnyUrl, List[Union[str, AnyUrl]]]] = Field(
        default=None,
        validation_alias=AliasChoices('gtin', 'https://schema.org/gtin'),
        serialization_alias='https://schema.org/gtin',
    )
    available_at_or_from: Optional[Union[Place, List[Place]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'availableAtOrFrom', 'https://schema.org/availableAtOrFrom'
        ),
        serialization_alias='https://schema.org/availableAtOrFrom',
    )
    add_on: Optional[Union[Offer, List[Offer]]] = Field(
        default=None,
        validation_alias=AliasChoices('addOn', 'https://schema.org/addOn'),
        serialization_alias='https://schema.org/addOn',
    )
    business_function: Optional[
        Union[BusinessFunction, List[BusinessFunction]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'businessFunction', 'https://schema.org/businessFunction'
        ),
        serialization_alias='https://schema.org/businessFunction',
    )
    gtin8: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices('gtin8', 'https://schema.org/gtin8'),
        serialization_alias='https://schema.org/gtin8',
    )
    seller: Optional[
        Union[Organization, Person, List[Union[Organization, Person]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('seller', 'https://schema.org/seller'),
        serialization_alias='https://schema.org/seller',
    )
    valid_through: Optional[
        Union[AwareDatetime, date, List[Union[AwareDatetime, date]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'validThrough', 'https://schema.org/validThrough'
        ),
        serialization_alias='https://schema.org/validThrough',
    )
    eligible_quantity: Optional[
        Union[QuantitativeValue, List[QuantitativeValue]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'eligibleQuantity', 'https://schema.org/eligibleQuantity'
        ),
        serialization_alias='https://schema.org/eligibleQuantity',
    )
    eligible_duration: Optional[
        Union[QuantitativeValue, List[QuantitativeValue]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'eligibleDuration', 'https://schema.org/eligibleDuration'
        ),
        serialization_alias='https://schema.org/eligibleDuration',
    )
    item_offered: Optional[
        Union[
            Event,
            Service,
            AggregateOffer,
            Product,
            MenuItem,
            CreativeWork,
            Trip,
            List[
                Union[
                    Event,
                    Service,
                    AggregateOffer,
                    Product,
                    MenuItem,
                    CreativeWork,
                    Trip,
                ]
            ],
        ]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('itemOffered', 'https://schema.org/itemOffered'),
        serialization_alias='https://schema.org/itemOffered',
    )
    warranty: Optional[Union[WarrantyPromise, List[WarrantyPromise]]] = Field(
        default=None,
        validation_alias=AliasChoices('warranty', 'https://schema.org/warranty'),
        serialization_alias='https://schema.org/warranty',
    )
    eligible_region: Optional[
        Union[GeoShape, str, Place, List[Union[GeoShape, str, Place]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'eligibleRegion', 'https://schema.org/eligibleRegion'
        ),
        serialization_alias='https://schema.org/eligibleRegion',
    )
    offered_by: Optional[
        Union[Organization, Person, List[Union[Organization, Person]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('offeredBy', 'https://schema.org/offeredBy'),
        serialization_alias='https://schema.org/offeredBy',
    )
    aggregate_rating: Optional[Union[AggregateRating, List[AggregateRating]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'aggregateRating', 'https://schema.org/aggregateRating'
        ),
        serialization_alias='https://schema.org/aggregateRating',
    )
    sku: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices('sku', 'https://schema.org/sku'),
        serialization_alias='https://schema.org/sku',
    )
    area_served: Optional[
        Union[
            GeoShape,
            str,
            AdministrativeArea,
            Place,
            List[Union[GeoShape, str, AdministrativeArea, Place]],
        ]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('areaServed', 'https://schema.org/areaServed'),
        serialization_alias='https://schema.org/areaServed',
    )


class MerchantReturnPolicy(Intangible):
    field_type: Literal['https://schema.org/MerchantReturnPolicy'] = Field(
        'https://schema.org/MerchantReturnPolicy', alias='@type'
    )
    additional_property: Optional[Union[PropertyValue, List[PropertyValue]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'additionalProperty', 'https://schema.org/additionalProperty'
        ),
        serialization_alias='https://schema.org/additionalProperty',
    )
    customer_remorse_return_shipping_fees_amount: Optional[
        Union[MonetaryAmount, List[MonetaryAmount]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'customerRemorseReturnShippingFeesAmount',
            'https://schema.org/customerRemorseReturnShippingFeesAmount',
        ),
        serialization_alias='https://schema.org/customerRemorseReturnShippingFeesAmount',
    )
    merchant_return_link: Optional[Union[AnyUrl, List[AnyUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'merchantReturnLink', 'https://schema.org/merchantReturnLink'
        ),
        serialization_alias='https://schema.org/merchantReturnLink',
    )
    return_policy_country: Optional[
        Union[str, Country, List[Union[str, Country]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'returnPolicyCountry', 'https://schema.org/returnPolicyCountry'
        ),
        serialization_alias='https://schema.org/returnPolicyCountry',
    )
    merchant_return_days: Optional[
        Union[date, int, AwareDatetime, List[Union[date, int, AwareDatetime]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'merchantReturnDays', 'https://schema.org/merchantReturnDays'
        ),
        serialization_alias='https://schema.org/merchantReturnDays',
    )
    refund_type: Optional[
        Union[RefundTypeEnumeration, List[RefundTypeEnumeration]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('refundType', 'https://schema.org/refundType'),
        serialization_alias='https://schema.org/refundType',
    )
    return_method: Optional[
        Union[ReturnMethodEnumeration, List[ReturnMethodEnumeration]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'returnMethod', 'https://schema.org/returnMethod'
        ),
        serialization_alias='https://schema.org/returnMethod',
    )
    in_store_returns_offered: Optional[Union[bool, List[bool]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'inStoreReturnsOffered', 'https://schema.org/inStoreReturnsOffered'
        ),
        serialization_alias='https://schema.org/inStoreReturnsOffered',
    )
    item_defect_return_fees: Optional[
        Union[ReturnFeesEnumeration, List[ReturnFeesEnumeration]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'itemDefectReturnFees', 'https://schema.org/itemDefectReturnFees'
        ),
        serialization_alias='https://schema.org/itemDefectReturnFees',
    )
    customer_remorse_return_fees: Optional[
        Union[ReturnFeesEnumeration, List[ReturnFeesEnumeration]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'customerRemorseReturnFees', 'https://schema.org/customerRemorseReturnFees'
        ),
        serialization_alias='https://schema.org/customerRemorseReturnFees',
    )
    item_defect_return_shipping_fees_amount: Optional[
        Union[MonetaryAmount, List[MonetaryAmount]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'itemDefectReturnShippingFeesAmount',
            'https://schema.org/itemDefectReturnShippingFeesAmount',
        ),
        serialization_alias='https://schema.org/itemDefectReturnShippingFeesAmount',
    )
    return_fees: Optional[
        Union[ReturnFeesEnumeration, List[ReturnFeesEnumeration]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('returnFees', 'https://schema.org/returnFees'),
        serialization_alias='https://schema.org/returnFees',
    )
    return_shipping_fees_amount: Optional[
        Union[MonetaryAmount, List[MonetaryAmount]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'returnShippingFeesAmount', 'https://schema.org/returnShippingFeesAmount'
        ),
        serialization_alias='https://schema.org/returnShippingFeesAmount',
    )
    valid_for_member_tier: Optional[
        Union[MemberProgramTier, List[MemberProgramTier]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'validForMemberTier', 'https://schema.org/validForMemberTier'
        ),
        serialization_alias='https://schema.org/validForMemberTier',
    )
    return_policy_category: Optional[
        Union[MerchantReturnEnumeration, List[MerchantReturnEnumeration]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'returnPolicyCategory', 'https://schema.org/returnPolicyCategory'
        ),
        serialization_alias='https://schema.org/returnPolicyCategory',
    )
    customer_remorse_return_label_source: Optional[
        Union[ReturnLabelSourceEnumeration, List[ReturnLabelSourceEnumeration]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'customerRemorseReturnLabelSource',
            'https://schema.org/customerRemorseReturnLabelSource',
        ),
        serialization_alias='https://schema.org/customerRemorseReturnLabelSource',
    )
    return_policy_seasonal_override: Optional[
        Union[
            MerchantReturnPolicySeasonalOverride,
            List[MerchantReturnPolicySeasonalOverride],
        ]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'returnPolicySeasonalOverride',
            'https://schema.org/returnPolicySeasonalOverride',
        ),
        serialization_alias='https://schema.org/returnPolicySeasonalOverride',
    )
    item_defect_return_label_source: Optional[
        Union[ReturnLabelSourceEnumeration, List[ReturnLabelSourceEnumeration]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'itemDefectReturnLabelSource',
            'https://schema.org/itemDefectReturnLabelSource',
        ),
        serialization_alias='https://schema.org/itemDefectReturnLabelSource',
    )
    applicable_country: Optional[
        Union[Country, str, List[Union[Country, str]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'applicableCountry', 'https://schema.org/applicableCountry'
        ),
        serialization_alias='https://schema.org/applicableCountry',
    )
    return_label_source: Optional[
        Union[ReturnLabelSourceEnumeration, List[ReturnLabelSourceEnumeration]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'returnLabelSource', 'https://schema.org/returnLabelSource'
        ),
        serialization_alias='https://schema.org/returnLabelSource',
    )
    restocking_fee: Optional[
        Union[MonetaryAmount, float, List[Union[MonetaryAmount, float]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'restockingFee', 'https://schema.org/restockingFee'
        ),
        serialization_alias='https://schema.org/restockingFee',
    )
    item_condition: Optional[
        Union[OfferItemCondition, List[OfferItemCondition]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'itemCondition', 'https://schema.org/itemCondition'
        ),
        serialization_alias='https://schema.org/itemCondition',
    )


class MerchantReturnPolicySeasonalOverride(Intangible):
    field_type: Literal[
        'https://schema.org/MerchantReturnPolicySeasonalOverride'
    ] = Field('https://schema.org/MerchantReturnPolicySeasonalOverride', alias='@type')
    start_date: Optional[
        Union[date, AwareDatetime, List[Union[date, AwareDatetime]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('startDate', 'https://schema.org/startDate'),
        serialization_alias='https://schema.org/startDate',
    )
    return_fees: Optional[
        Union[ReturnFeesEnumeration, List[ReturnFeesEnumeration]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('returnFees', 'https://schema.org/returnFees'),
        serialization_alias='https://schema.org/returnFees',
    )
    return_shipping_fees_amount: Optional[
        Union[MonetaryAmount, List[MonetaryAmount]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'returnShippingFeesAmount', 'https://schema.org/returnShippingFeesAmount'
        ),
        serialization_alias='https://schema.org/returnShippingFeesAmount',
    )
    return_policy_category: Optional[
        Union[MerchantReturnEnumeration, List[MerchantReturnEnumeration]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'returnPolicyCategory', 'https://schema.org/returnPolicyCategory'
        ),
        serialization_alias='https://schema.org/returnPolicyCategory',
    )
    restocking_fee: Optional[
        Union[MonetaryAmount, float, List[Union[MonetaryAmount, float]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'restockingFee', 'https://schema.org/restockingFee'
        ),
        serialization_alias='https://schema.org/restockingFee',
    )
    merchant_return_days: Optional[
        Union[date, int, AwareDatetime, List[Union[date, int, AwareDatetime]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'merchantReturnDays', 'https://schema.org/merchantReturnDays'
        ),
        serialization_alias='https://schema.org/merchantReturnDays',
    )
    refund_type: Optional[
        Union[RefundTypeEnumeration, List[RefundTypeEnumeration]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('refundType', 'https://schema.org/refundType'),
        serialization_alias='https://schema.org/refundType',
    )
    end_date: Optional[
        Union[AwareDatetime, date, List[Union[AwareDatetime, date]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('endDate', 'https://schema.org/endDate'),
        serialization_alias='https://schema.org/endDate',
    )
    return_method: Optional[
        Union[ReturnMethodEnumeration, List[ReturnMethodEnumeration]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'returnMethod', 'https://schema.org/returnMethod'
        ),
        serialization_alias='https://schema.org/returnMethod',
    )


class MenuItem(Intangible):
    field_type: Literal['https://schema.org/MenuItem'] = Field(
        'https://schema.org/MenuItem', alias='@type'
    )
    suitable_for_diet: Optional[Union[RestrictedDiet, List[RestrictedDiet]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'suitableForDiet', 'https://schema.org/suitableForDiet'
        ),
        serialization_alias='https://schema.org/suitableForDiet',
    )
    menu_add_on: Optional[
        Union[MenuItem, MenuSection, List[Union[MenuItem, MenuSection]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('menuAddOn', 'https://schema.org/menuAddOn'),
        serialization_alias='https://schema.org/menuAddOn',
    )
    offers: Optional[Union[Demand, Offer, List[Union[Demand, Offer]]]] = Field(
        default=None,
        validation_alias=AliasChoices('offers', 'https://schema.org/offers'),
        serialization_alias='https://schema.org/offers',
    )
    nutrition: Optional[
        Union[NutritionInformation, List[NutritionInformation]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('nutrition', 'https://schema.org/nutrition'),
        serialization_alias='https://schema.org/nutrition',
    )


class Trip(Intangible):
    field_type: Literal['https://schema.org/Trip'] = Field(
        'https://schema.org/Trip', alias='@type'
    )
    sub_trip: Optional[Union[Trip, List[Trip]]] = Field(
        default=None,
        validation_alias=AliasChoices('subTrip', 'https://schema.org/subTrip'),
        serialization_alias='https://schema.org/subTrip',
    )
    provider: Optional[
        Union[Person, Organization, List[Union[Person, Organization]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('provider', 'https://schema.org/provider'),
        serialization_alias='https://schema.org/provider',
    )
    part_of_trip: Optional[Union[Trip, List[Trip]]] = Field(
        default=None,
        validation_alias=AliasChoices('partOfTrip', 'https://schema.org/partOfTrip'),
        serialization_alias='https://schema.org/partOfTrip',
    )
    departure_time: Optional[
        Union[time, AwareDatetime, List[Union[time, AwareDatetime]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'departureTime', 'https://schema.org/departureTime'
        ),
        serialization_alias='https://schema.org/departureTime',
    )
    trip_origin: Optional[Union[Place, List[Place]]] = Field(
        default=None,
        validation_alias=AliasChoices('tripOrigin', 'https://schema.org/tripOrigin'),
        serialization_alias='https://schema.org/tripOrigin',
    )
    itinerary: Optional[Union[ItemList, Place, List[Union[ItemList, Place]]]] = Field(
        default=None,
        validation_alias=AliasChoices('itinerary', 'https://schema.org/itinerary'),
        serialization_alias='https://schema.org/itinerary',
    )
    arrival_time: Optional[
        Union[time, AwareDatetime, List[Union[time, AwareDatetime]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('arrivalTime', 'https://schema.org/arrivalTime'),
        serialization_alias='https://schema.org/arrivalTime',
    )
    offers: Optional[Union[Demand, Offer, List[Union[Demand, Offer]]]] = Field(
        default=None,
        validation_alias=AliasChoices('offers', 'https://schema.org/offers'),
        serialization_alias='https://schema.org/offers',
    )


class Audience(Intangible):
    field_type: Literal['https://schema.org/Audience'] = Field(
        'https://schema.org/Audience', alias='@type'
    )
    geographic_area: Optional[
        Union[AdministrativeArea, List[AdministrativeArea]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'geographicArea', 'https://schema.org/geographicArea'
        ),
        serialization_alias='https://schema.org/geographicArea',
    )
    audience_type: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'audienceType', 'https://schema.org/audienceType'
        ),
        serialization_alias='https://schema.org/audienceType',
    )


class Grant(Intangible):
    field_type: Literal['https://schema.org/Grant'] = Field(
        'https://schema.org/Grant', alias='@type'
    )
    sponsor: Optional[
        Union[Organization, Person, List[Union[Organization, Person]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('sponsor', 'https://schema.org/sponsor'),
        serialization_alias='https://schema.org/sponsor',
    )
    funder: Optional[
        Union[Organization, Person, List[Union[Organization, Person]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('funder', 'https://schema.org/funder'),
        serialization_alias='https://schema.org/funder',
    )
    funded_item: Optional[
        Union[
            Event,
            MedicalEntity,
            BioChemEntity,
            Product,
            CreativeWork,
            Person,
            Organization,
            List[
                Union[
                    Event,
                    MedicalEntity,
                    BioChemEntity,
                    Product,
                    CreativeWork,
                    Person,
                    Organization,
                ]
            ],
        ]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('fundedItem', 'https://schema.org/fundedItem'),
        serialization_alias='https://schema.org/fundedItem',
    )


class HealthInsurancePlan(Intangible):
    field_type: Literal['https://schema.org/HealthInsurancePlan'] = Field(
        'https://schema.org/HealthInsurancePlan', alias='@type'
    )
    benefits_summary_url: Optional[Union[AnyUrl, List[AnyUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'benefitsSummaryUrl', 'https://schema.org/benefitsSummaryUrl'
        ),
        serialization_alias='https://schema.org/benefitsSummaryUrl',
    )
    includes_health_plan_network: Optional[
        Union[HealthPlanNetwork, List[HealthPlanNetwork]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'includesHealthPlanNetwork', 'https://schema.org/includesHealthPlanNetwork'
        ),
        serialization_alias='https://schema.org/includesHealthPlanNetwork',
    )
    includes_health_plan_formulary: Optional[
        Union[HealthPlanFormulary, List[HealthPlanFormulary]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'includesHealthPlanFormulary',
            'https://schema.org/includesHealthPlanFormulary',
        ),
        serialization_alias='https://schema.org/includesHealthPlanFormulary',
    )
    contact_point: Optional[Union[ContactPoint, List[ContactPoint]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'contactPoint', 'https://schema.org/contactPoint'
        ),
        serialization_alias='https://schema.org/contactPoint',
    )
    health_plan_id: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'healthPlanId', 'https://schema.org/healthPlanId'
        ),
        serialization_alias='https://schema.org/healthPlanId',
    )
    health_plan_marketing_url: Optional[Union[AnyUrl, List[AnyUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'healthPlanMarketingUrl', 'https://schema.org/healthPlanMarketingUrl'
        ),
        serialization_alias='https://schema.org/healthPlanMarketingUrl',
    )
    uses_health_plan_id_standard: Optional[
        Union[str, AnyUrl, List[Union[str, AnyUrl]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'usesHealthPlanIdStandard', 'https://schema.org/usesHealthPlanIdStandard'
        ),
        serialization_alias='https://schema.org/usesHealthPlanIdStandard',
    )
    health_plan_drug_option: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'healthPlanDrugOption', 'https://schema.org/healthPlanDrugOption'
        ),
        serialization_alias='https://schema.org/healthPlanDrugOption',
    )
    health_plan_drug_tier: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'healthPlanDrugTier', 'https://schema.org/healthPlanDrugTier'
        ),
        serialization_alias='https://schema.org/healthPlanDrugTier',
    )


class HealthPlanNetwork(Intangible):
    field_type: Literal['https://schema.org/HealthPlanNetwork'] = Field(
        'https://schema.org/HealthPlanNetwork', alias='@type'
    )
    health_plan_network_tier: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'healthPlanNetworkTier', 'https://schema.org/healthPlanNetworkTier'
        ),
        serialization_alias='https://schema.org/healthPlanNetworkTier',
    )
    health_plan_network_id: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'healthPlanNetworkId', 'https://schema.org/healthPlanNetworkId'
        ),
        serialization_alias='https://schema.org/healthPlanNetworkId',
    )
    health_plan_cost_sharing: Optional[Union[bool, List[bool]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'healthPlanCostSharing', 'https://schema.org/healthPlanCostSharing'
        ),
        serialization_alias='https://schema.org/healthPlanCostSharing',
    )


class HealthPlanFormulary(Intangible):
    field_type: Literal['https://schema.org/HealthPlanFormulary'] = Field(
        'https://schema.org/HealthPlanFormulary', alias='@type'
    )
    offers_prescription_by_mail: Optional[Union[bool, List[bool]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'offersPrescriptionByMail', 'https://schema.org/offersPrescriptionByMail'
        ),
        serialization_alias='https://schema.org/offersPrescriptionByMail',
    )
    health_plan_drug_tier: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'healthPlanDrugTier', 'https://schema.org/healthPlanDrugTier'
        ),
        serialization_alias='https://schema.org/healthPlanDrugTier',
    )
    health_plan_cost_sharing: Optional[Union[bool, List[bool]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'healthPlanCostSharing', 'https://schema.org/healthPlanCostSharing'
        ),
        serialization_alias='https://schema.org/healthPlanCostSharing',
    )


class EnergyConsumptionDetails(Intangible):
    field_type: Literal['https://schema.org/EnergyConsumptionDetails'] = Field(
        'https://schema.org/EnergyConsumptionDetails', alias='@type'
    )
    has_energy_efficiency_category: Optional[
        Union[EnergyEfficiencyEnumeration, List[EnergyEfficiencyEnumeration]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'hasEnergyEfficiencyCategory',
            'https://schema.org/hasEnergyEfficiencyCategory',
        ),
        serialization_alias='https://schema.org/hasEnergyEfficiencyCategory',
    )
    energy_efficiency_scale_max: Optional[
        Union[EUEnergyEfficiencyEnumeration, List[EUEnergyEfficiencyEnumeration]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'energyEfficiencyScaleMax', 'https://schema.org/energyEfficiencyScaleMax'
        ),
        serialization_alias='https://schema.org/energyEfficiencyScaleMax',
    )
    energy_efficiency_scale_min: Optional[
        Union[EUEnergyEfficiencyEnumeration, List[EUEnergyEfficiencyEnumeration]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'energyEfficiencyScaleMin', 'https://schema.org/energyEfficiencyScaleMin'
        ),
        serialization_alias='https://schema.org/energyEfficiencyScaleMin',
    )


class Brand(Intangible):
    field_type: Literal['https://schema.org/Brand'] = Field(
        'https://schema.org/Brand', alias='@type'
    )
    review: Optional[Union[Review, List[Review]]] = Field(
        default=None,
        validation_alias=AliasChoices('review', 'https://schema.org/review'),
        serialization_alias='https://schema.org/review',
    )
    aggregate_rating: Optional[Union[AggregateRating, List[AggregateRating]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'aggregateRating', 'https://schema.org/aggregateRating'
        ),
        serialization_alias='https://schema.org/aggregateRating',
    )
    logo: Optional[
        Union[AnyUrl, ImageObject, List[Union[AnyUrl, ImageObject]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('logo', 'https://schema.org/logo'),
        serialization_alias='https://schema.org/logo',
    )
    slogan: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices('slogan', 'https://schema.org/slogan'),
        serialization_alias='https://schema.org/slogan',
    )


class GeospatialGeometry(Intangible):
    field_type: Literal['https://schema.org/GeospatialGeometry'] = Field(
        'https://schema.org/GeospatialGeometry', alias='@type'
    )
    geo_covered_by: Optional[
        Union[GeospatialGeometry, Place, List[Union[GeospatialGeometry, Place]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'geoCoveredBy', 'https://schema.org/geoCoveredBy'
        ),
        serialization_alias='https://schema.org/geoCoveredBy',
    )
    geo_equals: Optional[
        Union[Place, GeospatialGeometry, List[Union[Place, GeospatialGeometry]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('geoEquals', 'https://schema.org/geoEquals'),
        serialization_alias='https://schema.org/geoEquals',
    )
    geo_covers: Optional[
        Union[Place, GeospatialGeometry, List[Union[Place, GeospatialGeometry]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('geoCovers', 'https://schema.org/geoCovers'),
        serialization_alias='https://schema.org/geoCovers',
    )
    geo_overlaps: Optional[
        Union[Place, GeospatialGeometry, List[Union[Place, GeospatialGeometry]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('geoOverlaps', 'https://schema.org/geoOverlaps'),
        serialization_alias='https://schema.org/geoOverlaps',
    )
    geo_contains: Optional[
        Union[Place, GeospatialGeometry, List[Union[Place, GeospatialGeometry]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('geoContains', 'https://schema.org/geoContains'),
        serialization_alias='https://schema.org/geoContains',
    )
    geo_disjoint: Optional[
        Union[GeospatialGeometry, Place, List[Union[GeospatialGeometry, Place]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('geoDisjoint', 'https://schema.org/geoDisjoint'),
        serialization_alias='https://schema.org/geoDisjoint',
    )
    geo_within: Optional[
        Union[GeospatialGeometry, Place, List[Union[GeospatialGeometry, Place]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('geoWithin', 'https://schema.org/geoWithin'),
        serialization_alias='https://schema.org/geoWithin',
    )
    geo_touches: Optional[
        Union[Place, GeospatialGeometry, List[Union[Place, GeospatialGeometry]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('geoTouches', 'https://schema.org/geoTouches'),
        serialization_alias='https://schema.org/geoTouches',
    )
    geo_crosses: Optional[
        Union[Place, GeospatialGeometry, List[Union[Place, GeospatialGeometry]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('geoCrosses', 'https://schema.org/geoCrosses'),
        serialization_alias='https://schema.org/geoCrosses',
    )
    geo_intersects: Optional[
        Union[Place, GeospatialGeometry, List[Union[Place, GeospatialGeometry]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'geoIntersects', 'https://schema.org/geoIntersects'
        ),
        serialization_alias='https://schema.org/geoIntersects',
    )


class MediaSubscription(Intangible):
    field_type: Literal['https://schema.org/MediaSubscription'] = Field(
        'https://schema.org/MediaSubscription', alias='@type'
    )
    expects_acceptance_of: Optional[Union[Offer, List[Offer]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'expectsAcceptanceOf', 'https://schema.org/expectsAcceptanceOf'
        ),
        serialization_alias='https://schema.org/expectsAcceptanceOf',
    )
    authenticator: Optional[Union[Organization, List[Organization]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'authenticator', 'https://schema.org/authenticator'
        ),
        serialization_alias='https://schema.org/authenticator',
    )


class SpeakableSpecification(Intangible):
    field_type: Literal['https://schema.org/SpeakableSpecification'] = Field(
        'https://schema.org/SpeakableSpecification', alias='@type'
    )
    css_selector: Optional[Union[CssSelectorType, List[CssSelectorType]]] = Field(
        default=None,
        validation_alias=AliasChoices('cssSelector', 'https://schema.org/cssSelector'),
        serialization_alias='https://schema.org/cssSelector',
    )
    xpath: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices('xpath', 'https://schema.org/xpath'),
        serialization_alias='https://schema.org/xpath',
    )


class ServiceChannel(Intangible):
    field_type: Literal['https://schema.org/ServiceChannel'] = Field(
        'https://schema.org/ServiceChannel', alias='@type'
    )
    processing_time: Optional[Union[Duration, List[Duration]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'processingTime', 'https://schema.org/processingTime'
        ),
        serialization_alias='https://schema.org/processingTime',
    )
    available_language: Optional[
        Union[str, Language, List[Union[str, Language]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'availableLanguage', 'https://schema.org/availableLanguage'
        ),
        serialization_alias='https://schema.org/availableLanguage',
    )
    service_postal_address: Optional[Union[PostalAddress, List[PostalAddress]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'servicePostalAddress', 'https://schema.org/servicePostalAddress'
        ),
        serialization_alias='https://schema.org/servicePostalAddress',
    )
    provides_service: Optional[Union[Service, List[Service]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'providesService', 'https://schema.org/providesService'
        ),
        serialization_alias='https://schema.org/providesService',
    )
    service_sms_number: Optional[Union[ContactPoint, List[ContactPoint]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'serviceSmsNumber', 'https://schema.org/serviceSmsNumber'
        ),
        serialization_alias='https://schema.org/serviceSmsNumber',
    )
    service_url: Optional[Union[AnyUrl, List[AnyUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices('serviceUrl', 'https://schema.org/serviceUrl'),
        serialization_alias='https://schema.org/serviceUrl',
    )
    service_location: Optional[Union[Place, List[Place]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'serviceLocation', 'https://schema.org/serviceLocation'
        ),
        serialization_alias='https://schema.org/serviceLocation',
    )
    service_phone: Optional[Union[ContactPoint, List[ContactPoint]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'servicePhone', 'https://schema.org/servicePhone'
        ),
        serialization_alias='https://schema.org/servicePhone',
    )


class ProgramMembership(Intangible):
    field_type: Literal['https://schema.org/ProgramMembership'] = Field(
        'https://schema.org/ProgramMembership', alias='@type'
    )
    program_name: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices('programName', 'https://schema.org/programName'),
        serialization_alias='https://schema.org/programName',
    )
    members: Optional[
        Union[Organization, Person, List[Union[Organization, Person]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('members', 'https://schema.org/members'),
        serialization_alias='https://schema.org/members',
    )
    program: Optional[Union[MemberProgram, List[MemberProgram]]] = Field(
        default=None,
        validation_alias=AliasChoices('program', 'https://schema.org/program'),
        serialization_alias='https://schema.org/program',
    )
    membership_points_earned: Optional[
        Union[QuantitativeValue, float, List[Union[QuantitativeValue, float]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'membershipPointsEarned', 'https://schema.org/membershipPointsEarned'
        ),
        serialization_alias='https://schema.org/membershipPointsEarned',
    )
    membership_number: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'membershipNumber', 'https://schema.org/membershipNumber'
        ),
        serialization_alias='https://schema.org/membershipNumber',
    )
    member: Optional[
        Union[Person, Organization, List[Union[Person, Organization]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('member', 'https://schema.org/member'),
        serialization_alias='https://schema.org/member',
    )
    hosting_organization: Optional[Union[Organization, List[Organization]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'hostingOrganization', 'https://schema.org/hostingOrganization'
        ),
        serialization_alias='https://schema.org/hostingOrganization',
    )


class EntryPoint(Intangible):
    field_type: Literal['https://schema.org/EntryPoint'] = Field(
        'https://schema.org/EntryPoint', alias='@type'
    )
    http_method: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices('httpMethod', 'https://schema.org/httpMethod'),
        serialization_alias='https://schema.org/httpMethod',
    )
    content_type: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices('contentType', 'https://schema.org/contentType'),
        serialization_alias='https://schema.org/contentType',
    )
    url_template: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices('urlTemplate', 'https://schema.org/urlTemplate'),
        serialization_alias='https://schema.org/urlTemplate',
    )
    action_application: Optional[
        Union[SoftwareApplication, List[SoftwareApplication]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'actionApplication', 'https://schema.org/actionApplication'
        ),
        serialization_alias='https://schema.org/actionApplication',
    )
    encoding_type: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'encodingType', 'https://schema.org/encodingType'
        ),
        serialization_alias='https://schema.org/encodingType',
    )
    application: Optional[
        Union[SoftwareApplication, List[SoftwareApplication]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('application', 'https://schema.org/application'),
        serialization_alias='https://schema.org/application',
    )
    action_platform: Optional[
        Union[
            str,
            AnyUrl,
            DigitalPlatformEnumeration,
            List[Union[str, AnyUrl, DigitalPlatformEnumeration]],
        ]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'actionPlatform', 'https://schema.org/actionPlatform'
        ),
        serialization_alias='https://schema.org/actionPlatform',
    )


class ConstraintNode(Intangible):
    field_type: Literal['https://schema.org/ConstraintNode'] = Field(
        'https://schema.org/ConstraintNode', alias='@type'
    )
    num_constraints: Optional[Union[int, List[int]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'numConstraints', 'https://schema.org/numConstraints'
        ),
        serialization_alias='https://schema.org/numConstraints',
    )
    constraint_property: Optional[
        Union[AnyUrl, Property, List[Union[AnyUrl, Property]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'constraintProperty', 'https://schema.org/constraintProperty'
        ),
        serialization_alias='https://schema.org/constraintProperty',
    )


class DataFeedItem(Intangible):
    field_type: Literal['https://schema.org/DataFeedItem'] = Field(
        'https://schema.org/DataFeedItem', alias='@type'
    )
    item: Optional[Union[Thing, List[Thing]]] = Field(
        default=None,
        validation_alias=AliasChoices('item', 'https://schema.org/item'),
        serialization_alias='https://schema.org/item',
    )
    date_created: Optional[
        Union[date, AwareDatetime, List[Union[date, AwareDatetime]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('dateCreated', 'https://schema.org/dateCreated'),
        serialization_alias='https://schema.org/dateCreated',
    )
    date_deleted: Optional[
        Union[AwareDatetime, date, List[Union[AwareDatetime, date]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('dateDeleted', 'https://schema.org/dateDeleted'),
        serialization_alias='https://schema.org/dateDeleted',
    )
    date_modified: Optional[
        Union[AwareDatetime, date, List[Union[AwareDatetime, date]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'dateModified', 'https://schema.org/dateModified'
        ),
        serialization_alias='https://schema.org/dateModified',
    )


class Occupation(Intangible):
    field_type: Literal['https://schema.org/Occupation'] = Field(
        'https://schema.org/Occupation', alias='@type'
    )
    occupational_category: Optional[
        Union[CategoryCode, str, List[Union[CategoryCode, str]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'occupationalCategory', 'https://schema.org/occupationalCategory'
        ),
        serialization_alias='https://schema.org/occupationalCategory',
    )
    occupation_location: Optional[
        Union[AdministrativeArea, List[AdministrativeArea]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'occupationLocation', 'https://schema.org/occupationLocation'
        ),
        serialization_alias='https://schema.org/occupationLocation',
    )
    experience_requirements: Optional[
        Union[
            OccupationalExperienceRequirements,
            str,
            List[Union[OccupationalExperienceRequirements, str]],
        ]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'experienceRequirements', 'https://schema.org/experienceRequirements'
        ),
        serialization_alias='https://schema.org/experienceRequirements',
    )
    responsibilities: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'responsibilities', 'https://schema.org/responsibilities'
        ),
        serialization_alias='https://schema.org/responsibilities',
    )
    qualifications: Optional[
        Union[
            EducationalOccupationalCredential,
            str,
            List[Union[EducationalOccupationalCredential, str]],
        ]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'qualifications', 'https://schema.org/qualifications'
        ),
        serialization_alias='https://schema.org/qualifications',
    )
    skills: Optional[Union[DefinedTerm, str, List[Union[DefinedTerm, str]]]] = Field(
        default=None,
        validation_alias=AliasChoices('skills', 'https://schema.org/skills'),
        serialization_alias='https://schema.org/skills',
    )
    estimated_salary: Optional[
        Union[
            MonetaryAmountDistribution,
            float,
            MonetaryAmount,
            List[Union[MonetaryAmountDistribution, float, MonetaryAmount]],
        ]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'estimatedSalary', 'https://schema.org/estimatedSalary'
        ),
        serialization_alias='https://schema.org/estimatedSalary',
    )
    education_requirements: Optional[
        Union[
            EducationalOccupationalCredential,
            str,
            List[Union[EducationalOccupationalCredential, str]],
        ]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'educationRequirements', 'https://schema.org/educationRequirements'
        ),
        serialization_alias='https://schema.org/educationRequirements',
    )


class OccupationalExperienceRequirements(Intangible):
    field_type: Literal[
        'https://schema.org/OccupationalExperienceRequirements'
    ] = Field('https://schema.org/OccupationalExperienceRequirements', alias='@type')
    months_of_experience: Optional[Union[float, List[float]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'monthsOfExperience', 'https://schema.org/monthsOfExperience'
        ),
        serialization_alias='https://schema.org/monthsOfExperience',
    )


class BroadcastFrequencySpecification(Intangible):
    field_type: Literal['https://schema.org/BroadcastFrequencySpecification'] = Field(
        'https://schema.org/BroadcastFrequencySpecification', alias='@type'
    )
    broadcast_sub_channel: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'broadcastSubChannel', 'https://schema.org/broadcastSubChannel'
        ),
        serialization_alias='https://schema.org/broadcastSubChannel',
    )
    broadcast_frequency_value: Optional[
        Union[float, QuantitativeValue, List[Union[float, QuantitativeValue]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'broadcastFrequencyValue', 'https://schema.org/broadcastFrequencyValue'
        ),
        serialization_alias='https://schema.org/broadcastFrequencyValue',
    )
    broadcast_signal_modulation: Optional[
        Union[str, QualitativeValue, List[Union[str, QualitativeValue]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'broadcastSignalModulation', 'https://schema.org/broadcastSignalModulation'
        ),
        serialization_alias='https://schema.org/broadcastSignalModulation',
    )


class BroadcastChannel(Intangible):
    field_type: Literal['https://schema.org/BroadcastChannel'] = Field(
        'https://schema.org/BroadcastChannel', alias='@type'
    )
    in_broadcast_lineup: Optional[
        Union[CableOrSatelliteService, List[CableOrSatelliteService]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'inBroadcastLineup', 'https://schema.org/inBroadcastLineup'
        ),
        serialization_alias='https://schema.org/inBroadcastLineup',
    )
    broadcast_channel_id: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'broadcastChannelId', 'https://schema.org/broadcastChannelId'
        ),
        serialization_alias='https://schema.org/broadcastChannelId',
    )
    provides_broadcast_service: Optional[
        Union[BroadcastService, List[BroadcastService]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'providesBroadcastService', 'https://schema.org/providesBroadcastService'
        ),
        serialization_alias='https://schema.org/providesBroadcastService',
    )
    broadcast_frequency: Optional[
        Union[
            str,
            BroadcastFrequencySpecification,
            List[Union[str, BroadcastFrequencySpecification]],
        ]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'broadcastFrequency', 'https://schema.org/broadcastFrequency'
        ),
        serialization_alias='https://schema.org/broadcastFrequency',
    )
    broadcast_service_tier: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'broadcastServiceTier', 'https://schema.org/broadcastServiceTier'
        ),
        serialization_alias='https://schema.org/broadcastServiceTier',
    )
    genre: Optional[Union[AnyUrl, str, List[Union[AnyUrl, str]]]] = Field(
        default=None,
        validation_alias=AliasChoices('genre', 'https://schema.org/genre'),
        serialization_alias='https://schema.org/genre',
    )


class AlignmentObject(Intangible):
    field_type: Literal['https://schema.org/AlignmentObject'] = Field(
        'https://schema.org/AlignmentObject', alias='@type'
    )
    alignment_type: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'alignmentType', 'https://schema.org/alignmentType'
        ),
        serialization_alias='https://schema.org/alignmentType',
    )
    target_name: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices('targetName', 'https://schema.org/targetName'),
        serialization_alias='https://schema.org/targetName',
    )
    educational_framework: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'educationalFramework', 'https://schema.org/educationalFramework'
        ),
        serialization_alias='https://schema.org/educationalFramework',
    )
    target_description: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'targetDescription', 'https://schema.org/targetDescription'
        ),
        serialization_alias='https://schema.org/targetDescription',
    )
    target_url: Optional[Union[AnyUrl, List[AnyUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices('targetUrl', 'https://schema.org/targetUrl'),
        serialization_alias='https://schema.org/targetUrl',
    )


class MediaObject(CreativeWork):
    field_type: Literal['https://schema.org/MediaObject'] = Field(
        'https://schema.org/MediaObject', alias='@type'
    )
    encodes_creative_work: Optional[Union[CreativeWork, List[CreativeWork]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'encodesCreativeWork', 'https://schema.org/encodesCreativeWork'
        ),
        serialization_alias='https://schema.org/encodesCreativeWork',
    )
    height: Optional[
        Union[Distance, QuantitativeValue, List[Union[Distance, QuantitativeValue]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('height', 'https://schema.org/height'),
        serialization_alias='https://schema.org/height',
    )
    production_company: Optional[Union[Organization, List[Organization]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'productionCompany', 'https://schema.org/productionCompany'
        ),
        serialization_alias='https://schema.org/productionCompany',
    )
    regions_allowed: Optional[Union[Place, List[Place]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'regionsAllowed', 'https://schema.org/regionsAllowed'
        ),
        serialization_alias='https://schema.org/regionsAllowed',
    )
    content_size: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices('contentSize', 'https://schema.org/contentSize'),
        serialization_alias='https://schema.org/contentSize',
    )
    interpreted_as_claim: Optional[Union[Claim, List[Claim]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'interpretedAsClaim', 'https://schema.org/interpretedAsClaim'
        ),
        serialization_alias='https://schema.org/interpretedAsClaim',
    )
    requires_subscription: Optional[
        Union[bool, MediaSubscription, List[Union[bool, MediaSubscription]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'requiresSubscription', 'https://schema.org/requiresSubscription'
        ),
        serialization_alias='https://schema.org/requiresSubscription',
    )
    end_time: Optional[
        Union[time, AwareDatetime, List[Union[time, AwareDatetime]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('endTime', 'https://schema.org/endTime'),
        serialization_alias='https://schema.org/endTime',
    )
    bitrate: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices('bitrate', 'https://schema.org/bitrate'),
        serialization_alias='https://schema.org/bitrate',
    )
    encoding_format: Optional[Union[AnyUrl, str, List[Union[AnyUrl, str]]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'encodingFormat', 'https://schema.org/encodingFormat'
        ),
        serialization_alias='https://schema.org/encodingFormat',
    )
    content_url: Optional[Union[AnyUrl, List[AnyUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices('contentUrl', 'https://schema.org/contentUrl'),
        serialization_alias='https://schema.org/contentUrl',
    )
    associated_article: Optional[Union[NewsArticle, List[NewsArticle]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'associatedArticle', 'https://schema.org/associatedArticle'
        ),
        serialization_alias='https://schema.org/associatedArticle',
    )
    width: Optional[
        Union[QuantitativeValue, Distance, List[Union[QuantitativeValue, Distance]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('width', 'https://schema.org/width'),
        serialization_alias='https://schema.org/width',
    )
    player_type: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices('playerType', 'https://schema.org/playerType'),
        serialization_alias='https://schema.org/playerType',
    )
    duration: Optional[
        Union[Duration, QuantitativeValue, List[Union[Duration, QuantitativeValue]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('duration', 'https://schema.org/duration'),
        serialization_alias='https://schema.org/duration',
    )
    embed_url: Optional[Union[AnyUrl, List[AnyUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices('embedUrl', 'https://schema.org/embedUrl'),
        serialization_alias='https://schema.org/embedUrl',
    )
    start_time: Optional[
        Union[time, AwareDatetime, List[Union[time, AwareDatetime]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('startTime', 'https://schema.org/startTime'),
        serialization_alias='https://schema.org/startTime',
    )
    ineligible_region: Optional[
        Union[str, Place, GeoShape, List[Union[str, Place, GeoShape]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'ineligibleRegion', 'https://schema.org/ineligibleRegion'
        ),
        serialization_alias='https://schema.org/ineligibleRegion',
    )
    sha256: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices('sha256', 'https://schema.org/sha256'),
        serialization_alias='https://schema.org/sha256',
    )
    upload_date: Optional[
        Union[date, AwareDatetime, List[Union[date, AwareDatetime]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('uploadDate', 'https://schema.org/uploadDate'),
        serialization_alias='https://schema.org/uploadDate',
    )


class Review(CreativeWork):
    field_type: Literal['https://schema.org/Review'] = Field(
        'https://schema.org/Review', alias='@type'
    )
    item_reviewed: Optional[Union[Thing, List[Thing]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'itemReviewed', 'https://schema.org/itemReviewed'
        ),
        serialization_alias='https://schema.org/itemReviewed',
    )
    positive_notes: Optional[
        Union[
            WebContent,
            ItemList,
            str,
            ListItem,
            List[Union[WebContent, ItemList, str, ListItem]],
        ]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'positiveNotes', 'https://schema.org/positiveNotes'
        ),
        serialization_alias='https://schema.org/positiveNotes',
    )
    review_aspect: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'reviewAspect', 'https://schema.org/reviewAspect'
        ),
        serialization_alias='https://schema.org/reviewAspect',
    )
    review_rating: Optional[Union[Rating, List[Rating]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'reviewRating', 'https://schema.org/reviewRating'
        ),
        serialization_alias='https://schema.org/reviewRating',
    )
    associated_review: Optional[Union[Review, List[Review]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'associatedReview', 'https://schema.org/associatedReview'
        ),
        serialization_alias='https://schema.org/associatedReview',
    )
    associated_claim_review: Optional[Union[Review, List[Review]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'associatedClaimReview', 'https://schema.org/associatedClaimReview'
        ),
        serialization_alias='https://schema.org/associatedClaimReview',
    )
    negative_notes: Optional[
        Union[
            ListItem,
            WebContent,
            ItemList,
            str,
            List[Union[ListItem, WebContent, ItemList, str]],
        ]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'negativeNotes', 'https://schema.org/negativeNotes'
        ),
        serialization_alias='https://schema.org/negativeNotes',
    )
    review_body: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices('reviewBody', 'https://schema.org/reviewBody'),
        serialization_alias='https://schema.org/reviewBody',
    )
    associated_media_review: Optional[Union[Review, List[Review]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'associatedMediaReview', 'https://schema.org/associatedMediaReview'
        ),
        serialization_alias='https://schema.org/associatedMediaReview',
    )


class WebContent(CreativeWork):
    field_type: Literal['https://schema.org/WebContent'] = Field(
        'https://schema.org/WebContent', alias='@type'
    )


class Certification(CreativeWork):
    field_type: Literal['https://schema.org/Certification'] = Field(
        'https://schema.org/Certification', alias='@type'
    )
    certification_identification: Optional[
        Union[DefinedTerm, str, List[Union[DefinedTerm, str]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'certificationIdentification',
            'https://schema.org/certificationIdentification',
        ),
        serialization_alias='https://schema.org/certificationIdentification',
    )
    logo: Optional[
        Union[AnyUrl, ImageObject, List[Union[AnyUrl, ImageObject]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('logo', 'https://schema.org/logo'),
        serialization_alias='https://schema.org/logo',
    )
    about: Optional[Union[Thing, List[Thing]]] = Field(
        default=None,
        validation_alias=AliasChoices('about', 'https://schema.org/about'),
        serialization_alias='https://schema.org/about',
    )
    valid_from: Optional[
        Union[date, AwareDatetime, List[Union[date, AwareDatetime]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('validFrom', 'https://schema.org/validFrom'),
        serialization_alias='https://schema.org/validFrom',
    )
    audit_date: Optional[
        Union[date, AwareDatetime, List[Union[date, AwareDatetime]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('auditDate', 'https://schema.org/auditDate'),
        serialization_alias='https://schema.org/auditDate',
    )
    expires: Optional[
        Union[date, AwareDatetime, List[Union[date, AwareDatetime]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('expires', 'https://schema.org/expires'),
        serialization_alias='https://schema.org/expires',
    )
    certification_rating: Optional[Union[Rating, List[Rating]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'certificationRating', 'https://schema.org/certificationRating'
        ),
        serialization_alias='https://schema.org/certificationRating',
    )
    valid_in: Optional[Union[AdministrativeArea, List[AdministrativeArea]]] = Field(
        default=None,
        validation_alias=AliasChoices('validIn', 'https://schema.org/validIn'),
        serialization_alias='https://schema.org/validIn',
    )
    has_measurement: Optional[
        Union[QuantitativeValue, List[QuantitativeValue]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'hasMeasurement', 'https://schema.org/hasMeasurement'
        ),
        serialization_alias='https://schema.org/hasMeasurement',
    )
    issued_by: Optional[Union[Organization, List[Organization]]] = Field(
        default=None,
        validation_alias=AliasChoices('issuedBy', 'https://schema.org/issuedBy'),
        serialization_alias='https://schema.org/issuedBy',
    )
    certification_status: Optional[
        Union[CertificationStatusEnumeration, List[CertificationStatusEnumeration]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'certificationStatus', 'https://schema.org/certificationStatus'
        ),
        serialization_alias='https://schema.org/certificationStatus',
    )
    date_published: Optional[
        Union[date, AwareDatetime, List[Union[date, AwareDatetime]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'datePublished', 'https://schema.org/datePublished'
        ),
        serialization_alias='https://schema.org/datePublished',
    )


class DefinedTermSet(CreativeWork):
    field_type: Literal['https://schema.org/DefinedTermSet'] = Field(
        'https://schema.org/DefinedTermSet', alias='@type'
    )
    has_defined_term: Optional[Union[DefinedTerm, List[DefinedTerm]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'hasDefinedTerm', 'https://schema.org/hasDefinedTerm'
        ),
        serialization_alias='https://schema.org/hasDefinedTerm',
    )


class MenuSection(CreativeWork):
    field_type: Literal['https://schema.org/MenuSection'] = Field(
        'https://schema.org/MenuSection', alias='@type'
    )
    has_menu_item: Optional[Union[MenuItem, List[MenuItem]]] = Field(
        default=None,
        validation_alias=AliasChoices('hasMenuItem', 'https://schema.org/hasMenuItem'),
        serialization_alias='https://schema.org/hasMenuItem',
    )
    has_menu_section: Optional[Union[MenuSection, List[MenuSection]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'hasMenuSection', 'https://schema.org/hasMenuSection'
        ),
        serialization_alias='https://schema.org/hasMenuSection',
    )


class Map(CreativeWork):
    field_type: Literal['https://schema.org/Map'] = Field(
        'https://schema.org/Map', alias='@type'
    )
    map_type: Optional[Union[MapCategoryType, List[MapCategoryType]]] = Field(
        default=None,
        validation_alias=AliasChoices('mapType', 'https://schema.org/mapType'),
        serialization_alias='https://schema.org/mapType',
    )


class Photograph(CreativeWork):
    field_type: Literal['https://schema.org/Photograph'] = Field(
        'https://schema.org/Photograph', alias='@type'
    )


class Claim(CreativeWork):
    field_type: Literal['https://schema.org/Claim'] = Field(
        'https://schema.org/Claim', alias='@type'
    )
    claim_interpreter: Optional[
        Union[Organization, Person, List[Union[Organization, Person]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'claimInterpreter', 'https://schema.org/claimInterpreter'
        ),
        serialization_alias='https://schema.org/claimInterpreter',
    )
    first_appearance: Optional[Union[CreativeWork, List[CreativeWork]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'firstAppearance', 'https://schema.org/firstAppearance'
        ),
        serialization_alias='https://schema.org/firstAppearance',
    )
    appearance: Optional[Union[CreativeWork, List[CreativeWork]]] = Field(
        default=None,
        validation_alias=AliasChoices('appearance', 'https://schema.org/appearance'),
        serialization_alias='https://schema.org/appearance',
    )


class Article(CreativeWork):
    field_type: Literal['https://schema.org/Article'] = Field(
        'https://schema.org/Article', alias='@type'
    )
    pagination: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices('pagination', 'https://schema.org/pagination'),
        serialization_alias='https://schema.org/pagination',
    )
    article_body: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices('articleBody', 'https://schema.org/articleBody'),
        serialization_alias='https://schema.org/articleBody',
    )
    page_end: Optional[Union[str, int, List[Union[str, int]]]] = Field(
        default=None,
        validation_alias=AliasChoices('pageEnd', 'https://schema.org/pageEnd'),
        serialization_alias='https://schema.org/pageEnd',
    )
    backstory: Optional[
        Union[str, CreativeWork, List[Union[str, CreativeWork]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('backstory', 'https://schema.org/backstory'),
        serialization_alias='https://schema.org/backstory',
    )
    word_count: Optional[Union[int, List[int]]] = Field(
        default=None,
        validation_alias=AliasChoices('wordCount', 'https://schema.org/wordCount'),
        serialization_alias='https://schema.org/wordCount',
    )
    article_section: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'articleSection', 'https://schema.org/articleSection'
        ),
        serialization_alias='https://schema.org/articleSection',
    )
    speakable: Optional[
        Union[
            AnyUrl, SpeakableSpecification, List[Union[AnyUrl, SpeakableSpecification]]
        ]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('speakable', 'https://schema.org/speakable'),
        serialization_alias='https://schema.org/speakable',
    )
    page_start: Optional[Union[int, str, List[Union[int, str]]]] = Field(
        default=None,
        validation_alias=AliasChoices('pageStart', 'https://schema.org/pageStart'),
        serialization_alias='https://schema.org/pageStart',
    )


class WebPage(CreativeWork):
    field_type: Literal['https://schema.org/WebPage'] = Field(
        'https://schema.org/WebPage', alias='@type'
    )
    main_content_of_page: Optional[Union[WebPageElement, List[WebPageElement]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'mainContentOfPage', 'https://schema.org/mainContentOfPage'
        ),
        serialization_alias='https://schema.org/mainContentOfPage',
    )
    significant_link: Optional[Union[AnyUrl, List[AnyUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'significantLink', 'https://schema.org/significantLink'
        ),
        serialization_alias='https://schema.org/significantLink',
    )
    speakable: Optional[
        Union[
            AnyUrl, SpeakableSpecification, List[Union[AnyUrl, SpeakableSpecification]]
        ]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('speakable', 'https://schema.org/speakable'),
        serialization_alias='https://schema.org/speakable',
    )
    last_reviewed: Optional[Union[date, List[date]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'lastReviewed', 'https://schema.org/lastReviewed'
        ),
        serialization_alias='https://schema.org/lastReviewed',
    )
    primary_image_of_page: Optional[Union[ImageObject, List[ImageObject]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'primaryImageOfPage', 'https://schema.org/primaryImageOfPage'
        ),
        serialization_alias='https://schema.org/primaryImageOfPage',
    )
    reviewed_by: Optional[
        Union[Person, Organization, List[Union[Person, Organization]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('reviewedBy', 'https://schema.org/reviewedBy'),
        serialization_alias='https://schema.org/reviewedBy',
    )
    related_link: Optional[Union[AnyUrl, List[AnyUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices('relatedLink', 'https://schema.org/relatedLink'),
        serialization_alias='https://schema.org/relatedLink',
    )
    significant_links: Optional[Union[AnyUrl, List[AnyUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'significantLinks', 'https://schema.org/significantLinks'
        ),
        serialization_alias='https://schema.org/significantLinks',
    )
    specialty: Optional[Union[Specialty, List[Specialty]]] = Field(
        default=None,
        validation_alias=AliasChoices('specialty', 'https://schema.org/specialty'),
        serialization_alias='https://schema.org/specialty',
    )
    breadcrumb: Optional[
        Union[str, BreadcrumbList, List[Union[str, BreadcrumbList]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('breadcrumb', 'https://schema.org/breadcrumb'),
        serialization_alias='https://schema.org/breadcrumb',
    )


class WebPageElement(CreativeWork):
    field_type: Literal['https://schema.org/WebPageElement'] = Field(
        'https://schema.org/WebPageElement', alias='@type'
    )
    xpath: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices('xpath', 'https://schema.org/xpath'),
        serialization_alias='https://schema.org/xpath',
    )
    css_selector: Optional[Union[CssSelectorType, List[CssSelectorType]]] = Field(
        default=None,
        validation_alias=AliasChoices('cssSelector', 'https://schema.org/cssSelector'),
        serialization_alias='https://schema.org/cssSelector',
    )


class SoftwareApplication(CreativeWork):
    field_type: Literal['https://schema.org/SoftwareApplication'] = Field(
        'https://schema.org/SoftwareApplication', alias='@type'
    )
    application_category: Optional[
        Union[str, AnyUrl, List[Union[str, AnyUrl]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'applicationCategory', 'https://schema.org/applicationCategory'
        ),
        serialization_alias='https://schema.org/applicationCategory',
    )
    requirements: Optional[Union[str, AnyUrl, List[Union[str, AnyUrl]]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'requirements', 'https://schema.org/requirements'
        ),
        serialization_alias='https://schema.org/requirements',
    )
    memory_requirements: Optional[Union[str, AnyUrl, List[Union[str, AnyUrl]]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'memoryRequirements', 'https://schema.org/memoryRequirements'
        ),
        serialization_alias='https://schema.org/memoryRequirements',
    )
    countries_not_supported: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'countriesNotSupported', 'https://schema.org/countriesNotSupported'
        ),
        serialization_alias='https://schema.org/countriesNotSupported',
    )
    permissions: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices('permissions', 'https://schema.org/permissions'),
        serialization_alias='https://schema.org/permissions',
    )
    processor_requirements: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'processorRequirements', 'https://schema.org/processorRequirements'
        ),
        serialization_alias='https://schema.org/processorRequirements',
    )
    install_url: Optional[Union[AnyUrl, List[AnyUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices('installUrl', 'https://schema.org/installUrl'),
        serialization_alias='https://schema.org/installUrl',
    )
    application_sub_category: Optional[
        Union[AnyUrl, str, List[Union[AnyUrl, str]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'applicationSubCategory', 'https://schema.org/applicationSubCategory'
        ),
        serialization_alias='https://schema.org/applicationSubCategory',
    )
    download_url: Optional[Union[AnyUrl, List[AnyUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices('downloadUrl', 'https://schema.org/downloadUrl'),
        serialization_alias='https://schema.org/downloadUrl',
    )
    release_notes: Optional[Union[AnyUrl, str, List[Union[AnyUrl, str]]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'releaseNotes', 'https://schema.org/releaseNotes'
        ),
        serialization_alias='https://schema.org/releaseNotes',
    )
    available_on_device: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'availableOnDevice', 'https://schema.org/availableOnDevice'
        ),
        serialization_alias='https://schema.org/availableOnDevice',
    )
    software_help: Optional[Union[CreativeWork, List[CreativeWork]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'softwareHelp', 'https://schema.org/softwareHelp'
        ),
        serialization_alias='https://schema.org/softwareHelp',
    )
    software_requirements: Optional[
        Union[str, AnyUrl, List[Union[str, AnyUrl]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'softwareRequirements', 'https://schema.org/softwareRequirements'
        ),
        serialization_alias='https://schema.org/softwareRequirements',
    )
    feature_list: Optional[Union[AnyUrl, str, List[Union[AnyUrl, str]]]] = Field(
        default=None,
        validation_alias=AliasChoices('featureList', 'https://schema.org/featureList'),
        serialization_alias='https://schema.org/featureList',
    )
    supporting_data: Optional[Union[DataFeed, List[DataFeed]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'supportingData', 'https://schema.org/supportingData'
        ),
        serialization_alias='https://schema.org/supportingData',
    )
    file_size: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices('fileSize', 'https://schema.org/fileSize'),
        serialization_alias='https://schema.org/fileSize',
    )
    storage_requirements: Optional[
        Union[AnyUrl, str, List[Union[AnyUrl, str]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'storageRequirements', 'https://schema.org/storageRequirements'
        ),
        serialization_alias='https://schema.org/storageRequirements',
    )
    device: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices('device', 'https://schema.org/device'),
        serialization_alias='https://schema.org/device',
    )
    countries_supported: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'countriesSupported', 'https://schema.org/countriesSupported'
        ),
        serialization_alias='https://schema.org/countriesSupported',
    )
    operating_system: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'operatingSystem', 'https://schema.org/operatingSystem'
        ),
        serialization_alias='https://schema.org/operatingSystem',
    )
    screenshot: Optional[
        Union[AnyUrl, ImageObject, List[Union[AnyUrl, ImageObject]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('screenshot', 'https://schema.org/screenshot'),
        serialization_alias='https://schema.org/screenshot',
    )
    software_add_on: Optional[
        Union[SoftwareApplication, List[SoftwareApplication]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'softwareAddOn', 'https://schema.org/softwareAddOn'
        ),
        serialization_alias='https://schema.org/softwareAddOn',
    )
    software_version: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'softwareVersion', 'https://schema.org/softwareVersion'
        ),
        serialization_alias='https://schema.org/softwareVersion',
    )
    application_suite: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'applicationSuite', 'https://schema.org/applicationSuite'
        ),
        serialization_alias='https://schema.org/applicationSuite',
    )


class Dataset(CreativeWork):
    field_type: Literal['https://schema.org/Dataset'] = Field(
        'https://schema.org/Dataset', alias='@type'
    )
    issn: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices('issn', 'https://schema.org/issn'),
        serialization_alias='https://schema.org/issn',
    )
    variable_measured: Optional[
        Union[
            Property,
            StatisticalVariable,
            str,
            PropertyValue,
            List[Union[Property, StatisticalVariable, str, PropertyValue]],
        ]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'variableMeasured', 'https://schema.org/variableMeasured'
        ),
        serialization_alias='https://schema.org/variableMeasured',
    )
    included_data_catalog: Optional[Union[DataCatalog, List[DataCatalog]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'includedDataCatalog', 'https://schema.org/includedDataCatalog'
        ),
        serialization_alias='https://schema.org/includedDataCatalog',
    )
    included_in_data_catalog: Optional[Union[DataCatalog, List[DataCatalog]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'includedInDataCatalog', 'https://schema.org/includedInDataCatalog'
        ),
        serialization_alias='https://schema.org/includedInDataCatalog',
    )
    catalog: Optional[Union[DataCatalog, List[DataCatalog]]] = Field(
        default=None,
        validation_alias=AliasChoices('catalog', 'https://schema.org/catalog'),
        serialization_alias='https://schema.org/catalog',
    )
    variables_measured: Optional[
        Union[str, PropertyValue, List[Union[str, PropertyValue]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'variablesMeasured', 'https://schema.org/variablesMeasured'
        ),
        serialization_alias='https://schema.org/variablesMeasured',
    )
    distribution: Optional[Union[DataDownload, List[DataDownload]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'distribution', 'https://schema.org/distribution'
        ),
        serialization_alias='https://schema.org/distribution',
    )
    measurement_technique: Optional[
        Union[
            DefinedTerm,
            MeasurementMethodEnum,
            str,
            AnyUrl,
            List[Union[DefinedTerm, MeasurementMethodEnum, str, AnyUrl]],
        ]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'measurementTechnique', 'https://schema.org/measurementTechnique'
        ),
        serialization_alias='https://schema.org/measurementTechnique',
    )
    dataset_time_interval: Optional[Union[AwareDatetime, List[AwareDatetime]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'datasetTimeInterval', 'https://schema.org/datasetTimeInterval'
        ),
        serialization_alias='https://schema.org/datasetTimeInterval',
    )
    measurement_method: Optional[
        Union[
            DefinedTerm,
            str,
            MeasurementMethodEnum,
            AnyUrl,
            List[Union[DefinedTerm, str, MeasurementMethodEnum, AnyUrl]],
        ]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'measurementMethod', 'https://schema.org/measurementMethod'
        ),
        serialization_alias='https://schema.org/measurementMethod',
    )


class DataCatalog(CreativeWork):
    field_type: Literal['https://schema.org/DataCatalog'] = Field(
        'https://schema.org/DataCatalog', alias='@type'
    )
    measurement_technique: Optional[
        Union[
            DefinedTerm,
            MeasurementMethodEnum,
            str,
            AnyUrl,
            List[Union[DefinedTerm, MeasurementMethodEnum, str, AnyUrl]],
        ]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'measurementTechnique', 'https://schema.org/measurementTechnique'
        ),
        serialization_alias='https://schema.org/measurementTechnique',
    )
    dataset: Optional[Union[Dataset, List[Dataset]]] = Field(
        default=None,
        validation_alias=AliasChoices('dataset', 'https://schema.org/dataset'),
        serialization_alias='https://schema.org/dataset',
    )
    measurement_method: Optional[
        Union[
            DefinedTerm,
            str,
            MeasurementMethodEnum,
            AnyUrl,
            List[Union[DefinedTerm, str, MeasurementMethodEnum, AnyUrl]],
        ]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'measurementMethod', 'https://schema.org/measurementMethod'
        ),
        serialization_alias='https://schema.org/measurementMethod',
    )


class HowTo(CreativeWork):
    field_type: Literal['https://schema.org/HowTo'] = Field(
        'https://schema.org/HowTo', alias='@type'
    )
    prep_time: Optional[Union[Duration, List[Duration]]] = Field(
        default=None,
        validation_alias=AliasChoices('prepTime', 'https://schema.org/prepTime'),
        serialization_alias='https://schema.org/prepTime',
    )
    perform_time: Optional[Union[Duration, List[Duration]]] = Field(
        default=None,
        validation_alias=AliasChoices('performTime', 'https://schema.org/performTime'),
        serialization_alias='https://schema.org/performTime',
    )
    supply: Optional[Union[HowToSupply, str, List[Union[HowToSupply, str]]]] = Field(
        default=None,
        validation_alias=AliasChoices('supply', 'https://schema.org/supply'),
        serialization_alias='https://schema.org/supply',
    )
    total_time: Optional[Union[Duration, List[Duration]]] = Field(
        default=None,
        validation_alias=AliasChoices('totalTime', 'https://schema.org/totalTime'),
        serialization_alias='https://schema.org/totalTime',
    )
    step: Optional[
        Union[
            str,
            HowToStep,
            CreativeWork,
            HowToSection,
            List[Union[str, HowToStep, CreativeWork, HowToSection]],
        ]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('step', 'https://schema.org/step'),
        serialization_alias='https://schema.org/step',
    )
    estimated_cost: Optional[
        Union[str, MonetaryAmount, List[Union[str, MonetaryAmount]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'estimatedCost', 'https://schema.org/estimatedCost'
        ),
        serialization_alias='https://schema.org/estimatedCost',
    )
    steps: Optional[
        Union[str, CreativeWork, ItemList, List[Union[str, CreativeWork, ItemList]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('steps', 'https://schema.org/steps'),
        serialization_alias='https://schema.org/steps',
    )
    tool: Optional[Union[str, HowToTool, List[Union[str, HowToTool]]]] = Field(
        default=None,
        validation_alias=AliasChoices('tool', 'https://schema.org/tool'),
        serialization_alias='https://schema.org/tool',
    )
    yield_: Optional[
        Union[str, QuantitativeValue, List[Union[str, QuantitativeValue]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('yield', 'https://schema.org/yield'),
        serialization_alias='https://schema.org/yield',
    )


class HowToSection(CreativeWork):
    field_type: Literal['https://schema.org/HowToSection'] = Field(
        'https://schema.org/HowToSection', alias='@type'
    )
    steps: Optional[
        Union[str, CreativeWork, ItemList, List[Union[str, CreativeWork, ItemList]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('steps', 'https://schema.org/steps'),
        serialization_alias='https://schema.org/steps',
    )


class WebSite(CreativeWork):
    field_type: Literal['https://schema.org/WebSite'] = Field(
        'https://schema.org/WebSite', alias='@type'
    )
    issn: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices('issn', 'https://schema.org/issn'),
        serialization_alias='https://schema.org/issn',
    )


class EducationalOccupationalCredential(CreativeWork):
    field_type: Literal['https://schema.org/EducationalOccupationalCredential'] = Field(
        'https://schema.org/EducationalOccupationalCredential', alias='@type'
    )
    recognized_by: Optional[Union[Organization, List[Organization]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'recognizedBy', 'https://schema.org/recognizedBy'
        ),
        serialization_alias='https://schema.org/recognizedBy',
    )
    valid_for: Optional[Union[Duration, List[Duration]]] = Field(
        default=None,
        validation_alias=AliasChoices('validFor', 'https://schema.org/validFor'),
        serialization_alias='https://schema.org/validFor',
    )
    valid_in: Optional[Union[AdministrativeArea, List[AdministrativeArea]]] = Field(
        default=None,
        validation_alias=AliasChoices('validIn', 'https://schema.org/validIn'),
        serialization_alias='https://schema.org/validIn',
    )
    educational_level: Optional[
        Union[str, AnyUrl, DefinedTerm, List[Union[str, AnyUrl, DefinedTerm]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'educationalLevel', 'https://schema.org/educationalLevel'
        ),
        serialization_alias='https://schema.org/educationalLevel',
    )
    competency_required: Optional[
        Union[DefinedTerm, str, AnyUrl, List[Union[DefinedTerm, str, AnyUrl]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'competencyRequired', 'https://schema.org/competencyRequired'
        ),
        serialization_alias='https://schema.org/competencyRequired',
    )
    credential_category: Optional[
        Union[DefinedTerm, str, AnyUrl, List[Union[DefinedTerm, str, AnyUrl]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'credentialCategory', 'https://schema.org/credentialCategory'
        ),
        serialization_alias='https://schema.org/credentialCategory',
    )


class MusicRecording(CreativeWork):
    field_type: Literal['https://schema.org/MusicRecording'] = Field(
        'https://schema.org/MusicRecording', alias='@type'
    )
    in_playlist: Optional[Union[MusicPlaylist, List[MusicPlaylist]]] = Field(
        default=None,
        validation_alias=AliasChoices('inPlaylist', 'https://schema.org/inPlaylist'),
        serialization_alias='https://schema.org/inPlaylist',
    )
    in_album: Optional[Union[MusicAlbum, List[MusicAlbum]]] = Field(
        default=None,
        validation_alias=AliasChoices('inAlbum', 'https://schema.org/inAlbum'),
        serialization_alias='https://schema.org/inAlbum',
    )
    recording_of: Optional[Union[MusicComposition, List[MusicComposition]]] = Field(
        default=None,
        validation_alias=AliasChoices('recordingOf', 'https://schema.org/recordingOf'),
        serialization_alias='https://schema.org/recordingOf',
    )
    by_artist: Optional[
        Union[MusicGroup, Person, List[Union[MusicGroup, Person]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('byArtist', 'https://schema.org/byArtist'),
        serialization_alias='https://schema.org/byArtist',
    )
    isrc_code: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices('isrcCode', 'https://schema.org/isrcCode'),
        serialization_alias='https://schema.org/isrcCode',
    )
    duration: Optional[
        Union[Duration, QuantitativeValue, List[Union[Duration, QuantitativeValue]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('duration', 'https://schema.org/duration'),
        serialization_alias='https://schema.org/duration',
    )


class MusicPlaylist(CreativeWork):
    field_type: Literal['https://schema.org/MusicPlaylist'] = Field(
        'https://schema.org/MusicPlaylist', alias='@type'
    )
    tracks: Optional[Union[MusicRecording, List[MusicRecording]]] = Field(
        default=None,
        validation_alias=AliasChoices('tracks', 'https://schema.org/tracks'),
        serialization_alias='https://schema.org/tracks',
    )
    track: Optional[
        Union[ItemList, MusicRecording, List[Union[ItemList, MusicRecording]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('track', 'https://schema.org/track'),
        serialization_alias='https://schema.org/track',
    )
    num_tracks: Optional[Union[int, List[int]]] = Field(
        default=None,
        validation_alias=AliasChoices('numTracks', 'https://schema.org/numTracks'),
        serialization_alias='https://schema.org/numTracks',
    )


class MusicComposition(CreativeWork):
    field_type: Literal['https://schema.org/MusicComposition'] = Field(
        'https://schema.org/MusicComposition', alias='@type'
    )
    recorded_as: Optional[Union[MusicRecording, List[MusicRecording]]] = Field(
        default=None,
        validation_alias=AliasChoices('recordedAs', 'https://schema.org/recordedAs'),
        serialization_alias='https://schema.org/recordedAs',
    )
    composer: Optional[
        Union[Organization, Person, List[Union[Organization, Person]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('composer', 'https://schema.org/composer'),
        serialization_alias='https://schema.org/composer',
    )
    music_arrangement: Optional[
        Union[MusicComposition, List[MusicComposition]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'musicArrangement', 'https://schema.org/musicArrangement'
        ),
        serialization_alias='https://schema.org/musicArrangement',
    )
    lyrics: Optional[Union[CreativeWork, List[CreativeWork]]] = Field(
        default=None,
        validation_alias=AliasChoices('lyrics', 'https://schema.org/lyrics'),
        serialization_alias='https://schema.org/lyrics',
    )
    included_composition: Optional[
        Union[MusicComposition, List[MusicComposition]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'includedComposition', 'https://schema.org/includedComposition'
        ),
        serialization_alias='https://schema.org/includedComposition',
    )
    musical_key: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices('musicalKey', 'https://schema.org/musicalKey'),
        serialization_alias='https://schema.org/musicalKey',
    )
    iswc_code: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices('iswcCode', 'https://schema.org/iswcCode'),
        serialization_alias='https://schema.org/iswcCode',
    )
    lyricist: Optional[Union[Person, List[Person]]] = Field(
        default=None,
        validation_alias=AliasChoices('lyricist', 'https://schema.org/lyricist'),
        serialization_alias='https://schema.org/lyricist',
    )
    music_composition_form: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'musicCompositionForm', 'https://schema.org/musicCompositionForm'
        ),
        serialization_alias='https://schema.org/musicCompositionForm',
    )
    first_performance: Optional[Union[Event, List[Event]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'firstPerformance', 'https://schema.org/firstPerformance'
        ),
        serialization_alias='https://schema.org/firstPerformance',
    )


class Clip(CreativeWork):
    field_type: Literal['https://schema.org/Clip'] = Field(
        'https://schema.org/Clip', alias='@type'
    )
    clip_number: Optional[Union[int, str, List[Union[int, str]]]] = Field(
        default=None,
        validation_alias=AliasChoices('clipNumber', 'https://schema.org/clipNumber'),
        serialization_alias='https://schema.org/clipNumber',
    )
    director: Optional[Union[Person, List[Person]]] = Field(
        default=None,
        validation_alias=AliasChoices('director', 'https://schema.org/director'),
        serialization_alias='https://schema.org/director',
    )
    part_of_episode: Optional[Union[Episode, List[Episode]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'partOfEpisode', 'https://schema.org/partOfEpisode'
        ),
        serialization_alias='https://schema.org/partOfEpisode',
    )
    part_of_series: Optional[
        Union[CreativeWorkSeries, List[CreativeWorkSeries]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'partOfSeries', 'https://schema.org/partOfSeries'
        ),
        serialization_alias='https://schema.org/partOfSeries',
    )
    end_offset: Optional[
        Union[HyperTocEntry, float, List[Union[HyperTocEntry, float]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('endOffset', 'https://schema.org/endOffset'),
        serialization_alias='https://schema.org/endOffset',
    )
    part_of_season: Optional[
        Union[CreativeWorkSeason, List[CreativeWorkSeason]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'partOfSeason', 'https://schema.org/partOfSeason'
        ),
        serialization_alias='https://schema.org/partOfSeason',
    )
    actor: Optional[
        Union[Person, PerformingGroup, List[Union[Person, PerformingGroup]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('actor', 'https://schema.org/actor'),
        serialization_alias='https://schema.org/actor',
    )
    start_offset: Optional[
        Union[float, HyperTocEntry, List[Union[float, HyperTocEntry]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('startOffset', 'https://schema.org/startOffset'),
        serialization_alias='https://schema.org/startOffset',
    )
    actors: Optional[Union[Person, List[Person]]] = Field(
        default=None,
        validation_alias=AliasChoices('actors', 'https://schema.org/actors'),
        serialization_alias='https://schema.org/actors',
    )
    music_by: Optional[
        Union[MusicGroup, Person, List[Union[MusicGroup, Person]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('musicBy', 'https://schema.org/musicBy'),
        serialization_alias='https://schema.org/musicBy',
    )
    directors: Optional[Union[Person, List[Person]]] = Field(
        default=None,
        validation_alias=AliasChoices('directors', 'https://schema.org/directors'),
        serialization_alias='https://schema.org/directors',
    )


class Episode(CreativeWork):
    field_type: Literal['https://schema.org/Episode'] = Field(
        'https://schema.org/Episode', alias='@type'
    )
    part_of_series: Optional[
        Union[CreativeWorkSeries, List[CreativeWorkSeries]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'partOfSeries', 'https://schema.org/partOfSeries'
        ),
        serialization_alias='https://schema.org/partOfSeries',
    )
    episode_number: Optional[Union[str, int, List[Union[str, int]]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'episodeNumber', 'https://schema.org/episodeNumber'
        ),
        serialization_alias='https://schema.org/episodeNumber',
    )
    part_of_season: Optional[
        Union[CreativeWorkSeason, List[CreativeWorkSeason]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'partOfSeason', 'https://schema.org/partOfSeason'
        ),
        serialization_alias='https://schema.org/partOfSeason',
    )
    actor: Optional[
        Union[Person, PerformingGroup, List[Union[Person, PerformingGroup]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('actor', 'https://schema.org/actor'),
        serialization_alias='https://schema.org/actor',
    )
    production_company: Optional[Union[Organization, List[Organization]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'productionCompany', 'https://schema.org/productionCompany'
        ),
        serialization_alias='https://schema.org/productionCompany',
    )
    music_by: Optional[
        Union[MusicGroup, Person, List[Union[MusicGroup, Person]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('musicBy', 'https://schema.org/musicBy'),
        serialization_alias='https://schema.org/musicBy',
    )
    actors: Optional[Union[Person, List[Person]]] = Field(
        default=None,
        validation_alias=AliasChoices('actors', 'https://schema.org/actors'),
        serialization_alias='https://schema.org/actors',
    )
    trailer: Optional[Union[VideoObject, List[VideoObject]]] = Field(
        default=None,
        validation_alias=AliasChoices('trailer', 'https://schema.org/trailer'),
        serialization_alias='https://schema.org/trailer',
    )
    directors: Optional[Union[Person, List[Person]]] = Field(
        default=None,
        validation_alias=AliasChoices('directors', 'https://schema.org/directors'),
        serialization_alias='https://schema.org/directors',
    )
    duration: Optional[
        Union[Duration, QuantitativeValue, List[Union[Duration, QuantitativeValue]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('duration', 'https://schema.org/duration'),
        serialization_alias='https://schema.org/duration',
    )
    director: Optional[Union[Person, List[Person]]] = Field(
        default=None,
        validation_alias=AliasChoices('director', 'https://schema.org/director'),
        serialization_alias='https://schema.org/director',
    )


class CreativeWorkSeries(CreativeWork):
    field_type: Literal['https://schema.org/CreativeWorkSeries'] = Field(
        'https://schema.org/CreativeWorkSeries', alias='@type'
    )
    end_date: Optional[
        Union[AwareDatetime, date, List[Union[AwareDatetime, date]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('endDate', 'https://schema.org/endDate'),
        serialization_alias='https://schema.org/endDate',
    )
    start_date: Optional[
        Union[date, AwareDatetime, List[Union[date, AwareDatetime]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('startDate', 'https://schema.org/startDate'),
        serialization_alias='https://schema.org/startDate',
    )
    issn: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices('issn', 'https://schema.org/issn'),
        serialization_alias='https://schema.org/issn',
    )


class CreativeWorkSeason(CreativeWork):
    field_type: Literal['https://schema.org/CreativeWorkSeason'] = Field(
        'https://schema.org/CreativeWorkSeason', alias='@type'
    )
    director: Optional[Union[Person, List[Person]]] = Field(
        default=None,
        validation_alias=AliasChoices('director', 'https://schema.org/director'),
        serialization_alias='https://schema.org/director',
    )
    actor: Optional[
        Union[Person, PerformingGroup, List[Union[Person, PerformingGroup]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('actor', 'https://schema.org/actor'),
        serialization_alias='https://schema.org/actor',
    )
    part_of_series: Optional[
        Union[CreativeWorkSeries, List[CreativeWorkSeries]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'partOfSeries', 'https://schema.org/partOfSeries'
        ),
        serialization_alias='https://schema.org/partOfSeries',
    )
    episode: Optional[Union[Episode, List[Episode]]] = Field(
        default=None,
        validation_alias=AliasChoices('episode', 'https://schema.org/episode'),
        serialization_alias='https://schema.org/episode',
    )
    number_of_episodes: Optional[Union[int, List[int]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'numberOfEpisodes', 'https://schema.org/numberOfEpisodes'
        ),
        serialization_alias='https://schema.org/numberOfEpisodes',
    )
    end_date: Optional[
        Union[AwareDatetime, date, List[Union[AwareDatetime, date]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('endDate', 'https://schema.org/endDate'),
        serialization_alias='https://schema.org/endDate',
    )
    production_company: Optional[Union[Organization, List[Organization]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'productionCompany', 'https://schema.org/productionCompany'
        ),
        serialization_alias='https://schema.org/productionCompany',
    )
    season_number: Optional[Union[str, int, List[Union[str, int]]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'seasonNumber', 'https://schema.org/seasonNumber'
        ),
        serialization_alias='https://schema.org/seasonNumber',
    )
    episodes: Optional[Union[Episode, List[Episode]]] = Field(
        default=None,
        validation_alias=AliasChoices('episodes', 'https://schema.org/episodes'),
        serialization_alias='https://schema.org/episodes',
    )
    trailer: Optional[Union[VideoObject, List[VideoObject]]] = Field(
        default=None,
        validation_alias=AliasChoices('trailer', 'https://schema.org/trailer'),
        serialization_alias='https://schema.org/trailer',
    )
    start_date: Optional[
        Union[date, AwareDatetime, List[Union[date, AwareDatetime]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('startDate', 'https://schema.org/startDate'),
        serialization_alias='https://schema.org/startDate',
    )


class HyperTocEntry(CreativeWork):
    field_type: Literal['https://schema.org/HyperTocEntry'] = Field(
        'https://schema.org/HyperTocEntry', alias='@type'
    )
    utterances: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices('utterances', 'https://schema.org/utterances'),
        serialization_alias='https://schema.org/utterances',
    )
    toc_continuation: Optional[Union[HyperTocEntry, List[HyperTocEntry]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'tocContinuation', 'https://schema.org/tocContinuation'
        ),
        serialization_alias='https://schema.org/tocContinuation',
    )
    associated_media: Optional[Union[MediaObject, List[MediaObject]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'associatedMedia', 'https://schema.org/associatedMedia'
        ),
        serialization_alias='https://schema.org/associatedMedia',
    )


class Comment(CreativeWork):
    field_type: Literal['https://schema.org/Comment'] = Field(
        'https://schema.org/Comment', alias='@type'
    )
    parent_item: Optional[
        Union[CreativeWork, Comment, List[Union[CreativeWork, Comment]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('parentItem', 'https://schema.org/parentItem'),
        serialization_alias='https://schema.org/parentItem',
    )
    downvote_count: Optional[Union[int, List[int]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'downvoteCount', 'https://schema.org/downvoteCount'
        ),
        serialization_alias='https://schema.org/downvoteCount',
    )
    shared_content: Optional[Union[CreativeWork, List[CreativeWork]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'sharedContent', 'https://schema.org/sharedContent'
        ),
        serialization_alias='https://schema.org/sharedContent',
    )
    upvote_count: Optional[Union[int, List[int]]] = Field(
        default=None,
        validation_alias=AliasChoices('upvoteCount', 'https://schema.org/upvoteCount'),
        serialization_alias='https://schema.org/upvoteCount',
    )


class PerformingGroup(Organization):
    field_type: Literal['https://schema.org/PerformingGroup'] = Field(
        'https://schema.org/PerformingGroup', alias='@type'
    )


class AdministrativeArea(Place):
    field_type: Literal['https://schema.org/AdministrativeArea'] = Field(
        'https://schema.org/AdministrativeArea', alias='@type'
    )


class CivicStructure(Place):
    field_type: Literal['https://schema.org/CivicStructure'] = Field(
        'https://schema.org/CivicStructure', alias='@type'
    )
    opening_hours: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'openingHours', 'https://schema.org/openingHours'
        ),
        serialization_alias='https://schema.org/openingHours',
    )


class PublicationEvent(Event):
    field_type: Literal['https://schema.org/PublicationEvent'] = Field(
        'https://schema.org/PublicationEvent', alias='@type'
    )
    published_by: Optional[
        Union[Organization, Person, List[Union[Organization, Person]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('publishedBy', 'https://schema.org/publishedBy'),
        serialization_alias='https://schema.org/publishedBy',
    )
    published_on: Optional[Union[BroadcastService, List[BroadcastService]]] = Field(
        default=None,
        validation_alias=AliasChoices('publishedOn', 'https://schema.org/publishedOn'),
        serialization_alias='https://schema.org/publishedOn',
    )
    free: Optional[Union[bool, List[bool]]] = Field(
        default=None,
        validation_alias=AliasChoices('free', 'https://schema.org/free'),
        serialization_alias='https://schema.org/free',
    )


class ProductModel(Product):
    field_type: Literal['https://schema.org/ProductModel'] = Field(
        'https://schema.org/ProductModel', alias='@type'
    )
    predecessor_of: Optional[Union[ProductModel, List[ProductModel]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'predecessorOf', 'https://schema.org/predecessorOf'
        ),
        serialization_alias='https://schema.org/predecessorOf',
    )
    is_variant_of: Optional[
        Union[ProductModel, ProductGroup, List[Union[ProductModel, ProductGroup]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('isVariantOf', 'https://schema.org/isVariantOf'),
        serialization_alias='https://schema.org/isVariantOf',
    )
    successor_of: Optional[Union[ProductModel, List[ProductModel]]] = Field(
        default=None,
        validation_alias=AliasChoices('successorOf', 'https://schema.org/successorOf'),
        serialization_alias='https://schema.org/successorOf',
    )


class ProductGroup(Product):
    field_type: Literal['https://schema.org/ProductGroup'] = Field(
        'https://schema.org/ProductGroup', alias='@type'
    )
    varies_by: Optional[Union[DefinedTerm, str, List[Union[DefinedTerm, str]]]] = Field(
        default=None,
        validation_alias=AliasChoices('variesBy', 'https://schema.org/variesBy'),
        serialization_alias='https://schema.org/variesBy',
    )
    has_variant: Optional[Union[Product, List[Product]]] = Field(
        default=None,
        validation_alias=AliasChoices('hasVariant', 'https://schema.org/hasVariant'),
        serialization_alias='https://schema.org/hasVariant',
    )
    product_group_id: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'productGroupID', 'https://schema.org/productGroupID'
        ),
        serialization_alias='https://schema.org/productGroupID',
    )


class MedicalIntangible(MedicalEntity):
    field_type: Literal['https://schema.org/MedicalIntangible'] = Field(
        'https://schema.org/MedicalIntangible', alias='@type'
    )


class MedicalGuideline(MedicalEntity):
    field_type: Literal['https://schema.org/MedicalGuideline'] = Field(
        'https://schema.org/MedicalGuideline', alias='@type'
    )
    guideline_subject: Optional[Union[MedicalEntity, List[MedicalEntity]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'guidelineSubject', 'https://schema.org/guidelineSubject'
        ),
        serialization_alias='https://schema.org/guidelineSubject',
    )
    evidence_level: Optional[
        Union[MedicalEvidenceLevel, List[MedicalEvidenceLevel]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'evidenceLevel', 'https://schema.org/evidenceLevel'
        ),
        serialization_alias='https://schema.org/evidenceLevel',
    )
    evidence_origin: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'evidenceOrigin', 'https://schema.org/evidenceOrigin'
        ),
        serialization_alias='https://schema.org/evidenceOrigin',
    )
    guideline_date: Optional[Union[date, List[date]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'guidelineDate', 'https://schema.org/guidelineDate'
        ),
        serialization_alias='https://schema.org/guidelineDate',
    )


class MedicalStudy(MedicalEntity):
    field_type: Literal['https://schema.org/MedicalStudy'] = Field(
        'https://schema.org/MedicalStudy', alias='@type'
    )
    study_subject: Optional[Union[MedicalEntity, List[MedicalEntity]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'studySubject', 'https://schema.org/studySubject'
        ),
        serialization_alias='https://schema.org/studySubject',
    )
    sponsor: Optional[
        Union[Organization, Person, List[Union[Organization, Person]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('sponsor', 'https://schema.org/sponsor'),
        serialization_alias='https://schema.org/sponsor',
    )
    status: Optional[
        Union[
            EventStatusType,
            MedicalStudyStatus,
            str,
            List[Union[EventStatusType, MedicalStudyStatus, str]],
        ]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('status', 'https://schema.org/status'),
        serialization_alias='https://schema.org/status',
    )
    study_location: Optional[
        Union[AdministrativeArea, List[AdministrativeArea]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'studyLocation', 'https://schema.org/studyLocation'
        ),
        serialization_alias='https://schema.org/studyLocation',
    )
    health_condition: Optional[Union[MedicalCondition, List[MedicalCondition]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'healthCondition', 'https://schema.org/healthCondition'
        ),
        serialization_alias='https://schema.org/healthCondition',
    )


class MedicalCondition(MedicalEntity):
    field_type: Literal['https://schema.org/MedicalCondition'] = Field(
        'https://schema.org/MedicalCondition', alias='@type'
    )
    associated_anatomy: Optional[
        Union[
            AnatomicalSystem,
            SuperficialAnatomy,
            AnatomicalStructure,
            List[Union[AnatomicalSystem, SuperficialAnatomy, AnatomicalStructure]],
        ]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'associatedAnatomy', 'https://schema.org/associatedAnatomy'
        ),
        serialization_alias='https://schema.org/associatedAnatomy',
    )
    sign_or_symptom: Optional[
        Union[MedicalSignOrSymptom, List[MedicalSignOrSymptom]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'signOrSymptom', 'https://schema.org/signOrSymptom'
        ),
        serialization_alias='https://schema.org/signOrSymptom',
    )
    possible_treatment: Optional[Union[MedicalTherapy, List[MedicalTherapy]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'possibleTreatment', 'https://schema.org/possibleTreatment'
        ),
        serialization_alias='https://schema.org/possibleTreatment',
    )
    status: Optional[
        Union[
            EventStatusType,
            MedicalStudyStatus,
            str,
            List[Union[EventStatusType, MedicalStudyStatus, str]],
        ]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('status', 'https://schema.org/status'),
        serialization_alias='https://schema.org/status',
    )
    typical_test: Optional[Union[MedicalTest, List[MedicalTest]]] = Field(
        default=None,
        validation_alias=AliasChoices('typicalTest', 'https://schema.org/typicalTest'),
        serialization_alias='https://schema.org/typicalTest',
    )
    expected_prognosis: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'expectedPrognosis', 'https://schema.org/expectedPrognosis'
        ),
        serialization_alias='https://schema.org/expectedPrognosis',
    )
    risk_factor: Optional[Union[MedicalRiskFactor, List[MedicalRiskFactor]]] = Field(
        default=None,
        validation_alias=AliasChoices('riskFactor', 'https://schema.org/riskFactor'),
        serialization_alias='https://schema.org/riskFactor',
    )
    natural_progression: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'naturalProgression', 'https://schema.org/naturalProgression'
        ),
        serialization_alias='https://schema.org/naturalProgression',
    )
    secondary_prevention: Optional[Union[MedicalTherapy, List[MedicalTherapy]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'secondaryPrevention', 'https://schema.org/secondaryPrevention'
        ),
        serialization_alias='https://schema.org/secondaryPrevention',
    )
    drug: Optional[Union[Drug, List[Drug]]] = Field(
        default=None,
        validation_alias=AliasChoices('drug', 'https://schema.org/drug'),
        serialization_alias='https://schema.org/drug',
    )
    pathophysiology: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'pathophysiology', 'https://schema.org/pathophysiology'
        ),
        serialization_alias='https://schema.org/pathophysiology',
    )
    primary_prevention: Optional[Union[MedicalTherapy, List[MedicalTherapy]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'primaryPrevention', 'https://schema.org/primaryPrevention'
        ),
        serialization_alias='https://schema.org/primaryPrevention',
    )
    differential_diagnosis: Optional[Union[DDxElement, List[DDxElement]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'differentialDiagnosis', 'https://schema.org/differentialDiagnosis'
        ),
        serialization_alias='https://schema.org/differentialDiagnosis',
    )
    stage: Optional[Union[MedicalConditionStage, List[MedicalConditionStage]]] = Field(
        default=None,
        validation_alias=AliasChoices('stage', 'https://schema.org/stage'),
        serialization_alias='https://schema.org/stage',
    )
    epidemiology: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'epidemiology', 'https://schema.org/epidemiology'
        ),
        serialization_alias='https://schema.org/epidemiology',
    )
    possible_complication: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'possibleComplication', 'https://schema.org/possibleComplication'
        ),
        serialization_alias='https://schema.org/possibleComplication',
    )


class AnatomicalSystem(MedicalEntity):
    field_type: Literal['https://schema.org/AnatomicalSystem'] = Field(
        'https://schema.org/AnatomicalSystem', alias='@type'
    )
    associated_pathophysiology: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'associatedPathophysiology', 'https://schema.org/associatedPathophysiology'
        ),
        serialization_alias='https://schema.org/associatedPathophysiology',
    )
    comprised_of: Optional[
        Union[
            AnatomicalStructure,
            AnatomicalSystem,
            List[Union[AnatomicalStructure, AnatomicalSystem]],
        ]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('comprisedOf', 'https://schema.org/comprisedOf'),
        serialization_alias='https://schema.org/comprisedOf',
    )
    related_structure: Optional[
        Union[AnatomicalStructure, List[AnatomicalStructure]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'relatedStructure', 'https://schema.org/relatedStructure'
        ),
        serialization_alias='https://schema.org/relatedStructure',
    )
    related_condition: Optional[
        Union[MedicalCondition, List[MedicalCondition]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'relatedCondition', 'https://schema.org/relatedCondition'
        ),
        serialization_alias='https://schema.org/relatedCondition',
    )
    related_therapy: Optional[Union[MedicalTherapy, List[MedicalTherapy]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'relatedTherapy', 'https://schema.org/relatedTherapy'
        ),
        serialization_alias='https://schema.org/relatedTherapy',
    )


class AnatomicalStructure(MedicalEntity):
    field_type: Literal['https://schema.org/AnatomicalStructure'] = Field(
        'https://schema.org/AnatomicalStructure', alias='@type'
    )
    sub_structure: Optional[
        Union[AnatomicalStructure, List[AnatomicalStructure]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'subStructure', 'https://schema.org/subStructure'
        ),
        serialization_alias='https://schema.org/subStructure',
    )
    associated_pathophysiology: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'associatedPathophysiology', 'https://schema.org/associatedPathophysiology'
        ),
        serialization_alias='https://schema.org/associatedPathophysiology',
    )
    diagram: Optional[Union[ImageObject, List[ImageObject]]] = Field(
        default=None,
        validation_alias=AliasChoices('diagram', 'https://schema.org/diagram'),
        serialization_alias='https://schema.org/diagram',
    )
    related_condition: Optional[
        Union[MedicalCondition, List[MedicalCondition]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'relatedCondition', 'https://schema.org/relatedCondition'
        ),
        serialization_alias='https://schema.org/relatedCondition',
    )
    body_location: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'bodyLocation', 'https://schema.org/bodyLocation'
        ),
        serialization_alias='https://schema.org/bodyLocation',
    )
    connected_to: Optional[
        Union[AnatomicalStructure, List[AnatomicalStructure]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('connectedTo', 'https://schema.org/connectedTo'),
        serialization_alias='https://schema.org/connectedTo',
    )
    related_therapy: Optional[Union[MedicalTherapy, List[MedicalTherapy]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'relatedTherapy', 'https://schema.org/relatedTherapy'
        ),
        serialization_alias='https://schema.org/relatedTherapy',
    )
    part_of_system: Optional[Union[AnatomicalSystem, List[AnatomicalSystem]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'partOfSystem', 'https://schema.org/partOfSystem'
        ),
        serialization_alias='https://schema.org/partOfSystem',
    )


class MedicalProcedure(MedicalEntity):
    field_type: Literal['https://schema.org/MedicalProcedure'] = Field(
        'https://schema.org/MedicalProcedure', alias='@type'
    )
    body_location: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'bodyLocation', 'https://schema.org/bodyLocation'
        ),
        serialization_alias='https://schema.org/bodyLocation',
    )
    preparation: Optional[
        Union[MedicalEntity, str, List[Union[MedicalEntity, str]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('preparation', 'https://schema.org/preparation'),
        serialization_alias='https://schema.org/preparation',
    )
    status: Optional[
        Union[
            EventStatusType,
            MedicalStudyStatus,
            str,
            List[Union[EventStatusType, MedicalStudyStatus, str]],
        ]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('status', 'https://schema.org/status'),
        serialization_alias='https://schema.org/status',
    )
    how_performed: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'howPerformed', 'https://schema.org/howPerformed'
        ),
        serialization_alias='https://schema.org/howPerformed',
    )
    procedure_type: Optional[
        Union[MedicalProcedureType, List[MedicalProcedureType]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'procedureType', 'https://schema.org/procedureType'
        ),
        serialization_alias='https://schema.org/procedureType',
    )
    followup: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices('followup', 'https://schema.org/followup'),
        serialization_alias='https://schema.org/followup',
    )


class Substance(MedicalEntity):
    field_type: Literal['https://schema.org/Substance'] = Field(
        'https://schema.org/Substance', alias='@type'
    )
    maximum_intake: Optional[
        Union[MaximumDoseSchedule, List[MaximumDoseSchedule]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'maximumIntake', 'https://schema.org/maximumIntake'
        ),
        serialization_alias='https://schema.org/maximumIntake',
    )
    active_ingredient: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'activeIngredient', 'https://schema.org/activeIngredient'
        ),
        serialization_alias='https://schema.org/activeIngredient',
    )


class DrugClass(MedicalEntity):
    field_type: Literal['https://schema.org/DrugClass'] = Field(
        'https://schema.org/DrugClass', alias='@type'
    )
    drug: Optional[Union[Drug, List[Drug]]] = Field(
        default=None,
        validation_alias=AliasChoices('drug', 'https://schema.org/drug'),
        serialization_alias='https://schema.org/drug',
    )


class MedicalContraindication(MedicalEntity):
    field_type: Literal['https://schema.org/MedicalContraindication'] = Field(
        'https://schema.org/MedicalContraindication', alias='@type'
    )


class SuperficialAnatomy(MedicalEntity):
    field_type: Literal['https://schema.org/SuperficialAnatomy'] = Field(
        'https://schema.org/SuperficialAnatomy', alias='@type'
    )
    associated_pathophysiology: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'associatedPathophysiology', 'https://schema.org/associatedPathophysiology'
        ),
        serialization_alias='https://schema.org/associatedPathophysiology',
    )
    related_condition: Optional[
        Union[MedicalCondition, List[MedicalCondition]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'relatedCondition', 'https://schema.org/relatedCondition'
        ),
        serialization_alias='https://schema.org/relatedCondition',
    )
    related_therapy: Optional[Union[MedicalTherapy, List[MedicalTherapy]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'relatedTherapy', 'https://schema.org/relatedTherapy'
        ),
        serialization_alias='https://schema.org/relatedTherapy',
    )
    related_anatomy: Optional[
        Union[
            AnatomicalStructure,
            AnatomicalSystem,
            List[Union[AnatomicalStructure, AnatomicalSystem]],
        ]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'relatedAnatomy', 'https://schema.org/relatedAnatomy'
        ),
        serialization_alias='https://schema.org/relatedAnatomy',
    )
    significance: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'significance', 'https://schema.org/significance'
        ),
        serialization_alias='https://schema.org/significance',
    )


class MedicalTest(MedicalEntity):
    field_type: Literal['https://schema.org/MedicalTest'] = Field(
        'https://schema.org/MedicalTest', alias='@type'
    )
    affected_by: Optional[Union[Drug, List[Drug]]] = Field(
        default=None,
        validation_alias=AliasChoices('affectedBy', 'https://schema.org/affectedBy'),
        serialization_alias='https://schema.org/affectedBy',
    )
    sign_detected: Optional[Union[MedicalSign, List[MedicalSign]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'signDetected', 'https://schema.org/signDetected'
        ),
        serialization_alias='https://schema.org/signDetected',
    )
    uses_device: Optional[Union[MedicalDevice, List[MedicalDevice]]] = Field(
        default=None,
        validation_alias=AliasChoices('usesDevice', 'https://schema.org/usesDevice'),
        serialization_alias='https://schema.org/usesDevice',
    )
    used_to_diagnose: Optional[Union[MedicalCondition, List[MedicalCondition]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'usedToDiagnose', 'https://schema.org/usedToDiagnose'
        ),
        serialization_alias='https://schema.org/usedToDiagnose',
    )
    normal_range: Optional[
        Union[MedicalEnumeration, str, List[Union[MedicalEnumeration, str]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('normalRange', 'https://schema.org/normalRange'),
        serialization_alias='https://schema.org/normalRange',
    )


class MedicalDevice(MedicalEntity):
    field_type: Literal['https://schema.org/MedicalDevice'] = Field(
        'https://schema.org/MedicalDevice', alias='@type'
    )
    procedure: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices('procedure', 'https://schema.org/procedure'),
        serialization_alias='https://schema.org/procedure',
    )
    serious_adverse_outcome: Optional[
        Union[MedicalEntity, List[MedicalEntity]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'seriousAdverseOutcome', 'https://schema.org/seriousAdverseOutcome'
        ),
        serialization_alias='https://schema.org/seriousAdverseOutcome',
    )
    adverse_outcome: Optional[Union[MedicalEntity, List[MedicalEntity]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'adverseOutcome', 'https://schema.org/adverseOutcome'
        ),
        serialization_alias='https://schema.org/adverseOutcome',
    )
    pre_op: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices('preOp', 'https://schema.org/preOp'),
        serialization_alias='https://schema.org/preOp',
    )
    contraindication: Optional[
        Union[str, MedicalContraindication, List[Union[str, MedicalContraindication]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'contraindication', 'https://schema.org/contraindication'
        ),
        serialization_alias='https://schema.org/contraindication',
    )
    post_op: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices('postOp', 'https://schema.org/postOp'),
        serialization_alias='https://schema.org/postOp',
    )


class MedicalRiskFactor(MedicalEntity):
    field_type: Literal['https://schema.org/MedicalRiskFactor'] = Field(
        'https://schema.org/MedicalRiskFactor', alias='@type'
    )
    increases_risk_of: Optional[Union[MedicalEntity, List[MedicalEntity]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'increasesRiskOf', 'https://schema.org/increasesRiskOf'
        ),
        serialization_alias='https://schema.org/increasesRiskOf',
    )


class Gene(BioChemEntity):
    field_type: Literal['https://schema.org/Gene'] = Field(
        'https://schema.org/Gene', alias='@type'
    )
    expressed_in: Optional[
        Union[
            BioChemEntity,
            AnatomicalSystem,
            AnatomicalStructure,
            DefinedTerm,
            List[
                Union[BioChemEntity, AnatomicalSystem, AnatomicalStructure, DefinedTerm]
            ],
        ]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('expressedIn', 'https://schema.org/expressedIn'),
        serialization_alias='https://schema.org/expressedIn',
    )
    has_bio_polymer_sequence: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'hasBioPolymerSequence', 'https://schema.org/hasBioPolymerSequence'
        ),
        serialization_alias='https://schema.org/hasBioPolymerSequence',
    )
    alternative_of: Optional[Union[Gene, List[Gene]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'alternativeOf', 'https://schema.org/alternativeOf'
        ),
        serialization_alias='https://schema.org/alternativeOf',
    )
    encodes_bio_chem_entity: Optional[
        Union[BioChemEntity, List[BioChemEntity]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'encodesBioChemEntity', 'https://schema.org/encodesBioChemEntity'
        ),
        serialization_alias='https://schema.org/encodesBioChemEntity',
    )


class PropertyValue(StructuredValue):
    field_type: Literal['https://schema.org/PropertyValue'] = Field(
        'https://schema.org/PropertyValue', alias='@type'
    )
    unit_text: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices('unitText', 'https://schema.org/unitText'),
        serialization_alias='https://schema.org/unitText',
    )
    measurement_technique: Optional[
        Union[
            DefinedTerm,
            MeasurementMethodEnum,
            str,
            AnyUrl,
            List[Union[DefinedTerm, MeasurementMethodEnum, str, AnyUrl]],
        ]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'measurementTechnique', 'https://schema.org/measurementTechnique'
        ),
        serialization_alias='https://schema.org/measurementTechnique',
    )
    min_value: Optional[Union[float, List[float]]] = Field(
        default=None,
        validation_alias=AliasChoices('minValue', 'https://schema.org/minValue'),
        serialization_alias='https://schema.org/minValue',
    )
    property_id: Optional[Union[AnyUrl, str, List[Union[AnyUrl, str]]]] = Field(
        default=None,
        validation_alias=AliasChoices('propertyID', 'https://schema.org/propertyID'),
        serialization_alias='https://schema.org/propertyID',
    )
    value: Optional[
        Union[
            float,
            StructuredValue,
            bool,
            str,
            List[Union[float, StructuredValue, bool, str]],
        ]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('value', 'https://schema.org/value'),
        serialization_alias='https://schema.org/value',
    )
    max_value: Optional[Union[float, List[float]]] = Field(
        default=None,
        validation_alias=AliasChoices('maxValue', 'https://schema.org/maxValue'),
        serialization_alias='https://schema.org/maxValue',
    )
    unit_code: Optional[Union[AnyUrl, str, List[Union[AnyUrl, str]]]] = Field(
        default=None,
        validation_alias=AliasChoices('unitCode', 'https://schema.org/unitCode'),
        serialization_alias='https://schema.org/unitCode',
    )
    measurement_method: Optional[
        Union[
            DefinedTerm,
            str,
            MeasurementMethodEnum,
            AnyUrl,
            List[Union[DefinedTerm, str, MeasurementMethodEnum, AnyUrl]],
        ]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'measurementMethod', 'https://schema.org/measurementMethod'
        ),
        serialization_alias='https://schema.org/measurementMethod',
    )
    value_reference: Optional[
        Union[
            DefinedTerm,
            MeasurementTypeEnumeration,
            str,
            Enumeration,
            QualitativeValue,
            QuantitativeValue,
            PropertyValue,
            StructuredValue,
            List[
                Union[
                    DefinedTerm,
                    MeasurementTypeEnumeration,
                    str,
                    Enumeration,
                    QualitativeValue,
                    QuantitativeValue,
                    PropertyValue,
                    StructuredValue,
                ]
            ],
        ]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'valueReference', 'https://schema.org/valueReference'
        ),
        serialization_alias='https://schema.org/valueReference',
    )


class QuantitativeValue(StructuredValue):
    field_type: Literal['https://schema.org/QuantitativeValue'] = Field(
        'https://schema.org/QuantitativeValue', alias='@type'
    )
    unit_text: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices('unitText', 'https://schema.org/unitText'),
        serialization_alias='https://schema.org/unitText',
    )
    min_value: Optional[Union[float, List[float]]] = Field(
        default=None,
        validation_alias=AliasChoices('minValue', 'https://schema.org/minValue'),
        serialization_alias='https://schema.org/minValue',
    )
    value: Optional[
        Union[
            float,
            StructuredValue,
            bool,
            str,
            List[Union[float, StructuredValue, bool, str]],
        ]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('value', 'https://schema.org/value'),
        serialization_alias='https://schema.org/value',
    )
    max_value: Optional[Union[float, List[float]]] = Field(
        default=None,
        validation_alias=AliasChoices('maxValue', 'https://schema.org/maxValue'),
        serialization_alias='https://schema.org/maxValue',
    )
    unit_code: Optional[Union[AnyUrl, str, List[Union[AnyUrl, str]]]] = Field(
        default=None,
        validation_alias=AliasChoices('unitCode', 'https://schema.org/unitCode'),
        serialization_alias='https://schema.org/unitCode',
    )
    additional_property: Optional[Union[PropertyValue, List[PropertyValue]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'additionalProperty', 'https://schema.org/additionalProperty'
        ),
        serialization_alias='https://schema.org/additionalProperty',
    )
    value_reference: Optional[
        Union[
            DefinedTerm,
            MeasurementTypeEnumeration,
            str,
            Enumeration,
            QualitativeValue,
            QuantitativeValue,
            PropertyValue,
            StructuredValue,
            List[
                Union[
                    DefinedTerm,
                    MeasurementTypeEnumeration,
                    str,
                    Enumeration,
                    QualitativeValue,
                    QuantitativeValue,
                    PropertyValue,
                    StructuredValue,
                ]
            ],
        ]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'valueReference', 'https://schema.org/valueReference'
        ),
        serialization_alias='https://schema.org/valueReference',
    )


class ContactPoint(StructuredValue):
    field_type: Literal['https://schema.org/ContactPoint'] = Field(
        'https://schema.org/ContactPoint', alias='@type'
    )
    service_area: Optional[
        Union[
            AdministrativeArea,
            GeoShape,
            Place,
            List[Union[AdministrativeArea, GeoShape, Place]],
        ]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('serviceArea', 'https://schema.org/serviceArea'),
        serialization_alias='https://schema.org/serviceArea',
    )
    email: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices('email', 'https://schema.org/email'),
        serialization_alias='https://schema.org/email',
    )
    hours_available: Optional[
        Union[OpeningHoursSpecification, List[OpeningHoursSpecification]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'hoursAvailable', 'https://schema.org/hoursAvailable'
        ),
        serialization_alias='https://schema.org/hoursAvailable',
    )
    telephone: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices('telephone', 'https://schema.org/telephone'),
        serialization_alias='https://schema.org/telephone',
    )
    available_language: Optional[
        Union[str, Language, List[Union[str, Language]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'availableLanguage', 'https://schema.org/availableLanguage'
        ),
        serialization_alias='https://schema.org/availableLanguage',
    )
    product_supported: Optional[Union[str, Product, List[Union[str, Product]]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'productSupported', 'https://schema.org/productSupported'
        ),
        serialization_alias='https://schema.org/productSupported',
    )
    contact_option: Optional[
        Union[ContactPointOption, List[ContactPointOption]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'contactOption', 'https://schema.org/contactOption'
        ),
        serialization_alias='https://schema.org/contactOption',
    )
    contact_type: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices('contactType', 'https://schema.org/contactType'),
        serialization_alias='https://schema.org/contactType',
    )
    fax_number: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices('faxNumber', 'https://schema.org/faxNumber'),
        serialization_alias='https://schema.org/faxNumber',
    )
    area_served: Optional[
        Union[
            GeoShape,
            str,
            AdministrativeArea,
            Place,
            List[Union[GeoShape, str, AdministrativeArea, Place]],
        ]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('areaServed', 'https://schema.org/areaServed'),
        serialization_alias='https://schema.org/areaServed',
    )


class GeoShape(StructuredValue):
    field_type: Literal['https://schema.org/GeoShape'] = Field(
        'https://schema.org/GeoShape', alias='@type'
    )
    circle: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices('circle', 'https://schema.org/circle'),
        serialization_alias='https://schema.org/circle',
    )
    line: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices('line', 'https://schema.org/line'),
        serialization_alias='https://schema.org/line',
    )
    address: Optional[
        Union[str, PostalAddress, List[Union[str, PostalAddress]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('address', 'https://schema.org/address'),
        serialization_alias='https://schema.org/address',
    )
    postal_code: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices('postalCode', 'https://schema.org/postalCode'),
        serialization_alias='https://schema.org/postalCode',
    )
    elevation: Optional[Union[str, float, List[Union[str, float]]]] = Field(
        default=None,
        validation_alias=AliasChoices('elevation', 'https://schema.org/elevation'),
        serialization_alias='https://schema.org/elevation',
    )
    address_country: Optional[Union[str, Country, List[Union[str, Country]]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'addressCountry', 'https://schema.org/addressCountry'
        ),
        serialization_alias='https://schema.org/addressCountry',
    )
    polygon: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices('polygon', 'https://schema.org/polygon'),
        serialization_alias='https://schema.org/polygon',
    )
    box: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices('box', 'https://schema.org/box'),
        serialization_alias='https://schema.org/box',
    )


class OpeningHoursSpecification(StructuredValue):
    field_type: Literal['https://schema.org/OpeningHoursSpecification'] = Field(
        'https://schema.org/OpeningHoursSpecification', alias='@type'
    )
    day_of_week: Optional[Union[DayOfWeek, List[DayOfWeek]]] = Field(
        default=None,
        validation_alias=AliasChoices('dayOfWeek', 'https://schema.org/dayOfWeek'),
        serialization_alias='https://schema.org/dayOfWeek',
    )
    valid_from: Optional[
        Union[date, AwareDatetime, List[Union[date, AwareDatetime]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('validFrom', 'https://schema.org/validFrom'),
        serialization_alias='https://schema.org/validFrom',
    )
    closes: Optional[Union[time, List[time]]] = Field(
        default=None,
        validation_alias=AliasChoices('closes', 'https://schema.org/closes'),
        serialization_alias='https://schema.org/closes',
    )
    opens: Optional[Union[time, List[time]]] = Field(
        default=None,
        validation_alias=AliasChoices('opens', 'https://schema.org/opens'),
        serialization_alias='https://schema.org/opens',
    )
    valid_through: Optional[
        Union[AwareDatetime, date, List[Union[AwareDatetime, date]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'validThrough', 'https://schema.org/validThrough'
        ),
        serialization_alias='https://schema.org/validThrough',
    )


class PriceSpecification(StructuredValue):
    field_type: Literal['https://schema.org/PriceSpecification'] = Field(
        'https://schema.org/PriceSpecification', alias='@type'
    )
    min_price: Optional[Union[float, List[float]]] = Field(
        default=None,
        validation_alias=AliasChoices('minPrice', 'https://schema.org/minPrice'),
        serialization_alias='https://schema.org/minPrice',
    )
    max_price: Optional[Union[float, List[float]]] = Field(
        default=None,
        validation_alias=AliasChoices('maxPrice', 'https://schema.org/maxPrice'),
        serialization_alias='https://schema.org/maxPrice',
    )
    price_currency: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'priceCurrency', 'https://schema.org/priceCurrency'
        ),
        serialization_alias='https://schema.org/priceCurrency',
    )
    value_added_tax_included: Optional[Union[bool, List[bool]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'valueAddedTaxIncluded', 'https://schema.org/valueAddedTaxIncluded'
        ),
        serialization_alias='https://schema.org/valueAddedTaxIncluded',
    )
    eligible_quantity: Optional[
        Union[QuantitativeValue, List[QuantitativeValue]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'eligibleQuantity', 'https://schema.org/eligibleQuantity'
        ),
        serialization_alias='https://schema.org/eligibleQuantity',
    )
    valid_through: Optional[
        Union[AwareDatetime, date, List[Union[AwareDatetime, date]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'validThrough', 'https://schema.org/validThrough'
        ),
        serialization_alias='https://schema.org/validThrough',
    )
    eligible_transaction_volume: Optional[
        Union[PriceSpecification, List[PriceSpecification]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'eligibleTransactionVolume', 'https://schema.org/eligibleTransactionVolume'
        ),
        serialization_alias='https://schema.org/eligibleTransactionVolume',
    )
    valid_from: Optional[
        Union[date, AwareDatetime, List[Union[date, AwareDatetime]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('validFrom', 'https://schema.org/validFrom'),
        serialization_alias='https://schema.org/validFrom',
    )
    valid_for_member_tier: Optional[
        Union[MemberProgramTier, List[MemberProgramTier]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'validForMemberTier', 'https://schema.org/validForMemberTier'
        ),
        serialization_alias='https://schema.org/validForMemberTier',
    )
    membership_points_earned: Optional[
        Union[QuantitativeValue, float, List[Union[QuantitativeValue, float]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'membershipPointsEarned', 'https://schema.org/membershipPointsEarned'
        ),
        serialization_alias='https://schema.org/membershipPointsEarned',
    )
    price: Optional[Union[str, float, List[Union[str, float]]]] = Field(
        default=None,
        validation_alias=AliasChoices('price', 'https://schema.org/price'),
        serialization_alias='https://schema.org/price',
    )


class MonetaryAmount(StructuredValue):
    field_type: Literal['https://schema.org/MonetaryAmount'] = Field(
        'https://schema.org/MonetaryAmount', alias='@type'
    )
    currency: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices('currency', 'https://schema.org/currency'),
        serialization_alias='https://schema.org/currency',
    )
    valid_through: Optional[
        Union[AwareDatetime, date, List[Union[AwareDatetime, date]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'validThrough', 'https://schema.org/validThrough'
        ),
        serialization_alias='https://schema.org/validThrough',
    )
    min_value: Optional[Union[float, List[float]]] = Field(
        default=None,
        validation_alias=AliasChoices('minValue', 'https://schema.org/minValue'),
        serialization_alias='https://schema.org/minValue',
    )
    value: Optional[
        Union[
            float,
            StructuredValue,
            bool,
            str,
            List[Union[float, StructuredValue, bool, str]],
        ]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('value', 'https://schema.org/value'),
        serialization_alias='https://schema.org/value',
    )
    valid_from: Optional[
        Union[date, AwareDatetime, List[Union[date, AwareDatetime]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('validFrom', 'https://schema.org/validFrom'),
        serialization_alias='https://schema.org/validFrom',
    )
    max_value: Optional[Union[float, List[float]]] = Field(
        default=None,
        validation_alias=AliasChoices('maxValue', 'https://schema.org/maxValue'),
        serialization_alias='https://schema.org/maxValue',
    )


class TypeAndQuantityNode(StructuredValue):
    field_type: Literal['https://schema.org/TypeAndQuantityNode'] = Field(
        'https://schema.org/TypeAndQuantityNode', alias='@type'
    )
    amount_of_this_good: Optional[Union[float, List[float]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'amountOfThisGood', 'https://schema.org/amountOfThisGood'
        ),
        serialization_alias='https://schema.org/amountOfThisGood',
    )
    unit_text: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices('unitText', 'https://schema.org/unitText'),
        serialization_alias='https://schema.org/unitText',
    )
    business_function: Optional[
        Union[BusinessFunction, List[BusinessFunction]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'businessFunction', 'https://schema.org/businessFunction'
        ),
        serialization_alias='https://schema.org/businessFunction',
    )
    type_of_good: Optional[
        Union[Product, Service, List[Union[Product, Service]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('typeOfGood', 'https://schema.org/typeOfGood'),
        serialization_alias='https://schema.org/typeOfGood',
    )
    unit_code: Optional[Union[AnyUrl, str, List[Union[AnyUrl, str]]]] = Field(
        default=None,
        validation_alias=AliasChoices('unitCode', 'https://schema.org/unitCode'),
        serialization_alias='https://schema.org/unitCode',
    )


class RepaymentSpecification(StructuredValue):
    field_type: Literal['https://schema.org/RepaymentSpecification'] = Field(
        'https://schema.org/RepaymentSpecification', alias='@type'
    )
    number_of_loan_payments: Optional[Union[float, List[float]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'numberOfLoanPayments', 'https://schema.org/numberOfLoanPayments'
        ),
        serialization_alias='https://schema.org/numberOfLoanPayments',
    )
    loan_payment_amount: Optional[Union[MonetaryAmount, List[MonetaryAmount]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'loanPaymentAmount', 'https://schema.org/loanPaymentAmount'
        ),
        serialization_alias='https://schema.org/loanPaymentAmount',
    )
    early_prepayment_penalty: Optional[
        Union[MonetaryAmount, List[MonetaryAmount]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'earlyPrepaymentPenalty', 'https://schema.org/earlyPrepaymentPenalty'
        ),
        serialization_alias='https://schema.org/earlyPrepaymentPenalty',
    )
    down_payment: Optional[
        Union[float, MonetaryAmount, List[Union[float, MonetaryAmount]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('downPayment', 'https://schema.org/downPayment'),
        serialization_alias='https://schema.org/downPayment',
    )
    loan_payment_frequency: Optional[Union[float, List[float]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'loanPaymentFrequency', 'https://schema.org/loanPaymentFrequency'
        ),
        serialization_alias='https://schema.org/loanPaymentFrequency',
    )


class OfferShippingDetails(StructuredValue):
    field_type: Literal['https://schema.org/OfferShippingDetails'] = Field(
        'https://schema.org/OfferShippingDetails', alias='@type'
    )
    depth: Optional[
        Union[Distance, QuantitativeValue, List[Union[Distance, QuantitativeValue]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('depth', 'https://schema.org/depth'),
        serialization_alias='https://schema.org/depth',
    )
    shipping_label: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'shippingLabel', 'https://schema.org/shippingLabel'
        ),
        serialization_alias='https://schema.org/shippingLabel',
    )
    has_shipping_service: Optional[
        Union[ShippingService, List[ShippingService]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'hasShippingService', 'https://schema.org/hasShippingService'
        ),
        serialization_alias='https://schema.org/hasShippingService',
    )
    shipping_destination: Optional[Union[DefinedRegion, List[DefinedRegion]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'shippingDestination', 'https://schema.org/shippingDestination'
        ),
        serialization_alias='https://schema.org/shippingDestination',
    )
    delivery_time: Optional[
        Union[ShippingDeliveryTime, List[ShippingDeliveryTime]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'deliveryTime', 'https://schema.org/deliveryTime'
        ),
        serialization_alias='https://schema.org/deliveryTime',
    )
    does_not_ship: Optional[Union[bool, List[bool]]] = Field(
        default=None,
        validation_alias=AliasChoices('doesNotShip', 'https://schema.org/doesNotShip'),
        serialization_alias='https://schema.org/doesNotShip',
    )
    width: Optional[
        Union[QuantitativeValue, Distance, List[Union[QuantitativeValue, Distance]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('width', 'https://schema.org/width'),
        serialization_alias='https://schema.org/width',
    )
    valid_for_member_tier: Optional[
        Union[MemberProgramTier, List[MemberProgramTier]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'validForMemberTier', 'https://schema.org/validForMemberTier'
        ),
        serialization_alias='https://schema.org/validForMemberTier',
    )
    shipping_origin: Optional[Union[DefinedRegion, List[DefinedRegion]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'shippingOrigin', 'https://schema.org/shippingOrigin'
        ),
        serialization_alias='https://schema.org/shippingOrigin',
    )
    height: Optional[
        Union[Distance, QuantitativeValue, List[Union[Distance, QuantitativeValue]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('height', 'https://schema.org/height'),
        serialization_alias='https://schema.org/height',
    )
    transit_time_label: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'transitTimeLabel', 'https://schema.org/transitTimeLabel'
        ),
        serialization_alias='https://schema.org/transitTimeLabel',
    )
    weight: Optional[
        Union[QuantitativeValue, Mass, List[Union[QuantitativeValue, Mass]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('weight', 'https://schema.org/weight'),
        serialization_alias='https://schema.org/weight',
    )
    shipping_rate: Optional[
        Union[
            ShippingRateSettings,
            MonetaryAmount,
            List[Union[ShippingRateSettings, MonetaryAmount]],
        ]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'shippingRate', 'https://schema.org/shippingRate'
        ),
        serialization_alias='https://schema.org/shippingRate',
    )
    shipping_settings_link: Optional[Union[AnyUrl, List[AnyUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'shippingSettingsLink', 'https://schema.org/shippingSettingsLink'
        ),
        serialization_alias='https://schema.org/shippingSettingsLink',
    )


class ShippingService(StructuredValue):
    field_type: Literal['https://schema.org/ShippingService'] = Field(
        'https://schema.org/ShippingService', alias='@type'
    )
    fulfillment_type: Optional[
        Union[FulfillmentTypeEnumeration, List[FulfillmentTypeEnumeration]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'fulfillmentType', 'https://schema.org/fulfillmentType'
        ),
        serialization_alias='https://schema.org/fulfillmentType',
    )
    shipping_conditions: Optional[
        Union[ShippingConditions, List[ShippingConditions]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'shippingConditions', 'https://schema.org/shippingConditions'
        ),
        serialization_alias='https://schema.org/shippingConditions',
    )
    valid_for_member_tier: Optional[
        Union[MemberProgramTier, List[MemberProgramTier]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'validForMemberTier', 'https://schema.org/validForMemberTier'
        ),
        serialization_alias='https://schema.org/validForMemberTier',
    )
    handling_time: Optional[
        Union[
            ServicePeriod,
            QuantitativeValue,
            List[Union[ServicePeriod, QuantitativeValue]],
        ]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'handlingTime', 'https://schema.org/handlingTime'
        ),
        serialization_alias='https://schema.org/handlingTime',
    )


class ShippingConditions(StructuredValue):
    field_type: Literal['https://schema.org/ShippingConditions'] = Field(
        'https://schema.org/ShippingConditions', alias='@type'
    )
    weight: Optional[
        Union[QuantitativeValue, Mass, List[Union[QuantitativeValue, Mass]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('weight', 'https://schema.org/weight'),
        serialization_alias='https://schema.org/weight',
    )
    shipping_origin: Optional[Union[DefinedRegion, List[DefinedRegion]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'shippingOrigin', 'https://schema.org/shippingOrigin'
        ),
        serialization_alias='https://schema.org/shippingOrigin',
    )
    shipping_destination: Optional[Union[DefinedRegion, List[DefinedRegion]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'shippingDestination', 'https://schema.org/shippingDestination'
        ),
        serialization_alias='https://schema.org/shippingDestination',
    )
    seasonal_override: Optional[
        Union[OpeningHoursSpecification, List[OpeningHoursSpecification]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'seasonalOverride', 'https://schema.org/seasonalOverride'
        ),
        serialization_alias='https://schema.org/seasonalOverride',
    )
    shipping_rate: Optional[
        Union[
            ShippingRateSettings,
            MonetaryAmount,
            List[Union[ShippingRateSettings, MonetaryAmount]],
        ]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'shippingRate', 'https://schema.org/shippingRate'
        ),
        serialization_alias='https://schema.org/shippingRate',
    )
    depth: Optional[
        Union[Distance, QuantitativeValue, List[Union[Distance, QuantitativeValue]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('depth', 'https://schema.org/depth'),
        serialization_alias='https://schema.org/depth',
    )
    does_not_ship: Optional[Union[bool, List[bool]]] = Field(
        default=None,
        validation_alias=AliasChoices('doesNotShip', 'https://schema.org/doesNotShip'),
        serialization_alias='https://schema.org/doesNotShip',
    )
    width: Optional[
        Union[QuantitativeValue, Distance, List[Union[QuantitativeValue, Distance]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('width', 'https://schema.org/width'),
        serialization_alias='https://schema.org/width',
    )
    num_items: Optional[Union[QuantitativeValue, List[QuantitativeValue]]] = Field(
        default=None,
        validation_alias=AliasChoices('numItems', 'https://schema.org/numItems'),
        serialization_alias='https://schema.org/numItems',
    )
    order_value: Optional[Union[MonetaryAmount, List[MonetaryAmount]]] = Field(
        default=None,
        validation_alias=AliasChoices('orderValue', 'https://schema.org/orderValue'),
        serialization_alias='https://schema.org/orderValue',
    )
    transit_time: Optional[
        Union[
            ServicePeriod,
            QuantitativeValue,
            List[Union[ServicePeriod, QuantitativeValue]],
        ]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('transitTime', 'https://schema.org/transitTime'),
        serialization_alias='https://schema.org/transitTime',
    )
    height: Optional[
        Union[Distance, QuantitativeValue, List[Union[Distance, QuantitativeValue]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('height', 'https://schema.org/height'),
        serialization_alias='https://schema.org/height',
    )


class DefinedRegion(StructuredValue):
    field_type: Literal['https://schema.org/DefinedRegion'] = Field(
        'https://schema.org/DefinedRegion', alias='@type'
    )
    postal_code_range: Optional[
        Union[PostalCodeRangeSpecification, List[PostalCodeRangeSpecification]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'postalCodeRange', 'https://schema.org/postalCodeRange'
        ),
        serialization_alias='https://schema.org/postalCodeRange',
    )
    address_region: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'addressRegion', 'https://schema.org/addressRegion'
        ),
        serialization_alias='https://schema.org/addressRegion',
    )
    postal_code: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices('postalCode', 'https://schema.org/postalCode'),
        serialization_alias='https://schema.org/postalCode',
    )
    address_country: Optional[Union[str, Country, List[Union[str, Country]]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'addressCountry', 'https://schema.org/addressCountry'
        ),
        serialization_alias='https://schema.org/addressCountry',
    )
    postal_code_prefix: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'postalCodePrefix', 'https://schema.org/postalCodePrefix'
        ),
        serialization_alias='https://schema.org/postalCodePrefix',
    )


class PostalCodeRangeSpecification(StructuredValue):
    field_type: Literal['https://schema.org/PostalCodeRangeSpecification'] = Field(
        'https://schema.org/PostalCodeRangeSpecification', alias='@type'
    )
    postal_code_begin: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'postalCodeBegin', 'https://schema.org/postalCodeBegin'
        ),
        serialization_alias='https://schema.org/postalCodeBegin',
    )
    postal_code_end: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'postalCodeEnd', 'https://schema.org/postalCodeEnd'
        ),
        serialization_alias='https://schema.org/postalCodeEnd',
    )


class ShippingRateSettings(StructuredValue):
    field_type: Literal['https://schema.org/ShippingRateSettings'] = Field(
        'https://schema.org/ShippingRateSettings', alias='@type'
    )
    weight_percentage: Optional[Union[float, List[float]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'weightPercentage', 'https://schema.org/weightPercentage'
        ),
        serialization_alias='https://schema.org/weightPercentage',
    )
    does_not_ship: Optional[Union[bool, List[bool]]] = Field(
        default=None,
        validation_alias=AliasChoices('doesNotShip', 'https://schema.org/doesNotShip'),
        serialization_alias='https://schema.org/doesNotShip',
    )
    free_shipping_threshold: Optional[
        Union[
            DeliveryChargeSpecification,
            MonetaryAmount,
            List[Union[DeliveryChargeSpecification, MonetaryAmount]],
        ]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'freeShippingThreshold', 'https://schema.org/freeShippingThreshold'
        ),
        serialization_alias='https://schema.org/freeShippingThreshold',
    )
    is_unlabelled_fallback: Optional[Union[bool, List[bool]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'isUnlabelledFallback', 'https://schema.org/isUnlabelledFallback'
        ),
        serialization_alias='https://schema.org/isUnlabelledFallback',
    )
    order_percentage: Optional[Union[float, List[float]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'orderPercentage', 'https://schema.org/orderPercentage'
        ),
        serialization_alias='https://schema.org/orderPercentage',
    )
    shipping_label: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'shippingLabel', 'https://schema.org/shippingLabel'
        ),
        serialization_alias='https://schema.org/shippingLabel',
    )
    shipping_destination: Optional[Union[DefinedRegion, List[DefinedRegion]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'shippingDestination', 'https://schema.org/shippingDestination'
        ),
        serialization_alias='https://schema.org/shippingDestination',
    )
    shipping_rate: Optional[
        Union[
            ShippingRateSettings,
            MonetaryAmount,
            List[Union[ShippingRateSettings, MonetaryAmount]],
        ]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'shippingRate', 'https://schema.org/shippingRate'
        ),
        serialization_alias='https://schema.org/shippingRate',
    )


class ServicePeriod(StructuredValue):
    field_type: Literal['https://schema.org/ServicePeriod'] = Field(
        'https://schema.org/ServicePeriod', alias='@type'
    )
    business_days: Optional[
        Union[
            OpeningHoursSpecification,
            DayOfWeek,
            List[Union[OpeningHoursSpecification, DayOfWeek]],
        ]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'businessDays', 'https://schema.org/businessDays'
        ),
        serialization_alias='https://schema.org/businessDays',
    )
    duration: Optional[
        Union[Duration, QuantitativeValue, List[Union[Duration, QuantitativeValue]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('duration', 'https://schema.org/duration'),
        serialization_alias='https://schema.org/duration',
    )
    cutoff_time: Optional[Union[time, List[time]]] = Field(
        default=None,
        validation_alias=AliasChoices('cutoffTime', 'https://schema.org/cutoffTime'),
        serialization_alias='https://schema.org/cutoffTime',
    )


class ShippingDeliveryTime(StructuredValue):
    field_type: Literal['https://schema.org/ShippingDeliveryTime'] = Field(
        'https://schema.org/ShippingDeliveryTime', alias='@type'
    )
    business_days: Optional[
        Union[
            OpeningHoursSpecification,
            DayOfWeek,
            List[Union[OpeningHoursSpecification, DayOfWeek]],
        ]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'businessDays', 'https://schema.org/businessDays'
        ),
        serialization_alias='https://schema.org/businessDays',
    )
    transit_time: Optional[
        Union[
            ServicePeriod,
            QuantitativeValue,
            List[Union[ServicePeriod, QuantitativeValue]],
        ]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('transitTime', 'https://schema.org/transitTime'),
        serialization_alias='https://schema.org/transitTime',
    )
    handling_time: Optional[
        Union[
            ServicePeriod,
            QuantitativeValue,
            List[Union[ServicePeriod, QuantitativeValue]],
        ]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'handlingTime', 'https://schema.org/handlingTime'
        ),
        serialization_alias='https://schema.org/handlingTime',
    )
    cutoff_time: Optional[Union[time, List[time]]] = Field(
        default=None,
        validation_alias=AliasChoices('cutoffTime', 'https://schema.org/cutoffTime'),
        serialization_alias='https://schema.org/cutoffTime',
    )


class NutritionInformation(StructuredValue):
    field_type: Literal['https://schema.org/NutritionInformation'] = Field(
        'https://schema.org/NutritionInformation', alias='@type'
    )
    unsaturated_fat_content: Optional[Union[Mass, List[Mass]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'unsaturatedFatContent', 'https://schema.org/unsaturatedFatContent'
        ),
        serialization_alias='https://schema.org/unsaturatedFatContent',
    )
    cholesterol_content: Optional[Union[Mass, List[Mass]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'cholesterolContent', 'https://schema.org/cholesterolContent'
        ),
        serialization_alias='https://schema.org/cholesterolContent',
    )
    calories: Optional[Union[Energy, List[Energy]]] = Field(
        default=None,
        validation_alias=AliasChoices('calories', 'https://schema.org/calories'),
        serialization_alias='https://schema.org/calories',
    )
    trans_fat_content: Optional[Union[Mass, List[Mass]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'transFatContent', 'https://schema.org/transFatContent'
        ),
        serialization_alias='https://schema.org/transFatContent',
    )
    fiber_content: Optional[Union[Mass, List[Mass]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'fiberContent', 'https://schema.org/fiberContent'
        ),
        serialization_alias='https://schema.org/fiberContent',
    )
    serving_size: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices('servingSize', 'https://schema.org/servingSize'),
        serialization_alias='https://schema.org/servingSize',
    )
    carbohydrate_content: Optional[Union[Mass, List[Mass]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'carbohydrateContent', 'https://schema.org/carbohydrateContent'
        ),
        serialization_alias='https://schema.org/carbohydrateContent',
    )
    fat_content: Optional[Union[Mass, List[Mass]]] = Field(
        default=None,
        validation_alias=AliasChoices('fatContent', 'https://schema.org/fatContent'),
        serialization_alias='https://schema.org/fatContent',
    )
    sodium_content: Optional[Union[Mass, List[Mass]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'sodiumContent', 'https://schema.org/sodiumContent'
        ),
        serialization_alias='https://schema.org/sodiumContent',
    )
    sugar_content: Optional[Union[Mass, List[Mass]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'sugarContent', 'https://schema.org/sugarContent'
        ),
        serialization_alias='https://schema.org/sugarContent',
    )
    saturated_fat_content: Optional[Union[Mass, List[Mass]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'saturatedFatContent', 'https://schema.org/saturatedFatContent'
        ),
        serialization_alias='https://schema.org/saturatedFatContent',
    )
    protein_content: Optional[Union[Mass, List[Mass]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'proteinContent', 'https://schema.org/proteinContent'
        ),
        serialization_alias='https://schema.org/proteinContent',
    )


class WarrantyPromise(StructuredValue):
    field_type: Literal['https://schema.org/WarrantyPromise'] = Field(
        'https://schema.org/WarrantyPromise', alias='@type'
    )
    warranty_scope: Optional[Union[WarrantyScope, List[WarrantyScope]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'warrantyScope', 'https://schema.org/warrantyScope'
        ),
        serialization_alias='https://schema.org/warrantyScope',
    )
    duration_of_warranty: Optional[
        Union[QuantitativeValue, List[QuantitativeValue]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'durationOfWarranty', 'https://schema.org/durationOfWarranty'
        ),
        serialization_alias='https://schema.org/durationOfWarranty',
    )


class GeoCoordinates(StructuredValue):
    field_type: Literal['https://schema.org/GeoCoordinates'] = Field(
        'https://schema.org/GeoCoordinates', alias='@type'
    )
    longitude: Optional[Union[float, str, List[Union[float, str]]]] = Field(
        default=None,
        validation_alias=AliasChoices('longitude', 'https://schema.org/longitude'),
        serialization_alias='https://schema.org/longitude',
    )
    latitude: Optional[Union[str, float, List[Union[str, float]]]] = Field(
        default=None,
        validation_alias=AliasChoices('latitude', 'https://schema.org/latitude'),
        serialization_alias='https://schema.org/latitude',
    )
    address: Optional[
        Union[str, PostalAddress, List[Union[str, PostalAddress]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('address', 'https://schema.org/address'),
        serialization_alias='https://schema.org/address',
    )
    postal_code: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices('postalCode', 'https://schema.org/postalCode'),
        serialization_alias='https://schema.org/postalCode',
    )
    elevation: Optional[Union[str, float, List[Union[str, float]]]] = Field(
        default=None,
        validation_alias=AliasChoices('elevation', 'https://schema.org/elevation'),
        serialization_alias='https://schema.org/elevation',
    )
    address_country: Optional[Union[str, Country, List[Union[str, Country]]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'addressCountry', 'https://schema.org/addressCountry'
        ),
        serialization_alias='https://schema.org/addressCountry',
    )


class OwnershipInfo(StructuredValue):
    field_type: Literal['https://schema.org/OwnershipInfo'] = Field(
        'https://schema.org/OwnershipInfo', alias='@type'
    )
    owned_from: Optional[Union[AwareDatetime, List[AwareDatetime]]] = Field(
        default=None,
        validation_alias=AliasChoices('ownedFrom', 'https://schema.org/ownedFrom'),
        serialization_alias='https://schema.org/ownedFrom',
    )
    acquired_from: Optional[
        Union[Organization, Person, List[Union[Organization, Person]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'acquiredFrom', 'https://schema.org/acquiredFrom'
        ),
        serialization_alias='https://schema.org/acquiredFrom',
    )
    type_of_good: Optional[
        Union[Product, Service, List[Union[Product, Service]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('typeOfGood', 'https://schema.org/typeOfGood'),
        serialization_alias='https://schema.org/typeOfGood',
    )
    owned_through: Optional[Union[AwareDatetime, List[AwareDatetime]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'ownedThrough', 'https://schema.org/ownedThrough'
        ),
        serialization_alias='https://schema.org/ownedThrough',
    )


class InteractionCounter(StructuredValue):
    field_type: Literal['https://schema.org/InteractionCounter'] = Field(
        'https://schema.org/InteractionCounter', alias='@type'
    )
    interaction_type: Optional[Union[Action, List[Action]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'interactionType', 'https://schema.org/interactionType'
        ),
        serialization_alias='https://schema.org/interactionType',
    )
    user_interaction_count: Optional[Union[int, List[int]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'userInteractionCount', 'https://schema.org/userInteractionCount'
        ),
        serialization_alias='https://schema.org/userInteractionCount',
    )
    end_time: Optional[
        Union[time, AwareDatetime, List[Union[time, AwareDatetime]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('endTime', 'https://schema.org/endTime'),
        serialization_alias='https://schema.org/endTime',
    )
    location: Optional[
        Union[
            VirtualLocation,
            PostalAddress,
            str,
            Place,
            List[Union[VirtualLocation, PostalAddress, str, Place]],
        ]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('location', 'https://schema.org/location'),
        serialization_alias='https://schema.org/location',
    )
    interaction_service: Optional[
        Union[WebSite, SoftwareApplication, List[Union[WebSite, SoftwareApplication]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'interactionService', 'https://schema.org/interactionService'
        ),
        serialization_alias='https://schema.org/interactionService',
    )
    start_time: Optional[
        Union[time, AwareDatetime, List[Union[time, AwareDatetime]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('startTime', 'https://schema.org/startTime'),
        serialization_alias='https://schema.org/startTime',
    )


class QuantitativeValueDistribution(StructuredValue):
    field_type: Literal['https://schema.org/QuantitativeValueDistribution'] = Field(
        'https://schema.org/QuantitativeValueDistribution', alias='@type'
    )
    median: Optional[Union[float, List[float]]] = Field(
        default=None,
        validation_alias=AliasChoices('median', 'https://schema.org/median'),
        serialization_alias='https://schema.org/median',
    )
    percentile75: Optional[Union[float, List[float]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'percentile75', 'https://schema.org/percentile75'
        ),
        serialization_alias='https://schema.org/percentile75',
    )
    percentile25: Optional[Union[float, List[float]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'percentile25', 'https://schema.org/percentile25'
        ),
        serialization_alias='https://schema.org/percentile25',
    )
    percentile90: Optional[Union[float, List[float]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'percentile90', 'https://schema.org/percentile90'
        ),
        serialization_alias='https://schema.org/percentile90',
    )
    percentile10: Optional[Union[float, List[float]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'percentile10', 'https://schema.org/percentile10'
        ),
        serialization_alias='https://schema.org/percentile10',
    )
    duration: Optional[
        Union[Duration, QuantitativeValue, List[Union[Duration, QuantitativeValue]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('duration', 'https://schema.org/duration'),
        serialization_alias='https://schema.org/duration',
    )


class CategoryCode(DefinedTerm):
    field_type: Literal['https://schema.org/CategoryCode'] = Field(
        'https://schema.org/CategoryCode', alias='@type'
    )
    in_code_set: Optional[
        Union[AnyUrl, CategoryCodeSet, List[Union[AnyUrl, CategoryCodeSet]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('inCodeSet', 'https://schema.org/inCodeSet'),
        serialization_alias='https://schema.org/inCodeSet',
    )
    code_value: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices('codeValue', 'https://schema.org/codeValue'),
        serialization_alias='https://schema.org/codeValue',
    )


class GenderType(Enumeration):
    field_type: Literal['https://schema.org/GenderType'] = Field(
        'https://schema.org/GenderType', alias='@type'
    )


class PaymentMethodType(Enumeration):
    field_type: Literal['https://schema.org/PaymentMethodType'] = Field(
        'https://schema.org/PaymentMethodType', alias='@type'
    )


class MeasurementTypeEnumeration(Enumeration):
    field_type: Literal['https://schema.org/MeasurementTypeEnumeration'] = Field(
        'https://schema.org/MeasurementTypeEnumeration', alias='@type'
    )


class QualitativeValue(Enumeration):
    field_type: Literal['https://schema.org/QualitativeValue'] = Field(
        'https://schema.org/QualitativeValue', alias='@type'
    )
    greater_or_equal: Optional[Union[QualitativeValue, List[QualitativeValue]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'greaterOrEqual', 'https://schema.org/greaterOrEqual'
        ),
        serialization_alias='https://schema.org/greaterOrEqual',
    )
    equal: Optional[Union[QualitativeValue, List[QualitativeValue]]] = Field(
        default=None,
        validation_alias=AliasChoices('equal', 'https://schema.org/equal'),
        serialization_alias='https://schema.org/equal',
    )
    lesser_or_equal: Optional[Union[QualitativeValue, List[QualitativeValue]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'lesserOrEqual', 'https://schema.org/lesserOrEqual'
        ),
        serialization_alias='https://schema.org/lesserOrEqual',
    )
    greater: Optional[Union[QualitativeValue, List[QualitativeValue]]] = Field(
        default=None,
        validation_alias=AliasChoices('greater', 'https://schema.org/greater'),
        serialization_alias='https://schema.org/greater',
    )
    lesser: Optional[Union[QualitativeValue, List[QualitativeValue]]] = Field(
        default=None,
        validation_alias=AliasChoices('lesser', 'https://schema.org/lesser'),
        serialization_alias='https://schema.org/lesser',
    )
    additional_property: Optional[Union[PropertyValue, List[PropertyValue]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'additionalProperty', 'https://schema.org/additionalProperty'
        ),
        serialization_alias='https://schema.org/additionalProperty',
    )
    value_reference: Optional[
        Union[
            DefinedTerm,
            MeasurementTypeEnumeration,
            str,
            Enumeration,
            QualitativeValue,
            QuantitativeValue,
            PropertyValue,
            StructuredValue,
            List[
                Union[
                    DefinedTerm,
                    MeasurementTypeEnumeration,
                    str,
                    Enumeration,
                    QualitativeValue,
                    QuantitativeValue,
                    PropertyValue,
                    StructuredValue,
                ]
            ],
        ]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'valueReference', 'https://schema.org/valueReference'
        ),
        serialization_alias='https://schema.org/valueReference',
    )
    non_equal: Optional[Union[QualitativeValue, List[QualitativeValue]]] = Field(
        default=None,
        validation_alias=AliasChoices('nonEqual', 'https://schema.org/nonEqual'),
        serialization_alias='https://schema.org/nonEqual',
    )


class DayOfWeek(Enumeration):
    field_type: Literal['https://schema.org/DayOfWeek'] = Field(
        'https://schema.org/DayOfWeek', alias='@type'
    )


class ItemListOrderType(Enumeration):
    field_type: Literal['https://schema.org/ItemListOrderType'] = Field(
        'https://schema.org/ItemListOrderType', alias='@type'
    )


class CertificationStatusEnumeration(Enumeration):
    field_type: Literal['https://schema.org/CertificationStatusEnumeration'] = Field(
        'https://schema.org/CertificationStatusEnumeration', alias='@type'
    )


class AdultOrientedEnumeration(Enumeration):
    field_type: Literal['https://schema.org/AdultOrientedEnumeration'] = Field(
        'https://schema.org/AdultOrientedEnumeration', alias='@type'
    )


class TierBenefitEnumeration(Enumeration):
    field_type: Literal['https://schema.org/TierBenefitEnumeration'] = Field(
        'https://schema.org/TierBenefitEnumeration', alias='@type'
    )


class PriceComponentTypeEnumeration(Enumeration):
    field_type: Literal['https://schema.org/PriceComponentTypeEnumeration'] = Field(
        'https://schema.org/PriceComponentTypeEnumeration', alias='@type'
    )


class PriceTypeEnumeration(Enumeration):
    field_type: Literal['https://schema.org/PriceTypeEnumeration'] = Field(
        'https://schema.org/PriceTypeEnumeration', alias='@type'
    )


class BusinessFunction(Enumeration):
    field_type: Literal['https://schema.org/BusinessFunction'] = Field(
        'https://schema.org/BusinessFunction', alias='@type'
    )


class BusinessEntityType(Enumeration):
    field_type: Literal['https://schema.org/BusinessEntityType'] = Field(
        'https://schema.org/BusinessEntityType', alias='@type'
    )


class DeliveryMethod(Enumeration):
    field_type: Literal['https://schema.org/DeliveryMethod'] = Field(
        'https://schema.org/DeliveryMethod', alias='@type'
    )


class OfferItemCondition(Enumeration):
    field_type: Literal['https://schema.org/OfferItemCondition'] = Field(
        'https://schema.org/OfferItemCondition', alias='@type'
    )


class ItemAvailability(Enumeration):
    field_type: Literal['https://schema.org/ItemAvailability'] = Field(
        'https://schema.org/ItemAvailability', alias='@type'
    )


class FulfillmentTypeEnumeration(Enumeration):
    field_type: Literal['https://schema.org/FulfillmentTypeEnumeration'] = Field(
        'https://schema.org/FulfillmentTypeEnumeration', alias='@type'
    )


class PhysicalActivityCategory(Enumeration):
    field_type: Literal['https://schema.org/PhysicalActivityCategory'] = Field(
        'https://schema.org/PhysicalActivityCategory', alias='@type'
    )


class RefundTypeEnumeration(Enumeration):
    field_type: Literal['https://schema.org/RefundTypeEnumeration'] = Field(
        'https://schema.org/RefundTypeEnumeration', alias='@type'
    )


class ReturnMethodEnumeration(Enumeration):
    field_type: Literal['https://schema.org/ReturnMethodEnumeration'] = Field(
        'https://schema.org/ReturnMethodEnumeration', alias='@type'
    )


class ReturnFeesEnumeration(Enumeration):
    field_type: Literal['https://schema.org/ReturnFeesEnumeration'] = Field(
        'https://schema.org/ReturnFeesEnumeration', alias='@type'
    )


class MerchantReturnEnumeration(Enumeration):
    field_type: Literal['https://schema.org/MerchantReturnEnumeration'] = Field(
        'https://schema.org/MerchantReturnEnumeration', alias='@type'
    )


class ReturnLabelSourceEnumeration(Enumeration):
    field_type: Literal['https://schema.org/ReturnLabelSourceEnumeration'] = Field(
        'https://schema.org/ReturnLabelSourceEnumeration', alias='@type'
    )


class RestrictedDiet(Enumeration):
    field_type: Literal['https://schema.org/RestrictedDiet'] = Field(
        'https://schema.org/RestrictedDiet', alias='@type'
    )


class WarrantyScope(Enumeration):
    field_type: Literal['https://schema.org/WarrantyScope'] = Field(
        'https://schema.org/WarrantyScope', alias='@type'
    )


class MedicalEnumeration(Enumeration):
    field_type: Literal['https://schema.org/MedicalEnumeration'] = Field(
        'https://schema.org/MedicalEnumeration', alias='@type'
    )


class Specialty(Enumeration):
    field_type: Literal['https://schema.org/Specialty'] = Field(
        'https://schema.org/Specialty', alias='@type'
    )


class StatusEnumeration(Enumeration):
    field_type: Literal['https://schema.org/StatusEnumeration'] = Field(
        'https://schema.org/StatusEnumeration', alias='@type'
    )


class EnergyEfficiencyEnumeration(Enumeration):
    field_type: Literal['https://schema.org/EnergyEfficiencyEnumeration'] = Field(
        'https://schema.org/EnergyEfficiencyEnumeration', alias='@type'
    )


class SizeSystemEnumeration(Enumeration):
    field_type: Literal['https://schema.org/SizeSystemEnumeration'] = Field(
        'https://schema.org/SizeSystemEnumeration', alias='@type'
    )


class SizeGroupEnumeration(Enumeration):
    field_type: Literal['https://schema.org/SizeGroupEnumeration'] = Field(
        'https://schema.org/SizeGroupEnumeration', alias='@type'
    )


class ContactPointOption(Enumeration):
    field_type: Literal['https://schema.org/ContactPointOption'] = Field(
        'https://schema.org/ContactPointOption', alias='@type'
    )


class EventAttendanceModeEnumeration(Enumeration):
    field_type: Literal['https://schema.org/EventAttendanceModeEnumeration'] = Field(
        'https://schema.org/EventAttendanceModeEnumeration', alias='@type'
    )


class MapCategoryType(Enumeration):
    field_type: Literal['https://schema.org/MapCategoryType'] = Field(
        'https://schema.org/MapCategoryType', alias='@type'
    )


class GovernmentBenefitsType(Enumeration):
    field_type: Literal['https://schema.org/GovernmentBenefitsType'] = Field(
        'https://schema.org/GovernmentBenefitsType', alias='@type'
    )


class NonprofitType(Enumeration):
    field_type: Literal['https://schema.org/NonprofitType'] = Field(
        'https://schema.org/NonprofitType', alias='@type'
    )


class MeasurementMethodEnum(Enumeration):
    field_type: Literal['https://schema.org/MeasurementMethodEnum'] = Field(
        'https://schema.org/MeasurementMethodEnum', alias='@type'
    )


class DigitalPlatformEnumeration(Enumeration):
    field_type: Literal['https://schema.org/DigitalPlatformEnumeration'] = Field(
        'https://schema.org/DigitalPlatformEnumeration', alias='@type'
    )


class MusicReleaseFormatType(Enumeration):
    field_type: Literal['https://schema.org/MusicReleaseFormatType'] = Field(
        'https://schema.org/MusicReleaseFormatType', alias='@type'
    )


class MusicAlbumProductionType(Enumeration):
    field_type: Literal['https://schema.org/MusicAlbumProductionType'] = Field(
        'https://schema.org/MusicAlbumProductionType', alias='@type'
    )


class MusicAlbumReleaseType(Enumeration):
    field_type: Literal['https://schema.org/MusicAlbumReleaseType'] = Field(
        'https://schema.org/MusicAlbumReleaseType', alias='@type'
    )


class MediaEnumeration(Enumeration):
    field_type: Literal['https://schema.org/MediaEnumeration'] = Field(
        'https://schema.org/MediaEnumeration', alias='@type'
    )


class FinancialProduct(Service):
    field_type: Literal['https://schema.org/FinancialProduct'] = Field(
        'https://schema.org/FinancialProduct', alias='@type'
    )
    interest_rate: Optional[
        Union[float, QuantitativeValue, List[Union[float, QuantitativeValue]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'interestRate', 'https://schema.org/interestRate'
        ),
        serialization_alias='https://schema.org/interestRate',
    )
    annual_percentage_rate: Optional[
        Union[QuantitativeValue, float, List[Union[QuantitativeValue, float]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'annualPercentageRate', 'https://schema.org/annualPercentageRate'
        ),
        serialization_alias='https://schema.org/annualPercentageRate',
    )
    fees_and_commissions_specification: Optional[
        Union[str, AnyUrl, List[Union[str, AnyUrl]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'feesAndCommissionsSpecification',
            'https://schema.org/feesAndCommissionsSpecification',
        ),
        serialization_alias='https://schema.org/feesAndCommissionsSpecification',
    )


class BroadcastService(Service):
    field_type: Literal['https://schema.org/BroadcastService'] = Field(
        'https://schema.org/BroadcastService', alias='@type'
    )
    call_sign: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices('callSign', 'https://schema.org/callSign'),
        serialization_alias='https://schema.org/callSign',
    )
    broadcast_affiliate_of: Optional[Union[Organization, List[Organization]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'broadcastAffiliateOf', 'https://schema.org/broadcastAffiliateOf'
        ),
        serialization_alias='https://schema.org/broadcastAffiliateOf',
    )
    broadcaster: Optional[Union[Organization, List[Organization]]] = Field(
        default=None,
        validation_alias=AliasChoices('broadcaster', 'https://schema.org/broadcaster'),
        serialization_alias='https://schema.org/broadcaster',
    )
    area: Optional[Union[Place, List[Place]]] = Field(
        default=None,
        validation_alias=AliasChoices('area', 'https://schema.org/area'),
        serialization_alias='https://schema.org/area',
    )
    video_format: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices('videoFormat', 'https://schema.org/videoFormat'),
        serialization_alias='https://schema.org/videoFormat',
    )
    broadcast_display_name: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'broadcastDisplayName', 'https://schema.org/broadcastDisplayName'
        ),
        serialization_alias='https://schema.org/broadcastDisplayName',
    )
    in_language: Optional[Union[str, Language, List[Union[str, Language]]]] = Field(
        default=None,
        validation_alias=AliasChoices('inLanguage', 'https://schema.org/inLanguage'),
        serialization_alias='https://schema.org/inLanguage',
    )
    broadcast_frequency: Optional[
        Union[
            str,
            BroadcastFrequencySpecification,
            List[Union[str, BroadcastFrequencySpecification]],
        ]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'broadcastFrequency', 'https://schema.org/broadcastFrequency'
        ),
        serialization_alias='https://schema.org/broadcastFrequency',
    )
    has_broadcast_channel: Optional[
        Union[BroadcastChannel, List[BroadcastChannel]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'hasBroadcastChannel', 'https://schema.org/hasBroadcastChannel'
        ),
        serialization_alias='https://schema.org/hasBroadcastChannel',
    )
    parent_service: Optional[Union[BroadcastService, List[BroadcastService]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'parentService', 'https://schema.org/parentService'
        ),
        serialization_alias='https://schema.org/parentService',
    )
    broadcast_timezone: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'broadcastTimezone', 'https://schema.org/broadcastTimezone'
        ),
        serialization_alias='https://schema.org/broadcastTimezone',
    )


class CableOrSatelliteService(Service):
    field_type: Literal['https://schema.org/CableOrSatelliteService'] = Field(
        'https://schema.org/CableOrSatelliteService', alias='@type'
    )


class Distance(Quantity):
    field_type: Literal['https://schema.org/Distance'] = Field(
        'https://schema.org/Distance', alias='@type'
    )


class Duration(Quantity):
    field_type: Literal['https://schema.org/Duration'] = Field(
        'https://schema.org/Duration', alias='@type'
    )


class Mass(Quantity):
    field_type: Literal['https://schema.org/Mass'] = Field(
        'https://schema.org/Mass', alias='@type'
    )


class Energy(Quantity):
    field_type: Literal['https://schema.org/Energy'] = Field(
        'https://schema.org/Energy', alias='@type'
    )


class AggregateRating(Rating):
    field_type: Literal['https://schema.org/AggregateRating'] = Field(
        'https://schema.org/AggregateRating', alias='@type'
    )
    review_count: Optional[Union[int, List[int]]] = Field(
        default=None,
        validation_alias=AliasChoices('reviewCount', 'https://schema.org/reviewCount'),
        serialization_alias='https://schema.org/reviewCount',
    )
    rating_count: Optional[Union[int, List[int]]] = Field(
        default=None,
        validation_alias=AliasChoices('ratingCount', 'https://schema.org/ratingCount'),
        serialization_alias='https://schema.org/ratingCount',
    )
    item_reviewed: Optional[Union[Thing, List[Thing]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'itemReviewed', 'https://schema.org/itemReviewed'
        ),
        serialization_alias='https://schema.org/itemReviewed',
    )


class OfferCatalog(ItemList):
    field_type: Literal['https://schema.org/OfferCatalog'] = Field(
        'https://schema.org/OfferCatalog', alias='@type'
    )


class BreadcrumbList(ItemList):
    field_type: Literal['https://schema.org/BreadcrumbList'] = Field(
        'https://schema.org/BreadcrumbList', alias='@type'
    )


class HowToStep(ItemList):
    field_type: Literal['https://schema.org/HowToStep'] = Field(
        'https://schema.org/HowToStep', alias='@type'
    )


class HowToItem(ListItem):
    field_type: Literal['https://schema.org/HowToItem'] = Field(
        'https://schema.org/HowToItem', alias='@type'
    )
    required_quantity: Optional[
        Union[str, float, QuantitativeValue, List[Union[str, float, QuantitativeValue]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'requiredQuantity', 'https://schema.org/requiredQuantity'
        ),
        serialization_alias='https://schema.org/requiredQuantity',
    )


class AggregateOffer(Offer):
    field_type: Literal['https://schema.org/AggregateOffer'] = Field(
        'https://schema.org/AggregateOffer', alias='@type'
    )
    high_price: Optional[Union[str, float, List[Union[str, float]]]] = Field(
        default=None,
        validation_alias=AliasChoices('highPrice', 'https://schema.org/highPrice'),
        serialization_alias='https://schema.org/highPrice',
    )
    low_price: Optional[Union[str, float, List[Union[str, float]]]] = Field(
        default=None,
        validation_alias=AliasChoices('lowPrice', 'https://schema.org/lowPrice'),
        serialization_alias='https://schema.org/lowPrice',
    )
    offer_count: Optional[Union[int, List[int]]] = Field(
        default=None,
        validation_alias=AliasChoices('offerCount', 'https://schema.org/offerCount'),
        serialization_alias='https://schema.org/offerCount',
    )
    offers: Optional[Union[Demand, Offer, List[Union[Demand, Offer]]]] = Field(
        default=None,
        validation_alias=AliasChoices('offers', 'https://schema.org/offers'),
        serialization_alias='https://schema.org/offers',
    )


class StatisticalVariable(ConstraintNode):
    field_type: Literal['https://schema.org/StatisticalVariable'] = Field(
        'https://schema.org/StatisticalVariable', alias='@type'
    )
    stat_type: Optional[
        Union[AnyUrl, Property, str, List[Union[AnyUrl, Property, str]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('statType', 'https://schema.org/statType'),
        serialization_alias='https://schema.org/statType',
    )
    measurement_denominator: Optional[
        Union[StatisticalVariable, List[StatisticalVariable]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'measurementDenominator', 'https://schema.org/measurementDenominator'
        ),
        serialization_alias='https://schema.org/measurementDenominator',
    )
    population_type: Optional[Union[Class, List[Class]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'populationType', 'https://schema.org/populationType'
        ),
        serialization_alias='https://schema.org/populationType',
    )
    measurement_method: Optional[
        Union[
            DefinedTerm,
            str,
            MeasurementMethodEnum,
            AnyUrl,
            List[Union[DefinedTerm, str, MeasurementMethodEnum, AnyUrl]],
        ]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'measurementMethod', 'https://schema.org/measurementMethod'
        ),
        serialization_alias='https://schema.org/measurementMethod',
    )
    measured_property: Optional[Union[Property, List[Property]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'measuredProperty', 'https://schema.org/measuredProperty'
        ),
        serialization_alias='https://schema.org/measuredProperty',
    )
    measurement_qualifier: Optional[Union[Enumeration, List[Enumeration]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'measurementQualifier', 'https://schema.org/measurementQualifier'
        ),
        serialization_alias='https://schema.org/measurementQualifier',
    )
    measurement_technique: Optional[
        Union[
            DefinedTerm,
            MeasurementMethodEnum,
            str,
            AnyUrl,
            List[Union[DefinedTerm, MeasurementMethodEnum, str, AnyUrl]],
        ]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'measurementTechnique', 'https://schema.org/measurementTechnique'
        ),
        serialization_alias='https://schema.org/measurementTechnique',
    )


class ImageObject(MediaObject):
    field_type: Literal['https://schema.org/ImageObject'] = Field(
        'https://schema.org/ImageObject', alias='@type'
    )
    representative_of_page: Optional[Union[bool, List[bool]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'representativeOfPage', 'https://schema.org/representativeOfPage'
        ),
        serialization_alias='https://schema.org/representativeOfPage',
    )
    caption: Optional[Union[MediaObject, str, List[Union[MediaObject, str]]]] = Field(
        default=None,
        validation_alias=AliasChoices('caption', 'https://schema.org/caption'),
        serialization_alias='https://schema.org/caption',
    )
    embedded_text_caption: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'embeddedTextCaption', 'https://schema.org/embeddedTextCaption'
        ),
        serialization_alias='https://schema.org/embeddedTextCaption',
    )
    exif_data: Optional[
        Union[PropertyValue, str, List[Union[PropertyValue, str]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('exifData', 'https://schema.org/exifData'),
        serialization_alias='https://schema.org/exifData',
    )


class DataDownload(MediaObject):
    field_type: Literal['https://schema.org/DataDownload'] = Field(
        'https://schema.org/DataDownload', alias='@type'
    )
    measurement_method: Optional[
        Union[
            DefinedTerm,
            str,
            MeasurementMethodEnum,
            AnyUrl,
            List[Union[DefinedTerm, str, MeasurementMethodEnum, AnyUrl]],
        ]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'measurementMethod', 'https://schema.org/measurementMethod'
        ),
        serialization_alias='https://schema.org/measurementMethod',
    )
    measurement_technique: Optional[
        Union[
            DefinedTerm,
            MeasurementMethodEnum,
            str,
            AnyUrl,
            List[Union[DefinedTerm, MeasurementMethodEnum, str, AnyUrl]],
        ]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'measurementTechnique', 'https://schema.org/measurementTechnique'
        ),
        serialization_alias='https://schema.org/measurementTechnique',
    )


class AudioObject(MediaObject):
    field_type: Literal['https://schema.org/AudioObject'] = Field(
        'https://schema.org/AudioObject', alias='@type'
    )
    transcript: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices('transcript', 'https://schema.org/transcript'),
        serialization_alias='https://schema.org/transcript',
    )
    caption: Optional[Union[MediaObject, str, List[Union[MediaObject, str]]]] = Field(
        default=None,
        validation_alias=AliasChoices('caption', 'https://schema.org/caption'),
        serialization_alias='https://schema.org/caption',
    )
    embedded_text_caption: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'embeddedTextCaption', 'https://schema.org/embeddedTextCaption'
        ),
        serialization_alias='https://schema.org/embeddedTextCaption',
    )


class VideoObject(MediaObject):
    field_type: Literal['https://schema.org/VideoObject'] = Field(
        'https://schema.org/VideoObject', alias='@type'
    )
    directors: Optional[Union[Person, List[Person]]] = Field(
        default=None,
        validation_alias=AliasChoices('directors', 'https://schema.org/directors'),
        serialization_alias='https://schema.org/directors',
    )
    director: Optional[Union[Person, List[Person]]] = Field(
        default=None,
        validation_alias=AliasChoices('director', 'https://schema.org/director'),
        serialization_alias='https://schema.org/director',
    )
    video_frame_size: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'videoFrameSize', 'https://schema.org/videoFrameSize'
        ),
        serialization_alias='https://schema.org/videoFrameSize',
    )
    actor: Optional[
        Union[Person, PerformingGroup, List[Union[Person, PerformingGroup]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('actor', 'https://schema.org/actor'),
        serialization_alias='https://schema.org/actor',
    )
    transcript: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices('transcript', 'https://schema.org/transcript'),
        serialization_alias='https://schema.org/transcript',
    )
    actors: Optional[Union[Person, List[Person]]] = Field(
        default=None,
        validation_alias=AliasChoices('actors', 'https://schema.org/actors'),
        serialization_alias='https://schema.org/actors',
    )
    video_quality: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'videoQuality', 'https://schema.org/videoQuality'
        ),
        serialization_alias='https://schema.org/videoQuality',
    )
    music_by: Optional[
        Union[MusicGroup, Person, List[Union[MusicGroup, Person]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('musicBy', 'https://schema.org/musicBy'),
        serialization_alias='https://schema.org/musicBy',
    )
    caption: Optional[Union[MediaObject, str, List[Union[MediaObject, str]]]] = Field(
        default=None,
        validation_alias=AliasChoices('caption', 'https://schema.org/caption'),
        serialization_alias='https://schema.org/caption',
    )
    embedded_text_caption: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'embeddedTextCaption', 'https://schema.org/embeddedTextCaption'
        ),
        serialization_alias='https://schema.org/embeddedTextCaption',
    )


class TextObject(MediaObject):
    field_type: Literal['https://schema.org/TextObject'] = Field(
        'https://schema.org/TextObject', alias='@type'
    )


class CategoryCodeSet(DefinedTermSet):
    field_type: Literal['https://schema.org/CategoryCodeSet'] = Field(
        'https://schema.org/CategoryCodeSet', alias='@type'
    )
    has_category_code: Optional[Union[CategoryCode, List[CategoryCode]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'hasCategoryCode', 'https://schema.org/hasCategoryCode'
        ),
        serialization_alias='https://schema.org/hasCategoryCode',
    )


class NewsArticle(Article):
    field_type: Literal['https://schema.org/NewsArticle'] = Field(
        'https://schema.org/NewsArticle', alias='@type'
    )
    print_column: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices('printColumn', 'https://schema.org/printColumn'),
        serialization_alias='https://schema.org/printColumn',
    )
    dateline: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices('dateline', 'https://schema.org/dateline'),
        serialization_alias='https://schema.org/dateline',
    )
    print_edition: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'printEdition', 'https://schema.org/printEdition'
        ),
        serialization_alias='https://schema.org/printEdition',
    )
    print_section: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'printSection', 'https://schema.org/printSection'
        ),
        serialization_alias='https://schema.org/printSection',
    )
    print_page: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices('printPage', 'https://schema.org/printPage'),
        serialization_alias='https://schema.org/printPage',
    )


class AboutPage(WebPage):
    field_type: Literal['https://schema.org/AboutPage'] = Field(
        'https://schema.org/AboutPage', alias='@type'
    )


class DataFeed(Dataset):
    field_type: Literal['https://schema.org/DataFeed'] = Field(
        'https://schema.org/DataFeed', alias='@type'
    )
    data_feed_element: Optional[
        Union[DataFeedItem, str, Thing, List[Union[DataFeedItem, str, Thing]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'dataFeedElement', 'https://schema.org/dataFeedElement'
        ),
        serialization_alias='https://schema.org/dataFeedElement',
    )


class MusicAlbum(MusicPlaylist):
    field_type: Literal['https://schema.org/MusicAlbum'] = Field(
        'https://schema.org/MusicAlbum', alias='@type'
    )
    album_release: Optional[Union[MusicRelease, List[MusicRelease]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'albumRelease', 'https://schema.org/albumRelease'
        ),
        serialization_alias='https://schema.org/albumRelease',
    )
    by_artist: Optional[
        Union[MusicGroup, Person, List[Union[MusicGroup, Person]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('byArtist', 'https://schema.org/byArtist'),
        serialization_alias='https://schema.org/byArtist',
    )
    album_production_type: Optional[
        Union[MusicAlbumProductionType, List[MusicAlbumProductionType]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'albumProductionType', 'https://schema.org/albumProductionType'
        ),
        serialization_alias='https://schema.org/albumProductionType',
    )
    album_release_type: Optional[
        Union[MusicAlbumReleaseType, List[MusicAlbumReleaseType]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'albumReleaseType', 'https://schema.org/albumReleaseType'
        ),
        serialization_alias='https://schema.org/albumReleaseType',
    )


class MusicRelease(MusicPlaylist):
    field_type: Literal['https://schema.org/MusicRelease'] = Field(
        'https://schema.org/MusicRelease', alias='@type'
    )
    record_label: Optional[Union[Organization, List[Organization]]] = Field(
        default=None,
        validation_alias=AliasChoices('recordLabel', 'https://schema.org/recordLabel'),
        serialization_alias='https://schema.org/recordLabel',
    )
    music_release_format: Optional[
        Union[MusicReleaseFormatType, List[MusicReleaseFormatType]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'musicReleaseFormat', 'https://schema.org/musicReleaseFormat'
        ),
        serialization_alias='https://schema.org/musicReleaseFormat',
    )
    catalog_number: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'catalogNumber', 'https://schema.org/catalogNumber'
        ),
        serialization_alias='https://schema.org/catalogNumber',
    )
    release_of: Optional[Union[MusicAlbum, List[MusicAlbum]]] = Field(
        default=None,
        validation_alias=AliasChoices('releaseOf', 'https://schema.org/releaseOf'),
        serialization_alias='https://schema.org/releaseOf',
    )
    duration: Optional[
        Union[Duration, QuantitativeValue, List[Union[Duration, QuantitativeValue]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('duration', 'https://schema.org/duration'),
        serialization_alias='https://schema.org/duration',
    )
    credited_to: Optional[
        Union[Person, Organization, List[Union[Person, Organization]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('creditedTo', 'https://schema.org/creditedTo'),
        serialization_alias='https://schema.org/creditedTo',
    )


class CorrectionComment(Comment):
    field_type: Literal['https://schema.org/CorrectionComment'] = Field(
        'https://schema.org/CorrectionComment', alias='@type'
    )


class MusicGroup(PerformingGroup):
    field_type: Literal['https://schema.org/MusicGroup'] = Field(
        'https://schema.org/MusicGroup', alias='@type'
    )
    albums: Optional[Union[MusicAlbum, List[MusicAlbum]]] = Field(
        default=None,
        validation_alias=AliasChoices('albums', 'https://schema.org/albums'),
        serialization_alias='https://schema.org/albums',
    )
    album: Optional[Union[MusicAlbum, List[MusicAlbum]]] = Field(
        default=None,
        validation_alias=AliasChoices('album', 'https://schema.org/album'),
        serialization_alias='https://schema.org/album',
    )
    music_group_member: Optional[Union[Person, List[Person]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'musicGroupMember', 'https://schema.org/musicGroupMember'
        ),
        serialization_alias='https://schema.org/musicGroupMember',
    )
    tracks: Optional[Union[MusicRecording, List[MusicRecording]]] = Field(
        default=None,
        validation_alias=AliasChoices('tracks', 'https://schema.org/tracks'),
        serialization_alias='https://schema.org/tracks',
    )
    track: Optional[
        Union[ItemList, MusicRecording, List[Union[ItemList, MusicRecording]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('track', 'https://schema.org/track'),
        serialization_alias='https://schema.org/track',
    )
    genre: Optional[Union[AnyUrl, str, List[Union[AnyUrl, str]]]] = Field(
        default=None,
        validation_alias=AliasChoices('genre', 'https://schema.org/genre'),
        serialization_alias='https://schema.org/genre',
    )


class Country(AdministrativeArea):
    field_type: Literal['https://schema.org/Country'] = Field(
        'https://schema.org/Country', alias='@type'
    )


class EducationalOrganization(CivicStructure):
    field_type: Literal['https://schema.org/EducationalOrganization'] = Field(
        'https://schema.org/EducationalOrganization', alias='@type'
    )
    alumni: Optional[Union[Person, List[Person]]] = Field(
        default=None,
        validation_alias=AliasChoices('alumni', 'https://schema.org/alumni'),
        serialization_alias='https://schema.org/alumni',
    )


class MedicalCode(MedicalIntangible):
    field_type: Literal['https://schema.org/MedicalCode'] = Field(
        'https://schema.org/MedicalCode', alias='@type'
    )
    coding_system: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'codingSystem', 'https://schema.org/codingSystem'
        ),
        serialization_alias='https://schema.org/codingSystem',
    )
    code_value: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices('codeValue', 'https://schema.org/codeValue'),
        serialization_alias='https://schema.org/codeValue',
    )


class DrugLegalStatus(MedicalIntangible):
    field_type: Literal['https://schema.org/DrugLegalStatus'] = Field(
        'https://schema.org/DrugLegalStatus', alias='@type'
    )
    applicable_location: Optional[
        Union[AdministrativeArea, List[AdministrativeArea]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'applicableLocation', 'https://schema.org/applicableLocation'
        ),
        serialization_alias='https://schema.org/applicableLocation',
    )


class DoseSchedule(MedicalIntangible):
    field_type: Literal['https://schema.org/DoseSchedule'] = Field(
        'https://schema.org/DoseSchedule', alias='@type'
    )
    frequency: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices('frequency', 'https://schema.org/frequency'),
        serialization_alias='https://schema.org/frequency',
    )
    dose_value: Optional[
        Union[float, QualitativeValue, List[Union[float, QualitativeValue]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('doseValue', 'https://schema.org/doseValue'),
        serialization_alias='https://schema.org/doseValue',
    )
    target_population: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'targetPopulation', 'https://schema.org/targetPopulation'
        ),
        serialization_alias='https://schema.org/targetPopulation',
    )
    dose_unit: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices('doseUnit', 'https://schema.org/doseUnit'),
        serialization_alias='https://schema.org/doseUnit',
    )


class DrugStrength(MedicalIntangible):
    field_type: Literal['https://schema.org/DrugStrength'] = Field(
        'https://schema.org/DrugStrength', alias='@type'
    )
    strength_unit: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'strengthUnit', 'https://schema.org/strengthUnit'
        ),
        serialization_alias='https://schema.org/strengthUnit',
    )
    maximum_intake: Optional[
        Union[MaximumDoseSchedule, List[MaximumDoseSchedule]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'maximumIntake', 'https://schema.org/maximumIntake'
        ),
        serialization_alias='https://schema.org/maximumIntake',
    )
    available_in: Optional[Union[AdministrativeArea, List[AdministrativeArea]]] = Field(
        default=None,
        validation_alias=AliasChoices('availableIn', 'https://schema.org/availableIn'),
        serialization_alias='https://schema.org/availableIn',
    )
    strength_value: Optional[Union[float, List[float]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'strengthValue', 'https://schema.org/strengthValue'
        ),
        serialization_alias='https://schema.org/strengthValue',
    )
    active_ingredient: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'activeIngredient', 'https://schema.org/activeIngredient'
        ),
        serialization_alias='https://schema.org/activeIngredient',
    )


class DDxElement(MedicalIntangible):
    field_type: Literal['https://schema.org/DDxElement'] = Field(
        'https://schema.org/DDxElement', alias='@type'
    )
    distinguishing_sign: Optional[
        Union[MedicalSignOrSymptom, List[MedicalSignOrSymptom]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'distinguishingSign', 'https://schema.org/distinguishingSign'
        ),
        serialization_alias='https://schema.org/distinguishingSign',
    )
    diagnosis: Optional[Union[MedicalCondition, List[MedicalCondition]]] = Field(
        default=None,
        validation_alias=AliasChoices('diagnosis', 'https://schema.org/diagnosis'),
        serialization_alias='https://schema.org/diagnosis',
    )


class MedicalConditionStage(MedicalIntangible):
    field_type: Literal['https://schema.org/MedicalConditionStage'] = Field(
        'https://schema.org/MedicalConditionStage', alias='@type'
    )
    stage_as_number: Optional[Union[float, List[float]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'stageAsNumber', 'https://schema.org/stageAsNumber'
        ),
        serialization_alias='https://schema.org/stageAsNumber',
    )
    sub_stage_suffix: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'subStageSuffix', 'https://schema.org/subStageSuffix'
        ),
        serialization_alias='https://schema.org/subStageSuffix',
    )


class MedicalSignOrSymptom(MedicalCondition):
    field_type: Literal['https://schema.org/MedicalSignOrSymptom'] = Field(
        'https://schema.org/MedicalSignOrSymptom', alias='@type'
    )
    possible_treatment: Optional[Union[MedicalTherapy, List[MedicalTherapy]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'possibleTreatment', 'https://schema.org/possibleTreatment'
        ),
        serialization_alias='https://schema.org/possibleTreatment',
    )


class TherapeuticProcedure(MedicalProcedure):
    field_type: Literal['https://schema.org/TherapeuticProcedure'] = Field(
        'https://schema.org/TherapeuticProcedure', alias='@type'
    )
    drug: Optional[Union[Drug, List[Drug]]] = Field(
        default=None,
        validation_alias=AliasChoices('drug', 'https://schema.org/drug'),
        serialization_alias='https://schema.org/drug',
    )
    adverse_outcome: Optional[Union[MedicalEntity, List[MedicalEntity]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'adverseOutcome', 'https://schema.org/adverseOutcome'
        ),
        serialization_alias='https://schema.org/adverseOutcome',
    )
    dose_schedule: Optional[Union[DoseSchedule, List[DoseSchedule]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'doseSchedule', 'https://schema.org/doseSchedule'
        ),
        serialization_alias='https://schema.org/doseSchedule',
    )


class Drug(Substance):
    field_type: Literal['https://schema.org/Drug'] = Field(
        'https://schema.org/Drug', alias='@type'
    )
    alcohol_warning: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'alcoholWarning', 'https://schema.org/alcoholWarning'
        ),
        serialization_alias='https://schema.org/alcoholWarning',
    )
    legal_status: Optional[
        Union[
            DrugLegalStatus,
            MedicalEnumeration,
            str,
            List[Union[DrugLegalStatus, MedicalEnumeration, str]],
        ]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('legalStatus', 'https://schema.org/legalStatus'),
        serialization_alias='https://schema.org/legalStatus',
    )
    proprietary_name: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'proprietaryName', 'https://schema.org/proprietaryName'
        ),
        serialization_alias='https://schema.org/proprietaryName',
    )
    mechanism_of_action: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'mechanismOfAction', 'https://schema.org/mechanismOfAction'
        ),
        serialization_alias='https://schema.org/mechanismOfAction',
    )
    interacting_drug: Optional[Union[Drug, List[Drug]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'interactingDrug', 'https://schema.org/interactingDrug'
        ),
        serialization_alias='https://schema.org/interactingDrug',
    )
    is_available_generically: Optional[Union[bool, List[bool]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'isAvailableGenerically', 'https://schema.org/isAvailableGenerically'
        ),
        serialization_alias='https://schema.org/isAvailableGenerically',
    )
    is_proprietary: Optional[Union[bool, List[bool]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'isProprietary', 'https://schema.org/isProprietary'
        ),
        serialization_alias='https://schema.org/isProprietary',
    )
    maximum_intake: Optional[
        Union[MaximumDoseSchedule, List[MaximumDoseSchedule]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'maximumIntake', 'https://schema.org/maximumIntake'
        ),
        serialization_alias='https://schema.org/maximumIntake',
    )
    prescribing_info: Optional[Union[AnyUrl, List[AnyUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'prescribingInfo', 'https://schema.org/prescribingInfo'
        ),
        serialization_alias='https://schema.org/prescribingInfo',
    )
    dose_schedule: Optional[Union[DoseSchedule, List[DoseSchedule]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'doseSchedule', 'https://schema.org/doseSchedule'
        ),
        serialization_alias='https://schema.org/doseSchedule',
    )
    food_warning: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices('foodWarning', 'https://schema.org/foodWarning'),
        serialization_alias='https://schema.org/foodWarning',
    )
    administration_route: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'administrationRoute', 'https://schema.org/administrationRoute'
        ),
        serialization_alias='https://schema.org/administrationRoute',
    )
    overdosage: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices('overdosage', 'https://schema.org/overdosage'),
        serialization_alias='https://schema.org/overdosage',
    )
    active_ingredient: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'activeIngredient', 'https://schema.org/activeIngredient'
        ),
        serialization_alias='https://schema.org/activeIngredient',
    )
    rxcui: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices('rxcui', 'https://schema.org/rxcui'),
        serialization_alias='https://schema.org/rxcui',
    )
    pregnancy_warning: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'pregnancyWarning', 'https://schema.org/pregnancyWarning'
        ),
        serialization_alias='https://schema.org/pregnancyWarning',
    )
    related_drug: Optional[Union[Drug, List[Drug]]] = Field(
        default=None,
        validation_alias=AliasChoices('relatedDrug', 'https://schema.org/relatedDrug'),
        serialization_alias='https://schema.org/relatedDrug',
    )
    clinical_pharmacology: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'clinicalPharmacology', 'https://schema.org/clinicalPharmacology'
        ),
        serialization_alias='https://schema.org/clinicalPharmacology',
    )
    breastfeeding_warning: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'breastfeedingWarning', 'https://schema.org/breastfeedingWarning'
        ),
        serialization_alias='https://schema.org/breastfeedingWarning',
    )
    clincal_pharmacology: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'clincalPharmacology', 'https://schema.org/clincalPharmacology'
        ),
        serialization_alias='https://schema.org/clincalPharmacology',
    )
    label_details: Optional[Union[AnyUrl, List[AnyUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'labelDetails', 'https://schema.org/labelDetails'
        ),
        serialization_alias='https://schema.org/labelDetails',
    )
    available_strength: Optional[Union[DrugStrength, List[DrugStrength]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'availableStrength', 'https://schema.org/availableStrength'
        ),
        serialization_alias='https://schema.org/availableStrength',
    )
    warning: Optional[Union[str, AnyUrl, List[Union[str, AnyUrl]]]] = Field(
        default=None,
        validation_alias=AliasChoices('warning', 'https://schema.org/warning'),
        serialization_alias='https://schema.org/warning',
    )
    included_in_health_insurance_plan: Optional[
        Union[HealthInsurancePlan, List[HealthInsurancePlan]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'includedInHealthInsurancePlan',
            'https://schema.org/includedInHealthInsurancePlan',
        ),
        serialization_alias='https://schema.org/includedInHealthInsurancePlan',
    )
    drug_class: Optional[Union[DrugClass, List[DrugClass]]] = Field(
        default=None,
        validation_alias=AliasChoices('drugClass', 'https://schema.org/drugClass'),
        serialization_alias='https://schema.org/drugClass',
    )
    pregnancy_category: Optional[
        Union[DrugPregnancyCategory, List[DrugPregnancyCategory]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'pregnancyCategory', 'https://schema.org/pregnancyCategory'
        ),
        serialization_alias='https://schema.org/pregnancyCategory',
    )
    prescription_status: Optional[
        Union[DrugPrescriptionStatus, str, List[Union[DrugPrescriptionStatus, str]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'prescriptionStatus', 'https://schema.org/prescriptionStatus'
        ),
        serialization_alias='https://schema.org/prescriptionStatus',
    )
    non_proprietary_name: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'nonProprietaryName', 'https://schema.org/nonProprietaryName'
        ),
        serialization_alias='https://schema.org/nonProprietaryName',
    )
    dosage_form: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices('dosageForm', 'https://schema.org/dosageForm'),
        serialization_alias='https://schema.org/dosageForm',
    )
    drug_unit: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices('drugUnit', 'https://schema.org/drugUnit'),
        serialization_alias='https://schema.org/drugUnit',
    )


class LocationFeatureSpecification(PropertyValue):
    field_type: Literal['https://schema.org/LocationFeatureSpecification'] = Field(
        'https://schema.org/LocationFeatureSpecification', alias='@type'
    )
    valid_from: Optional[
        Union[date, AwareDatetime, List[Union[date, AwareDatetime]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('validFrom', 'https://schema.org/validFrom'),
        serialization_alias='https://schema.org/validFrom',
    )
    hours_available: Optional[
        Union[OpeningHoursSpecification, List[OpeningHoursSpecification]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'hoursAvailable', 'https://schema.org/hoursAvailable'
        ),
        serialization_alias='https://schema.org/hoursAvailable',
    )
    valid_through: Optional[
        Union[AwareDatetime, date, List[Union[AwareDatetime, date]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'validThrough', 'https://schema.org/validThrough'
        ),
        serialization_alias='https://schema.org/validThrough',
    )


class PostalAddress(ContactPoint):
    field_type: Literal['https://schema.org/PostalAddress'] = Field(
        'https://schema.org/PostalAddress', alias='@type'
    )
    address_region: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'addressRegion', 'https://schema.org/addressRegion'
        ),
        serialization_alias='https://schema.org/addressRegion',
    )
    postal_code: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices('postalCode', 'https://schema.org/postalCode'),
        serialization_alias='https://schema.org/postalCode',
    )
    street_address: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'streetAddress', 'https://schema.org/streetAddress'
        ),
        serialization_alias='https://schema.org/streetAddress',
    )
    address_country: Optional[Union[str, Country, List[Union[str, Country]]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'addressCountry', 'https://schema.org/addressCountry'
        ),
        serialization_alias='https://schema.org/addressCountry',
    )
    address_locality: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'addressLocality', 'https://schema.org/addressLocality'
        ),
        serialization_alias='https://schema.org/addressLocality',
    )
    extended_address: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'extendedAddress', 'https://schema.org/extendedAddress'
        ),
        serialization_alias='https://schema.org/extendedAddress',
    )
    post_office_box_number: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'postOfficeBoxNumber', 'https://schema.org/postOfficeBoxNumber'
        ),
        serialization_alias='https://schema.org/postOfficeBoxNumber',
    )


class UnitPriceSpecification(PriceSpecification):
    field_type: Literal['https://schema.org/UnitPriceSpecification'] = Field(
        'https://schema.org/UnitPriceSpecification', alias='@type'
    )
    unit_text: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices('unitText', 'https://schema.org/unitText'),
        serialization_alias='https://schema.org/unitText',
    )
    billing_duration: Optional[
        Union[
            Duration,
            float,
            QuantitativeValue,
            List[Union[Duration, float, QuantitativeValue]],
        ]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'billingDuration', 'https://schema.org/billingDuration'
        ),
        serialization_alias='https://schema.org/billingDuration',
    )
    unit_code: Optional[Union[AnyUrl, str, List[Union[AnyUrl, str]]]] = Field(
        default=None,
        validation_alias=AliasChoices('unitCode', 'https://schema.org/unitCode'),
        serialization_alias='https://schema.org/unitCode',
    )
    reference_quantity: Optional[
        Union[QuantitativeValue, List[QuantitativeValue]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'referenceQuantity', 'https://schema.org/referenceQuantity'
        ),
        serialization_alias='https://schema.org/referenceQuantity',
    )
    price_component_type: Optional[
        Union[PriceComponentTypeEnumeration, List[PriceComponentTypeEnumeration]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'priceComponentType', 'https://schema.org/priceComponentType'
        ),
        serialization_alias='https://schema.org/priceComponentType',
    )
    billing_increment: Optional[Union[float, List[float]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'billingIncrement', 'https://schema.org/billingIncrement'
        ),
        serialization_alias='https://schema.org/billingIncrement',
    )
    price_type: Optional[
        Union[str, PriceTypeEnumeration, List[Union[str, PriceTypeEnumeration]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('priceType', 'https://schema.org/priceType'),
        serialization_alias='https://schema.org/priceType',
    )
    billing_start: Optional[Union[float, List[float]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'billingStart', 'https://schema.org/billingStart'
        ),
        serialization_alias='https://schema.org/billingStart',
    )


class DeliveryChargeSpecification(PriceSpecification):
    field_type: Literal['https://schema.org/DeliveryChargeSpecification'] = Field(
        'https://schema.org/DeliveryChargeSpecification', alias='@type'
    )
    area_served: Optional[
        Union[
            GeoShape,
            str,
            AdministrativeArea,
            Place,
            List[Union[GeoShape, str, AdministrativeArea, Place]],
        ]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('areaServed', 'https://schema.org/areaServed'),
        serialization_alias='https://schema.org/areaServed',
    )
    eligible_region: Optional[
        Union[GeoShape, str, Place, List[Union[GeoShape, str, Place]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'eligibleRegion', 'https://schema.org/eligibleRegion'
        ),
        serialization_alias='https://schema.org/eligibleRegion',
    )
    applies_to_delivery_method: Optional[
        Union[DeliveryMethod, List[DeliveryMethod]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'appliesToDeliveryMethod', 'https://schema.org/appliesToDeliveryMethod'
        ),
        serialization_alias='https://schema.org/appliesToDeliveryMethod',
    )
    ineligible_region: Optional[
        Union[str, Place, GeoShape, List[Union[str, Place, GeoShape]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'ineligibleRegion', 'https://schema.org/ineligibleRegion'
        ),
        serialization_alias='https://schema.org/ineligibleRegion',
    )


class MonetaryAmountDistribution(QuantitativeValueDistribution):
    field_type: Literal['https://schema.org/MonetaryAmountDistribution'] = Field(
        'https://schema.org/MonetaryAmountDistribution', alias='@type'
    )
    currency: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices('currency', 'https://schema.org/currency'),
        serialization_alias='https://schema.org/currency',
    )


class SizeSpecification(QualitativeValue):
    field_type: Literal['https://schema.org/SizeSpecification'] = Field(
        'https://schema.org/SizeSpecification', alias='@type'
    )
    suggested_measurement: Optional[
        Union[QuantitativeValue, List[QuantitativeValue]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'suggestedMeasurement', 'https://schema.org/suggestedMeasurement'
        ),
        serialization_alias='https://schema.org/suggestedMeasurement',
    )
    size_system: Optional[
        Union[str, SizeSystemEnumeration, List[Union[str, SizeSystemEnumeration]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('sizeSystem', 'https://schema.org/sizeSystem'),
        serialization_alias='https://schema.org/sizeSystem',
    )
    suggested_age: Optional[Union[QuantitativeValue, List[QuantitativeValue]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'suggestedAge', 'https://schema.org/suggestedAge'
        ),
        serialization_alias='https://schema.org/suggestedAge',
    )
    size_group: Optional[
        Union[SizeGroupEnumeration, str, List[Union[SizeGroupEnumeration, str]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('sizeGroup', 'https://schema.org/sizeGroup'),
        serialization_alias='https://schema.org/sizeGroup',
    )
    has_measurement: Optional[
        Union[QuantitativeValue, List[QuantitativeValue]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'hasMeasurement', 'https://schema.org/hasMeasurement'
        ),
        serialization_alias='https://schema.org/hasMeasurement',
    )
    suggested_gender: Optional[
        Union[GenderType, str, List[Union[GenderType, str]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'suggestedGender', 'https://schema.org/suggestedGender'
        ),
        serialization_alias='https://schema.org/suggestedGender',
    )


class MedicalEvidenceLevel(MedicalEnumeration):
    field_type: Literal['https://schema.org/MedicalEvidenceLevel'] = Field(
        'https://schema.org/MedicalEvidenceLevel', alias='@type'
    )


class MedicineSystem(MedicalEnumeration):
    field_type: Literal['https://schema.org/MedicineSystem'] = Field(
        'https://schema.org/MedicineSystem', alias='@type'
    )


class MedicalStudyStatus(MedicalEnumeration):
    field_type: Literal['https://schema.org/MedicalStudyStatus'] = Field(
        'https://schema.org/MedicalStudyStatus', alias='@type'
    )


class MedicalProcedureType(MedicalEnumeration):
    field_type: Literal['https://schema.org/MedicalProcedureType'] = Field(
        'https://schema.org/MedicalProcedureType', alias='@type'
    )


class DrugPregnancyCategory(MedicalEnumeration):
    field_type: Literal['https://schema.org/DrugPregnancyCategory'] = Field(
        'https://schema.org/DrugPregnancyCategory', alias='@type'
    )


class DrugPrescriptionStatus(MedicalEnumeration):
    field_type: Literal['https://schema.org/DrugPrescriptionStatus'] = Field(
        'https://schema.org/DrugPrescriptionStatus', alias='@type'
    )


class PhysicalExam(MedicalEnumeration):
    field_type: Literal['https://schema.org/PhysicalExam'] = Field(
        'https://schema.org/PhysicalExam', alias='@type'
    )


class MedicalSpecialty(Specialty):
    field_type: Literal['https://schema.org/MedicalSpecialty'] = Field(
        'https://schema.org/MedicalSpecialty', alias='@type'
    )


class EventStatusType(StatusEnumeration):
    field_type: Literal['https://schema.org/EventStatusType'] = Field(
        'https://schema.org/EventStatusType', alias='@type'
    )


class ActionStatusType(StatusEnumeration):
    field_type: Literal['https://schema.org/ActionStatusType'] = Field(
        'https://schema.org/ActionStatusType', alias='@type'
    )


class EUEnergyEfficiencyEnumeration(EnergyEfficiencyEnumeration):
    field_type: Literal['https://schema.org/EUEnergyEfficiencyEnumeration'] = Field(
        'https://schema.org/EUEnergyEfficiencyEnumeration', alias='@type'
    )


class IPTCDigitalSourceEnumeration(MediaEnumeration):
    field_type: Literal['https://schema.org/IPTCDigitalSourceEnumeration'] = Field(
        'https://schema.org/IPTCDigitalSourceEnumeration', alias='@type'
    )


class PaymentCard(FinancialProduct):
    field_type: Literal['https://schema.org/PaymentCard'] = Field(
        'https://schema.org/PaymentCard', alias='@type'
    )
    monthly_minimum_repayment_amount: Optional[
        Union[float, MonetaryAmount, List[Union[float, MonetaryAmount]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'monthlyMinimumRepaymentAmount',
            'https://schema.org/monthlyMinimumRepaymentAmount',
        ),
        serialization_alias='https://schema.org/monthlyMinimumRepaymentAmount',
    )
    floor_limit: Optional[Union[MonetaryAmount, List[MonetaryAmount]]] = Field(
        default=None,
        validation_alias=AliasChoices('floorLimit', 'https://schema.org/floorLimit'),
        serialization_alias='https://schema.org/floorLimit',
    )
    cash_back: Optional[Union[float, bool, List[Union[float, bool]]]] = Field(
        default=None,
        validation_alias=AliasChoices('cashBack', 'https://schema.org/cashBack'),
        serialization_alias='https://schema.org/cashBack',
    )
    contactless_payment: Optional[Union[bool, List[bool]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'contactlessPayment', 'https://schema.org/contactlessPayment'
        ),
        serialization_alias='https://schema.org/contactlessPayment',
    )


class LoanOrCredit(FinancialProduct):
    field_type: Literal['https://schema.org/LoanOrCredit'] = Field(
        'https://schema.org/LoanOrCredit', alias='@type'
    )
    grace_period: Optional[Union[Duration, List[Duration]]] = Field(
        default=None,
        validation_alias=AliasChoices('gracePeriod', 'https://schema.org/gracePeriod'),
        serialization_alias='https://schema.org/gracePeriod',
    )
    required_collateral: Optional[Union[str, Thing, List[Union[str, Thing]]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'requiredCollateral', 'https://schema.org/requiredCollateral'
        ),
        serialization_alias='https://schema.org/requiredCollateral',
    )
    currency: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices('currency', 'https://schema.org/currency'),
        serialization_alias='https://schema.org/currency',
    )
    loan_repayment_form: Optional[
        Union[RepaymentSpecification, List[RepaymentSpecification]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'loanRepaymentForm', 'https://schema.org/loanRepaymentForm'
        ),
        serialization_alias='https://schema.org/loanRepaymentForm',
    )
    amount: Optional[
        Union[MonetaryAmount, float, List[Union[MonetaryAmount, float]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices('amount', 'https://schema.org/amount'),
        serialization_alias='https://schema.org/amount',
    )
    recourse_loan: Optional[Union[bool, List[bool]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'recourseLoan', 'https://schema.org/recourseLoan'
        ),
        serialization_alias='https://schema.org/recourseLoan',
    )
    loan_term: Optional[Union[QuantitativeValue, List[QuantitativeValue]]] = Field(
        default=None,
        validation_alias=AliasChoices('loanTerm', 'https://schema.org/loanTerm'),
        serialization_alias='https://schema.org/loanTerm',
    )
    loan_type: Optional[Union[str, AnyUrl, List[Union[str, AnyUrl]]]] = Field(
        default=None,
        validation_alias=AliasChoices('loanType', 'https://schema.org/loanType'),
        serialization_alias='https://schema.org/loanType',
    )
    renegotiable_loan: Optional[Union[bool, List[bool]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'renegotiableLoan', 'https://schema.org/renegotiableLoan'
        ),
        serialization_alias='https://schema.org/renegotiableLoan',
    )


class HowToSupply(HowToItem):
    field_type: Literal['https://schema.org/HowToSupply'] = Field(
        'https://schema.org/HowToSupply', alias='@type'
    )
    estimated_cost: Optional[
        Union[str, MonetaryAmount, List[Union[str, MonetaryAmount]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'estimatedCost', 'https://schema.org/estimatedCost'
        ),
        serialization_alias='https://schema.org/estimatedCost',
    )


class HowToTool(HowToItem):
    field_type: Literal['https://schema.org/HowToTool'] = Field(
        'https://schema.org/HowToTool', alias='@type'
    )


class MaximumDoseSchedule(DoseSchedule):
    field_type: Literal['https://schema.org/MaximumDoseSchedule'] = Field(
        'https://schema.org/MaximumDoseSchedule', alias='@type'
    )


class MedicalSign(MedicalSignOrSymptom):
    field_type: Literal['https://schema.org/MedicalSign'] = Field(
        'https://schema.org/MedicalSign', alias='@type'
    )
    identifying_test: Optional[Union[MedicalTest, List[MedicalTest]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'identifyingTest', 'https://schema.org/identifyingTest'
        ),
        serialization_alias='https://schema.org/identifyingTest',
    )
    identifying_exam: Optional[Union[PhysicalExam, List[PhysicalExam]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'identifyingExam', 'https://schema.org/identifyingExam'
        ),
        serialization_alias='https://schema.org/identifyingExam',
    )


class MedicalTherapy(TherapeuticProcedure):
    field_type: Literal['https://schema.org/MedicalTherapy'] = Field(
        'https://schema.org/MedicalTherapy', alias='@type'
    )
    serious_adverse_outcome: Optional[
        Union[MedicalEntity, List[MedicalEntity]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'seriousAdverseOutcome', 'https://schema.org/seriousAdverseOutcome'
        ),
        serialization_alias='https://schema.org/seriousAdverseOutcome',
    )
    contraindication: Optional[
        Union[str, MedicalContraindication, List[Union[str, MedicalContraindication]]]
    ] = Field(
        default=None,
        validation_alias=AliasChoices(
            'contraindication', 'https://schema.org/contraindication'
        ),
        serialization_alias='https://schema.org/contraindication',
    )
    duplicate_therapy: Optional[Union[MedicalTherapy, List[MedicalTherapy]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'duplicateTherapy', 'https://schema.org/duplicateTherapy'
        ),
        serialization_alias='https://schema.org/duplicateTherapy',
    )


class CreditCard(PaymentCard):
    field_type: Literal['https://schema.org/CreditCard'] = Field(
        'https://schema.org/CreditCard', alias='@type'
    )
