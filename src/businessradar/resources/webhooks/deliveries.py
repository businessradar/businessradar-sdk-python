# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
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
from ...types.webhooks import delivery_list_params, delivery_test_params
from ...types.webhook_delivery import WebhookDelivery

__all__ = ["DeliveriesResource", "AsyncDeliveriesResource"]


class DeliveriesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DeliveriesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/businessradar/businessradar-sdk-python#accessing-raw-response-data-eg-headers
        """
        return DeliveriesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DeliveriesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/businessradar/businessradar-sdk-python#with_streaming_response
        """
        return DeliveriesResourceWithStreamingResponse(self)

    def list(
        self,
        webhook_external_id: str,
        *,
        next_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncNextKey[WebhookDelivery]:
        """
        List deliveries newest first.

        The default cursor pagination ignores the queryset ordering and applies its own
        `ordering` attribute, so set it on the paginator here. The `-id` tiebreaker
        keeps cursor paging stable when deliveries share a `created_at` timestamp.

        Args:
          next_key: A cursor value used for pagination. Include the `next_key` value from your
              previous request to retrieve the subsequent page of results. If this value is
              `null`, the first page of results is returned.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not webhook_external_id:
            raise ValueError(
                f"Expected a non-empty value for `webhook_external_id` but received {webhook_external_id!r}"
            )
        return self._get_api_list(
            path_template(
                "/ext/v3/webhooks/{webhook_external_id}/deliveries/", webhook_external_id=webhook_external_id
            ),
            page=SyncNextKey[WebhookDelivery],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"next_key": next_key}, delivery_list_params.DeliveryListParams),
            ),
            model=WebhookDelivery,
        )

    def test(
        self,
        webhook_external_id: str,
        *,
        event_type: Literal[
            "compliance_check.status_changed",
            "compliance_check.status_completed",
            "compliance_check.results.new",
            "company_registration.status_changed",
            "company_registration.status_registered",
            "company.updated",
        ]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebhookDelivery:
        """
        Queue a synthetic test event by creating a pending WebhookDelivery.

        Args:
          event_type: - `compliance_check.status_changed` - Compliance Check Status Changed
              - `compliance_check.status_completed` - Compliance Check Status Completed
              - `compliance_check.results.new` - Compliance Check Results New
              - `company_registration.status_changed` - Company Registration Status Changed
              - `company_registration.status_registered` - Company Registration Status
                Registered
              - `company.updated` - Company Updated

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not webhook_external_id:
            raise ValueError(
                f"Expected a non-empty value for `webhook_external_id` but received {webhook_external_id!r}"
            )
        return self._post(
            path_template(
                "/ext/v3/webhooks/{webhook_external_id}/deliveries/test/", webhook_external_id=webhook_external_id
            ),
            body=maybe_transform({"event_type": event_type}, delivery_test_params.DeliveryTestParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WebhookDelivery,
        )


class AsyncDeliveriesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDeliveriesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/businessradar/businessradar-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDeliveriesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDeliveriesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/businessradar/businessradar-sdk-python#with_streaming_response
        """
        return AsyncDeliveriesResourceWithStreamingResponse(self)

    def list(
        self,
        webhook_external_id: str,
        *,
        next_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[WebhookDelivery, AsyncNextKey[WebhookDelivery]]:
        """
        List deliveries newest first.

        The default cursor pagination ignores the queryset ordering and applies its own
        `ordering` attribute, so set it on the paginator here. The `-id` tiebreaker
        keeps cursor paging stable when deliveries share a `created_at` timestamp.

        Args:
          next_key: A cursor value used for pagination. Include the `next_key` value from your
              previous request to retrieve the subsequent page of results. If this value is
              `null`, the first page of results is returned.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not webhook_external_id:
            raise ValueError(
                f"Expected a non-empty value for `webhook_external_id` but received {webhook_external_id!r}"
            )
        return self._get_api_list(
            path_template(
                "/ext/v3/webhooks/{webhook_external_id}/deliveries/", webhook_external_id=webhook_external_id
            ),
            page=AsyncNextKey[WebhookDelivery],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"next_key": next_key}, delivery_list_params.DeliveryListParams),
            ),
            model=WebhookDelivery,
        )

    async def test(
        self,
        webhook_external_id: str,
        *,
        event_type: Literal[
            "compliance_check.status_changed",
            "compliance_check.status_completed",
            "compliance_check.results.new",
            "company_registration.status_changed",
            "company_registration.status_registered",
            "company.updated",
        ]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebhookDelivery:
        """
        Queue a synthetic test event by creating a pending WebhookDelivery.

        Args:
          event_type: - `compliance_check.status_changed` - Compliance Check Status Changed
              - `compliance_check.status_completed` - Compliance Check Status Completed
              - `compliance_check.results.new` - Compliance Check Results New
              - `company_registration.status_changed` - Company Registration Status Changed
              - `company_registration.status_registered` - Company Registration Status
                Registered
              - `company.updated` - Company Updated

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not webhook_external_id:
            raise ValueError(
                f"Expected a non-empty value for `webhook_external_id` but received {webhook_external_id!r}"
            )
        return await self._post(
            path_template(
                "/ext/v3/webhooks/{webhook_external_id}/deliveries/test/", webhook_external_id=webhook_external_id
            ),
            body=await async_maybe_transform({"event_type": event_type}, delivery_test_params.DeliveryTestParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WebhookDelivery,
        )


class DeliveriesResourceWithRawResponse:
    def __init__(self, deliveries: DeliveriesResource) -> None:
        self._deliveries = deliveries

        self.list = to_raw_response_wrapper(
            deliveries.list,
        )
        self.test = to_raw_response_wrapper(
            deliveries.test,
        )


class AsyncDeliveriesResourceWithRawResponse:
    def __init__(self, deliveries: AsyncDeliveriesResource) -> None:
        self._deliveries = deliveries

        self.list = async_to_raw_response_wrapper(
            deliveries.list,
        )
        self.test = async_to_raw_response_wrapper(
            deliveries.test,
        )


class DeliveriesResourceWithStreamingResponse:
    def __init__(self, deliveries: DeliveriesResource) -> None:
        self._deliveries = deliveries

        self.list = to_streamed_response_wrapper(
            deliveries.list,
        )
        self.test = to_streamed_response_wrapper(
            deliveries.test,
        )


class AsyncDeliveriesResourceWithStreamingResponse:
    def __init__(self, deliveries: AsyncDeliveriesResource) -> None:
        self._deliveries = deliveries

        self.list = async_to_streamed_response_wrapper(
            deliveries.list,
        )
        self.test = async_to_streamed_response_wrapper(
            deliveries.test,
        )
