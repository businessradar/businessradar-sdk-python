# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import TypeAlias

from ..._models import BaseModel

__all__ = ["ArticleRetrieveRelatedResponse", "ArticleRetrieveRelatedResponseItem"]


class ArticleRetrieveRelatedResponseItem(BaseModel):
    """### Related Article

    An article that is semantically related to another, including a distance score
    indicating the degree of similarity.
    """

    article: "Article"
    """### Article

    The primary data structure for news articles. It provides comprehensive data,
    including: - Metadata (URLs, publication dates, languages, countries) - Content
    (titles, snippets, summaries - both original and translated) - Relationships
    (source, related companies, categories) - Analysis (sentiment, clustering
    status)
    """

    distance: float


ArticleRetrieveRelatedResponse: TypeAlias = List[ArticleRetrieveRelatedResponseItem]

from .article import Article
