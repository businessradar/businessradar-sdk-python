# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from .feedback_type_enum import FeedbackTypeEnum

__all__ = ["ArticleCreateFeedbackParams"]


class ArticleCreateFeedbackParams(TypedDict, total=False):
    article: Required[str]

    comment: Optional[str]

    email: Optional[str]

    feedback_type: FeedbackTypeEnum
    """
    - `false_positive` - False Positive
    - `no_risk` - No Risk
    - `risk_confirmed` - Risk Confirmed
    """
