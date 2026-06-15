# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel
from .webhook_subscription import WebhookSubscription

__all__ = ["Webhook"]


class Webhook(BaseModel):
    created_at: datetime

    external_id: str

    subscriptions: List[WebhookSubscription]

    updated_at: datetime

    url: str

    enabled: Optional[bool] = None
