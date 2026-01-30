# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from .._types import SequenceNotStr

__all__ = ["CompanyListParams"]


class CompanyListParams(TypedDict, total=False):
    country: SequenceNotStr[str]
    """ISO 2-letter Country Code (e.g., NL, US)"""

    duns_number: SequenceNotStr[str]
    """9-digit Dun And Bradstreet Number (can be multiple)"""

    next_key: str
    """A cursor value used for pagination.

    Include the `next_key` value from your previous request to retrieve the
    subsequent page of results. If this value is `null`, the first page of results
    is returned.
    """

    portfolio_id: SequenceNotStr[str]
    """Filter companies belonging to specific Portfolio IDs (UUID)"""

    query: str
    """Custom search query to text search all companies."""

    registration_number: SequenceNotStr[str]
    """Local Registration Number (can be multiple)"""

    website_url: str
    """Website URL to search for the company"""
