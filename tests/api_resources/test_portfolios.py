# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from businessradar import BusinessRadar, AsyncBusinessRadar
from businessradar.types import Portfolio
from businessradar.pagination import SyncNextKey, AsyncNextKey

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPortfolios:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: BusinessRadar) -> None:
        portfolio = client.portfolios.create(
            name="x",
        )
        assert_matches_type(Portfolio, portfolio, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: BusinessRadar) -> None:
        portfolio = client.portfolios.create(
            name="x",
            customer_reference="customer_reference",
            default_permission="view_only",
        )
        assert_matches_type(Portfolio, portfolio, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: BusinessRadar) -> None:
        response = client.portfolios.with_raw_response.create(
            name="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        portfolio = response.parse()
        assert_matches_type(Portfolio, portfolio, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: BusinessRadar) -> None:
        with client.portfolios.with_streaming_response.create(
            name="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            portfolio = response.parse()
            assert_matches_type(Portfolio, portfolio, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: BusinessRadar) -> None:
        portfolio = client.portfolios.list()
        assert_matches_type(SyncNextKey[Portfolio], portfolio, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: BusinessRadar) -> None:
        portfolio = client.portfolios.list(
            next_key="next_key",
        )
        assert_matches_type(SyncNextKey[Portfolio], portfolio, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: BusinessRadar) -> None:
        response = client.portfolios.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        portfolio = response.parse()
        assert_matches_type(SyncNextKey[Portfolio], portfolio, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: BusinessRadar) -> None:
        with client.portfolios.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            portfolio = response.parse()
            assert_matches_type(SyncNextKey[Portfolio], portfolio, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncPortfolios:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncBusinessRadar) -> None:
        portfolio = await async_client.portfolios.create(
            name="x",
        )
        assert_matches_type(Portfolio, portfolio, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncBusinessRadar) -> None:
        portfolio = await async_client.portfolios.create(
            name="x",
            customer_reference="customer_reference",
            default_permission="view_only",
        )
        assert_matches_type(Portfolio, portfolio, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncBusinessRadar) -> None:
        response = await async_client.portfolios.with_raw_response.create(
            name="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        portfolio = await response.parse()
        assert_matches_type(Portfolio, portfolio, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncBusinessRadar) -> None:
        async with async_client.portfolios.with_streaming_response.create(
            name="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            portfolio = await response.parse()
            assert_matches_type(Portfolio, portfolio, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncBusinessRadar) -> None:
        portfolio = await async_client.portfolios.list()
        assert_matches_type(AsyncNextKey[Portfolio], portfolio, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncBusinessRadar) -> None:
        portfolio = await async_client.portfolios.list(
            next_key="next_key",
        )
        assert_matches_type(AsyncNextKey[Portfolio], portfolio, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncBusinessRadar) -> None:
        response = await async_client.portfolios.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        portfolio = await response.parse()
        assert_matches_type(AsyncNextKey[Portfolio], portfolio, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncBusinessRadar) -> None:
        async with async_client.portfolios.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            portfolio = await response.parse()
            assert_matches_type(AsyncNextKey[Portfolio], portfolio, path=["response"])

        assert cast(Any, response.is_closed) is True
