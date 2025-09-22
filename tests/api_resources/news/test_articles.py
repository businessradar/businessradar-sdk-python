# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from businessradar import BusinessRadar, AsyncBusinessRadar
from businessradar._utils import parse_datetime
from businessradar.pagination import SyncNextKey, AsyncNextKey
from businessradar.types.news import (
    Article,
    ArticleCreateFeedbackResponse,
    ArticleRetrieveRelatedResponse,
    ArticleListSavedArticleFiltersResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestArticles:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: BusinessRadar) -> None:
        article = client.news.articles.list()
        assert_matches_type(SyncNextKey[Article], article, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: BusinessRadar) -> None:
        article = client.news.articles.list(
            category=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            company=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            country=["string"],
            duns_number=["string"],
            global_ultimate=["string"],
            include_clustered_articles=True,
            language=["string"],
            max_creation_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            max_publication_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            min_creation_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            min_publication_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            next_key="next_key",
            portfolio_id=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            query="query",
            registration_number=["string"],
            saved_article_filter_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            sentiment=True,
            sorting="creation_date",
            sorting_order="asc",
        )
        assert_matches_type(SyncNextKey[Article], article, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: BusinessRadar) -> None:
        response = client.news.articles.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        article = response.parse()
        assert_matches_type(SyncNextKey[Article], article, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: BusinessRadar) -> None:
        with client.news.articles.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            article = response.parse()
            assert_matches_type(SyncNextKey[Article], article, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_feedback(self, client: BusinessRadar) -> None:
        article = client.news.articles.create_feedback(
            article="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ArticleCreateFeedbackResponse, article, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_feedback_with_all_params(self, client: BusinessRadar) -> None:
        article = client.news.articles.create_feedback(
            article="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            comment="comment",
            email="dev@stainless.com",
            feedback_type="false_positive",
        )
        assert_matches_type(ArticleCreateFeedbackResponse, article, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_feedback(self, client: BusinessRadar) -> None:
        response = client.news.articles.with_raw_response.create_feedback(
            article="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        article = response.parse()
        assert_matches_type(ArticleCreateFeedbackResponse, article, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_feedback(self, client: BusinessRadar) -> None:
        with client.news.articles.with_streaming_response.create_feedback(
            article="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            article = response.parse()
            assert_matches_type(ArticleCreateFeedbackResponse, article, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_saved_article_filters(self, client: BusinessRadar) -> None:
        article = client.news.articles.list_saved_article_filters()
        assert_matches_type(SyncNextKey[ArticleListSavedArticleFiltersResponse], article, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_saved_article_filters_with_all_params(self, client: BusinessRadar) -> None:
        article = client.news.articles.list_saved_article_filters(
            next_key="next_key",
        )
        assert_matches_type(SyncNextKey[ArticleListSavedArticleFiltersResponse], article, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list_saved_article_filters(self, client: BusinessRadar) -> None:
        response = client.news.articles.with_raw_response.list_saved_article_filters()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        article = response.parse()
        assert_matches_type(SyncNextKey[ArticleListSavedArticleFiltersResponse], article, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list_saved_article_filters(self, client: BusinessRadar) -> None:
        with client.news.articles.with_streaming_response.list_saved_article_filters() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            article = response.parse()
            assert_matches_type(SyncNextKey[ArticleListSavedArticleFiltersResponse], article, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_related(self, client: BusinessRadar) -> None:
        article = client.news.articles.retrieve_related(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ArticleRetrieveRelatedResponse, article, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve_related(self, client: BusinessRadar) -> None:
        response = client.news.articles.with_raw_response.retrieve_related(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        article = response.parse()
        assert_matches_type(ArticleRetrieveRelatedResponse, article, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_related(self, client: BusinessRadar) -> None:
        with client.news.articles.with_streaming_response.retrieve_related(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            article = response.parse()
            assert_matches_type(ArticleRetrieveRelatedResponse, article, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve_related(self, client: BusinessRadar) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `article_id` but received ''"):
            client.news.articles.with_raw_response.retrieve_related(
                "",
            )


class TestAsyncArticles:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncBusinessRadar) -> None:
        article = await async_client.news.articles.list()
        assert_matches_type(AsyncNextKey[Article], article, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncBusinessRadar) -> None:
        article = await async_client.news.articles.list(
            category=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            company=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            country=["string"],
            duns_number=["string"],
            global_ultimate=["string"],
            include_clustered_articles=True,
            language=["string"],
            max_creation_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            max_publication_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            min_creation_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            min_publication_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            next_key="next_key",
            portfolio_id=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            query="query",
            registration_number=["string"],
            saved_article_filter_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            sentiment=True,
            sorting="creation_date",
            sorting_order="asc",
        )
        assert_matches_type(AsyncNextKey[Article], article, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncBusinessRadar) -> None:
        response = await async_client.news.articles.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        article = await response.parse()
        assert_matches_type(AsyncNextKey[Article], article, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncBusinessRadar) -> None:
        async with async_client.news.articles.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            article = await response.parse()
            assert_matches_type(AsyncNextKey[Article], article, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_feedback(self, async_client: AsyncBusinessRadar) -> None:
        article = await async_client.news.articles.create_feedback(
            article="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ArticleCreateFeedbackResponse, article, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_feedback_with_all_params(self, async_client: AsyncBusinessRadar) -> None:
        article = await async_client.news.articles.create_feedback(
            article="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            comment="comment",
            email="dev@stainless.com",
            feedback_type="false_positive",
        )
        assert_matches_type(ArticleCreateFeedbackResponse, article, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_feedback(self, async_client: AsyncBusinessRadar) -> None:
        response = await async_client.news.articles.with_raw_response.create_feedback(
            article="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        article = await response.parse()
        assert_matches_type(ArticleCreateFeedbackResponse, article, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_feedback(self, async_client: AsyncBusinessRadar) -> None:
        async with async_client.news.articles.with_streaming_response.create_feedback(
            article="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            article = await response.parse()
            assert_matches_type(ArticleCreateFeedbackResponse, article, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_saved_article_filters(self, async_client: AsyncBusinessRadar) -> None:
        article = await async_client.news.articles.list_saved_article_filters()
        assert_matches_type(AsyncNextKey[ArticleListSavedArticleFiltersResponse], article, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_saved_article_filters_with_all_params(self, async_client: AsyncBusinessRadar) -> None:
        article = await async_client.news.articles.list_saved_article_filters(
            next_key="next_key",
        )
        assert_matches_type(AsyncNextKey[ArticleListSavedArticleFiltersResponse], article, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list_saved_article_filters(self, async_client: AsyncBusinessRadar) -> None:
        response = await async_client.news.articles.with_raw_response.list_saved_article_filters()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        article = await response.parse()
        assert_matches_type(AsyncNextKey[ArticleListSavedArticleFiltersResponse], article, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list_saved_article_filters(self, async_client: AsyncBusinessRadar) -> None:
        async with async_client.news.articles.with_streaming_response.list_saved_article_filters() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            article = await response.parse()
            assert_matches_type(AsyncNextKey[ArticleListSavedArticleFiltersResponse], article, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_related(self, async_client: AsyncBusinessRadar) -> None:
        article = await async_client.news.articles.retrieve_related(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ArticleRetrieveRelatedResponse, article, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_related(self, async_client: AsyncBusinessRadar) -> None:
        response = await async_client.news.articles.with_raw_response.retrieve_related(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        article = await response.parse()
        assert_matches_type(ArticleRetrieveRelatedResponse, article, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_related(self, async_client: AsyncBusinessRadar) -> None:
        async with async_client.news.articles.with_streaming_response.retrieve_related(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            article = await response.parse()
            assert_matches_type(ArticleRetrieveRelatedResponse, article, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve_related(self, async_client: AsyncBusinessRadar) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `article_id` but received ''"):
            await async_client.news.articles.with_raw_response.retrieve_related(
                "",
            )
