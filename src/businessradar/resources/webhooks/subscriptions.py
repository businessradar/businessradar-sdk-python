# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
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
from ...types.webhooks import subscription_list_params, subscription_create_params
from ...types.webhook_subscription import WebhookSubscription

__all__ = ["SubscriptionsResource", "AsyncSubscriptionsResource"]


class SubscriptionsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SubscriptionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/businessradar/businessradar-sdk-python#accessing-raw-response-data-eg-headers
        """
        return SubscriptionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SubscriptionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/businessradar/businessradar-sdk-python#with_streaming_response
        """
        return SubscriptionsResourceWithStreamingResponse(self)

    def create(
        self,
        webhook_external_id: str,
        *,
        event_type: Literal[
            "compliance_check.status_changed",
            "compliance_check.status_completed",
            "company_registration.status_changed",
            "company_registration.status_registered",
        ],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebhookSubscription:
        """
        List and add subscriptions on a specific webhook.

        Args:
          event_type: - `compliance_check.status_changed` - Compliance Check Status Changed
              - `compliance_check.status_completed` - Compliance Check Status Completed
              - `company_registration.status_changed` - Company Registration Status Changed
              - `company_registration.status_registered` - Company Registration Status
                Registered

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
                "/ext/v3/webhooks/{webhook_external_id}/subscriptions/", webhook_external_id=webhook_external_id
            ),
            body=maybe_transform({"event_type": event_type}, subscription_create_params.SubscriptionCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WebhookSubscription,
        )

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
    ) -> SyncNextKey[WebhookSubscription]:
        """
        List and add subscriptions on a specific webhook.

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
                "/ext/v3/webhooks/{webhook_external_id}/subscriptions/", webhook_external_id=webhook_external_id
            ),
            page=SyncNextKey[WebhookSubscription],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"next_key": next_key}, subscription_list_params.SubscriptionListParams),
            ),
            model=WebhookSubscription,
        )

    def delete(
        self,
        subscription_external_id: str,
        *,
        webhook_external_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Remove a single subscription from a webhook.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not webhook_external_id:
            raise ValueError(
                f"Expected a non-empty value for `webhook_external_id` but received {webhook_external_id!r}"
            )
        if not subscription_external_id:
            raise ValueError(
                f"Expected a non-empty value for `subscription_external_id` but received {subscription_external_id!r}"
            )
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template(
                "/ext/v3/webhooks/{webhook_external_id}/subscriptions/{subscription_external_id}/",
                webhook_external_id=webhook_external_id,
                subscription_external_id=subscription_external_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncSubscriptionsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSubscriptionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/businessradar/businessradar-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSubscriptionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSubscriptionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/businessradar/businessradar-sdk-python#with_streaming_response
        """
        return AsyncSubscriptionsResourceWithStreamingResponse(self)

    async def create(
        self,
        webhook_external_id: str,
        *,
        event_type: Literal[
            "compliance_check.status_changed",
            "compliance_check.status_completed",
            "company_registration.status_changed",
            "company_registration.status_registered",
        ],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebhookSubscription:
        """
        List and add subscriptions on a specific webhook.

        Args:
          event_type: - `compliance_check.status_changed` - Compliance Check Status Changed
              - `compliance_check.status_completed` - Compliance Check Status Completed
              - `company_registration.status_changed` - Company Registration Status Changed
              - `company_registration.status_registered` - Company Registration Status
                Registered

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
                "/ext/v3/webhooks/{webhook_external_id}/subscriptions/", webhook_external_id=webhook_external_id
            ),
            body=await async_maybe_transform(
                {"event_type": event_type}, subscription_create_params.SubscriptionCreateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WebhookSubscription,
        )

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
    ) -> AsyncPaginator[WebhookSubscription, AsyncNextKey[WebhookSubscription]]:
        """
        List and add subscriptions on a specific webhook.

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
                "/ext/v3/webhooks/{webhook_external_id}/subscriptions/", webhook_external_id=webhook_external_id
            ),
            page=AsyncNextKey[WebhookSubscription],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"next_key": next_key}, subscription_list_params.SubscriptionListParams),
            ),
            model=WebhookSubscription,
        )

    async def delete(
        self,
        subscription_external_id: str,
        *,
        webhook_external_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Remove a single subscription from a webhook.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not webhook_external_id:
            raise ValueError(
                f"Expected a non-empty value for `webhook_external_id` but received {webhook_external_id!r}"
            )
        if not subscription_external_id:
            raise ValueError(
                f"Expected a non-empty value for `subscription_external_id` but received {subscription_external_id!r}"
            )
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template(
                "/ext/v3/webhooks/{webhook_external_id}/subscriptions/{subscription_external_id}/",
                webhook_external_id=webhook_external_id,
                subscription_external_id=subscription_external_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class SubscriptionsResourceWithRawResponse:
    def __init__(self, subscriptions: SubscriptionsResource) -> None:
        self._subscriptions = subscriptions

        self.create = to_raw_response_wrapper(
            subscriptions.create,
        )
        self.list = to_raw_response_wrapper(
            subscriptions.list,
        )
        self.delete = to_raw_response_wrapper(
            subscriptions.delete,
        )


class AsyncSubscriptionsResourceWithRawResponse:
    def __init__(self, subscriptions: AsyncSubscriptionsResource) -> None:
        self._subscriptions = subscriptions

        self.create = async_to_raw_response_wrapper(
            subscriptions.create,
        )
        self.list = async_to_raw_response_wrapper(
            subscriptions.list,
        )
        self.delete = async_to_raw_response_wrapper(
            subscriptions.delete,
        )


class SubscriptionsResourceWithStreamingResponse:
    def __init__(self, subscriptions: SubscriptionsResource) -> None:
        self._subscriptions = subscriptions

        self.create = to_streamed_response_wrapper(
            subscriptions.create,
        )
        self.list = to_streamed_response_wrapper(
            subscriptions.list,
        )
        self.delete = to_streamed_response_wrapper(
            subscriptions.delete,
        )


class AsyncSubscriptionsResourceWithStreamingResponse:
    def __init__(self, subscriptions: AsyncSubscriptionsResource) -> None:
        self._subscriptions = subscriptions

        self.create = async_to_streamed_response_wrapper(
            subscriptions.create,
        )
        self.list = async_to_streamed_response_wrapper(
            subscriptions.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            subscriptions.delete,
        )
