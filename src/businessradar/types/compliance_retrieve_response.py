# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import date, datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = [
    "ComplianceRetrieveResponse",
    "Entity",
    "EntityResult",
    "EntityResultAddress",
    "EntityResultSource",
    "EntityResultTag",
    "EntityUbo",
]


class EntityResultAddress(BaseModel):
    city: Optional[str] = None

    country: Optional[
        Literal[
            "AF",
            "AX",
            "AL",
            "DZ",
            "AS",
            "AD",
            "AO",
            "AI",
            "AQ",
            "AG",
            "AR",
            "AM",
            "AW",
            "AU",
            "AT",
            "AZ",
            "BS",
            "BH",
            "BD",
            "BB",
            "BY",
            "BE",
            "BZ",
            "BJ",
            "BM",
            "BT",
            "BO",
            "BQ",
            "BA",
            "BW",
            "BV",
            "BR",
            "IO",
            "BN",
            "BG",
            "BF",
            "BI",
            "CV",
            "KH",
            "CM",
            "CA",
            "KY",
            "CF",
            "TD",
            "CL",
            "CN",
            "CX",
            "CC",
            "CO",
            "KM",
            "CG",
            "CD",
            "CK",
            "CR",
            "CI",
            "HR",
            "CU",
            "CW",
            "CY",
            "CZ",
            "DK",
            "DJ",
            "DM",
            "DO",
            "EC",
            "EG",
            "SV",
            "GQ",
            "ER",
            "EE",
            "SZ",
            "ET",
            "FK",
            "FO",
            "FJ",
            "FI",
            "FR",
            "GF",
            "PF",
            "TF",
            "GA",
            "GM",
            "GE",
            "DE",
            "GH",
            "GI",
            "GR",
            "GL",
            "GD",
            "GP",
            "GU",
            "GT",
            "GG",
            "GN",
            "GW",
            "GY",
            "HT",
            "HM",
            "VA",
            "HN",
            "HK",
            "HU",
            "IS",
            "IN",
            "ID",
            "IR",
            "IQ",
            "IE",
            "IM",
            "IL",
            "IT",
            "JM",
            "JP",
            "JE",
            "JO",
            "KZ",
            "KE",
            "KI",
            "KP",
            "KR",
            "KW",
            "KG",
            "LA",
            "LV",
            "LB",
            "LS",
            "LR",
            "LY",
            "LI",
            "LT",
            "LU",
            "MO",
            "MG",
            "MW",
            "MY",
            "MV",
            "ML",
            "MT",
            "MH",
            "MQ",
            "MR",
            "MU",
            "YT",
            "MX",
            "FM",
            "MD",
            "MC",
            "MN",
            "ME",
            "MS",
            "MA",
            "MZ",
            "MM",
            "NA",
            "NR",
            "NP",
            "NL",
            "NC",
            "NZ",
            "NI",
            "NE",
            "NG",
            "NU",
            "NF",
            "MK",
            "MP",
            "NO",
            "OM",
            "PK",
            "PW",
            "PS",
            "PA",
            "PG",
            "PY",
            "PE",
            "PH",
            "PN",
            "PL",
            "PT",
            "PR",
            "QA",
            "RE",
            "RO",
            "RU",
            "RW",
            "BL",
            "SH",
            "KN",
            "LC",
            "MF",
            "PM",
            "VC",
            "WS",
            "SM",
            "ST",
            "SA",
            "SN",
            "RS",
            "SC",
            "SL",
            "SG",
            "SX",
            "SK",
            "SI",
            "SB",
            "SO",
            "ZA",
            "GS",
            "SS",
            "ES",
            "LK",
            "SD",
            "SR",
            "SJ",
            "SE",
            "CH",
            "SY",
            "TW",
            "TJ",
            "TZ",
            "TH",
            "TL",
            "TG",
            "TK",
            "TO",
            "TT",
            "TN",
            "TR",
            "TM",
            "TC",
            "TV",
            "UG",
            "UA",
            "AE",
            "GB",
            "UM",
            "US",
            "UY",
            "UZ",
            "VU",
            "VE",
            "VN",
            "VG",
            "VI",
            "WF",
            "EH",
            "YE",
            "ZM",
            "ZW",
            "",
        ]
    ] = None

    postal_code: Optional[str] = None

    street: Optional[str] = None


