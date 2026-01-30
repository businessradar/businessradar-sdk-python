# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["CompanyListAttributeChangesParams"]


class CompanyListAttributeChangesParams(TypedDict, total=False):
    max_created_at: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Filter updates created at or before this time."""

    min_created_at: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Filter updates created at or after this time."""

    next_key: str
    """An opaque cursor value used for pagination.

    Pass the `next_key` received from a previous response to retrieve the next set
    of results.
    """
