# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ComplianceListParams"]


class ComplianceListParams(TypedDict, total=False):
    adverse_media_monitoring_enabled: bool
    """
    Filter checks that have entities with adverse media monitoring enabled (pending
    or active).
    """

    compliance_score: Literal["high", "low", "medium"]
    """Filter by compliance score."""

    created_at_gte: Annotated[Union[str, datetime], PropertyInfo(alias="created_at__gte", format="iso8601")]
    """Filter checks created at or after this time."""

    created_at_lte: Annotated[Union[str, datetime], PropertyInfo(alias="created_at__lte", format="iso8601")]
    """Filter checks created at or before this time."""

    next_key: str
    """A cursor value used for pagination.

    Include the `next_key` value from your previous request to retrieve the
    subsequent page of results. If this value is `null`, the first page of results
    is returned.
    """

    order: Literal["asc", "desc"]
    """Sorting order."""

    results_changed_at_gte: Annotated[
        Union[str, datetime], PropertyInfo(alias="results_changed_at__gte", format="iso8601")
    ]
    """Filter checks with results changed at or after this time."""

    results_changed_at_lte: Annotated[
        Union[str, datetime], PropertyInfo(alias="results_changed_at__lte", format="iso8601")
    ]
    """Filter checks with results changed at or before this time."""

    sanction_monitoring_enabled: bool
    """
    Filter checks that have entities with sanction monitoring enabled (pending or
    active).
    """

    sorting: Literal["created_at", "finished_at", "results_changed_at"]
    """Sorting field."""

    status: Literal["completed", "failed", "in_progress", "pending", "queued", "searching_directors"]
    """Filter by compliance check status."""
