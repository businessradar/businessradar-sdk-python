# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["AnalyticsGetCountByDateParams"]


class AnalyticsGetCountByDateParams(TypedDict, total=False):
    category: List[str]
    """Category ID to filter articles"""

    company: List[str]
    """Company ID's"""

    country: List[str]
    """ISO 2-letter Country Code"""

    duns_number: List[str]
    """9-digit Dun And Bradstreet Number"""

    global_ultimate: List[str]
    """9-digit Dun And Bradstreet Number"""

    include_clustered_articles: bool
    """Include clustered articles"""

    interval: Literal["day", "month", "week", "year"]

    language: List[str]
    """ISO 2-letter Language Code"""

    max_creation_date: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Filter articles created before this date"""

    max_publication_date: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Filter articles published before this date"""

    min_creation_date: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Filter articles created after this date"""

    min_publication_date: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Filter articles published after this date"""

    portfolio_id: List[str]
    """Portfolio ID to filter articles"""

    query: str
    """Custom search filters to text search all articles."""

    registration_number: List[str]
    """Local Registration Number"""

    saved_article_filter_id: str
    """Filter articles on already saved article filter id"""

    sentiment: bool
    """Filter articles with sentiment"""
