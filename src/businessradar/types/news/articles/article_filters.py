# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["ArticleFilters"]


class ArticleFilters(BaseModel):
    """### Article Filters

    Used to validate and process filters for article searches. Supports filtering by
    query text, countries, languages, specific companies (DUNS), and portfolios.
    """

    categories: Optional[List[str]] = None

    companies: Optional[List[str]] = None

    countries: Optional[List[str]] = None

    disable_company_article_deduplication: Optional[bool] = None

    duns_numbers: Optional[List[str]] = None

    global_ultimates: Optional[List[str]] = None

    include_clustered_articles: Optional[bool] = None

    industries: Optional[List[str]] = None

    is_material: Optional[bool] = None

    languages: Optional[List[str]] = None

    max_creation_date: Optional[datetime] = None

    max_publication_date: Optional[datetime] = None

    media_type: Optional[Literal["GAZETTE", "MAINSTREAM"]] = None

    min_creation_date: Optional[datetime] = None

    min_publication_date: Optional[datetime] = None

    parent_category: Optional[str] = None

    portfolios: Optional[List[str]] = None

    query: Optional[str] = None

    registration_numbers: Optional[List[str]] = None

    sentiment: Optional[bool] = None
