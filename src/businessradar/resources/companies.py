# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal

import httpx

from ..types import (
    CountryEnum,
    company_list_params,
    company_create_params,
    company_list_attribute_changes_params,
    company_list_missing_company_investigations_params,
    company_create_missing_company_investigation_params,
)
from .._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..pagination import SyncNextKey, AsyncNextKey
from .._base_client import AsyncPaginator, make_request_options
from ..types.country_enum import CountryEnum
from ..types.registration import Registration
from ..types.company_list_response import CompanyListResponse
from ..types.company_retrieve_response import CompanyRetrieveResponse
from ..types.company_list_attribute_changes_response import CompanyListAttributeChangesResponse
from ..types.shared_params.portfolio_company_detail_request import PortfolioCompanyDetailRequest
from ..types.company_list_missing_company_investigations_response import CompanyListMissingCompanyInvestigationsResponse
from ..types.company_create_missing_company_investigation_response import (
    CompanyCreateMissingCompanyInvestigationResponse,
)
from ..types.company_retrieve_missing_company_investigation_response import (
    CompanyRetrieveMissingCompanyInvestigationResponse,
)

__all__ = ["CompaniesResource", "AsyncCompaniesResource"]


class CompaniesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CompaniesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/businessradar/businessradar-sdk-python#accessing-raw-response-data-eg-headers
        """
        return CompaniesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CompaniesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/businessradar/businessradar-sdk-python#with_streaming_response
        """
        return CompaniesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        company: Optional[PortfolioCompanyDetailRequest] | Omit = omit,
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
        ]
        | Omit = omit,
        customer_reference: Optional[str] | Omit = omit,
        duns_number: Optional[str] | Omit = omit,
        primary_name: Optional[str] | Omit = omit,
        registration_number: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Registration:
        """
        ### Register Company (Asynchronous)

        Register a new company to Business Radar using its identification details. Once
        posted, Business Radar processes the request in the background.

        To check the progress and/or retrieve the final result, you can use the
        [GET /registrations/{registration_id}](/ext/v3/#/ext/ext_v3_registrations_retrieve)
        endpoint.

        If the company is already registered, the existing registration will be
        returned.

        Args:
          company: ### Portfolio Company Detail (Simplified)

              A lightweight data structure for company identification (UUID, DUNS, Name,
              Country).

          customer_reference: Customer reference for the client to understand relationship.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/ext/v3/companies",
            body=maybe_transform(
                {
                    "company": company,
                    "country": country,
                    "customer_reference": customer_reference,
                    "duns_number": duns_number,
                    "primary_name": primary_name,
                    "registration_number": registration_number,
                },
                company_create_params.CompanyCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Registration,
        )

    def retrieve(
        self,
        external_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CompanyRetrieveResponse:
        """
        ### Retrieve Company Information

        Fetch detailed information about a specific company using its `external_id`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not external_id:
            raise ValueError(f"Expected a non-empty value for `external_id` but received {external_id!r}")
        return self._get(
            f"/ext/v3/companies/{external_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CompanyRetrieveResponse,
        )

    def list(
        self,
        *,
        country: SequenceNotStr[str] | Omit = omit,
        duns_number: SequenceNotStr[str] | Omit = omit,
        next_key: str | Omit = omit,
        portfolio_id: SequenceNotStr[str] | Omit = omit,
        query: str | Omit = omit,
        registration_number: SequenceNotStr[str] | Omit = omit,
        website_url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncNextKey[CompanyListResponse]:
        """
        ### Search Companies

        Search for companies across internal and external databases.

        - If `query` and an optional `country` are provided, the search is primarily
          conducted via Dun & Bradstreet.

        - If other filters (like `portfolio_id`) are provided, the search is limited to
          our internal database.

        The results include an `external_id` if the company is already registered in
        Business Radar.

        Args:
          country: ISO 2-letter Country Code (e.g., NL, US)

          duns_number: 9-digit Dun And Bradstreet Number (can be multiple)

          next_key: A cursor value used for pagination. Include the `next_key` value from your
              previous request to retrieve the subsequent page of results. If this value is
              `null`, the first page of results is returned.

          portfolio_id: Filter companies belonging to specific Portfolio IDs (UUID)

          query: Custom search query to text search all companies.

          registration_number: Local Registration Number (can be multiple)

          website_url: Website URL to search for the company

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/ext/v3/companies",
            page=SyncNextKey[CompanyListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "country": country,
                        "duns_number": duns_number,
                        "next_key": next_key,
                        "portfolio_id": portfolio_id,
                        "query": query,
                        "registration_number": registration_number,
                        "website_url": website_url,
                    },
                    company_list_params.CompanyListParams,
                ),
            ),
            model=CompanyListResponse,
        )

    def create_missing_company_investigation(
        self,
        *,
        country: CountryEnum,
        legal_name: str,
        address_number: Optional[str] | Omit = omit,
        address_phone: Optional[str] | Omit = omit,
        address_place: Optional[str] | Omit = omit,
        address_postal: Optional[str] | Omit = omit,
        address_region: Optional[str] | Omit = omit,
        address_street: Optional[str] | Omit = omit,
        description: Optional[str] | Omit = omit,
        officer_name: Optional[str] | Omit = omit,
        officer_title: Optional[str] | Omit = omit,
        trade_name: Optional[str] | Omit = omit,
        website_url: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CompanyCreateMissingCompanyInvestigationResponse:
        """
        ### Submit Missing Company Investigation (Asynchronous)

        Submit a new investigation for a company that could not be found. Once
        submitted, Business Radar processes the investigation in the background.

        To check the progress and/or retrieve the final result, you can use the GET
        endpoint.

        Args:
          country: - `AF` - Afghanistan
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

          legal_name: Official name of the company as registered in legal documents.

          address_phone: Phone number should include international code prefix, e.g., +31.

          description: Any additional notes or details about the company.

          officer_name: Name of the primary officer or CEO of the company.

          officer_title: Title or position of the named officer in the company.

          trade_name: Alternate name the company might use in its operations, distinct from the legal
              name.

          website_url: Provide the official website of the company if available.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/ext/v3/companies/investigations",
            body=maybe_transform(
                {
                    "country": country,
                    "legal_name": legal_name,
                    "address_number": address_number,
                    "address_phone": address_phone,
                    "address_place": address_place,
                    "address_postal": address_postal,
                    "address_region": address_region,
                    "address_street": address_street,
                    "description": description,
                    "officer_name": officer_name,
                    "officer_title": officer_title,
                    "trade_name": trade_name,
                    "website_url": website_url,
                },
                company_create_missing_company_investigation_params.CompanyCreateMissingCompanyInvestigationParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CompanyCreateMissingCompanyInvestigationResponse,
        )

    def list_attribute_changes(
        self,
        *,
        max_created_at: Union[str, datetime] | Omit = omit,
        min_created_at: Union[str, datetime] | Omit = omit,
        next_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncNextKey[CompanyListAttributeChangesResponse]:
        """### List Company Updates

        Retrieve a list of attribute changes for companies.

        This allows monitoring how
        company data has evolved over time.

        Args:
          max_created_at: Filter updates created at or before this time.

          min_created_at: Filter updates created at or after this time.

          next_key: A cursor value used for pagination. Include the `next_key` value from your
              previous request to retrieve the subsequent page of results. If this value is
              `null`, the first page of results is returned.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/ext/v3/companies/attribute_changes",
            page=SyncNextKey[CompanyListAttributeChangesResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "max_created_at": max_created_at,
                        "min_created_at": min_created_at,
                        "next_key": next_key,
                    },
                    company_list_attribute_changes_params.CompanyListAttributeChangesParams,
                ),
            ),
            model=CompanyListAttributeChangesResponse,
        )

    def list_missing_company_investigations(
        self,
        *,
        next_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncNextKey[CompanyListMissingCompanyInvestigationsResponse]:
        """
        ### Missing Company Investigations

        List existing investigations or submit a new one for a company that could not be
        found.

        Args:
          next_key: A cursor value used for pagination. Include the `next_key` value from your
              previous request to retrieve the subsequent page of results. If this value is
              `null`, the first page of results is returned.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/ext/v3/companies/investigations",
            page=SyncNextKey[CompanyListMissingCompanyInvestigationsResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"next_key": next_key},
                    company_list_missing_company_investigations_params.CompanyListMissingCompanyInvestigationsParams,
                ),
            ),
            model=CompanyListMissingCompanyInvestigationsResponse,
        )

    def retrieve_missing_company_investigation(
        self,
        external_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CompanyRetrieveMissingCompanyInvestigationResponse:
        """
        ### Retrieve Missing Company Investigation

        Fetch details about a specific missing company investigation using its
        `external_id`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not external_id:
            raise ValueError(f"Expected a non-empty value for `external_id` but received {external_id!r}")
        return self._get(
            f"/ext/v3/companies/investigations/{external_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CompanyRetrieveMissingCompanyInvestigationResponse,
        )

    def retrieve_registration(
        self,
        registration_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Registration:
        """
        ### Retrieve Registration Information

        Fetch details about a specific company registration request using its
        `registration_id`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not registration_id:
            raise ValueError(f"Expected a non-empty value for `registration_id` but received {registration_id!r}")
        return self._get(
            f"/ext/v3/registrations/{registration_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Registration,
        )


class AsyncCompaniesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCompaniesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/businessradar/businessradar-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCompaniesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCompaniesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/businessradar/businessradar-sdk-python#with_streaming_response
        """
        return AsyncCompaniesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        company: Optional[PortfolioCompanyDetailRequest] | Omit = omit,
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
        ]
        | Omit = omit,
        customer_reference: Optional[str] | Omit = omit,
        duns_number: Optional[str] | Omit = omit,
        primary_name: Optional[str] | Omit = omit,
        registration_number: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Registration:
        """
        ### Register Company (Asynchronous)

        Register a new company to Business Radar using its identification details. Once
        posted, Business Radar processes the request in the background.

        To check the progress and/or retrieve the final result, you can use the
        [GET /registrations/{registration_id}](/ext/v3/#/ext/ext_v3_registrations_retrieve)
        endpoint.

        If the company is already registered, the existing registration will be
        returned.

        Args:
          company: ### Portfolio Company Detail (Simplified)

              A lightweight data structure for company identification (UUID, DUNS, Name,
              Country).

          customer_reference: Customer reference for the client to understand relationship.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/ext/v3/companies",
            body=await async_maybe_transform(
                {
                    "company": company,
                    "country": country,
                    "customer_reference": customer_reference,
                    "duns_number": duns_number,
                    "primary_name": primary_name,
                    "registration_number": registration_number,
                },
                company_create_params.CompanyCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Registration,
        )

    async def retrieve(
        self,
        external_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CompanyRetrieveResponse:
        """
        ### Retrieve Company Information

        Fetch detailed information about a specific company using its `external_id`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not external_id:
            raise ValueError(f"Expected a non-empty value for `external_id` but received {external_id!r}")
        return await self._get(
            f"/ext/v3/companies/{external_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CompanyRetrieveResponse,
        )

    def list(
        self,
        *,
        country: SequenceNotStr[str] | Omit = omit,
        duns_number: SequenceNotStr[str] | Omit = omit,
        next_key: str | Omit = omit,
        portfolio_id: SequenceNotStr[str] | Omit = omit,
        query: str | Omit = omit,
        registration_number: SequenceNotStr[str] | Omit = omit,
        website_url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[CompanyListResponse, AsyncNextKey[CompanyListResponse]]:
        """
        ### Search Companies

        Search for companies across internal and external databases.

        - If `query` and an optional `country` are provided, the search is primarily
          conducted via Dun & Bradstreet.

        - If other filters (like `portfolio_id`) are provided, the search is limited to
          our internal database.

        The results include an `external_id` if the company is already registered in
        Business Radar.

        Args:
          country: ISO 2-letter Country Code (e.g., NL, US)

          duns_number: 9-digit Dun And Bradstreet Number (can be multiple)

          next_key: A cursor value used for pagination. Include the `next_key` value from your
              previous request to retrieve the subsequent page of results. If this value is
              `null`, the first page of results is returned.

          portfolio_id: Filter companies belonging to specific Portfolio IDs (UUID)

          query: Custom search query to text search all companies.

          registration_number: Local Registration Number (can be multiple)

          website_url: Website URL to search for the company

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/ext/v3/companies",
            page=AsyncNextKey[CompanyListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "country": country,
                        "duns_number": duns_number,
                        "next_key": next_key,
                        "portfolio_id": portfolio_id,
                        "query": query,
                        "registration_number": registration_number,
                        "website_url": website_url,
                    },
                    company_list_params.CompanyListParams,
                ),
            ),
            model=CompanyListResponse,
        )

    async def create_missing_company_investigation(
        self,
        *,
        country: CountryEnum,
        legal_name: str,
        address_number: Optional[str] | Omit = omit,
        address_phone: Optional[str] | Omit = omit,
        address_place: Optional[str] | Omit = omit,
        address_postal: Optional[str] | Omit = omit,
        address_region: Optional[str] | Omit = omit,
        address_street: Optional[str] | Omit = omit,
        description: Optional[str] | Omit = omit,
        officer_name: Optional[str] | Omit = omit,
        officer_title: Optional[str] | Omit = omit,
        trade_name: Optional[str] | Omit = omit,
        website_url: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CompanyCreateMissingCompanyInvestigationResponse:
        """
        ### Submit Missing Company Investigation (Asynchronous)

        Submit a new investigation for a company that could not be found. Once
        submitted, Business Radar processes the investigation in the background.

        To check the progress and/or retrieve the final result, you can use the GET
        endpoint.

        Args:
          country: - `AF` - Afghanistan
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

          legal_name: Official name of the company as registered in legal documents.

          address_phone: Phone number should include international code prefix, e.g., +31.

          description: Any additional notes or details about the company.

          officer_name: Name of the primary officer or CEO of the company.

          officer_title: Title or position of the named officer in the company.

          trade_name: Alternate name the company might use in its operations, distinct from the legal
              name.

          website_url: Provide the official website of the company if available.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/ext/v3/companies/investigations",
            body=await async_maybe_transform(
                {
                    "country": country,
                    "legal_name": legal_name,
                    "address_number": address_number,
                    "address_phone": address_phone,
                    "address_place": address_place,
                    "address_postal": address_postal,
                    "address_region": address_region,
                    "address_street": address_street,
                    "description": description,
                    "officer_name": officer_name,
                    "officer_title": officer_title,
                    "trade_name": trade_name,
                    "website_url": website_url,
                },
                company_create_missing_company_investigation_params.CompanyCreateMissingCompanyInvestigationParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CompanyCreateMissingCompanyInvestigationResponse,
        )

    def list_attribute_changes(
        self,
        *,
        max_created_at: Union[str, datetime] | Omit = omit,
        min_created_at: Union[str, datetime] | Omit = omit,
        next_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[CompanyListAttributeChangesResponse, AsyncNextKey[CompanyListAttributeChangesResponse]]:
        """### List Company Updates

        Retrieve a list of attribute changes for companies.

        This allows monitoring how
        company data has evolved over time.

        Args:
          max_created_at: Filter updates created at or before this time.

          min_created_at: Filter updates created at or after this time.

          next_key: A cursor value used for pagination. Include the `next_key` value from your
              previous request to retrieve the subsequent page of results. If this value is
              `null`, the first page of results is returned.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/ext/v3/companies/attribute_changes",
            page=AsyncNextKey[CompanyListAttributeChangesResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "max_created_at": max_created_at,
                        "min_created_at": min_created_at,
                        "next_key": next_key,
                    },
                    company_list_attribute_changes_params.CompanyListAttributeChangesParams,
                ),
            ),
            model=CompanyListAttributeChangesResponse,
        )

    def list_missing_company_investigations(
        self,
        *,
        next_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[
        CompanyListMissingCompanyInvestigationsResponse, AsyncNextKey[CompanyListMissingCompanyInvestigationsResponse]
    ]:
        """
        ### Missing Company Investigations

        List existing investigations or submit a new one for a company that could not be
        found.

        Args:
          next_key: A cursor value used for pagination. Include the `next_key` value from your
              previous request to retrieve the subsequent page of results. If this value is
              `null`, the first page of results is returned.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/ext/v3/companies/investigations",
            page=AsyncNextKey[CompanyListMissingCompanyInvestigationsResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"next_key": next_key},
                    company_list_missing_company_investigations_params.CompanyListMissingCompanyInvestigationsParams,
                ),
            ),
            model=CompanyListMissingCompanyInvestigationsResponse,
        )

    async def retrieve_missing_company_investigation(
        self,
        external_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CompanyRetrieveMissingCompanyInvestigationResponse:
        """
        ### Retrieve Missing Company Investigation

        Fetch details about a specific missing company investigation using its
        `external_id`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not external_id:
            raise ValueError(f"Expected a non-empty value for `external_id` but received {external_id!r}")
        return await self._get(
            f"/ext/v3/companies/investigations/{external_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CompanyRetrieveMissingCompanyInvestigationResponse,
        )

    async def retrieve_registration(
        self,
        registration_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Registration:
        """
        ### Retrieve Registration Information

        Fetch details about a specific company registration request using its
        `registration_id`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not registration_id:
            raise ValueError(f"Expected a non-empty value for `registration_id` but received {registration_id!r}")
        return await self._get(
            f"/ext/v3/registrations/{registration_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Registration,
        )


class CompaniesResourceWithRawResponse:
    def __init__(self, companies: CompaniesResource) -> None:
        self._companies = companies

        self.create = to_raw_response_wrapper(
            companies.create,
        )
        self.retrieve = to_raw_response_wrapper(
            companies.retrieve,
        )
        self.list = to_raw_response_wrapper(
            companies.list,
        )
        self.create_missing_company_investigation = to_raw_response_wrapper(
            companies.create_missing_company_investigation,
        )
        self.list_attribute_changes = to_raw_response_wrapper(
            companies.list_attribute_changes,
        )
        self.list_missing_company_investigations = to_raw_response_wrapper(
            companies.list_missing_company_investigations,
        )
        self.retrieve_missing_company_investigation = to_raw_response_wrapper(
            companies.retrieve_missing_company_investigation,
        )
        self.retrieve_registration = to_raw_response_wrapper(
            companies.retrieve_registration,
        )


class AsyncCompaniesResourceWithRawResponse:
    def __init__(self, companies: AsyncCompaniesResource) -> None:
        self._companies = companies

        self.create = async_to_raw_response_wrapper(
            companies.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            companies.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            companies.list,
        )
        self.create_missing_company_investigation = async_to_raw_response_wrapper(
            companies.create_missing_company_investigation,
        )
        self.list_attribute_changes = async_to_raw_response_wrapper(
            companies.list_attribute_changes,
        )
        self.list_missing_company_investigations = async_to_raw_response_wrapper(
            companies.list_missing_company_investigations,
        )
        self.retrieve_missing_company_investigation = async_to_raw_response_wrapper(
            companies.retrieve_missing_company_investigation,
        )
        self.retrieve_registration = async_to_raw_response_wrapper(
            companies.retrieve_registration,
        )


class CompaniesResourceWithStreamingResponse:
    def __init__(self, companies: CompaniesResource) -> None:
        self._companies = companies

        self.create = to_streamed_response_wrapper(
            companies.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            companies.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            companies.list,
        )
        self.create_missing_company_investigation = to_streamed_response_wrapper(
            companies.create_missing_company_investigation,
        )
        self.list_attribute_changes = to_streamed_response_wrapper(
            companies.list_attribute_changes,
        )
        self.list_missing_company_investigations = to_streamed_response_wrapper(
            companies.list_missing_company_investigations,
        )
        self.retrieve_missing_company_investigation = to_streamed_response_wrapper(
            companies.retrieve_missing_company_investigation,
        )
        self.retrieve_registration = to_streamed_response_wrapper(
            companies.retrieve_registration,
        )


class AsyncCompaniesResourceWithStreamingResponse:
    def __init__(self, companies: AsyncCompaniesResource) -> None:
        self._companies = companies

        self.create = async_to_streamed_response_wrapper(
            companies.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            companies.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            companies.list,
        )
        self.create_missing_company_investigation = async_to_streamed_response_wrapper(
            companies.create_missing_company_investigation,
        )
        self.list_attribute_changes = async_to_streamed_response_wrapper(
            companies.list_attribute_changes,
        )
        self.list_missing_company_investigations = async_to_streamed_response_wrapper(
            companies.list_missing_company_investigations,
        )
        self.retrieve_missing_company_investigation = async_to_streamed_response_wrapper(
            companies.retrieve_missing_company_investigation,
        )
        self.retrieve_registration = async_to_streamed_response_wrapper(
            companies.retrieve_registration,
        )
