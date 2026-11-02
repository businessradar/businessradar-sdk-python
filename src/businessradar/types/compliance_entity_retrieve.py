# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .ubo import Ubo
from .._models import BaseModel

__all__ = ["ComplianceEntityRetrieve", "Director", "DirectorManagementResponsibility"]


class DirectorManagementResponsibility(BaseModel):
    description: str

    mrc_code: str = FieldInfo(alias="mrcCode")


class Director(BaseModel):
    """Custom Serializer for the Director Model."""

    created_at: datetime

    full_name: str

    management_responsibilities: List[DirectorManagementResponsibility]

    source_name: str
    """Get Source Name."""

    updated_at: datetime

    external_id: Optional[str] = None

    first_name: Optional[str] = None

    gender: Optional[Literal["M", "F", ""]] = None

    inactive_since: Optional[datetime] = None
    """Indicate if the director is no longer active for this company."""

    is_most_senior: Optional[bool] = None

    last_name: Optional[str] = None

    middle_name: Optional[str] = None

    role_group: Optional[Literal["BOARD", "MANAGEMENT", "OFFICER", "OTHER"]] = None
    """
    - `BOARD` - Board
    - `MANAGEMENT` - Management
    - `OFFICER` - Officer / Signatory
    - `OTHER` - Other
    """

    title: Optional[str] = None
    """Function title within this organization."""

    url: Optional[str] = None


class ComplianceEntityRetrieve(BaseModel):
    adverse_media_monitoring_enabled: bool

    aliases: List[str]

    director: Optional[Director] = None
    """Custom Serializer for the Director Model."""

    entity_role: str

    entity_type: Literal["individual", "company", "vessel"]
    """
    - `individual` - Individual
    - `company` - Company
    - `vessel` - Vessel
    """

    external_id: str

    name: str

    sanction_monitoring_enabled: bool

    ubo: Optional[Ubo] = None

    country: Optional[str] = None

    date_of_birth: Optional[str] = None

    gender: Optional[Literal["male", "female", ""]] = None

    status: Optional[Literal["on_hold", "queued", "in_progress", "completed", "skipped", "failed"]] = None
    """
    - `on_hold` - On Hold
    - `queued` - Queued
    - `in_progress` - In Progress
    - `completed` - Completed
    - `skipped` - Skipped
    - `failed` - Failed
    """
