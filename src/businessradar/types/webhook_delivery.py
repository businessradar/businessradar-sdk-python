# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel
from .webhook_delivery_status_enum import WebhookDeliveryStatusEnum

__all__ = ["WebhookDelivery"]


class WebhookDelivery(BaseModel):
    attempt_count: int

    created_at: datetime

    data: object

    error_details: Optional[str] = None

    external_id: str

    status: WebhookDeliveryStatusEnum
    """
    - `pending` - Pending
    - `in_progress` - In Progress
    - `completed` - Completed
    - `failed` - Failed
    """

    updated_at: datetime
