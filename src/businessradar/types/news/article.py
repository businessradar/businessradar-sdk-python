# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel
from ..country_enum import CountryEnum
from .language_enum import LanguageEnum

__all__ = ["Article", "CompanyArticle", "CompanyArticleCompany", "Source", "SubArticle"]


class CompanyArticleCompany(BaseModel):
    country: CountryEnum
    """
    - `AF` - Afghanistan
    - `AX` - Aland Islands
    - `AL` - Albania
    - `DZ` - Algeria
    - `AS` - American Samoa
    - `AD` - Andorra
    - `AO` - Angola
    - `AI` - Anguilla
    - `AQ` - Antarctica
    - `AG` - Antigua and Barbuda
    - `AR` - Argentina
    - `AM` - Armenia
    - `AW` - Aruba
    - `AU` - Australia
    - `AT` - Austria
    - `AZ` - Azerbaijan
    - `BS` - Bahamas
    - `BH` - Bahrain
    - `BD` - Bangladesh
    - `BB` - Barbados
    - `BY` - Belarus
    - `BE` - Belgium
    - `BZ` - Belize
    - `BJ` - Benin
    - `BM` - Bermuda
    - `BT` - Bhutan
    - `BO` - Bolivia
    - `BQ` - Bonaire
    - `BA` - Bosnia and Herzegovina
    - `BW` - Botswana
    - `BV` - Bouvet Island
    - `BR` - Brazil
    - `IO` - British Indian Ocean Territory
    - `BN` - Brunei Darussalam
    - `BG` - Bulgaria
    - `BF` - Burkina Faso
    - `BI` - Burundi
    - `CV` - Cabo Verde
    - `KH` - Cambodia
    - `CM` - Cameroon
    - `CA` - Canada
    - `KY` - Cayman Islands
    - `CF` - Central African Republic
    - `TD` - Chad
    - `CL` - Chile
    - `CN` - China
    - `CX` - Christmas Island
    - `CC` - Cocos Keeling Islands
    - `CO` - Colombia
    - `KM` - Comoros
    - `CG` - Congo
    - `CD` - Congo Democratic Republic
    - `CK` - Cook Islands
    - `CR` - Costa Rica
    - `CI` - Cote d'Ivoire
    - `HR` - Croatia
    - `CU` - Cuba
    - `CW` - Curacao
    - `CY` - Cyprus
    - `CZ` - Czechia
    - `DK` - Denmark
    - `DJ` - Djibouti
    - `DM` - Dominica
    - `DO` - Dominican Republic
    - `EC` - Ecuador
    - `EG` - Egypt
    - `SV` - El Salvador
    - `GQ` - Equatorial Guinea
    - `ER` - Eritrea
    - `EE` - Estonia
    - `SZ` - Eswatini
    - `ET` - Ethiopia
    - `FK` - Falkland Islands
    - `FO` - Faroe Islands
    - `FJ` - Fiji
    - `FI` - Finland
    - `FR` - France
    - `GF` - French Guiana
    - `PF` - French Polynesia
    - `TF` - French Southern Territories
    - `GA` - Gabon
    - `GM` - Gambia
    - `GE` - Georgia
    - `DE` - Germany
    - `GH` - Ghana
    - `GI` - Gibraltar
    - `GR` - Greece
    - `GL` - Greenland
    - `GD` - Grenada
    - `GP` - Guadeloupe
    - `GU` - Guam
    - `GT` - Guatemala
    - `GG` - Guernsey
    - `GN` - Guinea
    - `GW` - Guinea-Bissau
    - `GY` - Guyana
    - `HT` - Haiti
    - `HM` - Heard Island and McDonald Islands
    - `VA` - Holy See
    - `HN` - Honduras
    - `HK` - Hong Kong
    - `HU` - Hungary
    - `IS` - Iceland
    - `IN` - India
    - `ID` - Indonesia
    - `IR` - Iran (Islamic Republic of)
    - `IQ` - Iraq
    - `IE` - Ireland
    - `IM` - Isle of Man
    - `IL` - Israel
    - `IT` - Italy
    - `JM` - Jamaica
    - `JP` - Japan
    - `JE` - Jersey
    - `JO` - Jordan
    - `KZ` - Kazakhstan
    - `KE` - Kenya
    - `KI` - Kiribati
    - `KP` - Korea (the Democratic People's Republic of)
    - `KR` - Korea (the Republic of)
    - `KW` - Kuwait
    - `KG` - Kyrgyzstan
    - `LA` - Lao People's Democratic Republic
    - `LV` - Latvia
    - `LB` - Lebanon
    - `LS` - Lesotho
    - `LR` - Liberia
    - `LY` - Libya
    - `LI` - Liechtenstein
    - `LT` - Lithuania
    - `LU` - Luxembourg
    - `MO` - Macao
    - `MG` - Madagascar
    - `MW` - Malawi
    - `MY` - Malaysia
    - `MV` - Maldives
    - `ML` - Mali
    - `MT` - Malta
    - `MH` - Marshall Islands
    - `MQ` - Martinique
    - `MR` - Mauritania
    - `MU` - Mauritius
    - `YT` - Mayotte
    - `MX` - Mexico
    - `FM` - Micronesia
    - `MD` - Moldova
    - `MC` - Monaco
    - `MN` - Mongolia
    - `ME` - Montenegro
    - `MS` - Montserrat
    - `MA` - Morocco
    - `MZ` - Mozambique
    - `MM` - Myanmar
    - `NA` - Namibia
    - `NR` - Nauru
    - `NP` - Nepal
    - `NL` - Netherlands
    - `NC` - New Caledonia
    - `NZ` - New Zealand
    - `NI` - Nicaragua
    - `NE` - Niger
    - `NG` - Nigeria
    - `NU` - Niue
    - `NF` - Norfolk Island
    - `MK` - North Macedonia
    - `MP` - Northern Mariana Islands
    - `NO` - Norway
    - `OM` - Oman
    - `PK` - Pakistan
    - `PW` - Palau
    - `PS` - Palestine, State of
    - `PA` - Panama
    - `PG` - Papua New Guinea
    - `PY` - Paraguay
    - `PE` - Peru
    - `PH` - Philippines
    - `PN` - Pitcairn
    - `PL` - Poland
    - `PT` - Portugal
    - `PR` - Puerto Rico
    - `QA` - Qatar
    - `RE` - Réunion
    - `RO` - Romania
    - `RU` - Russian Federation
    - `RW` - Rwanda
    - `BL` - Saint Barthélemy
    - `SH` - Saint Helena
    - `KN` - Saint Kitts and Nevis
    - `LC` - Saint Lucia
    - `MF` - Saint Martin
    - `PM` - Saint Pierre and Miquelon
    - `VC` - Saint Vincent and the Grenadines
    - `WS` - Samoa
    - `SM` - San Marino
    - `ST` - Sao Tome and Principe
    - `SA` - Saudi Arabia
    - `SN` - Senegal
    - `RS` - Serbia
    - `SC` - Seychelles
    - `SL` - Sierra Leone
    - `SG` - Singapore
    - `SX` - Sint Maarten
    - `SK` - Slovakia
    - `SI` - Slovenia
    - `SB` - Solomon Islands
    - `SO` - Somalia
    - `ZA` - South Africa
    - `GS` - South Georgia and the South Sandwich Islands
    - `SS` - South Sudan
    - `ES` - Spain
    - `LK` - Sri Lanka
    - `SD` - Sudan
    - `SR` - Suriname
    - `SJ` - Svalbard and Jan Mayen
    - `SE` - Sweden
    - `CH` - Switzerland
    - `SY` - Syrian Arab Republic
    - `TW` - Taiwan
    - `TJ` - Tajikistan
    - `TZ` - Tanzania
    - `TH` - Thailand
    - `TL` - Timor-Leste
    - `TG` - Togo
    - `TK` - Tokelau
    - `TO` - Tonga
    - `TT` - Trinidad and Tobago
    - `TN` - Tunisia
    - `TR` - Turkey
    - `TM` - Turkmenistan
    - `TC` - Turks and Caicos Islands
    - `TV` - Tuvalu
    - `UG` - Uganda
    - `UA` - Ukraine
    - `AE` - United Arab Emirates
    - `GB` - United Kingdom
    - `UM` - United States Minor Outlying Islands
    - `US` - United States of America
    - `UY` - Uruguay
    - `UZ` - Uzbekistan
    - `VU` - Vanuatu
    - `VE` - Venezuela
    - `VN` - Viet Nam
    - `VG` - Virgin Islands
    - `VI` - Virgin Islands
    - `WF` - Wallis and Futuna
    - `EH` - Western Sahara
    - `YE` - Yemen
    - `ZM` - Zambia
    - `ZW` - Zimbabwe
    """

    customer_reference: str
    """Get Customer reference."""

    name: str

    duns_number: Optional[str] = None

    external_id: Optional[str] = None

    global_ultimate_duns_number: Optional[str] = None

    global_ultimate_name: Optional[str] = None


