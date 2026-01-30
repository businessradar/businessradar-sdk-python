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
    """
    The next_key is an cursor used to make it possible to paginate to the next
    results, pass the next_key from the previous request to retrieve next results.
    """

    order: Literal["asc", "desc"]
    """Sorting order"""

    result_type: Literal["adverse_media", "enforcement", "govt_owned", "pep", "sanction"]
    """Filter by result type"""

    sorting: Literal["confidence", "created_at", "source_date"]
    """Sorting field"""
