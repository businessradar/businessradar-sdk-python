# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from .feedback_type_enum import FeedbackTypeEnum

__all__ = ["ArticleCreateFeedbackResponse"]


class ArticleCreateFeedbackResponse(BaseModel):
    """### External Article Feedback

    Allows users to provide feedback on specific articles, including feedback type,
    comments, and contact information.
    """

    article: str

    external_id: str

    comment: Optional[str] = None

    email: Optional[str] = None

    feedback_type: Optional[FeedbackTypeEnum] = None
    """
    - `false_positive` - False Positive
    - `no_risk` - No Risk
    - `risk_confirmed` - Risk Confirmed
    """
