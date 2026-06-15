# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from .webhook_subscription_request_param import WebhookSubscriptionRequestParam

__all__ = ["WebhookUpdateParams"]


class WebhookUpdateParams(TypedDict, total=False):
    subscriptions: Required[Iterable[WebhookSubscriptionRequestParam]]

    url: Required[str]

    enabled: bool
