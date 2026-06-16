# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["Ubo"]


class Ubo(BaseModel):
    name: str

    beneficial_ownership_percentage: Optional[float] = None

    birth_date: Optional[str] = None

    degree_of_separation: Optional[int] = None

    direct_ownership_percentage: Optional[float] = None

    implied_beneficial_ownership_percentage: Optional[float] = None

    implied_direct_ownership_percentage: Optional[float] = None

    implied_indirect_ownership_percentage: Optional[float] = None

    indirect_ownership_percentage: Optional[float] = None

    is_beneficiary: Optional[bool] = None

    is_person_with_significant_control: Optional[bool] = None
