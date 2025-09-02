# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import datetime
from typing import List
from typing_extensions import TypeAlias

from ...._models import BaseModel

__all__ = ["AnalyticsGetCountByDateResponse", "AnalyticsGetCountByDateResponseItem"]


class AnalyticsGetCountByDateResponseItem(BaseModel):
    average_sentiment: float

    count: int

    date: datetime.date


AnalyticsGetCountByDateResponse: TypeAlias = List[AnalyticsGetCountByDateResponseItem]
