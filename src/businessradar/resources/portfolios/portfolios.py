# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

import httpx

from ...types import portfolio_list_params, portfolio_create_params
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from .companies import (
    CompaniesResource,
    AsyncCompaniesResource,
    CompaniesResourceWithRawResponse,
    AsyncCompaniesResourceWithRawResponse,
    CompaniesResourceWithStreamingResponse,
    AsyncCompaniesResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.portfolio import Portfolio
from ...types.portfolio_list_response import PortfolioListResponse

__all__ = ["PortfoliosResource", "AsyncPortfoliosResource"]


class PortfoliosResource(SyncAPIResource):
    @cached_property
    def companies(self) -> CompaniesResource:
        return CompaniesResource(self._client)

    @cached_property
    def with_raw_response(self) -> PortfoliosResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/businessradar/businessradar-sdk-python#accessing-raw-response-data-eg-headers
        """
        return PortfoliosResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PortfoliosResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/businessradar/businessradar-sdk-python#with_streaming_response
        """
        return PortfoliosResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        customer_reference: Optional[str] | NotGiven = NOT_GIVEN,
        default_permission: Optional[Literal["view_only", "write", "admin", "owner", ""]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Portfolio:
        """
        List Create Portfolio.

        Args:
          customer_reference: Customer reference for the client to understand relationship.

          default_permission: Default permission for all users in organization.

              - `view_only` - Only Viewing Access
              - `write` - View and Write Access
              - `admin` - View, Write and Admin Access
              - `owner` - Portfolio Owner

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/ext/v3/portfolios",
            body=maybe_transform(
                {
                    "name": name,
                    "customer_reference": customer_reference,
                    "default_permission": default_permission,
                },
                portfolio_create_params.PortfolioCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Portfolio,
        )

    def list(
        self,
        *,
        next_key: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PortfolioListResponse:
        """
        List Create Portfolio.

        Args:
          next_key: The next_key is an cursor used to make it possible to paginate to the next
              results, pass the next_key from the previous request to retrieve next results.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/ext/v3/portfolios",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"next_key": next_key}, portfolio_list_params.PortfolioListParams),
            ),
            cast_to=PortfolioListResponse,
        )


class AsyncPortfoliosResource(AsyncAPIResource):
    @cached_property
    def companies(self) -> AsyncCompaniesResource:
        return AsyncCompaniesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncPortfoliosResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/businessradar/businessradar-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPortfoliosResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPortfoliosResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/businessradar/businessradar-sdk-python#with_streaming_response
        """
        return AsyncPortfoliosResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        customer_reference: Optional[str] | NotGiven = NOT_GIVEN,
        default_permission: Optional[Literal["view_only", "write", "admin", "owner", ""]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Portfolio:
        """
        List Create Portfolio.

        Args:
          customer_reference: Customer reference for the client to understand relationship.

          default_permission: Default permission for all users in organization.

              - `view_only` - Only Viewing Access
              - `write` - View and Write Access
              - `admin` - View, Write and Admin Access
              - `owner` - Portfolio Owner

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/ext/v3/portfolios",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "customer_reference": customer_reference,
                    "default_permission": default_permission,
                },
                portfolio_create_params.PortfolioCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Portfolio,
        )

    async def list(
        self,
        *,
        next_key: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PortfolioListResponse:
        """
        List Create Portfolio.

        Args:
          next_key: The next_key is an cursor used to make it possible to paginate to the next
              results, pass the next_key from the previous request to retrieve next results.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/ext/v3/portfolios",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"next_key": next_key}, portfolio_list_params.PortfolioListParams),
            ),
            cast_to=PortfolioListResponse,
        )


class PortfoliosResourceWithRawResponse:
    def __init__(self, portfolios: PortfoliosResource) -> None:
        self._portfolios = portfolios

        self.create = to_raw_response_wrapper(
            portfolios.create,
        )
        self.list = to_raw_response_wrapper(
            portfolios.list,
        )

    @cached_property
    def companies(self) -> CompaniesResourceWithRawResponse:
        return CompaniesResourceWithRawResponse(self._portfolios.companies)


class AsyncPortfoliosResourceWithRawResponse:
    def __init__(self, portfolios: AsyncPortfoliosResource) -> None:
        self._portfolios = portfolios

        self.create = async_to_raw_response_wrapper(
            portfolios.create,
        )
        self.list = async_to_raw_response_wrapper(
            portfolios.list,
        )

    @cached_property
    def companies(self) -> AsyncCompaniesResourceWithRawResponse:
        return AsyncCompaniesResourceWithRawResponse(self._portfolios.companies)


class PortfoliosResourceWithStreamingResponse:
    def __init__(self, portfolios: PortfoliosResource) -> None:
        self._portfolios = portfolios

        self.create = to_streamed_response_wrapper(
            portfolios.create,
        )
        self.list = to_streamed_response_wrapper(
            portfolios.list,
        )

    @cached_property
    def companies(self) -> CompaniesResourceWithStreamingResponse:
        return CompaniesResourceWithStreamingResponse(self._portfolios.companies)


class AsyncPortfoliosResourceWithStreamingResponse:
    def __init__(self, portfolios: AsyncPortfoliosResource) -> None:
        self._portfolios = portfolios

        self.create = async_to_streamed_response_wrapper(
            portfolios.create,
        )
        self.list = async_to_streamed_response_wrapper(
            portfolios.list,
        )

    @cached_property
    def companies(self) -> AsyncCompaniesResourceWithStreamingResponse:
        return AsyncCompaniesResourceWithStreamingResponse(self._portfolios.companies)
