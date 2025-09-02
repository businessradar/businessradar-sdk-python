# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Portfolio"]


class Portfolio(BaseModel):
    external_id: str

    name: str

    customer_reference: Optional[str] = None
    """Customer reference for the client to understand relationship."""

    default_permission: Optional[Literal["view_only", "write", "admin", "owner", ""]] = None
    """Default permission for all users in organization.

    - `view_only` - Only Viewing Access
    - `write` - View and Write Access
    - `admin` - View, Write and Admin Access
    - `owner` - Portfolio Owner
    """
