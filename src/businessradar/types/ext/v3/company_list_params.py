# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import TypedDict

__all__ = ["CompanyListParams"]


class CompanyListParams(TypedDict, total=False):
    country: List[str]
    """ISO 2-letter Country Code"""

    duns_number: List[str]
    """9-digit Dun And Bradstreet Number"""

    next_key: str
    """
    The next_key is an cursor used to make it possible to paginate to the next
    results, pass the next_key from the previous request to retrieve next results.
    """

    portfolio_id: List[str]
    """Portfolio ID to filter companies"""

    query: str
    """Custom search query to text search all companies."""

    registration_number: List[str]
    """Local Registration Number"""

    website_url: str
    """Website URL to search"""
