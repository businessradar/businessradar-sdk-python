# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .ubo import Ubo
from .._models import BaseModel

__all__ = ["ComplianceEntityRetrieve"]


class ComplianceEntityRetrieve(BaseModel):
    adverse_media_monitoring_enabled: bool

    aliases: List[str]

    entity_role: str

    entity_type: Literal["individual", "company"]
    """
    - `individual` - Individual
    - `company` - Company
    """

    external_id: str

    name: str

    sanction_monitoring_enabled: bool

    status: Literal["on_hold", "queued", "in_progress", "completed", "skipped", "failed"]
    """
    - `on_hold` - On Hold
    - `queued` - Queued
    - `in_progress` - In Progress
    - `completed` - Completed
    - `skipped` - Skipped
    - `failed` - Failed
    """

    ubo: Optional[Ubo] = None

    country: Optional[str] = None

    date_of_birth: Optional[str] = None

    gender: Optional[Literal["male", "female", ""]] = None
