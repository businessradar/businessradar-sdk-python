# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from ...._types import SequenceNotStr
from ...._utils import PropertyInfo

__all__ = ["AnalyticsGetCountByDateParams"]


class AnalyticsGetCountByDateParams(TypedDict, total=False):
    category: SequenceNotStr[str]
    """Filter by article Category IDs (UUIDs)."""

    company: SequenceNotStr[str]
    """Filter by internal Company UUIDs."""

    country: SequenceNotStr[str]
    """Filter by ISO 2-letter Country Codes (e.g., 'US', 'GB')."""

    disable_company_article_deduplication: bool
    """
    By default, companies with the same trade names are grouped and the best match
    is selected. Enable this to see all associated companies.
    """

    duns_number: SequenceNotStr[str]
    """Filter by one or more 9-digit Dun & Bradstreet Numbers."""

    global_ultimate: SequenceNotStr[str]
    """Filter by Global Ultimate DUNS Numbers."""

    include_clustered_articles: bool
    """Include articles that are part of a cluster (reprints or similar articles)."""

    interval: Literal["day", "month", "week", "year"]
    """The time interval for aggregation."""

    is_material: bool
    """Filter by materiality flag (relevance to business risk)."""

    language: SequenceNotStr[str]
    """Filter by ISO 2-letter Language Codes (e.g., 'en', 'nl')."""

    max_creation_date: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Filter articles added to our database at or before this date/time."""

    max_publication_date: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Filter articles published at or before this date/time."""

    min_creation_date: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Filter articles added to our database at or after this date/time."""

    min_publication_date: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Filter articles published at or after this date/time."""

    portfolio_id: SequenceNotStr[str]
    """Filter articles related to companies in specific Portfolios (UUIDs)."""

    query: str
    """Full-text search query for filtering articles by content."""

    registration_number: SequenceNotStr[str]
    """Filter by local company registration numbers."""

    saved_article_filter_id: str
    """Apply a previously saved set of article filters (UUID)."""

    sentiment: bool
    """Filter by sentiment: `true` for positive, `false` for negative."""
