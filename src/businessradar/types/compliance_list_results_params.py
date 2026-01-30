# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["ComplianceListResultsParams"]


class ComplianceListResultsParams(TypedDict, total=False):
    entity: str
    """Filter by entity external ID"""

    min_confidence: float
    """Filter by minimum confidence score (0.0 - 1.0)"""

    next_key: str
    """A cursor value used for pagination.

    Include the `next_key` value from your previous request to retrieve the
    subsequent page of results. If this value is `null`, the first page of results
    is returned.
    """

    order: Literal["asc", "desc"]
    """Sorting order"""

    result_type: Literal["adverse_media", "enforcement", "govt_owned", "pep", "sanction"]
    """Filter by result type"""

    sorting: Literal["confidence", "created_at", "source_date"]
    """Sorting field"""
