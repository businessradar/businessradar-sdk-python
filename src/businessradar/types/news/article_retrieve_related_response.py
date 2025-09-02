# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import TypeAlias

from ..._models import BaseModel

__all__ = ["ArticleRetrieveRelatedResponse", "ArticleRetrieveRelatedResponseItem"]


class ArticleRetrieveRelatedResponseItem(BaseModel):
    article: "Article"
    """Custom Serializer for the Article Model."""

    distance: float


ArticleRetrieveRelatedResponse: TypeAlias = List[ArticleRetrieveRelatedResponseItem]

from .article import Article
