# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["CompanyListParams"]


class CompanyListParams(TypedDict, total=False):
    country: SequenceNotStr[str]
    """ISO 2-letter Country Code (e.g., NL, US)"""

    duns_number: SequenceNotStr[str]
    """9-digit Dun And Bradstreet Number (can be multiple)"""

    is_listed: bool
    """Filter on publicly listed companies (has a `ticker_symbol`)"""

    max_created_at: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Companies added at or before this time (inclusive).

    ISO 8601, UTC when no offset is given, millisecond precision. Cannot be combined
    with `query`.
    """

    max_updated_at: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Companies updated at or before this time (inclusive).

    ISO 8601, UTC when no offset is given, millisecond precision. Cannot be combined
    with `query`.
    """

    min_created_at: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Companies added at or after this time (inclusive).

    ISO 8601, UTC when no offset is given, millisecond precision. Cannot be combined
    with `query`.
    """

    min_updated_at: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Companies updated at or after this time (inclusive).

    ISO 8601, UTC when no offset is given, millisecond precision. Cannot be combined
    with `query`.
    """

    next_key: str
    """A cursor value used for pagination.

    Include the `next_key` value from your previous request to retrieve the
    subsequent page of results. If this value is `null`, the first page of results
    is returned.
    """

    page_size: int
    """Number of results per page.

    Default 50, max 100. Dun & Bradstreet results (no other filters besides
    `query`/`country`) are capped at 50 and do not support continuation.
    """

    portfolio_id: SequenceNotStr[str]
    """Filter companies belonging to specific Portfolio IDs (UUID)"""

    query: str
    """Custom search query to text search all companies."""

    registration_number: SequenceNotStr[str]
    """Local Registration Number (can be multiple)"""

    website_url: str
    """Website URL to search for the company"""
