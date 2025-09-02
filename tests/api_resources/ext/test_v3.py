# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from businessradar import Businessradar, AsyncBusinessradar
from businessradar.types.ext import (
    V3GetSchemaResponse,
    V3ListSavedArticleFiltersResponse,
)
from businessradar.types.ext.v3 import Registration

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestV3:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_registration(self, client: Businessradar) -> None:
        v3 = client.ext.v3.get_registration(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Registration, v3, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_registration(self, client: Businessradar) -> None:
        response = client.ext.v3.with_raw_response.get_registration(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v3 = response.parse()
        assert_matches_type(Registration, v3, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_registration(self, client: Businessradar) -> None:
        with client.ext.v3.with_streaming_response.get_registration(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v3 = response.parse()
            assert_matches_type(Registration, v3, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get_registration(self, client: Businessradar) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `registration_id` but received ''"):
            client.ext.v3.with_raw_response.get_registration(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_schema(self, client: Businessradar) -> None:
        v3 = client.ext.v3.get_schema()
        assert_matches_type(V3GetSchemaResponse, v3, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_schema_with_all_params(self, client: Businessradar) -> None:
        v3 = client.ext.v3.get_schema(
            format="json",
            lang="af",
        )
        assert_matches_type(V3GetSchemaResponse, v3, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_schema(self, client: Businessradar) -> None:
        response = client.ext.v3.with_raw_response.get_schema()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v3 = response.parse()
        assert_matches_type(V3GetSchemaResponse, v3, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_schema(self, client: Businessradar) -> None:
        with client.ext.v3.with_streaming_response.get_schema() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v3 = response.parse()
            assert_matches_type(V3GetSchemaResponse, v3, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_saved_article_filters(self, client: Businessradar) -> None:
        v3 = client.ext.v3.list_saved_article_filters()
        assert_matches_type(V3ListSavedArticleFiltersResponse, v3, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_saved_article_filters_with_all_params(self, client: Businessradar) -> None:
        v3 = client.ext.v3.list_saved_article_filters(
            next_key="next_key",
        )
        assert_matches_type(V3ListSavedArticleFiltersResponse, v3, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list_saved_article_filters(self, client: Businessradar) -> None:
        response = client.ext.v3.with_raw_response.list_saved_article_filters()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v3 = response.parse()
        assert_matches_type(V3ListSavedArticleFiltersResponse, v3, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list_saved_article_filters(self, client: Businessradar) -> None:
        with client.ext.v3.with_streaming_response.list_saved_article_filters() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v3 = response.parse()
            assert_matches_type(V3ListSavedArticleFiltersResponse, v3, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncV3:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_registration(self, async_client: AsyncBusinessradar) -> None:
        v3 = await async_client.ext.v3.get_registration(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Registration, v3, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_registration(self, async_client: AsyncBusinessradar) -> None:
        response = await async_client.ext.v3.with_raw_response.get_registration(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v3 = await response.parse()
        assert_matches_type(Registration, v3, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_registration(self, async_client: AsyncBusinessradar) -> None:
        async with async_client.ext.v3.with_streaming_response.get_registration(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v3 = await response.parse()
            assert_matches_type(Registration, v3, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get_registration(self, async_client: AsyncBusinessradar) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `registration_id` but received ''"):
            await async_client.ext.v3.with_raw_response.get_registration(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_schema(self, async_client: AsyncBusinessradar) -> None:
        v3 = await async_client.ext.v3.get_schema()
        assert_matches_type(V3GetSchemaResponse, v3, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_schema_with_all_params(self, async_client: AsyncBusinessradar) -> None:
        v3 = await async_client.ext.v3.get_schema(
            format="json",
            lang="af",
        )
        assert_matches_type(V3GetSchemaResponse, v3, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_schema(self, async_client: AsyncBusinessradar) -> None:
        response = await async_client.ext.v3.with_raw_response.get_schema()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v3 = await response.parse()
        assert_matches_type(V3GetSchemaResponse, v3, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_schema(self, async_client: AsyncBusinessradar) -> None:
        async with async_client.ext.v3.with_streaming_response.get_schema() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v3 = await response.parse()
            assert_matches_type(V3GetSchemaResponse, v3, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_saved_article_filters(self, async_client: AsyncBusinessradar) -> None:
        v3 = await async_client.ext.v3.list_saved_article_filters()
        assert_matches_type(V3ListSavedArticleFiltersResponse, v3, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_saved_article_filters_with_all_params(self, async_client: AsyncBusinessradar) -> None:
        v3 = await async_client.ext.v3.list_saved_article_filters(
            next_key="next_key",
        )
        assert_matches_type(V3ListSavedArticleFiltersResponse, v3, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list_saved_article_filters(self, async_client: AsyncBusinessradar) -> None:
        response = await async_client.ext.v3.with_raw_response.list_saved_article_filters()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v3 = await response.parse()
        assert_matches_type(V3ListSavedArticleFiltersResponse, v3, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list_saved_article_filters(self, async_client: AsyncBusinessradar) -> None:
        async with async_client.ext.v3.with_streaming_response.list_saved_article_filters() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v3 = await response.parse()
            assert_matches_type(V3ListSavedArticleFiltersResponse, v3, path=["response"])

        assert cast(Any, response.is_closed) is True
