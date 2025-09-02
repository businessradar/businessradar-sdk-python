# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .v3.v3 import (
    V3Resource,
    AsyncV3Resource,
    V3ResourceWithRawResponse,
    AsyncV3ResourceWithRawResponse,
    V3ResourceWithStreamingResponse,
    AsyncV3ResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["ExtResource", "AsyncExtResource"]


class ExtResource(SyncAPIResource):
    @cached_property
    def v3(self) -> V3Resource:
        return V3Resource(self._client)

    @cached_property
    def with_raw_response(self) -> ExtResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/businessradar/businessradar-sdk-python#accessing-raw-response-data-eg-headers
        """
        return ExtResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ExtResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/businessradar/businessradar-sdk-python#with_streaming_response
        """
        return ExtResourceWithStreamingResponse(self)


class AsyncExtResource(AsyncAPIResource):
    @cached_property
    def v3(self) -> AsyncV3Resource:
        return AsyncV3Resource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncExtResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/businessradar/businessradar-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncExtResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncExtResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/businessradar/businessradar-sdk-python#with_streaming_response
        """
        return AsyncExtResourceWithStreamingResponse(self)


class ExtResourceWithRawResponse:
    def __init__(self, ext: ExtResource) -> None:
        self._ext = ext

    @cached_property
    def v3(self) -> V3ResourceWithRawResponse:
        return V3ResourceWithRawResponse(self._ext.v3)


class AsyncExtResourceWithRawResponse:
    def __init__(self, ext: AsyncExtResource) -> None:
        self._ext = ext

    @cached_property
    def v3(self) -> AsyncV3ResourceWithRawResponse:
        return AsyncV3ResourceWithRawResponse(self._ext.v3)


class ExtResourceWithStreamingResponse:
    def __init__(self, ext: ExtResource) -> None:
        self._ext = ext

    @cached_property
    def v3(self) -> V3ResourceWithStreamingResponse:
        return V3ResourceWithStreamingResponse(self._ext.v3)


class AsyncExtResourceWithStreamingResponse:
    def __init__(self, ext: AsyncExtResource) -> None:
        self._ext = ext

    @cached_property
    def v3(self) -> AsyncV3ResourceWithStreamingResponse:
        return AsyncV3ResourceWithStreamingResponse(self._ext.v3)
