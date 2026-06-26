# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from businessradar import BusinessRadar, AsyncBusinessRadar
from businessradar.types import (
    Webhook,
    WebhookRegenerateSecretResponse,
)
from businessradar.pagination import SyncNextKey, AsyncNextKey

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestWebhooks:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: BusinessRadar) -> None:
        webhook = client.webhooks.create(
            subscriptions=[{"event_type": "compliance_check.status_changed"}],
            url="https://example.com",
        )
        assert_matches_type(Webhook, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: BusinessRadar) -> None:
        webhook = client.webhooks.create(
            subscriptions=[
                {
                    "event_type": "compliance_check.status_changed",
                    "portfolio": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                }
            ],
            url="https://example.com",
            enabled=True,
        )
        assert_matches_type(Webhook, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: BusinessRadar) -> None:
        response = client.webhooks.with_raw_response.create(
            subscriptions=[{"event_type": "compliance_check.status_changed"}],
            url="https://example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert_matches_type(Webhook, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: BusinessRadar) -> None:
        with client.webhooks.with_streaming_response.create(
            subscriptions=[{"event_type": "compliance_check.status_changed"}],
            url="https://example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert_matches_type(Webhook, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: BusinessRadar) -> None:
        webhook = client.webhooks.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Webhook, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: BusinessRadar) -> None:
        response = client.webhooks.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert_matches_type(Webhook, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: BusinessRadar) -> None:
        with client.webhooks.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert_matches_type(Webhook, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: BusinessRadar) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `webhook_external_id` but received ''"):
            client.webhooks.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: BusinessRadar) -> None:
        webhook = client.webhooks.update(
            webhook_external_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            subscriptions=[{"event_type": "compliance_check.status_changed"}],
            url="https://example.com",
        )
        assert_matches_type(Webhook, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: BusinessRadar) -> None:
        webhook = client.webhooks.update(
            webhook_external_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            subscriptions=[
                {
                    "event_type": "compliance_check.status_changed",
                    "portfolio": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                }
            ],
            url="https://example.com",
            enabled=True,
        )
        assert_matches_type(Webhook, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: BusinessRadar) -> None:
        response = client.webhooks.with_raw_response.update(
            webhook_external_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            subscriptions=[{"event_type": "compliance_check.status_changed"}],
            url="https://example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert_matches_type(Webhook, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: BusinessRadar) -> None:
        with client.webhooks.with_streaming_response.update(
            webhook_external_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            subscriptions=[{"event_type": "compliance_check.status_changed"}],
            url="https://example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert_matches_type(Webhook, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: BusinessRadar) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `webhook_external_id` but received ''"):
            client.webhooks.with_raw_response.update(
                webhook_external_id="",
                subscriptions=[{"event_type": "compliance_check.status_changed"}],
                url="https://example.com",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: BusinessRadar) -> None:
        webhook = client.webhooks.list()
        assert_matches_type(SyncNextKey[Webhook], webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: BusinessRadar) -> None:
        webhook = client.webhooks.list(
            next_key="next_key",
        )
        assert_matches_type(SyncNextKey[Webhook], webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: BusinessRadar) -> None:
        response = client.webhooks.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert_matches_type(SyncNextKey[Webhook], webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: BusinessRadar) -> None:
        with client.webhooks.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert_matches_type(SyncNextKey[Webhook], webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: BusinessRadar) -> None:
        webhook = client.webhooks.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert webhook is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: BusinessRadar) -> None:
        response = client.webhooks.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert webhook is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: BusinessRadar) -> None:
        with client.webhooks.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert webhook is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: BusinessRadar) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `webhook_external_id` but received ''"):
            client.webhooks.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_partial_update(self, client: BusinessRadar) -> None:
        webhook = client.webhooks.partial_update(
            webhook_external_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Webhook, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_partial_update_with_all_params(self, client: BusinessRadar) -> None:
        webhook = client.webhooks.partial_update(
            webhook_external_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            enabled=True,
            subscriptions=[
                {
                    "event_type": "compliance_check.status_changed",
                    "portfolio": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                }
            ],
            url="https://example.com",
        )
        assert_matches_type(Webhook, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_partial_update(self, client: BusinessRadar) -> None:
        response = client.webhooks.with_raw_response.partial_update(
            webhook_external_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert_matches_type(Webhook, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_partial_update(self, client: BusinessRadar) -> None:
        with client.webhooks.with_streaming_response.partial_update(
            webhook_external_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert_matches_type(Webhook, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_partial_update(self, client: BusinessRadar) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `webhook_external_id` but received ''"):
            client.webhooks.with_raw_response.partial_update(
                webhook_external_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_regenerate_secret(self, client: BusinessRadar) -> None:
        webhook = client.webhooks.regenerate_secret(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(WebhookRegenerateSecretResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_regenerate_secret(self, client: BusinessRadar) -> None:
        response = client.webhooks.with_raw_response.regenerate_secret(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert_matches_type(WebhookRegenerateSecretResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_regenerate_secret(self, client: BusinessRadar) -> None:
        with client.webhooks.with_streaming_response.regenerate_secret(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert_matches_type(WebhookRegenerateSecretResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_regenerate_secret(self, client: BusinessRadar) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `webhook_external_id` but received ''"):
            client.webhooks.with_raw_response.regenerate_secret(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_event_types(self, client: BusinessRadar) -> None:
        webhook = client.webhooks.retrieve_event_types()
        assert webhook is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_event_types(self, client: BusinessRadar) -> None:
        response = client.webhooks.with_raw_response.retrieve_event_types()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert webhook is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_event_types(self, client: BusinessRadar) -> None:
        with client.webhooks.with_streaming_response.retrieve_event_types() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert webhook is None

        assert cast(Any, response.is_closed) is True


class TestAsyncWebhooks:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncBusinessRadar) -> None:
        webhook = await async_client.webhooks.create(
            subscriptions=[{"event_type": "compliance_check.status_changed"}],
            url="https://example.com",
        )
        assert_matches_type(Webhook, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncBusinessRadar) -> None:
        webhook = await async_client.webhooks.create(
            subscriptions=[
                {
                    "event_type": "compliance_check.status_changed",
                    "portfolio": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                }
            ],
            url="https://example.com",
            enabled=True,
        )
        assert_matches_type(Webhook, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncBusinessRadar) -> None:
        response = await async_client.webhooks.with_raw_response.create(
            subscriptions=[{"event_type": "compliance_check.status_changed"}],
            url="https://example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert_matches_type(Webhook, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncBusinessRadar) -> None:
        async with async_client.webhooks.with_streaming_response.create(
            subscriptions=[{"event_type": "compliance_check.status_changed"}],
            url="https://example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert_matches_type(Webhook, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncBusinessRadar) -> None:
        webhook = await async_client.webhooks.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Webhook, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncBusinessRadar) -> None:
        response = await async_client.webhooks.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert_matches_type(Webhook, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncBusinessRadar) -> None:
        async with async_client.webhooks.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert_matches_type(Webhook, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncBusinessRadar) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `webhook_external_id` but received ''"):
            await async_client.webhooks.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncBusinessRadar) -> None:
        webhook = await async_client.webhooks.update(
            webhook_external_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            subscriptions=[{"event_type": "compliance_check.status_changed"}],
            url="https://example.com",
        )
        assert_matches_type(Webhook, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncBusinessRadar) -> None:
        webhook = await async_client.webhooks.update(
            webhook_external_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            subscriptions=[
                {
                    "event_type": "compliance_check.status_changed",
                    "portfolio": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                }
            ],
            url="https://example.com",
            enabled=True,
        )
        assert_matches_type(Webhook, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncBusinessRadar) -> None:
        response = await async_client.webhooks.with_raw_response.update(
            webhook_external_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            subscriptions=[{"event_type": "compliance_check.status_changed"}],
            url="https://example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert_matches_type(Webhook, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncBusinessRadar) -> None:
        async with async_client.webhooks.with_streaming_response.update(
            webhook_external_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            subscriptions=[{"event_type": "compliance_check.status_changed"}],
            url="https://example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert_matches_type(Webhook, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncBusinessRadar) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `webhook_external_id` but received ''"):
            await async_client.webhooks.with_raw_response.update(
                webhook_external_id="",
                subscriptions=[{"event_type": "compliance_check.status_changed"}],
                url="https://example.com",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncBusinessRadar) -> None:
        webhook = await async_client.webhooks.list()
        assert_matches_type(AsyncNextKey[Webhook], webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncBusinessRadar) -> None:
        webhook = await async_client.webhooks.list(
            next_key="next_key",
        )
        assert_matches_type(AsyncNextKey[Webhook], webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncBusinessRadar) -> None:
        response = await async_client.webhooks.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert_matches_type(AsyncNextKey[Webhook], webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncBusinessRadar) -> None:
        async with async_client.webhooks.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert_matches_type(AsyncNextKey[Webhook], webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncBusinessRadar) -> None:
        webhook = await async_client.webhooks.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert webhook is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncBusinessRadar) -> None:
        response = await async_client.webhooks.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert webhook is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncBusinessRadar) -> None:
        async with async_client.webhooks.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert webhook is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncBusinessRadar) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `webhook_external_id` but received ''"):
            await async_client.webhooks.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_partial_update(self, async_client: AsyncBusinessRadar) -> None:
        webhook = await async_client.webhooks.partial_update(
            webhook_external_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Webhook, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_partial_update_with_all_params(self, async_client: AsyncBusinessRadar) -> None:
        webhook = await async_client.webhooks.partial_update(
            webhook_external_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            enabled=True,
            subscriptions=[
                {
                    "event_type": "compliance_check.status_changed",
                    "portfolio": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                }
            ],
            url="https://example.com",
        )
        assert_matches_type(Webhook, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_partial_update(self, async_client: AsyncBusinessRadar) -> None:
        response = await async_client.webhooks.with_raw_response.partial_update(
            webhook_external_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert_matches_type(Webhook, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_partial_update(self, async_client: AsyncBusinessRadar) -> None:
        async with async_client.webhooks.with_streaming_response.partial_update(
            webhook_external_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert_matches_type(Webhook, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_partial_update(self, async_client: AsyncBusinessRadar) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `webhook_external_id` but received ''"):
            await async_client.webhooks.with_raw_response.partial_update(
                webhook_external_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_regenerate_secret(self, async_client: AsyncBusinessRadar) -> None:
        webhook = await async_client.webhooks.regenerate_secret(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(WebhookRegenerateSecretResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_regenerate_secret(self, async_client: AsyncBusinessRadar) -> None:
        response = await async_client.webhooks.with_raw_response.regenerate_secret(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert_matches_type(WebhookRegenerateSecretResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_regenerate_secret(self, async_client: AsyncBusinessRadar) -> None:
        async with async_client.webhooks.with_streaming_response.regenerate_secret(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert_matches_type(WebhookRegenerateSecretResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_regenerate_secret(self, async_client: AsyncBusinessRadar) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `webhook_external_id` but received ''"):
            await async_client.webhooks.with_raw_response.regenerate_secret(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_event_types(self, async_client: AsyncBusinessRadar) -> None:
        webhook = await async_client.webhooks.retrieve_event_types()
        assert webhook is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_event_types(self, async_client: AsyncBusinessRadar) -> None:
        response = await async_client.webhooks.with_raw_response.retrieve_event_types()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert webhook is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_event_types(self, async_client: AsyncBusinessRadar) -> None:
        async with async_client.webhooks.with_streaming_response.retrieve_event_types() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert webhook is None

        assert cast(Any, response.is_closed) is True
