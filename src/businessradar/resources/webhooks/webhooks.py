# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

import httpx

from ...types import webhook_list_params, webhook_create_params, webhook_update_params, webhook_partial_update_params
from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from .deliveries import (
    DeliveriesResource,
    AsyncDeliveriesResource,
    DeliveriesResourceWithRawResponse,
    AsyncDeliveriesResourceWithRawResponse,
    DeliveriesResourceWithStreamingResponse,
    AsyncDeliveriesResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import SyncNextKey, AsyncNextKey
from .subscriptions import (
    SubscriptionsResource,
    AsyncSubscriptionsResource,
    SubscriptionsResourceWithRawResponse,
    AsyncSubscriptionsResourceWithRawResponse,
    SubscriptionsResourceWithStreamingResponse,
    AsyncSubscriptionsResourceWithStreamingResponse,
)
from ..._base_client import AsyncPaginator, make_request_options
from ...types.webhook import Webhook
from ...types.webhook_regenerate_secret_response import WebhookRegenerateSecretResponse
from ...types.webhook_subscription_request_param import WebhookSubscriptionRequestParam

__all__ = ["WebhooksResource", "AsyncWebhooksResource"]


class WebhooksResource(SyncAPIResource):
    @cached_property
    def deliveries(self) -> DeliveriesResource:
        return DeliveriesResource(self._client)

    @cached_property
    def subscriptions(self) -> SubscriptionsResource:
        return SubscriptionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> WebhooksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/businessradar/businessradar-sdk-python#accessing-raw-response-data-eg-headers
        """
        return WebhooksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WebhooksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/businessradar/businessradar-sdk-python#with_streaming_response
        """
        return WebhooksResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        subscriptions: Iterable[WebhookSubscriptionRequestParam],
        url: str,
        enabled: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Webhook:
        """
        List and create webhooks for the active profile.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/ext/v3/webhooks/",
            body=maybe_transform(
                {
                    "subscriptions": subscriptions,
                    "url": url,
                    "enabled": enabled,
                },
                webhook_create_params.WebhookCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Webhook,
        )

    def retrieve(
        self,
        webhook_external_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Webhook:
        """
        Retrieve, update, or delete a single webhook.

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
        return self._get(
            path_template("/ext/v3/webhooks/{webhook_external_id}/", webhook_external_id=webhook_external_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Webhook,
        )

    def update(
        self,
        webhook_external_id: str,
        *,
        subscriptions: Iterable[WebhookSubscriptionRequestParam],
        url: str,
        enabled: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Webhook:
        """
        Retrieve, update, or delete a single webhook.

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
        return self._put(
            path_template("/ext/v3/webhooks/{webhook_external_id}/", webhook_external_id=webhook_external_id),
            body=maybe_transform(
                {
                    "subscriptions": subscriptions,
                    "url": url,
                    "enabled": enabled,
                },
                webhook_update_params.WebhookUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Webhook,
        )

    def list(
        self,
        *,
        next_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncNextKey[Webhook]:
        """
        List and create webhooks for the active profile.

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
            "/ext/v3/webhooks/",
            page=SyncNextKey[Webhook],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"next_key": next_key}, webhook_list_params.WebhookListParams),
            ),
            model=Webhook,
        )

    def delete(
        self,
        webhook_external_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Retrieve, update, or delete a single webhook.

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
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/ext/v3/webhooks/{webhook_external_id}/", webhook_external_id=webhook_external_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def partial_update(
        self,
        webhook_external_id: str,
        *,
        enabled: bool | Omit = omit,
        subscriptions: Iterable[WebhookSubscriptionRequestParam] | Omit = omit,
        url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Webhook:
        """
        Retrieve, update, or delete a single webhook.

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
        return self._patch(
            path_template("/ext/v3/webhooks/{webhook_external_id}/", webhook_external_id=webhook_external_id),
            body=maybe_transform(
                {
                    "enabled": enabled,
                    "subscriptions": subscriptions,
                    "url": url,
                },
                webhook_partial_update_params.WebhookPartialUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Webhook,
        )

    def regenerate_secret(
        self,
        webhook_external_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebhookRegenerateSecretResponse:
        """Rotate the secret.

        The new value is returned once and never shown again.

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
        return self._post(
            path_template(
                "/ext/v3/webhooks/{webhook_external_id}/regenerate_secret/", webhook_external_id=webhook_external_id
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WebhookRegenerateSecretResponse,
        )

    def retrieve_event_types(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Return all available webhook event types."""
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            "/ext/v3/webhooks/event_types/",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncWebhooksResource(AsyncAPIResource):
    @cached_property
    def deliveries(self) -> AsyncDeliveriesResource:
        return AsyncDeliveriesResource(self._client)

    @cached_property
    def subscriptions(self) -> AsyncSubscriptionsResource:
        return AsyncSubscriptionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncWebhooksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/businessradar/businessradar-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncWebhooksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWebhooksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/businessradar/businessradar-sdk-python#with_streaming_response
        """
        return AsyncWebhooksResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        subscriptions: Iterable[WebhookSubscriptionRequestParam],
        url: str,
        enabled: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Webhook:
        """
        List and create webhooks for the active profile.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/ext/v3/webhooks/",
            body=await async_maybe_transform(
                {
                    "subscriptions": subscriptions,
                    "url": url,
                    "enabled": enabled,
                },
                webhook_create_params.WebhookCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Webhook,
        )

    async def retrieve(
        self,
        webhook_external_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Webhook:
        """
        Retrieve, update, or delete a single webhook.

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
        return await self._get(
            path_template("/ext/v3/webhooks/{webhook_external_id}/", webhook_external_id=webhook_external_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Webhook,
        )

    async def update(
        self,
        webhook_external_id: str,
        *,
        subscriptions: Iterable[WebhookSubscriptionRequestParam],
        url: str,
        enabled: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Webhook:
        """
        Retrieve, update, or delete a single webhook.

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
        return await self._put(
            path_template("/ext/v3/webhooks/{webhook_external_id}/", webhook_external_id=webhook_external_id),
            body=await async_maybe_transform(
                {
                    "subscriptions": subscriptions,
                    "url": url,
                    "enabled": enabled,
                },
                webhook_update_params.WebhookUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Webhook,
        )

    def list(
        self,
        *,
        next_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[Webhook, AsyncNextKey[Webhook]]:
        """
        List and create webhooks for the active profile.

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
            "/ext/v3/webhooks/",
            page=AsyncNextKey[Webhook],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"next_key": next_key}, webhook_list_params.WebhookListParams),
            ),
            model=Webhook,
        )

    async def delete(
        self,
        webhook_external_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Retrieve, update, or delete a single webhook.

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
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/ext/v3/webhooks/{webhook_external_id}/", webhook_external_id=webhook_external_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def partial_update(
        self,
        webhook_external_id: str,
        *,
        enabled: bool | Omit = omit,
        subscriptions: Iterable[WebhookSubscriptionRequestParam] | Omit = omit,
        url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Webhook:
        """
        Retrieve, update, or delete a single webhook.

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
        return await self._patch(
            path_template("/ext/v3/webhooks/{webhook_external_id}/", webhook_external_id=webhook_external_id),
            body=await async_maybe_transform(
                {
                    "enabled": enabled,
                    "subscriptions": subscriptions,
                    "url": url,
                },
                webhook_partial_update_params.WebhookPartialUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Webhook,
        )

    async def regenerate_secret(
        self,
        webhook_external_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebhookRegenerateSecretResponse:
        """Rotate the secret.

        The new value is returned once and never shown again.

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
        return await self._post(
            path_template(
                "/ext/v3/webhooks/{webhook_external_id}/regenerate_secret/", webhook_external_id=webhook_external_id
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WebhookRegenerateSecretResponse,
        )

    async def retrieve_event_types(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Return all available webhook event types."""
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            "/ext/v3/webhooks/event_types/",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class WebhooksResourceWithRawResponse:
    def __init__(self, webhooks: WebhooksResource) -> None:
        self._webhooks = webhooks

        self.create = to_raw_response_wrapper(
            webhooks.create,
        )
        self.retrieve = to_raw_response_wrapper(
            webhooks.retrieve,
        )
        self.update = to_raw_response_wrapper(
            webhooks.update,
        )
        self.list = to_raw_response_wrapper(
            webhooks.list,
        )
        self.delete = to_raw_response_wrapper(
            webhooks.delete,
        )
        self.partial_update = to_raw_response_wrapper(
            webhooks.partial_update,
        )
        self.regenerate_secret = to_raw_response_wrapper(
            webhooks.regenerate_secret,
        )
        self.retrieve_event_types = to_raw_response_wrapper(
            webhooks.retrieve_event_types,
        )

    @cached_property
    def deliveries(self) -> DeliveriesResourceWithRawResponse:
        return DeliveriesResourceWithRawResponse(self._webhooks.deliveries)

    @cached_property
    def subscriptions(self) -> SubscriptionsResourceWithRawResponse:
        return SubscriptionsResourceWithRawResponse(self._webhooks.subscriptions)


class AsyncWebhooksResourceWithRawResponse:
    def __init__(self, webhooks: AsyncWebhooksResource) -> None:
        self._webhooks = webhooks

        self.create = async_to_raw_response_wrapper(
            webhooks.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            webhooks.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            webhooks.update,
        )
        self.list = async_to_raw_response_wrapper(
            webhooks.list,
        )
        self.delete = async_to_raw_response_wrapper(
            webhooks.delete,
        )
        self.partial_update = async_to_raw_response_wrapper(
            webhooks.partial_update,
        )
        self.regenerate_secret = async_to_raw_response_wrapper(
            webhooks.regenerate_secret,
        )
        self.retrieve_event_types = async_to_raw_response_wrapper(
            webhooks.retrieve_event_types,
        )

    @cached_property
    def deliveries(self) -> AsyncDeliveriesResourceWithRawResponse:
        return AsyncDeliveriesResourceWithRawResponse(self._webhooks.deliveries)

    @cached_property
    def subscriptions(self) -> AsyncSubscriptionsResourceWithRawResponse:
        return AsyncSubscriptionsResourceWithRawResponse(self._webhooks.subscriptions)


class WebhooksResourceWithStreamingResponse:
    def __init__(self, webhooks: WebhooksResource) -> None:
        self._webhooks = webhooks

        self.create = to_streamed_response_wrapper(
            webhooks.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            webhooks.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            webhooks.update,
        )
        self.list = to_streamed_response_wrapper(
            webhooks.list,
        )
        self.delete = to_streamed_response_wrapper(
            webhooks.delete,
        )
        self.partial_update = to_streamed_response_wrapper(
            webhooks.partial_update,
        )
        self.regenerate_secret = to_streamed_response_wrapper(
            webhooks.regenerate_secret,
        )
        self.retrieve_event_types = to_streamed_response_wrapper(
            webhooks.retrieve_event_types,
        )

    @cached_property
    def deliveries(self) -> DeliveriesResourceWithStreamingResponse:
        return DeliveriesResourceWithStreamingResponse(self._webhooks.deliveries)

    @cached_property
    def subscriptions(self) -> SubscriptionsResourceWithStreamingResponse:
        return SubscriptionsResourceWithStreamingResponse(self._webhooks.subscriptions)


class AsyncWebhooksResourceWithStreamingResponse:
    def __init__(self, webhooks: AsyncWebhooksResource) -> None:
        self._webhooks = webhooks

        self.create = async_to_streamed_response_wrapper(
            webhooks.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            webhooks.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            webhooks.update,
        )
        self.list = async_to_streamed_response_wrapper(
            webhooks.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            webhooks.delete,
        )
        self.partial_update = async_to_streamed_response_wrapper(
            webhooks.partial_update,
        )
        self.regenerate_secret = async_to_streamed_response_wrapper(
            webhooks.regenerate_secret,
        )
        self.retrieve_event_types = async_to_streamed_response_wrapper(
            webhooks.retrieve_event_types,
        )

    @cached_property
    def deliveries(self) -> AsyncDeliveriesResourceWithStreamingResponse:
        return AsyncDeliveriesResourceWithStreamingResponse(self._webhooks.deliveries)

    @cached_property
    def subscriptions(self) -> AsyncSubscriptionsResourceWithStreamingResponse:
        return AsyncSubscriptionsResourceWithStreamingResponse(self._webhooks.subscriptions)
