# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .portfolio import Portfolio

__all__ = ["PortfolioListResponse"]


class PortfolioListResponse(BaseModel):
    next_key: Optional[str] = None
    """
    The next_key is an cursor used to make it possible to paginate to the next
    results, pass this next_key onto the next request to retrieve next results.
    """

    results: Optional[List[Portfolio]] = None

    total_results: Optional[float] = None
    """Total amount of results available"""
