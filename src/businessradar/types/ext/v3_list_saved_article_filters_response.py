# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["V3ListSavedArticleFiltersResponse", "Result"]


class Result(BaseModel):
    external_id: str

    name: str


class V3ListSavedArticleFiltersResponse(BaseModel):
    next_key: Optional[str] = None
    """
    The next_key is an cursor used to make it possible to paginate to the next
    results, pass this next_key onto the next request to retrieve next results.
    """

    results: Optional[List[Result]] = None

    total_results: Optional[float] = None
    """Total amount of results available"""
