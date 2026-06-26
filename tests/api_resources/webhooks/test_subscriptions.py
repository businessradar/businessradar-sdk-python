# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from businessradar import BusinessRadar, AsyncBusinessRadar
from businessradar.types import WebhookSubscription
from businessradar.pagination import SyncNextKey, AsyncNextKey

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSubscriptions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: BusinessRadar) -> None:
        subscription = client.webhooks.subscriptions.create(
            webhook_external_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            event_type="compliance_check.status_changed",
        )
        assert_matches_type(WebhookSubscription, subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: BusinessRadar) -> None:
        subscription = client.webhooks.subscriptions.create(
            webhook_external_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            event_type="compliance_check.status_changed",
            portfolio="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(WebhookSubscription, subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: BusinessRadar) -> None:
        response = client.webhooks.subscriptions.with_raw_response.create(
            webhook_external_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            event_type="compliance_check.status_changed",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert_matches_type(WebhookSubscription, subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: BusinessRadar) -> None:
        with client.webhooks.subscriptions.with_streaming_response.create(
            webhook_external_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            event_type="compliance_check.status_changed",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = response.parse()
            assert_matches_type(WebhookSubscription, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create(self, client: BusinessRadar) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `webhook_external_id` but received ''"):
            client.webhooks.subscriptions.with_raw_response.create(
                webhook_external_id="",
                event_type="compliance_check.status_changed",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: BusinessRadar) -> None:
        subscription = client.webhooks.subscriptions.list(
            webhook_external_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SyncNextKey[WebhookSubscription], subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: BusinessRadar) -> None:
        subscription = client.webhooks.subscriptions.list(
            webhook_external_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            next_key="next_key",
        )
        assert_matches_type(SyncNextKey[WebhookSubscription], subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: BusinessRadar) -> None:
        response = client.webhooks.subscriptions.with_raw_response.list(
            webhook_external_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert_matches_type(SyncNextKey[WebhookSubscription], subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: BusinessRadar) -> None:
        with client.webhooks.subscriptions.with_streaming_response.list(
            webhook_external_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = response.parse()
            assert_matches_type(SyncNextKey[WebhookSubscription], subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: BusinessRadar) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `webhook_external_id` but received ''"):
            client.webhooks.subscriptions.with_raw_response.list(
                webhook_external_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: BusinessRadar) -> None:
        subscription = client.webhooks.subscriptions.delete(
            subscription_external_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            webhook_external_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert subscription is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: BusinessRadar) -> None:
        response = client.webhooks.subscriptions.with_raw_response.delete(
            subscription_external_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            webhook_external_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert subscription is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: BusinessRadar) -> None:
        with client.webhooks.subscriptions.with_streaming_response.delete(
            subscription_external_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            webhook_external_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = response.parse()
            assert subscription is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: BusinessRadar) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `webhook_external_id` but received ''"):
            client.webhooks.subscriptions.with_raw_response.delete(
                subscription_external_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                webhook_external_id="",
            )

        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `subscription_external_id` but received ''"
        ):
            client.webhooks.subscriptions.with_raw_response.delete(
                subscription_external_id="",
                webhook_external_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )


class TestAsyncSubscriptions:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncBusinessRadar) -> None:
        subscription = await async_client.webhooks.subscriptions.create(
            webhook_external_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            event_type="compliance_check.status_changed",
        )
        assert_matches_type(WebhookSubscription, subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncBusinessRadar) -> None:
        subscription = await async_client.webhooks.subscriptions.create(
            webhook_external_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            event_type="compliance_check.status_changed",
            portfolio="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(WebhookSubscription, subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncBusinessRadar) -> None:
        response = await async_client.webhooks.subscriptions.with_raw_response.create(
            webhook_external_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            event_type="compliance_check.status_changed",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = await response.parse()
        assert_matches_type(WebhookSubscription, subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncBusinessRadar) -> None:
        async with async_client.webhooks.subscriptions.with_streaming_response.create(
            webhook_external_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            event_type="compliance_check.status_changed",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = await response.parse()
            assert_matches_type(WebhookSubscription, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncBusinessRadar) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `webhook_external_id` but received ''"):
            await async_client.webhooks.subscriptions.with_raw_response.create(
                webhook_external_id="",
                event_type="compliance_check.status_changed",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncBusinessRadar) -> None:
        subscription = await async_client.webhooks.subscriptions.list(
            webhook_external_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AsyncNextKey[WebhookSubscription], subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncBusinessRadar) -> None:
        subscription = await async_client.webhooks.subscriptions.list(
            webhook_external_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            next_key="next_key",
        )
        assert_matches_type(AsyncNextKey[WebhookSubscription], subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncBusinessRadar) -> None:
        response = await async_client.webhooks.subscriptions.with_raw_response.list(
            webhook_external_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = await response.parse()
        assert_matches_type(AsyncNextKey[WebhookSubscription], subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncBusinessRadar) -> None:
        async with async_client.webhooks.subscriptions.with_streaming_response.list(
            webhook_external_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = await response.parse()
            assert_matches_type(AsyncNextKey[WebhookSubscription], subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncBusinessRadar) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `webhook_external_id` but received ''"):
            await async_client.webhooks.subscriptions.with_raw_response.list(
                webhook_external_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncBusinessRadar) -> None:
        subscription = await async_client.webhooks.subscriptions.delete(
            subscription_external_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            webhook_external_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert subscription is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncBusinessRadar) -> None:
        response = await async_client.webhooks.subscriptions.with_raw_response.delete(
            subscription_external_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            webhook_external_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = await response.parse()
        assert subscription is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncBusinessRadar) -> None:
        async with async_client.webhooks.subscriptions.with_streaming_response.delete(
            subscription_external_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            webhook_external_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = await response.parse()
            assert subscription is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncBusinessRadar) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `webhook_external_id` but received ''"):
            await async_client.webhooks.subscriptions.with_raw_response.delete(
                subscription_external_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                webhook_external_id="",
            )

        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `subscription_external_id` but received ''"
        ):
            await async_client.webhooks.subscriptions.with_raw_response.delete(
                subscription_external_id="",
                webhook_external_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )
