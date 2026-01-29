# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import date
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ComplianceRetrieveResponse", "Entity", "EntityUbo"]


class EntityUbo(BaseModel):
    name: str

    beneficial_ownership_percentage: Optional[float] = None

    birth_date: Optional[date] = None

    degree_of_separation: Optional[int] = None

    direct_ownership_percentage: Optional[float] = None

    implied_beneficial_ownership_percentage: Optional[float] = None

    implied_direct_ownership_percentage: Optional[float] = None

    implied_indirect_ownership_percentage: Optional[float] = None

    indirect_ownership_percentage: Optional[float] = None

    is_beneficiary: Optional[bool] = None

    is_person_with_significant_control: Optional[bool] = None


class Entity(BaseModel):
    entity_role: Literal["ubo", "director", "company", "manually_added"]
    """
    - `ubo` - Ultimate Beneficial Owner
    - `director` - Director
    - `company` - Company
    - `manually_added` - Manually added
    """

    entity_type: Literal["individual", "company"]
    """
    - `individual` - Individual
    - `company` - Company
    """

    external_id: str

    name: str

    status: Literal["on_hold", "queued", "in_progress", "completed", "skipped", "failed"]
    """
    - `on_hold` - On Hold
    - `queued` - Queued
    - `in_progress` - In Progress
    - `completed` - Completed
    - `skipped` - Skipped
    - `failed` - Failed
    """

    ubo: Optional[EntityUbo] = None

    country: Optional[str] = None

    gender: Optional[Literal["male", "female", ""]] = None


class ComplianceRetrieveResponse(BaseModel):
    entities: List[Entity]

    external_id: str

    progress: float

    activity_score: Optional[Literal["low", "medium", "high", ""]] = None

    adverse_media_score: Optional[Literal["low", "medium", "high", ""]] = None

    compliance_score: Optional[Literal["low", "medium", "high", ""]] = None

    country_score: Optional[Literal["low", "medium", "high", ""]] = None

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
