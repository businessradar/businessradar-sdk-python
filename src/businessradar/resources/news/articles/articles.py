# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional
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
from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
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
from ....types.news import FeedbackTypeEnum, article_list_params, article_create_feedback_params
from ...._base_client import make_request_options
from ....types.news.feedback_type_enum import FeedbackTypeEnum
from ....types.news.article_list_response import ArticleListResponse
from ....types.news.article_create_feedback_response import ArticleCreateFeedbackResponse
from ....types.news.article_retrieve_related_response import ArticleRetrieveRelatedResponse

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
        category: List[str] | NotGiven = NOT_GIVEN,
        company: List[str] | NotGiven = NOT_GIVEN,
        country: List[str] | NotGiven = NOT_GIVEN,
        duns_number: List[str] | NotGiven = NOT_GIVEN,
        global_ultimate: List[str] | NotGiven = NOT_GIVEN,
        include_clustered_articles: bool | NotGiven = NOT_GIVEN,
        language: List[str] | NotGiven = NOT_GIVEN,
        max_creation_date: Union[str, datetime] | NotGiven = NOT_GIVEN,
        max_publication_date: Union[str, datetime] | NotGiven = NOT_GIVEN,
        min_creation_date: Union[str, datetime] | NotGiven = NOT_GIVEN,
        min_publication_date: Union[str, datetime] | NotGiven = NOT_GIVEN,
        next_key: str | NotGiven = NOT_GIVEN,
        portfolio_id: List[str] | NotGiven = NOT_GIVEN,
        query: str | NotGiven = NOT_GIVEN,
        registration_number: List[str] | NotGiven = NOT_GIVEN,
        saved_article_filter_id: str | NotGiven = NOT_GIVEN,
        sentiment: bool | NotGiven = NOT_GIVEN,
        sorting: Literal[
            "creation_date",
            "publication_date_clustering",
            "publication_date_priority",
            "publication_date_source_references",
            "publication_datetime",
        ]
        | NotGiven = NOT_GIVEN,
        sorting_order: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ArticleListResponse:
        """
        Search News Articles.

        List Articles from the Business Radar platform, search using advanced queries or
        check articles that have been published since last check.

        Args:
          category: Category ID to filter articles

          company: Company ID's

          country: ISO 2-letter Country Code

          duns_number: 9-digit Dun And Bradstreet Number

          global_ultimate: 9-digit Dun And Bradstreet Number

          include_clustered_articles: Include clustered articles

          language: ISO 2-letter Language Code

          max_creation_date: Filter articles created before this date

          max_publication_date: Filter articles published before this date

          min_creation_date: Filter articles created after this date

          min_publication_date: Filter articles published after this date

          next_key: The next_key is an cursor used to make it possible to paginate to the next
              results, pass the next_key from the previous request to retrieve next results.

          portfolio_id: Portfolio ID to filter articles

          query: Custom search filters to text search all articles.

          registration_number: Local Registration Number

          saved_article_filter_id: Filter articles on already saved article filter id

          sentiment: Filter articles with sentiment

          sorting: Sort articles

          sorting_order: Sort order

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/ext/v3/articles",
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
                        "duns_number": duns_number,
                        "global_ultimate": global_ultimate,
                        "include_clustered_articles": include_clustered_articles,
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
            cast_to=ArticleListResponse,
        )

    def create_feedback(
        self,
        *,
        article: str,
        comment: Optional[str] | NotGiven = NOT_GIVEN,
        email: Optional[str] | NotGiven = NOT_GIVEN,
        feedback_type: FeedbackTypeEnum | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ArticleCreateFeedbackResponse:
        """
        Create Article Feedback.

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

    def retrieve_related(
        self,
        article_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ArticleRetrieveRelatedResponse:
        """
        Retrieve Article Embedding Search.

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

    async def list(
        self,
        *,
        category: List[str] | NotGiven = NOT_GIVEN,
        company: List[str] | NotGiven = NOT_GIVEN,
        country: List[str] | NotGiven = NOT_GIVEN,
        duns_number: List[str] | NotGiven = NOT_GIVEN,
        global_ultimate: List[str] | NotGiven = NOT_GIVEN,
        include_clustered_articles: bool | NotGiven = NOT_GIVEN,
        language: List[str] | NotGiven = NOT_GIVEN,
        max_creation_date: Union[str, datetime] | NotGiven = NOT_GIVEN,
        max_publication_date: Union[str, datetime] | NotGiven = NOT_GIVEN,
        min_creation_date: Union[str, datetime] | NotGiven = NOT_GIVEN,
        min_publication_date: Union[str, datetime] | NotGiven = NOT_GIVEN,
        next_key: str | NotGiven = NOT_GIVEN,
        portfolio_id: List[str] | NotGiven = NOT_GIVEN,
        query: str | NotGiven = NOT_GIVEN,
        registration_number: List[str] | NotGiven = NOT_GIVEN,
        saved_article_filter_id: str | NotGiven = NOT_GIVEN,
        sentiment: bool | NotGiven = NOT_GIVEN,
        sorting: Literal[
            "creation_date",
            "publication_date_clustering",
            "publication_date_priority",
            "publication_date_source_references",
            "publication_datetime",
        ]
        | NotGiven = NOT_GIVEN,
        sorting_order: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ArticleListResponse:
        """
        Search News Articles.

        List Articles from the Business Radar platform, search using advanced queries or
        check articles that have been published since last check.

        Args:
          category: Category ID to filter articles

          company: Company ID's

          country: ISO 2-letter Country Code

          duns_number: 9-digit Dun And Bradstreet Number

          global_ultimate: 9-digit Dun And Bradstreet Number

          include_clustered_articles: Include clustered articles

          language: ISO 2-letter Language Code

          max_creation_date: Filter articles created before this date

          max_publication_date: Filter articles published before this date

          min_creation_date: Filter articles created after this date

          min_publication_date: Filter articles published after this date

          next_key: The next_key is an cursor used to make it possible to paginate to the next
              results, pass the next_key from the previous request to retrieve next results.

          portfolio_id: Portfolio ID to filter articles

          query: Custom search filters to text search all articles.

          registration_number: Local Registration Number

          saved_article_filter_id: Filter articles on already saved article filter id

          sentiment: Filter articles with sentiment

          sorting: Sort articles

          sorting_order: Sort order

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/ext/v3/articles",
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
                        "duns_number": duns_number,
                        "global_ultimate": global_ultimate,
                        "include_clustered_articles": include_clustered_articles,
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
            cast_to=ArticleListResponse,
        )

    async def create_feedback(
        self,
        *,
        article: str,
        comment: Optional[str] | NotGiven = NOT_GIVEN,
        email: Optional[str] | NotGiven = NOT_GIVEN,
        feedback_type: FeedbackTypeEnum | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ArticleCreateFeedbackResponse:
        """
        Create Article Feedback.

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

    async def retrieve_related(
        self,
        article_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ArticleRetrieveRelatedResponse:
        """
        Retrieve Article Embedding Search.

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
        self.retrieve_related = async_to_streamed_response_wrapper(
            articles.retrieve_related,
        )

    @cached_property
    def analytics(self) -> AsyncAnalyticsResourceWithStreamingResponse:
        return AsyncAnalyticsResourceWithStreamingResponse(self._articles.analytics)

    @cached_property
    def export(self) -> AsyncExportResourceWithStreamingResponse:
        return AsyncExportResourceWithStreamingResponse(self._articles.export)
