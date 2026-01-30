# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["ArticleListSavedArticleFiltersParams"]


class ArticleListSavedArticleFiltersParams(TypedDict, total=False):
    next_key: str
    """An opaque cursor value used for pagination.

    Pass the `next_key` received from a previous response to retrieve the next set
    of results.
    """
