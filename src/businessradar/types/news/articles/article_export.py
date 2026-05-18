# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ...._models import BaseModel
from .article_filters import ArticleFilters
from .data_export_file_type import DataExportFileType

__all__ = ["ArticleExport"]


class ArticleExport(BaseModel):
    """Data Export Serializer."""

    created_at: datetime

    export_type: Literal["NEWS", "BINDER", "COMPANIES", "REGISTRATIONS", "COMPLIANCE", "BILLING", "KEY_EVENTS"]
    """
    - `NEWS` - News
    - `BINDER` - Binder
    - `COMPANIES` - Companies
    - `REGISTRATIONS` - Registrations
    - `COMPLIANCE` - Compliance
    - `BILLING` - Billing
    - `KEY_EVENTS` - Key Events
    """

    external_id: str

    file_type: DataExportFileType
    """
    - `PDF` - PDF
    - `EXCEL` - Excel
    - `JSONL` - JSONL
    """

    filters: ArticleFilters
    """### Article Filters

    Used to validate and process filters for article searches. Supports filtering by
    query text, countries, languages, specific companies (DUNS), and portfolios.
    """

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
