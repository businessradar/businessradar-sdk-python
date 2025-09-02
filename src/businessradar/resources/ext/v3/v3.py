# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import maybe_transform, async_maybe_transform
from .companies import (
    CompaniesResource,
    AsyncCompaniesResource,
    CompaniesResourceWithRawResponse,
    AsyncCompaniesResourceWithRawResponse,
    CompaniesResourceWithStreamingResponse,
    AsyncCompaniesResourceWithStreamingResponse,
)
from ...._compat import cached_property
from .compliance import (
    ComplianceResource,
    AsyncComplianceResource,
    ComplianceResourceWithRawResponse,
    AsyncComplianceResourceWithRawResponse,
    ComplianceResourceWithStreamingResponse,
    AsyncComplianceResourceWithStreamingResponse,
)
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....types.ext import v3_get_schema_params, v3_list_saved_article_filters_params
from ...._base_client import make_request_options
from .articles.articles import (
    ArticlesResource,
    AsyncArticlesResource,
    ArticlesResourceWithRawResponse,
    AsyncArticlesResourceWithRawResponse,
    ArticlesResourceWithStreamingResponse,
    AsyncArticlesResourceWithStreamingResponse,
)
from .portfolios.portfolios import (
    PortfoliosResource,
    AsyncPortfoliosResource,
    PortfoliosResourceWithRawResponse,
    AsyncPortfoliosResourceWithRawResponse,
    PortfoliosResourceWithStreamingResponse,
    AsyncPortfoliosResourceWithStreamingResponse,
)
from ....types.ext.v3.registration import Registration
from ....types.ext.v3_get_schema_response import V3GetSchemaResponse
from ....types.ext.v3_list_saved_article_filters_response import V3ListSavedArticleFiltersResponse

__all__ = ["V3Resource", "AsyncV3Resource"]


class V3Resource(SyncAPIResource):
    @cached_property
    def articles(self) -> ArticlesResource:
        return ArticlesResource(self._client)

    @cached_property
    def companies(self) -> CompaniesResource:
        return CompaniesResource(self._client)

    @cached_property
    def compliance(self) -> ComplianceResource:
        return ComplianceResource(self._client)

    @cached_property
    def portfolios(self) -> PortfoliosResource:
        return PortfoliosResource(self._client)

    @cached_property
    def with_raw_response(self) -> V3ResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/businessradar-python#accessing-raw-response-data-eg-headers
        """
        return V3ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> V3ResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/businessradar-python#with_streaming_response
        """
        return V3ResourceWithStreamingResponse(self)

    def get_registration(
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

    def get_schema(
        self,
        *,
        format: Literal["json", "yaml"] | NotGiven = NOT_GIVEN,
        lang: Literal[
            "af",
            "ar",
            "az",
            "be",
            "bg",
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
            "no",
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
        ]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V3GetSchemaResponse:
        """OpenApi3 schema for this API.

        Format can be selected via content negotiation.

        - YAML: application/vnd.oai.openapi
        - JSON: application/vnd.oai.openapi+json

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/ext/v3/schema",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "format": format,
                        "lang": lang,
                    },
                    v3_get_schema_params.V3GetSchemaParams,
                ),
            ),
            cast_to=V3GetSchemaResponse,
        )

    def list_saved_article_filters(
        self,
        *,
        next_key: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V3ListSavedArticleFiltersResponse:
        """
        List Create Saved Article Filter.

        Args:
          next_key: The next_key is an cursor used to make it possible to paginate to the next
              results, pass the next_key from the previous request to retrieve next results.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/ext/v3/saved_article_filters",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"next_key": next_key}, v3_list_saved_article_filters_params.V3ListSavedArticleFiltersParams
                ),
            ),
            cast_to=V3ListSavedArticleFiltersResponse,
        )


class AsyncV3Resource(AsyncAPIResource):
    @cached_property
    def articles(self) -> AsyncArticlesResource:
        return AsyncArticlesResource(self._client)

    @cached_property
    def companies(self) -> AsyncCompaniesResource:
        return AsyncCompaniesResource(self._client)

    @cached_property
    def compliance(self) -> AsyncComplianceResource:
        return AsyncComplianceResource(self._client)

    @cached_property
    def portfolios(self) -> AsyncPortfoliosResource:
        return AsyncPortfoliosResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncV3ResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/businessradar-python#accessing-raw-response-data-eg-headers
        """
        return AsyncV3ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncV3ResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/businessradar-python#with_streaming_response
        """
        return AsyncV3ResourceWithStreamingResponse(self)

    async def get_registration(
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

    async def get_schema(
        self,
        *,
        format: Literal["json", "yaml"] | NotGiven = NOT_GIVEN,
        lang: Literal[
            "af",
            "ar",
            "az",
            "be",
            "bg",
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
            "no",
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
        ]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V3GetSchemaResponse:
        """OpenApi3 schema for this API.

        Format can be selected via content negotiation.

        - YAML: application/vnd.oai.openapi
        - JSON: application/vnd.oai.openapi+json

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/ext/v3/schema",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "format": format,
                        "lang": lang,
                    },
                    v3_get_schema_params.V3GetSchemaParams,
                ),
            ),
            cast_to=V3GetSchemaResponse,
        )

    async def list_saved_article_filters(
        self,
        *,
        next_key: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V3ListSavedArticleFiltersResponse:
        """
        List Create Saved Article Filter.

        Args:
          next_key: The next_key is an cursor used to make it possible to paginate to the next
              results, pass the next_key from the previous request to retrieve next results.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/ext/v3/saved_article_filters",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"next_key": next_key}, v3_list_saved_article_filters_params.V3ListSavedArticleFiltersParams
                ),
            ),
            cast_to=V3ListSavedArticleFiltersResponse,
        )


