# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from businessradar import Businessradar, AsyncBusinessradar
from businessradar.types import Registration
from businessradar.types.portfolios import CompanyListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCompanies:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Businessradar) -> None:
        company = client.portfolios.companies.create(
            portfolio_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Registration, company, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Businessradar) -> None:
        company = client.portfolios.companies.create(
            portfolio_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
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
    def test_raw_response_create(self, client: Businessradar) -> None:
        response = client.portfolios.companies.with_raw_response.create(
            portfolio_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        company = response.parse()
        assert_matches_type(Registration, company, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Businessradar) -> None:
        with client.portfolios.companies.with_streaming_response.create(
            portfolio_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            company = response.parse()
            assert_matches_type(Registration, company, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_create(self, client: Businessradar) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `portfolio_id` but received ''"):
            client.portfolios.companies.with_raw_response.create(
                portfolio_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Businessradar) -> None:
        company = client.portfolios.companies.list(
            portfolio_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(CompanyListResponse, company, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Businessradar) -> None:
        company = client.portfolios.companies.list(
            portfolio_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            next_key="next_key",
        )
        assert_matches_type(CompanyListResponse, company, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Businessradar) -> None:
        response = client.portfolios.companies.with_raw_response.list(
            portfolio_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        company = response.parse()
        assert_matches_type(CompanyListResponse, company, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Businessradar) -> None:
        with client.portfolios.companies.with_streaming_response.list(
            portfolio_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            company = response.parse()
            assert_matches_type(CompanyListResponse, company, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Businessradar) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `portfolio_id` but received ''"):
            client.portfolios.companies.with_raw_response.list(
                portfolio_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: Businessradar) -> None:
        company = client.portfolios.companies.delete(
            external_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            portfolio_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert company is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Businessradar) -> None:
        response = client.portfolios.companies.with_raw_response.delete(
            external_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            portfolio_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        company = response.parse()
        assert company is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Businessradar) -> None:
        with client.portfolios.companies.with_streaming_response.delete(
            external_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            portfolio_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            company = response.parse()
            assert company is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Businessradar) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `portfolio_id` but received ''"):
            client.portfolios.companies.with_raw_response.delete(
                external_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                portfolio_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `external_id` but received ''"):
            client.portfolios.companies.with_raw_response.delete(
                external_id="",
                portfolio_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )


class TestAsyncCompanies:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncBusinessradar) -> None:
        company = await async_client.portfolios.companies.create(
            portfolio_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Registration, company, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncBusinessradar) -> None:
        company = await async_client.portfolios.companies.create(
            portfolio_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
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
    async def test_raw_response_create(self, async_client: AsyncBusinessradar) -> None:
        response = await async_client.portfolios.companies.with_raw_response.create(
            portfolio_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        company = await response.parse()
        assert_matches_type(Registration, company, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncBusinessradar) -> None:
        async with async_client.portfolios.companies.with_streaming_response.create(
            portfolio_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            company = await response.parse()
            assert_matches_type(Registration, company, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncBusinessradar) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `portfolio_id` but received ''"):
            await async_client.portfolios.companies.with_raw_response.create(
                portfolio_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncBusinessradar) -> None:
        company = await async_client.portfolios.companies.list(
            portfolio_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(CompanyListResponse, company, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncBusinessradar) -> None:
        company = await async_client.portfolios.companies.list(
            portfolio_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            next_key="next_key",
        )
        assert_matches_type(CompanyListResponse, company, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncBusinessradar) -> None:
        response = await async_client.portfolios.companies.with_raw_response.list(
            portfolio_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        company = await response.parse()
        assert_matches_type(CompanyListResponse, company, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncBusinessradar) -> None:
        async with async_client.portfolios.companies.with_streaming_response.list(
            portfolio_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            company = await response.parse()
            assert_matches_type(CompanyListResponse, company, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncBusinessradar) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `portfolio_id` but received ''"):
            await async_client.portfolios.companies.with_raw_response.list(
                portfolio_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncBusinessradar) -> None:
        company = await async_client.portfolios.companies.delete(
            external_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            portfolio_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert company is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncBusinessradar) -> None:
        response = await async_client.portfolios.companies.with_raw_response.delete(
            external_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            portfolio_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        company = await response.parse()
        assert company is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncBusinessradar) -> None:
        async with async_client.portfolios.companies.with_streaming_response.delete(
            external_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            portfolio_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            company = await response.parse()
            assert company is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncBusinessradar) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `portfolio_id` but received ''"):
            await async_client.portfolios.companies.with_raw_response.delete(
                external_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                portfolio_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `external_id` but received ''"):
            await async_client.portfolios.companies.with_raw_response.delete(
                external_id="",
                portfolio_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )
