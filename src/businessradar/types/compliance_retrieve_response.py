# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .compliance_entity_retrieve import ComplianceEntityRetrieve

__all__ = ["ComplianceRetrieveResponse"]


class ComplianceRetrieveResponse(BaseModel):
    entities: List[ComplianceEntityRetrieve]

    external_id: str

    progress: float

    activity_score: Optional[Literal["low", "medium", "high", ""]] = None

    adverse_media_score: Optional[Literal["low", "medium", "high", ""]] = None

    compliance_score: Optional[Literal["low", "medium", "high", ""]] = None

    country_score: Optional[Literal["low", "medium", "high", ""]] = None

    name: Optional[str] = None
    """Custom name for this compliance check."""

    pep_score: Optional[Literal["low", "medium", "high", ""]] = None

    sanction_score: Optional[Literal["low", "medium", "high", ""]] = None

    status: Optional[Literal["pending", "queued", "in_progress", "searching_directors", "completed", "failed"]] = None
    """
    - `pending` - Pending
    - `queued` - Queued
    - `in_progress` - In Progress
    - `searching_directors` - Searching Directors
    - `completed` - Completed
    - `failed` - Failed
    """
