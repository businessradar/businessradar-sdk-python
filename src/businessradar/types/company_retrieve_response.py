# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import date

from .._models import BaseModel
from .country_enum import CountryEnum
from .industry_code import IndustryCode

__all__ = ["CompanyRetrieveResponse", "RegistrationNumber"]


class RegistrationNumber(BaseModel):
    description: str

    number: str

    type: int
    """Dun and Bradstreet type code for the source of thisRegistration number."""


class CompanyRetrieveResponse(BaseModel):
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

    duns_number: str

    founding_date: date

    industry_codes: List[IndustryCode]

    name: str

    primary_industry_codes: List[IndustryCode]

    registration_numbers: List[RegistrationNumber]

    slug: str

    social_description: Optional[str] = None
    """Get Social Description."""

    social_logo: Optional[str] = None
    """Get Social Logo."""

    address_latitude: Optional[float] = None

    address_longitude: Optional[float] = None

    address_phone: Optional[str] = None

    address_place: Optional[str] = None

    address_postal: Optional[str] = None

    address_region: Optional[str] = None

    address_street: Optional[str] = None

    article_count: Optional[int] = None
    """Amount of articles available"""

    external_id: Optional[str] = None

    linkedin_url: Optional[str] = None

    publication_count: Optional[int] = None
    """Amount of publications available"""

    report_count: Optional[int] = None
    """Amount of reports available"""

    review_average_score: Optional[float] = None
    """Average review score"""

    review_count: Optional[int] = None
    """Amount of reviews available"""

    ticker_symbol: Optional[str] = None

    website_domain: Optional[str] = None

    website_icon_url: Optional[str] = None
    """Icon of the found website"""

    website_url: Optional[str] = None
