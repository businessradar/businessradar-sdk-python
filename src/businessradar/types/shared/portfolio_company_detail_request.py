# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["PortfolioCompanyDetailRequest"]


class PortfolioCompanyDetailRequest(BaseModel):
    """Portfolio Company Detail Serializer.

    Alternative serializer for the Company model which is limited.
    """

    external_id: str
