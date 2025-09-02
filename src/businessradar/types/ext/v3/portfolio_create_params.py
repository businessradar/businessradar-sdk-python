# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["PortfolioCreateParams"]


class PortfolioCreateParams(TypedDict, total=False):
    name: Required[str]

    customer_reference: Optional[str]
    """Customer reference for the client to understand relationship."""

    default_permission: Optional[Literal["view_only", "write", "admin", "owner", ""]]
    """Default permission for all users in organization.

    - `view_only` - Only Viewing Access
    - `write` - View and Write Access
    - `admin` - View, Write and Admin Access
    - `owner` - Portfolio Owner
    """
