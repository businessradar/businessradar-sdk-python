# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._types import SequenceNotStr
from ...._utils import PropertyInfo
from .data_export_file_type import DataExportFileType

__all__ = ["ExportCreateParams", "Filters"]


class ExportCreateParams(TypedDict, total=False):
    file_type: Required[DataExportFileType]
    """
    - `PDF` - PDF
    - `EXCEL` - Excel
    - `JSONL` - JSONL
    """

    filters: Required[Filters]
    """Article Filter Serializer."""


class Filters(TypedDict, total=False):
    """Article Filter Serializer."""

    categories: Optional[SequenceNotStr[str]]

    companies: Optional[SequenceNotStr[str]]

    countries: Optional[SequenceNotStr[str]]

    disable_company_article_deduplication: bool

    duns_numbers: Optional[SequenceNotStr[str]]

    global_ultimates: Optional[SequenceNotStr[str]]

    include_clustered_articles: bool

    industries: Optional[SequenceNotStr[str]]

    is_material: Optional[bool]

    languages: Optional[SequenceNotStr[str]]

    max_creation_date: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]

    max_publication_date: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]

    media_type: Optional[Literal["GAZETTE", "MAINSTREAM"]]

    min_creation_date: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]

    min_publication_date: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]

    parent_category: Optional[str]

    portfolios: Optional[SequenceNotStr[str]]

    query: Optional[str]

    registration_numbers: Optional[SequenceNotStr[str]]

    sentiment: Optional[bool]
