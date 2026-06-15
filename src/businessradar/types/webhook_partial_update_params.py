# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import TypedDict

from .webhook_subscription_request_param import WebhookSubscriptionRequestParam

__all__ = ["WebhookPartialUpdateParams"]


class WebhookPartialUpdateParams(TypedDict, total=False):
    enabled: bool

    subscriptions: Iterable[WebhookSubscriptionRequestParam]

    url: str