class EntityResultSource(BaseModel):
    url: str

    description: Optional[str] = None

    document: Optional[str] = None

    domain: Optional[str] = None

    publication_date: Optional[date] = None

    title: Optional[str] = None


class EntityResultTag(BaseModel):
    tag: str


class EntityResult(BaseModel):
    addresses: List[EntityResultAddress]

    created_at: datetime

    external_id: str

    name: str

    result_type: Literal["sanction", "pep", "adverse_media", "enforcement", "govt_owned"]
    """
    - `sanction` - Sanction
    - `pep` - Politically Exposed Person
    - `adverse_media` - Adverse media
    - `enforcement` - Enforcement
    - `govt_owned` - Government owned
    """

    sources: List[EntityResultSource]

    tags: List[EntityResultTag]

    confidence: Optional[float] = None

    formatted_text: Optional[str] = None

    formatted_text_en: Optional[str] = None

    formatted_title: Optional[str] = None

    formatted_title_en: Optional[str] = None

    image: Optional[str] = None

    language: Optional[
        Literal[
            "af",
            "ar",
            "az",
            "bg",
            "be",
            "bn",
            "br",
            "bs",
            "ca",
            "cs",
            "cy",
            "da",
            "de",
            "el",
            "en",
            "eo",
            "es",
            "et",
            "eu",
            "fa",
            "fi",
            "fr",
            "fy",
            "ga",
            "gd",
            "gl",
            "he",
            "hi",
            "hr",
            "hu",
            "hy",
            "ia",
            "id",
            "ig",
            "io",
            "is",
            "it",
            "ja",
            "ka",
            "kk",
            "km",
            "no",
            "kn",
            "ko",
            "ky",
            "lb",
            "lt",
            "lv",
            "mk",
            "ml",
            "mn",
            "mr",
            "my",
            "ne",
            "nl",
            "os",
            "pa",
            "pl",
            "pt",
            "ro",
            "ru",
            "sk",
            "sl",
            "sq",
            "sr",
            "sv",
            "sw",
            "ta",
            "te",
            "tg",
            "th",
            "tk",
            "tr",
            "tt",
            "uk",
            "ur",
            "uz",
            "vi",
            "zh",
            "",
        ]
    ] = None

    source_date: Optional[datetime] = None

    source_name: Optional[str] = None

    text: Optional[str] = None

    text_en: Optional[str] = None

    title: Optional[str] = None

    title_en: Optional[str] = None

    url: Optional[str] = None


class EntityUbo(BaseModel):
    name: str

    beneficial_ownership_percentage: Optional[float] = None

    birth_date: Optional[date] = None

    degree_of_separation: Optional[int] = None

    direct_ownership_percentage: Optional[float] = None

    implied_beneficial_ownership_percentage: Optional[float] = None

    implied_direct_ownership_percentage: Optional[float] = None

    implied_indirect_ownership_percentage: Optional[float] = None

    indirect_ownership_percentage: Optional[float] = None

    is_beneficiary: Optional[bool] = None

    is_person_with_significant_control: Optional[bool] = None


class Entity(BaseModel):
    entity_role: Literal["ubo", "director", "company", "manually_added"]
    """
    - `ubo` - Ultimate Beneficial Owner
    - `director` - Director
    - `company` - Company
    - `manually_added` - Manually added
    """

    entity_type: Literal["individual", "company"]
    """
    - `individual` - Individual
    - `company` - Company
    """

    external_id: str

    name: str

    results: List[EntityResult]

    ubo: Optional[EntityUbo] = None

    country: Optional[str] = None


class ComplianceRetrieveResponse(BaseModel):
    entities: List[Entity]

    external_id: str

    activity_score: Optional[Literal["low", "medium", "high", ""]] = None

    adverse_media_score: Optional[Literal["low", "medium", "high", ""]] = None

    compliance_score: Optional[Literal["low", "medium", "high", ""]] = None

    country_score: Optional[Literal["low", "medium", "high", ""]] = None

    pep_score: Optional[Literal["low", "medium", "high", ""]] = None

    sanction_score: Optional[Literal["low", "medium", "high", ""]] = None

    status: Optional[Literal["pending", "queued", "in_progress", "searching_directors", "completed", "failed"]] = None
    """
    - `pending` - Pending
    - `queued` - Queued
    - `in_progress` - In Progress
    - `searching_directors` - Searching Directors
    - `completed` - Completed
    - `failed` - Failed
    """
