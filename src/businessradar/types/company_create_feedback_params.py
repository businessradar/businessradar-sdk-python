# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["CompanyCreateFeedbackParams"]


class CompanyCreateFeedbackParams(TypedDict, total=False):
    company: Required[str]

    feedback_type: Required[
        Literal[
            "NOT_ENOUGH_NEWS",
            "COMPANY_NAME_OUTDATED",
            "INCORRECT_COMPANY_WEBSITE",
            "MISSING_REGISTRATION_NUMBER",
            "MISSING_TRADE_NAME",
            "INCORRECT_TRADE_NAME",
            "NOT_ENOUGH_REVIEWS",
            "OUTDATED_CORPORATE_LINKAGE",
            "INCORRECT_CORPORATE_LINKAGE",
            "OTHER",
        ]
    ]
    """
    - `NOT_ENOUGH_NEWS` - Not Enough News
    - `COMPANY_NAME_OUTDATED` - Company Name Outdated
    - `INCORRECT_COMPANY_WEBSITE` - Incorrect Company Website
    - `MISSING_REGISTRATION_NUMBER` - Missing Registration Number
    - `MISSING_TRADE_NAME` - Missing Trade Name
    - `INCORRECT_TRADE_NAME` - Incorrect Trade Name
    - `NOT_ENOUGH_REVIEWS` - Not Enough Reviews
    - `OUTDATED_CORPORATE_LINKAGE` - Outdated Corporate Linkage
    - `INCORRECT_CORPORATE_LINKAGE` - Incorrect Corporate Linkage
    - `OTHER` - Other
    """

    comment: Optional[str]

    notification_email: Optional[str]
    """Email address to notify when feedback is resolved."""

    trade_name: Optional[str]
