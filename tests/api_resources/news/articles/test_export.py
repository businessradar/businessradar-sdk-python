# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from businessradar import Businessradar, AsyncBusinessradar
from businessradar._utils import parse_datetime
from businessradar.types.news.articles import ArticleExport

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestExport:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Businessradar) -> None:
        export = client.news.articles.export.create(
            file_type="PDF",
            filters={},
        )
        assert_matches_type(ArticleExport, export, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Businessradar) -> None:
        export = client.news.articles.export.create(
            file_type="PDF",
            filters={
                "categories": ["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
                "companies": ["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
                "countries": ["xx"],
                "duns_numbers": ["xxxxxxxx"],
                "global_ultimates": ["xxxxxxxx"],
                "include_clustered_articles": True,
                "industries": ["x"],
                "languages": ["xx"],
                "max_creation_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                "max_publication_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                "media_type": "GAZETTE",
                "min_creation_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                "min_publication_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                "parent_category": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "portfolios": ["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
                "query": "query",
                "registration_numbers": ["x"],
                "sentiment": True,
            },
        )
        assert_matches_type(ArticleExport, export, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Businessradar) -> None:
        response = client.news.articles.export.with_raw_response.create(
            file_type="PDF",
            filters={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        export = response.parse()
        assert_matches_type(ArticleExport, export, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Businessradar) -> None:
        with client.news.articles.export.with_streaming_response.create(
            file_type="PDF",
            filters={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            export = response.parse()
            assert_matches_type(ArticleExport, export, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Businessradar) -> None:
        export = client.news.articles.export.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ArticleExport, export, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Businessradar) -> None:
        response = client.news.articles.export.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        export = response.parse()
        assert_matches_type(ArticleExport, export, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Businessradar) -> None:
        with client.news.articles.export.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            export = response.parse()
            assert_matches_type(ArticleExport, export, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Businessradar) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `external_id` but received ''"):
            client.news.articles.export.with_raw_response.retrieve(
                "",
            )


class TestAsyncExport:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncBusinessradar) -> None:
        export = await async_client.news.articles.export.create(
            file_type="PDF",
            filters={},
        )
        assert_matches_type(ArticleExport, export, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncBusinessradar) -> None:
        export = await async_client.news.articles.export.create(
            file_type="PDF",
            filters={
                "categories": ["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
                "companies": ["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
                "countries": ["xx"],
                "duns_numbers": ["xxxxxxxx"],
                "global_ultimates": ["xxxxxxxx"],
                "include_clustered_articles": True,
                "industries": ["x"],
                "languages": ["xx"],
                "max_creation_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                "max_publication_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                "media_type": "GAZETTE",
                "min_creation_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                "min_publication_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                "parent_category": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "portfolios": ["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
                "query": "query",
                "registration_numbers": ["x"],
                "sentiment": True,
            },
        )
        assert_matches_type(ArticleExport, export, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncBusinessradar) -> None:
        response = await async_client.news.articles.export.with_raw_response.create(
            file_type="PDF",
            filters={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        export = await response.parse()
        assert_matches_type(ArticleExport, export, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncBusinessradar) -> None:
        async with async_client.news.articles.export.with_streaming_response.create(
            file_type="PDF",
            filters={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            export = await response.parse()
            assert_matches_type(ArticleExport, export, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncBusinessradar) -> None:
        export = await async_client.news.articles.export.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ArticleExport, export, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncBusinessradar) -> None:
        response = await async_client.news.articles.export.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        export = await response.parse()
        assert_matches_type(ArticleExport, export, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncBusinessradar) -> None:
        async with async_client.news.articles.export.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            export = await response.parse()
            assert_matches_type(ArticleExport, export, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncBusinessradar) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `external_id` but received ''"):
            await async_client.news.articles.export.with_raw_response.retrieve(
                "",
            )
