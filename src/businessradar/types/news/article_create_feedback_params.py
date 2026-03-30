# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["ArticleCreateFeedbackParams"]


class ArticleCreateFeedbackParams(TypedDict, total=False):
    article: Required[str]

    comment: Optional[str]

    email: Optional[str]

    feedback_type: Literal["false_positive", "no_risk", "risk_confirmed"]
    """
    - `false_positive` - False Positive
    - `no_risk` - No Risk
    - `risk_confirmed` - Risk Confirmed
    """
