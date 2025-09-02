# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from businessradar import BusinessRadar, AsyncBusinessRadar
from businessradar.types import (
    Registration,
    CompanyListResponse,
    CompanyRetrieveResponse,
)
from businessradar.pagination import SyncNextKey, AsyncNextKey

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCompanies:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: BusinessRadar) -> None:
        company = client.companies.create()
        assert_matches_type(Registration, company, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: BusinessRadar) -> None:
        company = client.companies.create(
            company={"external_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"},
            country="AF",
            customer_reference="customer_reference",
            duns_number="duns_number",
            primary_name="primary_name",
            registration_number="registration_number",
        )
        assert_matches_type(Registration, company, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: BusinessRadar) -> None:
        response = client.companies.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        company = response.parse()
        assert_matches_type(Registration, company, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: BusinessRadar) -> None:
        with client.companies.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            company = response.parse()
            assert_matches_type(Registration, company, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: BusinessRadar) -> None:
        company = client.companies.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(CompanyRetrieveResponse, company, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: BusinessRadar) -> None:
        response = client.companies.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        company = response.parse()
        assert_matches_type(CompanyRetrieveResponse, company, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: BusinessRadar) -> None:
        with client.companies.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            company = response.parse()
            assert_matches_type(CompanyRetrieveResponse, company, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: BusinessRadar) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `external_id` but received ''"):
            client.companies.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: BusinessRadar) -> None:
        company = client.companies.list()
        assert_matches_type(SyncNextKey[CompanyListResponse], company, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: BusinessRadar) -> None:
        company = client.companies.list(
            country=["string"],
            duns_number=["string"],
            next_key="next_key",
            portfolio_id=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            query="query",
            registration_number=["string"],
            website_url="website_url",
        )
        assert_matches_type(SyncNextKey[CompanyListResponse], company, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: BusinessRadar) -> None:
        response = client.companies.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        company = response.parse()
        assert_matches_type(SyncNextKey[CompanyListResponse], company, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: BusinessRadar) -> None:
        with client.companies.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            company = response.parse()
            assert_matches_type(SyncNextKey[CompanyListResponse], company, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_registration(self, client: BusinessRadar) -> None:
        company = client.companies.retrieve_registration(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Registration, company, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve_registration(self, client: BusinessRadar) -> None:
        response = client.companies.with_raw_response.retrieve_registration(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        company = response.parse()
        assert_matches_type(Registration, company, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_registration(self, client: BusinessRadar) -> None:
        with client.companies.with_streaming_response.retrieve_registration(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            company = response.parse()
            assert_matches_type(Registration, company, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve_registration(self, client: BusinessRadar) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `registration_id` but received ''"):
            client.companies.with_raw_response.retrieve_registration(
                "",
            )


class TestAsyncCompanies:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncBusinessRadar) -> None:
        company = await async_client.companies.create()
        assert_matches_type(Registration, company, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncBusinessRadar) -> None:
        company = await async_client.companies.create(
            company={"external_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"},
            country="AF",
            customer_reference="customer_reference",
            duns_number="duns_number",
            primary_name="primary_name",
            registration_number="registration_number",
        )
        assert_matches_type(Registration, company, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncBusinessRadar) -> None:
        response = await async_client.companies.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        company = await response.parse()
        assert_matches_type(Registration, company, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncBusinessRadar) -> None:
        async with async_client.companies.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            company = await response.parse()
            assert_matches_type(Registration, company, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncBusinessRadar) -> None:
        company = await async_client.companies.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(CompanyRetrieveResponse, company, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncBusinessRadar) -> None:
        response = await async_client.companies.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        company = await response.parse()
        assert_matches_type(CompanyRetrieveResponse, company, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncBusinessRadar) -> None:
        async with async_client.companies.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            company = await response.parse()
            assert_matches_type(CompanyRetrieveResponse, company, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncBusinessRadar) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `external_id` but received ''"):
            await async_client.companies.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncBusinessRadar) -> None:
        company = await async_client.companies.list()
        assert_matches_type(AsyncNextKey[CompanyListResponse], company, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncBusinessRadar) -> None:
        company = await async_client.companies.list(
            country=["string"],
            duns_number=["string"],
            next_key="next_key",
            portfolio_id=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            query="query",
            registration_number=["string"],
            website_url="website_url",
        )
        assert_matches_type(AsyncNextKey[CompanyListResponse], company, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncBusinessRadar) -> None:
        response = await async_client.companies.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        company = await response.parse()
        assert_matches_type(AsyncNextKey[CompanyListResponse], company, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncBusinessRadar) -> None:
        async with async_client.companies.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            company = await response.parse()
            assert_matches_type(AsyncNextKey[CompanyListResponse], company, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_registration(self, async_client: AsyncBusinessRadar) -> None:
        company = await async_client.companies.retrieve_registration(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Registration, company, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_registration(self, async_client: AsyncBusinessRadar) -> None:
        response = await async_client.companies.with_raw_response.retrieve_registration(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        company = await response.parse()
        assert_matches_type(Registration, company, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_registration(self, async_client: AsyncBusinessRadar) -> None:
        async with async_client.companies.with_streaming_response.retrieve_registration(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            company = await response.parse()
            assert_matches_type(Registration, company, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve_registration(self, async_client: AsyncBusinessRadar) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `registration_id` but received ''"):
            await async_client.companies.with_raw_response.retrieve_registration(
                "",
            )
