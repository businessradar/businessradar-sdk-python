# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["CompanyListResponse", "IndustryCode"]


class IndustryCode(BaseModel):
    code: str

    description: str


class CompanyListResponse(BaseModel):
    address_place: str

    address_postal: str

    address_region: str

    address_street: str

    country: str

    duns_number: str

    external_id: Optional[str] = None

    industry_codes: List[IndustryCode]

    name: str

    social_logo: Optional[str] = None

    website_icon_url: Optional[str] = None
