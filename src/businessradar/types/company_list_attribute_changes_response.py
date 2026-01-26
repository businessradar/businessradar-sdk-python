# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["CompanyListAttributeChangesResponse"]


class CompanyListAttributeChangesResponse(BaseModel):
    """Company Attribute Change Serializer."""

    attribute: str

    company_external_id: str

    created_at: datetime

    new_value: Optional[str] = None

    old_value: Optional[str] = None
