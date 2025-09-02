# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["ArticleListResponse"]


class ArticleListResponse(BaseModel):
    next_key: Optional[str] = None
    """
    The next_key is an cursor used to make it possible to paginate to the next
    results, pass this next_key onto the next request to retrieve next results.
    """

    results: Optional[List["Article"]] = None

    total_results: Optional[float] = None
    """Total amount of results available"""


from .article import Article
