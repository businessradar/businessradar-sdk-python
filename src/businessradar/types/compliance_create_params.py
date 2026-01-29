# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["ComplianceCreateParams"]


class ComplianceCreateParams(TypedDict, total=False):
    all_entities_screening_enabled: bool
    """If enabled all found entities UBOs, directors, shareholders will be screened.

    This can have an high cost impact.
    """

    company_id: Optional[str]

    directors_screening_enabled: bool

    ownership_screening_threshold: float
