# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["ComplianceCreateResponse"]


class ComplianceCreateResponse(BaseModel):
    """### Compliance Check

    Used for creating a minimal compliance check record.
    """

    external_id: str