class V3ResourceWithRawResponse:
    def __init__(self, v3: V3Resource) -> None:
        self._v3 = v3

        self.get_registration = to_raw_response_wrapper(
            v3.get_registration,
        )
        self.get_schema = to_raw_response_wrapper(
            v3.get_schema,
        )
        self.list_saved_article_filters = to_raw_response_wrapper(
            v3.list_saved_article_filters,
        )

    @cached_property
    def articles(self) -> ArticlesResourceWithRawResponse:
        return ArticlesResourceWithRawResponse(self._v3.articles)

    @cached_property
    def companies(self) -> CompaniesResourceWithRawResponse:
        return CompaniesResourceWithRawResponse(self._v3.companies)

    @cached_property
    def compliance(self) -> ComplianceResourceWithRawResponse:
        return ComplianceResourceWithRawResponse(self._v3.compliance)

    @cached_property
    def portfolios(self) -> PortfoliosResourceWithRawResponse:
        return PortfoliosResourceWithRawResponse(self._v3.portfolios)


class AsyncV3ResourceWithRawResponse:
    def __init__(self, v3: AsyncV3Resource) -> None:
        self._v3 = v3

        self.get_registration = async_to_raw_response_wrapper(
            v3.get_registration,
        )
        self.get_schema = async_to_raw_response_wrapper(
            v3.get_schema,
        )
        self.list_saved_article_filters = async_to_raw_response_wrapper(
            v3.list_saved_article_filters,
        )

    @cached_property
    def articles(self) -> AsyncArticlesResourceWithRawResponse:
        return AsyncArticlesResourceWithRawResponse(self._v3.articles)

    @cached_property
    def companies(self) -> AsyncCompaniesResourceWithRawResponse:
        return AsyncCompaniesResourceWithRawResponse(self._v3.companies)

    @cached_property
    def compliance(self) -> AsyncComplianceResourceWithRawResponse:
        return AsyncComplianceResourceWithRawResponse(self._v3.compliance)

    @cached_property
    def portfolios(self) -> AsyncPortfoliosResourceWithRawResponse:
        return AsyncPortfoliosResourceWithRawResponse(self._v3.portfolios)


class V3ResourceWithStreamingResponse:
    def __init__(self, v3: V3Resource) -> None:
        self._v3 = v3

        self.get_registration = to_streamed_response_wrapper(
            v3.get_registration,
        )
        self.get_schema = to_streamed_response_wrapper(
            v3.get_schema,
        )
        self.list_saved_article_filters = to_streamed_response_wrapper(
            v3.list_saved_article_filters,
        )

    @cached_property
    def articles(self) -> ArticlesResourceWithStreamingResponse:
        return ArticlesResourceWithStreamingResponse(self._v3.articles)

    @cached_property
    def companies(self) -> CompaniesResourceWithStreamingResponse:
        return CompaniesResourceWithStreamingResponse(self._v3.companies)

    @cached_property
    def compliance(self) -> ComplianceResourceWithStreamingResponse:
        return ComplianceResourceWithStreamingResponse(self._v3.compliance)

    @cached_property
    def portfolios(self) -> PortfoliosResourceWithStreamingResponse:
        return PortfoliosResourceWithStreamingResponse(self._v3.portfolios)


class AsyncV3ResourceWithStreamingResponse:
    def __init__(self, v3: AsyncV3Resource) -> None:
        self._v3 = v3

        self.get_registration = async_to_streamed_response_wrapper(
            v3.get_registration,
        )
        self.get_schema = async_to_streamed_response_wrapper(
            v3.get_schema,
        )
        self.list_saved_article_filters = async_to_streamed_response_wrapper(
            v3.list_saved_article_filters,
        )

    @cached_property
    def articles(self) -> AsyncArticlesResourceWithStreamingResponse:
        return AsyncArticlesResourceWithStreamingResponse(self._v3.articles)

    @cached_property
    def companies(self) -> AsyncCompaniesResourceWithStreamingResponse:
        return AsyncCompaniesResourceWithStreamingResponse(self._v3.companies)

    @cached_property
    def compliance(self) -> AsyncComplianceResourceWithStreamingResponse:
        return AsyncComplianceResourceWithStreamingResponse(self._v3.compliance)

    @cached_property
    def portfolios(self) -> AsyncPortfoliosResourceWithStreamingResponse:
        return AsyncPortfoliosResourceWithStreamingResponse(self._v3.portfolios)