class CompanyArticle(BaseModel):
    categories: List["CategoryTree"]

    company: CompanyArticleCompany
    """Custom Company Serializer for News Articles."""

    sentiment: Optional[float] = None

    snippet: Optional[str] = None

    snippet_en: Optional[str] = None


class Source(BaseModel):
    domain: str

    name: str

    url: str


class SubArticle(BaseModel):
    url: str

    external_id: Optional[str] = None


class Article(BaseModel):
    categories: List["CategoryTree"]

    company_articles: List[CompanyArticle]

    created_at: datetime

    image_url: str
    """Get Image URL if allowed for source."""

    is_clustered: bool
    """Check if article is clustered."""

    language: LanguageEnum
    """
    - `af` - Afrikaans
    - `ar` - Arabic
    - `az` - Azerbaijani
    - `bg` - Bulgarian
    - `be` - Belarusian
    - `bn` - Bengali
    - `br` - Breton
    - `bs` - Bosnian
    - `ca` - Catalan
    - `cs` - Czech
    - `cy` - Welsh
    - `da` - Danish
    - `de` - German
    - `el` - Greek
    - `en` - English
    - `eo` - Esperanto
    - `es` - Spanish
    - `et` - Estonian
    - `eu` - Basque
    - `fa` - Persian
    - `fi` - Finnish
    - `fr` - French
    - `fy` - Frisian
    - `ga` - Irish
    - `gd` - Scottish Gaelic
    - `gl` - Galician
    - `he` - Hebrew
    - `hi` - Hindi
    - `hr` - Croatian
    - `hu` - Hungarian
    - `hy` - Armenian
    - `ia` - Interlingua
    - `id` - Indonesian
    - `ig` - Igbo
    - `io` - Ido
    - `is` - Icelandic
    - `it` - Italian
    - `ja` - Japanese
    - `ka` - Georgian
    - `kk` - Kazakh
    - `km` - Khmer
    - `no` - Norwegian
    - `kn` - Kannada
    - `ko` - Korean
    - `ky` - Kyrgyz
    - `lb` - Luxembourgish
    - `lt` - Lithuanian
    - `lv` - Latvian
    - `mk` - Macedonian
    - `ml` - Malayalam
    - `mn` - Mongolian
    - `mr` - Marathi
    - `my` - Burmese
    - `ne` - Nepali
    - `nl` - Dutch
    - `os` - Ossetic
    - `pa` - Punjabi
    - `pl` - Polish
    - `pt` - Portuguese
    - `ro` - Romanian
    - `ru` - Russian
    - `sk` - Slovak
    - `sl` - Slovenian
    - `sq` - Albanian
    - `sr` - Serbian
    - `sv` - Swedish
    - `sw` - Swahili
    - `ta` - Tamil
    - `te` - Telugu
    - `tg` - Tajik
    - `th` - Thai
    - `tk` - Turkmen
    - `tr` - Turkish
    - `tt` - Tatar
    - `uk` - Ukrainian
    - `ur` - Urdu
    - `uz` - Uzbek
    - `vi` - Vietnamese
    - `zh` - Chinese
    """

    publication_datetime: datetime
    """Calculate publication datetime of article."""

    snippet: str
    """Get snippet if allowed for source."""

    snippet_en: str
    """Get snippet if allowed for source."""

    source: Source
    """Serializer for Source Information."""

    sub_articles: List[SubArticle]

    title: str

    title_en: str

    updated_at: datetime

    url: str

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

    external_id: Optional[str] = None

    is_paywalled: Optional[Literal["full", "partial", ""]] = None

    sentiment: Optional[float] = None

    summary: Optional[str] = None

    summary_en: Optional[str] = None


from .category_tree import CategoryTree
