# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["CompanyMatchResponse", "IndustryCode"]


class IndustryCode(BaseModel):
    code: str

    description: str


class CompanyMatchResponse(BaseModel):
    """### Universal Company Data

    Handles company data from both internal and external sources (e.g., Dun &
    Bradstreet). Provides a unified representation of a company.

    - **DUNS Number**: Unique 9-digit identifier. - **External ID**: Internal unique
    identifier if the company is registered. - **Industry Codes**: List of industry
    classifications.
    """

    address_place: str

    address_postal: str

    address_region: str

    address_street: str

    country: str

    duns_number: Optional[str] = None

    external_id: Optional[str] = None

    industry_codes: List[IndustryCode]

    name: str

    social_logo: Optional[str] = None

    website_icon_url: Optional[str] = None

    is_out_of_business: Optional[bool] = None

    registration_candidate_id: Optional[str] = None
    """Reference number for this company.

    Always present. Pass it as `registration_candidate_id` to POST /companies or
    POST /portfolios/{id}/companies to register it.
    """

    ticker_symbol: Optional[str] = None
