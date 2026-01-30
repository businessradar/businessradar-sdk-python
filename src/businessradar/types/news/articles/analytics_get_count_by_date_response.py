# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import datetime
from typing import List
from typing_extensions import TypeAlias

from ...._models import BaseModel

__all__ = ["AnalyticsGetCountByDateResponse", "AnalyticsGetCountByDateResponseItem"]


class AnalyticsGetCountByDateResponseItem(BaseModel):
    """### Article Date Aggregation

    Provides aggregated metrics for articles on a per-date basis. - **count**: Total
    articles found for the given date. - **average_sentiment**: Average sentiment score
    of these articles. - **date**: The specific date of the aggregation.
    """

    average_sentiment: float

    count: int

    date: datetime.date


AnalyticsGetCountByDateResponse: TypeAlias = List[AnalyticsGetCountByDateResponseItem]
