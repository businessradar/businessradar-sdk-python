# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from businessradar import Businessradar, AsyncBusinessradar
from businessradar._utils import parse_datetime
from businessradar.types.news.articles import AnalyticsGetCountByDateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAnalytics:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_count_by_date(self, client: Businessradar) -> None:
        analytics = client.news.articles.analytics.get_count_by_date()
        assert_matches_type(AnalyticsGetCountByDateResponse, analytics, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_count_by_date_with_all_params(self, client: Businessradar) -> None:
        analytics = client.news.articles.analytics.get_count_by_date(
            category=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            company=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            country=["string"],
            duns_number=["string"],
            global_ultimate=["string"],
            include_clustered_articles=True,
            interval="day",
            language=["string"],
            max_creation_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            max_publication_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            min_creation_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            min_publication_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            portfolio_id=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            query="query",
            registration_number=["string"],
            saved_article_filter_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            sentiment=True,
        )
        assert_matches_type(AnalyticsGetCountByDateResponse, analytics, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_count_by_date(self, client: Businessradar) -> None:
        response = client.news.articles.analytics.with_raw_response.get_count_by_date()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        analytics = response.parse()
        assert_matches_type(AnalyticsGetCountByDateResponse, analytics, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_count_by_date(self, client: Businessradar) -> None:
        with client.news.articles.analytics.with_streaming_response.get_count_by_date() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            analytics = response.parse()
            assert_matches_type(AnalyticsGetCountByDateResponse, analytics, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAnalytics:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_count_by_date(self, async_client: AsyncBusinessradar) -> None:
        analytics = await async_client.news.articles.analytics.get_count_by_date()
        assert_matches_type(AnalyticsGetCountByDateResponse, analytics, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_count_by_date_with_all_params(self, async_client: AsyncBusinessradar) -> None:
        analytics = await async_client.news.articles.analytics.get_count_by_date(
            category=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            company=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            country=["string"],
            duns_number=["string"],
            global_ultimate=["string"],
            include_clustered_articles=True,
            interval="day",
            language=["string"],
            max_creation_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            max_publication_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            min_creation_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            min_publication_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            portfolio_id=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            query="query",
            registration_number=["string"],
            saved_article_filter_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            sentiment=True,
        )
        assert_matches_type(AnalyticsGetCountByDateResponse, analytics, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_count_by_date(self, async_client: AsyncBusinessradar) -> None:
        response = await async_client.news.articles.analytics.with_raw_response.get_count_by_date()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        analytics = await response.parse()
        assert_matches_type(AnalyticsGetCountByDateResponse, analytics, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_count_by_date(self, async_client: AsyncBusinessradar) -> None:
        async with async_client.news.articles.analytics.with_streaming_response.get_count_by_date() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            analytics = await response.parse()
            assert_matches_type(AnalyticsGetCountByDateResponse, analytics, path=["response"])

        assert cast(Any, response.is_closed) is True
