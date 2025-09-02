# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["IndustryCode"]


class IndustryCode(BaseModel):
    code: str

    description: Optional[str] = None
