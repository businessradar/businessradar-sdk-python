# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["PortfolioCompanyDetailRequest"]


class PortfolioCompanyDetailRequest(TypedDict, total=False):
    """### Portfolio Company Detail (Simplified)

    A lightweight data structure for company identification (UUID, DUNS, Name, Country).
    """

    external_id: Required[str]
