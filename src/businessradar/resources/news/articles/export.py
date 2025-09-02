# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
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
from ....types.news.articles import DataExportFileType, export_create_params
from ....types.news.articles.article_export import ArticleExport
from ....types.news.articles.data_export_file_type import DataExportFileType

__all__ = ["ExportResource", "AsyncExportResource"]


class ExportResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ExportResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/businessradar/businessradar-sdk-python#accessing-raw-response-data-eg-headers
        """
        return ExportResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ExportResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/businessradar/businessradar-sdk-python#with_streaming_response
        """
        return ExportResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        file_type: DataExportFileType,
        filters: export_create_params.Filters,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ArticleExport:
        """
        Export articles, get status using get Export details API.

        The export returns the location to an JSON-Lines file located on our S3 bucket.
        The file is available for 7 days.

        There is a max restriction of 25.000 articles per export. No pagination
        supported. For larger exports please contact support@businessradar.com

        Args:
          file_type: - `PDF` - PDF
              - `EXCEL` - Excel
              - `JSONL` - JSONL

          filters: Article Filter Serializer.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/ext/v3/articles/export/",
            body=maybe_transform(
                {
                    "file_type": file_type,
                    "filters": filters,
                },
                export_create_params.ExportCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ArticleExport,
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
    ) -> ArticleExport:
        """
        Export article details.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not external_id:
            raise ValueError(f"Expected a non-empty value for `external_id` but received {external_id!r}")
        return self._get(
            f"/ext/v3/articles/export/{external_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ArticleExport,
        )


class AsyncExportResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncExportResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/businessradar/businessradar-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncExportResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncExportResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/businessradar/businessradar-sdk-python#with_streaming_response
        """
        return AsyncExportResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        file_type: DataExportFileType,
        filters: export_create_params.Filters,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ArticleExport:
        """
        Export articles, get status using get Export details API.

        The export returns the location to an JSON-Lines file located on our S3 bucket.
        The file is available for 7 days.

        There is a max restriction of 25.000 articles per export. No pagination
        supported. For larger exports please contact support@businessradar.com

        Args:
          file_type: - `PDF` - PDF
              - `EXCEL` - Excel
              - `JSONL` - JSONL

          filters: Article Filter Serializer.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/ext/v3/articles/export/",
            body=await async_maybe_transform(
                {
                    "file_type": file_type,
                    "filters": filters,
                },
                export_create_params.ExportCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ArticleExport,
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
    ) -> ArticleExport:
        """
        Export article details.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not external_id:
            raise ValueError(f"Expected a non-empty value for `external_id` but received {external_id!r}")
        return await self._get(
            f"/ext/v3/articles/export/{external_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ArticleExport,
        )


class ExportResourceWithRawResponse:
    def __init__(self, export: ExportResource) -> None:
        self._export = export

        self.create = to_raw_response_wrapper(
            export.create,
        )
        self.retrieve = to_raw_response_wrapper(
            export.retrieve,
        )


class AsyncExportResourceWithRawResponse:
    def __init__(self, export: AsyncExportResource) -> None:
        self._export = export

        self.create = async_to_raw_response_wrapper(
            export.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            export.retrieve,
        )


class ExportResourceWithStreamingResponse:
    def __init__(self, export: ExportResource) -> None:
        self._export = export

        self.create = to_streamed_response_wrapper(
            export.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            export.retrieve,
        )


class AsyncExportResourceWithStreamingResponse:
    def __init__(self, export: AsyncExportResource) -> None:
        self._export = export

        self.create = async_to_streamed_response_wrapper(
            export.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            export.retrieve,
        )
