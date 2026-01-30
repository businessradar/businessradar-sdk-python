# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["PortfolioCompanyDetailRequest"]


class PortfolioCompanyDetailRequest(BaseModel):
    """### Portfolio Company Detail (Simplified)

    A lightweight data structure for company identification (UUID, DUNS, Name, Country).
    """

    external_id: str
