# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ...._models import BaseModel
from .data_export_file_type import DataExportFileType

__all__ = ["ArticleExport", "Filters"]


class Filters(BaseModel):
    categories: Optional[List[str]] = None

    companies: Optional[List[str]] = None

    countries: Optional[List[str]] = None

    duns_numbers: Optional[List[str]] = None

    global_ultimates: Optional[List[str]] = None

    include_clustered_articles: Optional[bool] = None

    industries: Optional[List[str]] = None

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


class ArticleExport(BaseModel):
    created_at: datetime

    export_type: Literal["NEWS", "BINDER", "COMPANIES", "REGISTRATIONS", "COMPLIANCE", "BILLING"]
    """
    - `NEWS` - News
    - `BINDER` - Binder
    - `COMPANIES` - Companies
    - `REGISTRATIONS` - Registrations
    - `COMPLIANCE` - Compliance
    - `BILLING` - Billing
    """

    external_id: str

    file_type: DataExportFileType
    """
    - `PDF` - PDF
    - `EXCEL` - Excel
    - `JSONL` - JSONL
    """

    filters: Filters
    """Article Filter Serializer."""

    location: Optional[str] = None
    """Location of exports"""

    result_count: Optional[int] = None

    status: Literal["pending", "in_progress", "failed", "finished"]
    """
    - `pending` - Pending
    - `in_progress` - In Progress
    - `failed` - Failed
    - `finished` - Finished
    """

    updated_at: datetime
