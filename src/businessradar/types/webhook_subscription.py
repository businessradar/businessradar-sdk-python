# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["WebhookSubscription"]


class WebhookSubscription(BaseModel):
    event_type: Literal[
        "compliance_check.status_changed",
        "compliance_check.status_completed",
        "company_registration.status_changed",
        "company_registration.status_registered",
    ]
    """
    - `compliance_check.status_changed` - Compliance Check Status Changed
    - `compliance_check.status_completed` - Compliance Check Status Completed
    - `company_registration.status_changed` - Company Registration Status Changed
    - `company_registration.status_registered` - Company Registration Status
      Registered
    """

    external_id: str
