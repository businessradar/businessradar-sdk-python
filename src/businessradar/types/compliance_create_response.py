# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["ComplianceCreateResponse"]


class ComplianceCreateResponse(BaseModel):
    """Compliance check create serializer."""

    external_id: str
