# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["WebhookSubscriptionRequestParam"]


class WebhookSubscriptionRequestParam(TypedDict, total=False):
    event_type: Required[
        Literal[
            "compliance_check.status_changed",
            "compliance_check.status_completed",
            "compliance_check.results.new",
            "company_registration.status_changed",
            "company_registration.status_registered",
            "company.updated",
        ]
    ]
    """
    - `compliance_check.status_changed` - Compliance Check Status Changed
    - `compliance_check.status_completed` - Compliance Check Status Completed
    - `compliance_check.results.new` - Compliance Check Results New
    - `company_registration.status_changed` - Company Registration Status Changed
    - `company_registration.status_registered` - Company Registration Status
      Registered
    - `company.updated` - Company Updated
    """

    portfolio: Optional[str]
    """Portfolio external_id.

    Required for portfolio-scoped events (e.g. company.updated); must be omitted for
    all other events.
    """
