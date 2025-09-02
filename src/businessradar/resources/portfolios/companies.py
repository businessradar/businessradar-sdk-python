# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import SyncNextKey, AsyncNextKey
from ..._base_client import AsyncPaginator, make_request_options
from ...types.portfolios import company_list_params, company_create_params
from ...types.registration import Registration
from ...types.portfolios.company_list_response import CompanyListResponse
from ...types.shared_params.portfolio_company_detail_request import PortfolioCompanyDetailRequest

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
        portfolio_id: str,
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
        Register a new Portfolio Company.

        Args:
          company: Portfolio Company Detail Serializer.

              Alternative serializer for the Company model which is limited.

          customer_reference: Customer reference for the client to understand relationship.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not portfolio_id:
            raise ValueError(f"Expected a non-empty value for `portfolio_id` but received {portfolio_id!r}")
        return self._post(
            f"/ext/v3/portfolios/{portfolio_id}/companies",
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

    def list(
        self,
        portfolio_id: str,
        *,
        next_key: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncNextKey[CompanyListResponse]:
        """
        List And Create Portfolio Companies.

        Args:
          next_key: The next_key is an cursor used to make it possible to paginate to the next
              results, pass the next_key from the previous request to retrieve next results.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not portfolio_id:
            raise ValueError(f"Expected a non-empty value for `portfolio_id` but received {portfolio_id!r}")
        return self._get_api_list(
            f"/ext/v3/portfolios/{portfolio_id}/companies",
            page=SyncNextKey[CompanyListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"next_key": next_key}, company_list_params.CompanyListParams),
            ),
            model=CompanyListResponse,
        )

    def delete(
        self,
        external_id: str,
        *,
        portfolio_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Remove Portfolio Companies.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not portfolio_id:
            raise ValueError(f"Expected a non-empty value for `portfolio_id` but received {portfolio_id!r}")
        if not external_id:
            raise ValueError(f"Expected a non-empty value for `external_id` but received {external_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/ext/v3/portfolios/{portfolio_id}/companies/{external_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
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
        portfolio_id: str,
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
        Register a new Portfolio Company.

        Args:
          company: Portfolio Company Detail Serializer.

              Alternative serializer for the Company model which is limited.

          customer_reference: Customer reference for the client to understand relationship.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not portfolio_id:
            raise ValueError(f"Expected a non-empty value for `portfolio_id` but received {portfolio_id!r}")
        return await self._post(
            f"/ext/v3/portfolios/{portfolio_id}/companies",
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

    def list(
        self,
        portfolio_id: str,
        *,
        next_key: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[CompanyListResponse, AsyncNextKey[CompanyListResponse]]:
        """
        List And Create Portfolio Companies.

        Args:
          next_key: The next_key is an cursor used to make it possible to paginate to the next
              results, pass the next_key from the previous request to retrieve next results.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not portfolio_id:
            raise ValueError(f"Expected a non-empty value for `portfolio_id` but received {portfolio_id!r}")
        return self._get_api_list(
            f"/ext/v3/portfolios/{portfolio_id}/companies",
            page=AsyncNextKey[CompanyListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"next_key": next_key}, company_list_params.CompanyListParams),
            ),
            model=CompanyListResponse,
        )

    async def delete(
        self,
        external_id: str,
        *,
        portfolio_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Remove Portfolio Companies.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not portfolio_id:
            raise ValueError(f"Expected a non-empty value for `portfolio_id` but received {portfolio_id!r}")
        if not external_id:
            raise ValueError(f"Expected a non-empty value for `external_id` but received {external_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/ext/v3/portfolios/{portfolio_id}/companies/{external_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class CompaniesResourceWithRawResponse:
    def __init__(self, companies: CompaniesResource) -> None:
        self._companies = companies

        self.create = to_raw_response_wrapper(
            companies.create,
        )
        self.list = to_raw_response_wrapper(
            companies.list,
        )
        self.delete = to_raw_response_wrapper(
            companies.delete,
        )


class AsyncCompaniesResourceWithRawResponse:
    def __init__(self, companies: AsyncCompaniesResource) -> None:
        self._companies = companies

        self.create = async_to_raw_response_wrapper(
            companies.create,
        )
        self.list = async_to_raw_response_wrapper(
            companies.list,
        )
        self.delete = async_to_raw_response_wrapper(
            companies.delete,
        )


class CompaniesResourceWithStreamingResponse:
    def __init__(self, companies: CompaniesResource) -> None:
        self._companies = companies

        self.create = to_streamed_response_wrapper(
            companies.create,
        )
        self.list = to_streamed_response_wrapper(
            companies.list,
        )
        self.delete = to_streamed_response_wrapper(
            companies.delete,
        )


class AsyncCompaniesResourceWithStreamingResponse:
    def __init__(self, companies: AsyncCompaniesResource) -> None:
        self._companies = companies

        self.create = async_to_streamed_response_wrapper(
            companies.create,
        )
        self.list = async_to_streamed_response_wrapper(
            companies.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            companies.delete,
        )
