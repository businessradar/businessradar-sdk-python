# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal

import httpx

from ..types import company_list_params, company_create_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
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
from ..types.registration import Registration
from ..types.company_list_response import CompanyListResponse
from ..types.company_retrieve_response import CompanyRetrieveResponse
from ..types.shared_params.portfolio_company_detail_request import PortfolioCompanyDetailRequest

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
        company: Optional[PortfolioCompanyDetailRequest] | NotGiven = NOT_GIVEN,
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
        | NotGiven = NOT_GIVEN,
        customer_reference: Optional[str] | NotGiven = NOT_GIVEN,
        duns_number: Optional[str] | NotGiven = NOT_GIVEN,
        primary_name: Optional[str] | NotGiven = NOT_GIVEN,
        registration_number: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Registration:
        """
        Register new Company to Business Radar.

        Args:
          company: Portfolio Company Detail Serializer.

              Alternative serializer for the Company model which is limited.

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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CompanyRetrieveResponse:
        """
        Get Company Information.

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
        country: List[str] | NotGiven = NOT_GIVEN,
        duns_number: List[str] | NotGiven = NOT_GIVEN,
        next_key: str | NotGiven = NOT_GIVEN,
        portfolio_id: List[str] | NotGiven = NOT_GIVEN,
        query: str | NotGiven = NOT_GIVEN,
        registration_number: List[str] | NotGiven = NOT_GIVEN,
        website_url: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncNextKey[CompanyListResponse]:
        """
        Search all companies using Dun and Bradstreet.

        Companies will contain an optional external_id, which is null if company is not
        registered in Business Radar.

        When you pass query and optional country it will search using dun and
        bradstreet, otherwise using internal search.

        Args:
          country: ISO 2-letter Country Code

          duns_number: 9-digit Dun And Bradstreet Number

          next_key: The next_key is an cursor used to make it possible to paginate to the next
              results, pass the next_key from the previous request to retrieve next results.

          portfolio_id: Portfolio ID to filter companies

          query: Custom search query to text search all companies.

          registration_number: Local Registration Number

          website_url: Website URL to search

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

    def retrieve_registration(
        self,
        registration_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Registration:
        """
        Get Registration Information.

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
        company: Optional[PortfolioCompanyDetailRequest] | NotGiven = NOT_GIVEN,
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
        | NotGiven = NOT_GIVEN,
        customer_reference: Optional[str] | NotGiven = NOT_GIVEN,
        duns_number: Optional[str] | NotGiven = NOT_GIVEN,
        primary_name: Optional[str] | NotGiven = NOT_GIVEN,
        registration_number: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Registration:
        """
        Register new Company to Business Radar.

        Args:
          company: Portfolio Company Detail Serializer.

              Alternative serializer for the Company model which is limited.

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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CompanyRetrieveResponse:
        """
        Get Company Information.

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
        country: List[str] | NotGiven = NOT_GIVEN,
        duns_number: List[str] | NotGiven = NOT_GIVEN,
        next_key: str | NotGiven = NOT_GIVEN,
        portfolio_id: List[str] | NotGiven = NOT_GIVEN,
        query: str | NotGiven = NOT_GIVEN,
        registration_number: List[str] | NotGiven = NOT_GIVEN,
        website_url: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[CompanyListResponse, AsyncNextKey[CompanyListResponse]]:
        """
        Search all companies using Dun and Bradstreet.

        Companies will contain an optional external_id, which is null if company is not
        registered in Business Radar.

        When you pass query and optional country it will search using dun and
        bradstreet, otherwise using internal search.

        Args:
          country: ISO 2-letter Country Code

          duns_number: 9-digit Dun And Bradstreet Number

          next_key: The next_key is an cursor used to make it possible to paginate to the next
              results, pass the next_key from the previous request to retrieve next results.

          portfolio_id: Portfolio ID to filter companies

          query: Custom search query to text search all companies.

          registration_number: Local Registration Number

          website_url: Website URL to search

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

    async def retrieve_registration(
        self,
        registration_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Registration:
        """
        Get Registration Information.

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
        self.retrieve_registration = async_to_streamed_response_wrapper(
            companies.retrieve_registration,
        )
