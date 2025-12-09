# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["CategoryTree"]


class CategoryTree(BaseModel):
    """Category Tree Structure."""

    name: str

    sub_categories: List["CategoryTree"]

    external_id: Optional[str] = None

    priority: Optional[int] = None
