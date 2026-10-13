# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["ComplianceCreateParams", "Entity"]


class ComplianceCreateParams(TypedDict, total=False):
    adverse_media_monitoring_enabled: bool
    """Deprecated: monitoring is now derived from screening.

    This flag (OR'd with sanction_monitoring_enabled) sets the check's monitoring
    master switch; per-type coverage follows which screenings run.
    """

    company_id: Optional[str]

    directors_screening_enabled: bool
    """If directors should be screened."""

    entities: Iterable[Entity]

    name: Optional[str]
    """Custom name for this compliance check."""

    ownership_screening_threshold: Optional[float]
    """The threshold for ultimate ownership to enable for screening."""

    sanction_monitoring_enabled: bool
    """Deprecated: monitoring is now derived from screening.

    This flag (OR'd with adverse_media_monitoring_enabled) sets the check's
    monitoring master switch; per-type coverage follows which screenings run.
    """

    ubo_screening_enabled: bool
    """If enabled, UBOs discovered for the company will be screened."""


class Entity(TypedDict, total=False):
    """### Compliance Entity Request

    Represents an entity (individual or organization) to be included in a compliance
    screening.
    """

    name: Required[str]

    aliases: SequenceNotStr[str]
    """Alternative names or aliases for the compliance entity."""

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
            "XK",
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
    ]
    """ISO 3166-1 alpha-2 country code.

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
    - `XK` - Kosovo
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

    date_of_birth: Optional[str]
    """Date of birth.

    Accepts a full or partial date in YYYY, YYYY-MM or YYYY-MM-DD format (e.g. when
    only the year is known).
    """

    entity_type: Literal["individual", "company", "vessel"]
    """
    - `individual` - Individual
    - `company` - Company
    - `vessel` - Vessel
    """

    first_name: Optional[str]

    last_name: Optional[str]

    middle_name: Optional[str]
