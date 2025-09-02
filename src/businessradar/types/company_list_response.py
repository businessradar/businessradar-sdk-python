# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["CompanyListResponse", "Result", "ResultIndustryCode"]


class ResultIndustryCode(BaseModel):
    code: str

    description: str


class Result(BaseModel):
    address_place: str

    address_postal: str

    address_region: str

    address_street: str

    country: str

    duns_number: str

    external_id: Optional[str] = None

    industry_codes: List[ResultIndustryCode]

    name: str

    social_logo: Optional[str] = None

    website_icon_url: Optional[str] = None


class CompanyListResponse(BaseModel):
    next_key: Optional[str] = None
    """
    The next_key is an cursor used to make it possible to paginate to the next
    results, pass this next_key onto the next request to retrieve next results.
    """

    results: Optional[List[Result]] = None

    total_results: Optional[float] = None
    """Total amount of results available"""
