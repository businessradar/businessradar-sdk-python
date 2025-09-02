# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .articles.articles import (
    ArticlesResource,
    AsyncArticlesResource,
    ArticlesResourceWithRawResponse,
    AsyncArticlesResourceWithRawResponse,
    ArticlesResourceWithStreamingResponse,
    AsyncArticlesResourceWithStreamingResponse,
)

__all__ = ["NewsResource", "AsyncNewsResource"]


class NewsResource(SyncAPIResource):
    @cached_property
    def articles(self) -> ArticlesResource:
        return ArticlesResource(self._client)

    @cached_property
    def with_raw_response(self) -> NewsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/businessradar/businessradar-sdk-python#accessing-raw-response-data-eg-headers
        """
        return NewsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> NewsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/businessradar/businessradar-sdk-python#with_streaming_response
        """
        return NewsResourceWithStreamingResponse(self)


class AsyncNewsResource(AsyncAPIResource):
    @cached_property
    def articles(self) -> AsyncArticlesResource:
        return AsyncArticlesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncNewsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/businessradar/businessradar-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncNewsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncNewsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/businessradar/businessradar-sdk-python#with_streaming_response
        """
        return AsyncNewsResourceWithStreamingResponse(self)


class NewsResourceWithRawResponse:
    def __init__(self, news: NewsResource) -> None:
        self._news = news

    @cached_property
    def articles(self) -> ArticlesResourceWithRawResponse:
        return ArticlesResourceWithRawResponse(self._news.articles)


class AsyncNewsResourceWithRawResponse:
    def __init__(self, news: AsyncNewsResource) -> None:
        self._news = news

    @cached_property
    def articles(self) -> AsyncArticlesResourceWithRawResponse:
        return AsyncArticlesResourceWithRawResponse(self._news.articles)


class NewsResourceWithStreamingResponse:
    def __init__(self, news: NewsResource) -> None:
        self._news = news

    @cached_property
    def articles(self) -> ArticlesResourceWithStreamingResponse:
        return ArticlesResourceWithStreamingResponse(self._news.articles)


class AsyncNewsResourceWithStreamingResponse:
    def __init__(self, news: AsyncNewsResource) -> None:
        self._news = news

    @cached_property
    def articles(self) -> AsyncArticlesResourceWithStreamingResponse:
        return AsyncArticlesResourceWithStreamingResponse(self._news.articles)
