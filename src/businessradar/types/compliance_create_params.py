# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from datetime import date
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ComplianceCreateParams", "Entity"]


class ComplianceCreateParams(TypedDict, total=False):
    all_entities_screening_enabled: bool
    """If enabled all found entities UBOs, directors, shareholders will be screened.

    This can have an high cost impact.
    """

    company_id: Optional[str]

    directors_screening_enabled: bool
    """If directors should be screened."""

    entities: Iterable[Entity]

    ownership_screening_threshold: Optional[float]
    """The threshold for ultimate ownership to enable for screening."""


class Entity(TypedDict, total=False):
    """Compliance entity request serializer."""

    name: Required[str]

    country: Optional[str]

    date_of_birth: Annotated[Union[str, date, None], PropertyInfo(format="iso8601")]

    entity_type: Literal["individual", "company"]
    """
    - `individual` - Individual
    - `company` - Company
    """

    first_name: Optional[str]

    last_name: Optional[str]

    middle_name: Optional[str]
