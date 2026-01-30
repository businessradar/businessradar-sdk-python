# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal

import httpx

from .export import (
    ExportResource,
    AsyncExportResource,
    ExportResourceWithRawResponse,
    AsyncExportResourceWithRawResponse,
    ExportResourceWithStreamingResponse,
    AsyncExportResourceWithStreamingResponse,
)
from ...._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ...._utils import maybe_transform, async_maybe_transform
from .analytics import (
    AnalyticsResource,
    AsyncAnalyticsResource,
    AnalyticsResourceWithRawResponse,
    AsyncAnalyticsResourceWithRawResponse,
    AnalyticsResourceWithStreamingResponse,
    AsyncAnalyticsResourceWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....pagination import SyncNextKey, AsyncNextKey
from ....types.news import (
    FeedbackTypeEnum,
    article_list_params,
    article_create_feedback_params,
    article_list_saved_article_filters_params,
)
from ...._base_client import AsyncPaginator, make_request_options
from ....types.news.article import Article
from ....types.news.feedback_type_enum import FeedbackTypeEnum
from ....types.news.article_create_feedback_response import ArticleCreateFeedbackResponse
from ....types.news.article_retrieve_related_response import ArticleRetrieveRelatedResponse
from ....types.news.article_list_saved_article_filters_response import ArticleListSavedArticleFiltersResponse

__all__ = ["ArticlesResource", "AsyncArticlesResource"]


class ArticlesResource(SyncAPIResource):
    @cached_property
    def analytics(self) -> AnalyticsResource:
        return AnalyticsResource(self._client)

    @cached_property
    def export(self) -> ExportResource:
        return ExportResource(self._client)

    @cached_property
    def with_raw_response(self) -> ArticlesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/businessradar/businessradar-sdk-python#accessing-raw-response-data-eg-headers
        """
        return ArticlesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ArticlesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/businessradar/businessradar-sdk-python#with_streaming_response
        """
        return ArticlesResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        category: SequenceNotStr[str] | Omit = omit,
        company: SequenceNotStr[str] | Omit = omit,
        country: SequenceNotStr[str] | Omit = omit,
        disable_company_article_deduplication: bool | Omit = omit,
        duns_number: SequenceNotStr[str] | Omit = omit,
        global_ultimate: SequenceNotStr[str] | Omit = omit,
        include_clustered_articles: bool | Omit = omit,
        is_material: bool | Omit = omit,
        language: SequenceNotStr[str] | Omit = omit,
        max_creation_date: Union[str, datetime] | Omit = omit,
        max_publication_date: Union[str, datetime] | Omit = omit,
        min_creation_date: Union[str, datetime] | Omit = omit,
        min_publication_date: Union[str, datetime] | Omit = omit,
        next_key: str | Omit = omit,
        portfolio_id: SequenceNotStr[str] | Omit = omit,
        query: str | Omit = omit,
        registration_number: SequenceNotStr[str] | Omit = omit,
        saved_article_filter_id: str | Omit = omit,
        sentiment: bool | Omit = omit,
        sorting: Literal[
            "creation_date",
            "publication_date_clustering",
            "publication_date_priority",
            "publication_date_source_references",
            "publication_datetime",
        ]
        | Omit = omit,
        sorting_order: Literal["asc", "desc"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncNextKey[Article]:
        """
        ### Search News Articles

        Retrieve articles matching the specified search criteria. Advanced queries and
        incremental checks (using publication/creation dates) are supported.

        Args:
          category: Filter by article Category IDs (UUIDs).

          company: Filter by internal Company UUIDs.

          country: Filter by ISO 2-letter Country Codes (e.g., 'US', 'GB').

          disable_company_article_deduplication: By default, companies with the same trade names are grouped and the best match
              is selected. Enable this to see all associated companies.

          duns_number: Filter by one or more 9-digit Dun & Bradstreet Numbers.

          global_ultimate: Filter by Global Ultimate DUNS Numbers.

          include_clustered_articles: Include articles that are part of a cluster (reprints or similar articles).

          is_material: Filter by materiality flag (relevance to business risk).

          language: Filter by ISO 2-letter Language Codes (e.g., 'en', 'nl').

          max_creation_date: Filter articles added to our database at or before this date/time.

          max_publication_date: Filter articles published at or before this date/time.

          min_creation_date: Filter articles added to our database at or after this date/time.

          min_publication_date: Filter articles published at or after this date/time.

          next_key: A cursor value used for pagination. Include the `next_key` value from your
              previous request to retrieve the subsequent page of results. If this value is
              `null`, the first page of results is returned.

          portfolio_id: Filter articles related to companies in specific Portfolios (UUIDs).

          query: Full-text search query for filtering articles by content.

          registration_number: Filter by local company registration numbers.

          saved_article_filter_id: Apply a previously saved set of article filters (UUID).

          sentiment: Filter by sentiment: `true` for positive, `false` for negative.

          sorting: Sort articles

          sorting_order: Sort order

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/ext/v3/articles",
            page=SyncNextKey[Article],
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
                        "is_material": is_material,
                        "language": language,
                        "max_creation_date": max_creation_date,
                        "max_publication_date": max_publication_date,
                        "min_creation_date": min_creation_date,
                        "min_publication_date": min_publication_date,
                        "next_key": next_key,
                        "portfolio_id": portfolio_id,
                        "query": query,
                        "registration_number": registration_number,
                        "saved_article_filter_id": saved_article_filter_id,
                        "sentiment": sentiment,
                        "sorting": sorting,
                        "sorting_order": sorting_order,
                    },
                    article_list_params.ArticleListParams,
                ),
            ),
            model=Article,
        )

    def create_feedback(
        self,
        *,
        article: str,
        comment: Optional[str] | Omit = omit,
        email: Optional[str] | Omit = omit,
        feedback_type: FeedbackTypeEnum | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ArticleCreateFeedbackResponse:
        """### Submit Article Feedback

        Submit feedback for a specific article.

        This helps improve our analysis and
        relevance.

        Args:
          feedback_type: - `false_positive` - False Positive
              - `no_risk` - No Risk
              - `risk_confirmed` - Risk Confirmed

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/ext/v3/articles/feedback/",
            body=maybe_transform(
                {
                    "article": article,
                    "comment": comment,
                    "email": email,
                    "feedback_type": feedback_type,
                },
                article_create_feedback_params.ArticleCreateFeedbackParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ArticleCreateFeedbackResponse,
        )

    def list_saved_article_filters(
        self,
        *,
        next_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncNextKey[ArticleListSavedArticleFiltersResponse]:
        """
        ### Saved Article Filters

        Retrieve a list of all search filters saved by the current profile. These
        filters can be applied to article search requests using the
        `saved_article_filter_id` parameter.

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
            "/ext/v3/saved_article_filters",
            page=SyncNextKey[ArticleListSavedArticleFiltersResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"next_key": next_key},
                    article_list_saved_article_filters_params.ArticleListSavedArticleFiltersParams,
                ),
            ),
            model=ArticleListSavedArticleFiltersResponse,
        )

    def retrieve_related(
        self,
        article_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ArticleRetrieveRelatedResponse:
        """
        ### Find Related Articles

        Retrieve a list of articles that are semantically similar to the specified
        article, ranked by similarity distance.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not article_id:
            raise ValueError(f"Expected a non-empty value for `article_id` but received {article_id!r}")
        return self._get(
            f"/ext/v3/articles/{article_id}/related/",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ArticleRetrieveRelatedResponse,
        )


class AsyncArticlesResource(AsyncAPIResource):
    @cached_property
    def analytics(self) -> AsyncAnalyticsResource:
        return AsyncAnalyticsResource(self._client)

    @cached_property
    def export(self) -> AsyncExportResource:
        return AsyncExportResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncArticlesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/businessradar/businessradar-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncArticlesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncArticlesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/businessradar/businessradar-sdk-python#with_streaming_response
        """
        return AsyncArticlesResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        category: SequenceNotStr[str] | Omit = omit,
        company: SequenceNotStr[str] | Omit = omit,
        country: SequenceNotStr[str] | Omit = omit,
        disable_company_article_deduplication: bool | Omit = omit,
        duns_number: SequenceNotStr[str] | Omit = omit,
        global_ultimate: SequenceNotStr[str] | Omit = omit,
        include_clustered_articles: bool | Omit = omit,
        is_material: bool | Omit = omit,
        language: SequenceNotStr[str] | Omit = omit,
        max_creation_date: Union[str, datetime] | Omit = omit,
        max_publication_date: Union[str, datetime] | Omit = omit,
        min_creation_date: Union[str, datetime] | Omit = omit,
        min_publication_date: Union[str, datetime] | Omit = omit,
        next_key: str | Omit = omit,
        portfolio_id: SequenceNotStr[str] | Omit = omit,
        query: str | Omit = omit,
        registration_number: SequenceNotStr[str] | Omit = omit,
        saved_article_filter_id: str | Omit = omit,
        sentiment: bool | Omit = omit,
        sorting: Literal[
            "creation_date",
            "publication_date_clustering",
            "publication_date_priority",
            "publication_date_source_references",
            "publication_datetime",
        ]
        | Omit = omit,
        sorting_order: Literal["asc", "desc"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[Article, AsyncNextKey[Article]]:
        """
        ### Search News Articles

        Retrieve articles matching the specified search criteria. Advanced queries and
        incremental checks (using publication/creation dates) are supported.

        Args:
          category: Filter by article Category IDs (UUIDs).

          company: Filter by internal Company UUIDs.

          country: Filter by ISO 2-letter Country Codes (e.g., 'US', 'GB').

          disable_company_article_deduplication: By default, companies with the same trade names are grouped and the best match
              is selected. Enable this to see all associated companies.

          duns_number: Filter by one or more 9-digit Dun & Bradstreet Numbers.

          global_ultimate: Filter by Global Ultimate DUNS Numbers.

          include_clustered_articles: Include articles that are part of a cluster (reprints or similar articles).

          is_material: Filter by materiality flag (relevance to business risk).

          language: Filter by ISO 2-letter Language Codes (e.g., 'en', 'nl').

          max_creation_date: Filter articles added to our database at or before this date/time.

          max_publication_date: Filter articles published at or before this date/time.

          min_creation_date: Filter articles added to our database at or after this date/time.

          min_publication_date: Filter articles published at or after this date/time.

          next_key: A cursor value used for pagination. Include the `next_key` value from your
              previous request to retrieve the subsequent page of results. If this value is
              `null`, the first page of results is returned.

          portfolio_id: Filter articles related to companies in specific Portfolios (UUIDs).

          query: Full-text search query for filtering articles by content.

          registration_number: Filter by local company registration numbers.

          saved_article_filter_id: Apply a previously saved set of article filters (UUID).

          sentiment: Filter by sentiment: `true` for positive, `false` for negative.

          sorting: Sort articles

          sorting_order: Sort order

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/ext/v3/articles",
            page=AsyncNextKey[Article],
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
                        "is_material": is_material,
                        "language": language,
                        "max_creation_date": max_creation_date,
                        "max_publication_date": max_publication_date,
                        "min_creation_date": min_creation_date,
                        "min_publication_date": min_publication_date,
                        "next_key": next_key,
                        "portfolio_id": portfolio_id,
                        "query": query,
                        "registration_number": registration_number,
                        "saved_article_filter_id": saved_article_filter_id,
                        "sentiment": sentiment,
                        "sorting": sorting,
                        "sorting_order": sorting_order,
                    },
                    article_list_params.ArticleListParams,
                ),
            ),
            model=Article,
        )

    async def create_feedback(
        self,
        *,
        article: str,
        comment: Optional[str] | Omit = omit,
        email: Optional[str] | Omit = omit,
        feedback_type: FeedbackTypeEnum | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ArticleCreateFeedbackResponse:
        """### Submit Article Feedback

        Submit feedback for a specific article.

        This helps improve our analysis and
        relevance.

        Args:
          feedback_type: - `false_positive` - False Positive
              - `no_risk` - No Risk
              - `risk_confirmed` - Risk Confirmed

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/ext/v3/articles/feedback/",
            body=await async_maybe_transform(
                {
                    "article": article,
                    "comment": comment,
                    "email": email,
                    "feedback_type": feedback_type,
                },
                article_create_feedback_params.ArticleCreateFeedbackParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ArticleCreateFeedbackResponse,
        )

    def list_saved_article_filters(
        self,
        *,
        next_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[ArticleListSavedArticleFiltersResponse, AsyncNextKey[ArticleListSavedArticleFiltersResponse]]:
        """
        ### Saved Article Filters

        Retrieve a list of all search filters saved by the current profile. These
        filters can be applied to article search requests using the
        `saved_article_filter_id` parameter.

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
            "/ext/v3/saved_article_filters",
            page=AsyncNextKey[ArticleListSavedArticleFiltersResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"next_key": next_key},
                    article_list_saved_article_filters_params.ArticleListSavedArticleFiltersParams,
                ),
            ),
            model=ArticleListSavedArticleFiltersResponse,
        )

    async def retrieve_related(
        self,
        article_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ArticleRetrieveRelatedResponse:
        """
        ### Find Related Articles

        Retrieve a list of articles that are semantically similar to the specified
        article, ranked by similarity distance.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not article_id:
            raise ValueError(f"Expected a non-empty value for `article_id` but received {article_id!r}")
        return await self._get(
            f"/ext/v3/articles/{article_id}/related/",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ArticleRetrieveRelatedResponse,
        )


class ArticlesResourceWithRawResponse:
    def __init__(self, articles: ArticlesResource) -> None:
        self._articles = articles

        self.list = to_raw_response_wrapper(
            articles.list,
        )
        self.create_feedback = to_raw_response_wrapper(
            articles.create_feedback,
        )
        self.list_saved_article_filters = to_raw_response_wrapper(
            articles.list_saved_article_filters,
        )
        self.retrieve_related = to_raw_response_wrapper(
            articles.retrieve_related,
        )

    @cached_property
    def analytics(self) -> AnalyticsResourceWithRawResponse:
        return AnalyticsResourceWithRawResponse(self._articles.analytics)

    @cached_property
    def export(self) -> ExportResourceWithRawResponse:
        return ExportResourceWithRawResponse(self._articles.export)


class AsyncArticlesResourceWithRawResponse:
    def __init__(self, articles: AsyncArticlesResource) -> None:
        self._articles = articles

        self.list = async_to_raw_response_wrapper(
            articles.list,
        )
        self.create_feedback = async_to_raw_response_wrapper(
            articles.create_feedback,
        )
        self.list_saved_article_filters = async_to_raw_response_wrapper(
            articles.list_saved_article_filters,
        )
        self.retrieve_related = async_to_raw_response_wrapper(
            articles.retrieve_related,
        )

    @cached_property
    def analytics(self) -> AsyncAnalyticsResourceWithRawResponse:
        return AsyncAnalyticsResourceWithRawResponse(self._articles.analytics)

    @cached_property
    def export(self) -> AsyncExportResourceWithRawResponse:
        return AsyncExportResourceWithRawResponse(self._articles.export)


class ArticlesResourceWithStreamingResponse:
    def __init__(self, articles: ArticlesResource) -> None:
        self._articles = articles

        self.list = to_streamed_response_wrapper(
            articles.list,
        )
        self.create_feedback = to_streamed_response_wrapper(
            articles.create_feedback,
        )
        self.list_saved_article_filters = to_streamed_response_wrapper(
            articles.list_saved_article_filters,
        )
        self.retrieve_related = to_streamed_response_wrapper(
            articles.retrieve_related,
        )

    @cached_property
    def analytics(self) -> AnalyticsResourceWithStreamingResponse:
        return AnalyticsResourceWithStreamingResponse(self._articles.analytics)

    @cached_property
    def export(self) -> ExportResourceWithStreamingResponse:
        return ExportResourceWithStreamingResponse(self._articles.export)


class AsyncArticlesResourceWithStreamingResponse:
    def __init__(self, articles: AsyncArticlesResource) -> None:
        self._articles = articles

        self.list = async_to_streamed_response_wrapper(
            articles.list,
        )
        self.create_feedback = async_to_streamed_response_wrapper(
            articles.create_feedback,
        )
        self.list_saved_article_filters = async_to_streamed_response_wrapper(
            articles.list_saved_article_filters,
        )
        self.retrieve_related = async_to_streamed_response_wrapper(
            articles.retrieve_related,
        )

    @cached_property
    def analytics(self) -> AsyncAnalyticsResourceWithStreamingResponse:
        return AsyncAnalyticsResourceWithStreamingResponse(self._articles.analytics)

    @cached_property
    def export(self) -> AsyncExportResourceWithStreamingResponse:
        return AsyncExportResourceWithStreamingResponse(self._articles.export)
