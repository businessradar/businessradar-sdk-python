# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from businessradar import BusinessRadar, AsyncBusinessRadar
from businessradar.types import ComplianceCreateResponse, ComplianceRetrieveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCompliance:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: BusinessRadar) -> None:
        compliance = client.compliance.create(
            company_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ComplianceCreateResponse, compliance, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: BusinessRadar) -> None:
        compliance = client.compliance.create(
            company_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            all_entities_screening_enabled=True,
            directors_screening_enabled=True,
            ownership_screening_threshold=0,
        )
        assert_matches_type(ComplianceCreateResponse, compliance, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: BusinessRadar) -> None:
        response = client.compliance.with_raw_response.create(
            company_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        compliance = response.parse()
        assert_matches_type(ComplianceCreateResponse, compliance, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: BusinessRadar) -> None:
        with client.compliance.with_streaming_response.create(
            company_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            compliance = response.parse()
            assert_matches_type(ComplianceCreateResponse, compliance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: BusinessRadar) -> None:
        compliance = client.compliance.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ComplianceRetrieveResponse, compliance, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: BusinessRadar) -> None:
        response = client.compliance.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        compliance = response.parse()
        assert_matches_type(ComplianceRetrieveResponse, compliance, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: BusinessRadar) -> None:
        with client.compliance.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            compliance = response.parse()
            assert_matches_type(ComplianceRetrieveResponse, compliance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: BusinessRadar) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `external_id` but received ''"):
            client.compliance.with_raw_response.retrieve(
                "",
            )


class TestAsyncCompliance:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncBusinessRadar) -> None:
        compliance = await async_client.compliance.create(
            company_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ComplianceCreateResponse, compliance, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncBusinessRadar) -> None:
        compliance = await async_client.compliance.create(
            company_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            all_entities_screening_enabled=True,
            directors_screening_enabled=True,
            ownership_screening_threshold=0,
        )
        assert_matches_type(ComplianceCreateResponse, compliance, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncBusinessRadar) -> None:
        response = await async_client.compliance.with_raw_response.create(
            company_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        compliance = await response.parse()
        assert_matches_type(ComplianceCreateResponse, compliance, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncBusinessRadar) -> None:
        async with async_client.compliance.with_streaming_response.create(
            company_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            compliance = await response.parse()
            assert_matches_type(ComplianceCreateResponse, compliance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncBusinessRadar) -> None:
        compliance = await async_client.compliance.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ComplianceRetrieveResponse, compliance, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncBusinessRadar) -> None:
        response = await async_client.compliance.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        compliance = await response.parse()
        assert_matches_type(ComplianceRetrieveResponse, compliance, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncBusinessRadar) -> None:
        async with async_client.compliance.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            compliance = await response.parse()
            assert_matches_type(ComplianceRetrieveResponse, compliance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncBusinessRadar) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `external_id` but received ''"):
            await async_client.compliance.with_raw_response.retrieve(
                "",
            )
