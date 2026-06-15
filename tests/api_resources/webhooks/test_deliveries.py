# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from businessradar import BusinessRadar, AsyncBusinessRadar
from businessradar.types import WebhookDelivery
from businessradar.pagination import SyncNextKey, AsyncNextKey

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDeliveries:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: BusinessRadar) -> None:
        delivery = client.webhooks.deliveries.list(
            webhook_external_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SyncNextKey[WebhookDelivery], delivery, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: BusinessRadar) -> None:
        delivery = client.webhooks.deliveries.list(
            webhook_external_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            next_key="next_key",
        )
        assert_matches_type(SyncNextKey[WebhookDelivery], delivery, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: BusinessRadar) -> None:
        response = client.webhooks.deliveries.with_raw_response.list(
            webhook_external_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        delivery = response.parse()
        assert_matches_type(SyncNextKey[WebhookDelivery], delivery, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: BusinessRadar) -> None:
        with client.webhooks.deliveries.with_streaming_response.list(
            webhook_external_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            delivery = response.parse()
            assert_matches_type(SyncNextKey[WebhookDelivery], delivery, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: BusinessRadar) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `webhook_external_id` but received ''"):
            client.webhooks.deliveries.with_raw_response.list(
                webhook_external_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_test(self, client: BusinessRadar) -> None:
        delivery = client.webhooks.deliveries.test(
            webhook_external_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(WebhookDelivery, delivery, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_test_with_all_params(self, client: BusinessRadar) -> None:
        delivery = client.webhooks.deliveries.test(
            webhook_external_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            event_type="compliance_check.status_changed",
        )
        assert_matches_type(WebhookDelivery, delivery, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_test(self, client: BusinessRadar) -> None:
        response = client.webhooks.deliveries.with_raw_response.test(
            webhook_external_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        delivery = response.parse()
        assert_matches_type(WebhookDelivery, delivery, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_test(self, client: BusinessRadar) -> None:
        with client.webhooks.deliveries.with_streaming_response.test(
            webhook_external_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            delivery = response.parse()
            assert_matches_type(WebhookDelivery, delivery, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_test(self, client: BusinessRadar) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `webhook_external_id` but received ''"):
            client.webhooks.deliveries.with_raw_response.test(
                webhook_external_id="",
            )


class TestAsyncDeliveries:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncBusinessRadar) -> None:
        delivery = await async_client.webhooks.deliveries.list(
            webhook_external_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AsyncNextKey[WebhookDelivery], delivery, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncBusinessRadar) -> None:
        delivery = await async_client.webhooks.deliveries.list(
            webhook_external_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            next_key="next_key",
        )
        assert_matches_type(AsyncNextKey[WebhookDelivery], delivery, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncBusinessRadar) -> None:
        response = await async_client.webhooks.deliveries.with_raw_response.list(
            webhook_external_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        delivery = await response.parse()
        assert_matches_type(AsyncNextKey[WebhookDelivery], delivery, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncBusinessRadar) -> None:
        async with async_client.webhooks.deliveries.with_streaming_response.list(
            webhook_external_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            delivery = await response.parse()
            assert_matches_type(AsyncNextKey[WebhookDelivery], delivery, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncBusinessRadar) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `webhook_external_id` but received ''"):
            await async_client.webhooks.deliveries.with_raw_response.list(
                webhook_external_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_test(self, async_client: AsyncBusinessRadar) -> None:
        delivery = await async_client.webhooks.deliveries.test(
            webhook_external_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(WebhookDelivery, delivery, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_test_with_all_params(self, async_client: AsyncBusinessRadar) -> None:
        delivery = await async_client.webhooks.deliveries.test(
            webhook_external_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            event_type="compliance_check.status_changed",
        )
        assert_matches_type(WebhookDelivery, delivery, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_test(self, async_client: AsyncBusinessRadar) -> None:
        response = await async_client.webhooks.deliveries.with_raw_response.test(
            webhook_external_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        delivery = await response.parse()
        assert_matches_type(WebhookDelivery, delivery, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_test(self, async_client: AsyncBusinessRadar) -> None:
        async with async_client.webhooks.deliveries.with_streaming_response.test(
            webhook_external_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            delivery = await response.parse()
            assert_matches_type(WebhookDelivery, delivery, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_test(self, async_client: AsyncBusinessRadar) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `webhook_external_id` but received ''"):
            await async_client.webhooks.deliveries.with_raw_response.test(
                webhook_external_id="",
            )
