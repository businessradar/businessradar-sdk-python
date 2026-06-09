# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.news.articles import analytics_get_count_by_date_params
from ....types.news.articles.analytics_get_count_by_date_response import AnalyticsGetCountByDateResponse

__all__ = ["AnalyticsResource", "AsyncAnalyticsResource"]


class AnalyticsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AnalyticsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/businessradar/businessradar-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AnalyticsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AnalyticsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/businessradar/businessradar-sdk-python#with_streaming_response
        """
        return AnalyticsResourceWithStreamingResponse(self)

    def get_count_by_date(
        self,
        *,
        category: SequenceNotStr[str] | Omit = omit,
        company: SequenceNotStr[str] | Omit = omit,
        country: SequenceNotStr[str] | Omit = omit,
        disable_company_article_deduplication: bool | Omit = omit,
        duns_number: SequenceNotStr[str] | Omit = omit,
        global_ultimate: SequenceNotStr[str] | Omit = omit,
        include_clustered_articles: bool | Omit = omit,
        interval: Literal["day", "month", "week", "year"] | Omit = omit,
        is_material: bool | Omit = omit,
        language: SequenceNotStr[str] | Omit = omit,
        max_creation_date: Union[str, datetime] | Omit = omit,
        max_publication_date: Union[str, datetime] | Omit = omit,
        min_creation_date: Union[str, datetime] | Omit = omit,
        min_publication_date: Union[str, datetime] | Omit = omit,
        portfolio_id: SequenceNotStr[str] | Omit = omit,
        query: str | Omit = omit,
        registration_number: SequenceNotStr[str] | Omit = omit,
        saved_article_filter_id: str | Omit = omit,
        sentiment: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AnalyticsGetCountByDateResponse:
        """
        ### Get Article Aggregations

        Retrieve the number of articles and their average sentiment, grouped by date.

        Args:
          category: Filter by article Category IDs (UUIDs).

          company: Filter by internal Company UUIDs.

          country: Filter by ISO 2-letter Country Codes (e.g., 'US', 'GB').

          disable_company_article_deduplication: By default, companies with the same trade names are grouped and the best match
              is selected. Enable this to see all associated companies.

          duns_number: Filter by one or more 9-digit Dun & Bradstreet Numbers.

          global_ultimate: Filter by Global Ultimate DUNS Numbers.

          include_clustered_articles: Include articles that are part of a cluster (reprints or similar articles).

          interval: The time interval for aggregation.

          is_material: Filter by materiality flag (relevance to business risk).

          language: Filter by ISO 2-letter Language Codes (e.g., 'en', 'nl').

          max_creation_date: Filter articles added to our database at or before this date/time.

          max_publication_date: Filter articles published at or before this date/time.

          min_creation_date: Filter articles added to our database at or after this date/time.

          min_publication_date: Filter articles published at or after this date/time.

          portfolio_id: Filter articles related to companies in specific Portfolios (UUIDs).

          query: Full-text search query for filtering articles by content.

          registration_number: Filter by local company registration numbers.

          saved_article_filter_id: Apply a previously saved set of article filters (UUID).

          sentiment: Filter by sentiment: `true` for positive, `false` for negative.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/ext/v3/articles/analytics/dates/",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "category": category,
                        "company": company,
                        "country": country,
                        "disable_company_article_deduplication": disable_company_article_deduplication,
                        "duns_number": duns_number,
                        "global_ultimate": global_ultimate,
                        "include_clustered_articles": include_clustered_articles,
                        "interval": interval,
                        "is_material": is_material,
                        "language": language,
                        "max_creation_date": max_creation_date,
                        "max_publication_date": max_publication_date,
                        "min_creation_date": min_creation_date,
                        "min_publication_date": min_publication_date,
                        "portfolio_id": portfolio_id,
                        "query": query,
                        "registration_number": registration_number,
                        "saved_article_filter_id": saved_article_filter_id,
                        "sentiment": sentiment,
                    },
                    analytics_get_count_by_date_params.AnalyticsGetCountByDateParams,
                ),
            ),
            cast_to=AnalyticsGetCountByDateResponse,
        )


class AsyncAnalyticsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAnalyticsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/businessradar/businessradar-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAnalyticsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAnalyticsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/businessradar/businessradar-sdk-python#with_streaming_response
        """
        return AsyncAnalyticsResourceWithStreamingResponse(self)

    async def get_count_by_date(
        self,
        *,
        category: SequenceNotStr[str] | Omit = omit,
        company: SequenceNotStr[str] | Omit = omit,
        country: SequenceNotStr[str] | Omit = omit,
        disable_company_article_deduplication: bool | Omit = omit,
        duns_number: SequenceNotStr[str] | Omit = omit,
        global_ultimate: SequenceNotStr[str] | Omit = omit,
        include_clustered_articles: bool | Omit = omit,
        interval: Literal["day", "month", "week", "year"] | Omit = omit,
        is_material: bool | Omit = omit,
        language: SequenceNotStr[str] | Omit = omit,
        max_creation_date: Union[str, datetime] | Omit = omit,
        max_publication_date: Union[str, datetime] | Omit = omit,
        min_creation_date: Union[str, datetime] | Omit = omit,
        min_publication_date: Union[str, datetime] | Omit = omit,
        portfolio_id: SequenceNotStr[str] | Omit = omit,
        query: str | Omit = omit,
        registration_number: SequenceNotStr[str] | Omit = omit,
        saved_article_filter_id: str | Omit = omit,
        sentiment: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AnalyticsGetCountByDateResponse:
        """
        ### Get Article Aggregations

        Retrieve the number of articles and their average sentiment, grouped by date.

        Args:
          category: Filter by article Category IDs (UUIDs).

          company: Filter by internal Company UUIDs.

          country: Filter by ISO 2-letter Country Codes (e.g., 'US', 'GB').

          disable_company_article_deduplication: By default, companies with the same trade names are grouped and the best match
              is selected. Enable this to see all associated companies.

          duns_number: Filter by one or more 9-digit Dun & Bradstreet Numbers.

          global_ultimate: Filter by Global Ultimate DUNS Numbers.

          include_clustered_articles: Include articles that are part of a cluster (reprints or similar articles).

          interval: The time interval for aggregation.

          is_material: Filter by materiality flag (relevance to business risk).

          language: Filter by ISO 2-letter Language Codes (e.g., 'en', 'nl').

          max_creation_date: Filter articles added to our database at or before this date/time.

          max_publication_date: Filter articles published at or before this date/time.

          min_creation_date: Filter articles added to our database at or after this date/time.

          min_publication_date: Filter articles published at or after this date/time.

          portfolio_id: Filter articles related to companies in specific Portfolios (UUIDs).

          query: Full-text search query for filtering articles by content.

          registration_number: Filter by local company registration numbers.

          saved_article_filter_id: Apply a previously saved set of article filters (UUID).

          sentiment: Filter by sentiment: `true` for positive, `false` for negative.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/ext/v3/articles/analytics/dates/",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "category": category,
                        "company": company,
                        "country": country,
                        "disable_company_article_deduplication": disable_company_article_deduplication,
                        "duns_number": duns_number,
                        "global_ultimate": global_ultimate,
                        "include_clustered_articles": include_clustered_articles,
                        "interval": interval,
                        "is_material": is_material,
                        "language": language,
                        "max_creation_date": max_creation_date,
                        "max_publication_date": max_publication_date,
                        "min_creation_date": min_creation_date,
                        "min_publication_date": min_publication_date,
                        "portfolio_id": portfolio_id,
                        "query": query,
                        "registration_number": registration_number,
                        "saved_article_filter_id": saved_article_filter_id,
                        "sentiment": sentiment,
                    },
                    analytics_get_count_by_date_params.AnalyticsGetCountByDateParams,
                ),
            ),
            cast_to=AnalyticsGetCountByDateResponse,
        )


class AnalyticsResourceWithRawResponse:
    def __init__(self, analytics: AnalyticsResource) -> None:
        self._analytics = analytics

        self.get_count_by_date = to_raw_response_wrapper(
            analytics.get_count_by_date,
        )


class AsyncAnalyticsResourceWithRawResponse:
    def __init__(self, analytics: AsyncAnalyticsResource) -> None:
        self._analytics = analytics

        self.get_count_by_date = async_to_raw_response_wrapper(
            analytics.get_count_by_date,
        )


class AnalyticsResourceWithStreamingResponse:
    def __init__(self, analytics: AnalyticsResource) -> None:
        self._analytics = analytics

        self.get_count_by_date = to_streamed_response_wrapper(
            analytics.get_count_by_date,
        )


class AsyncAnalyticsResourceWithStreamingResponse:
    def __init__(self, analytics: AsyncAnalyticsResource) -> None:
        self._analytics = analytics

        self.get_count_by_date = async_to_streamed_response_wrapper(
            analytics.get_count_by_date,
        )
