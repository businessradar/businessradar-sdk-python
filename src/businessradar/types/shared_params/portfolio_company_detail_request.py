# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["PortfolioCompanyDetailRequest"]


class PortfolioCompanyDetailRequest(TypedDict, total=False):
    """Portfolio Company Detail Serializer.

    Alternative serializer for the Company model which is limited.
    """

    external_id: Required[str]
