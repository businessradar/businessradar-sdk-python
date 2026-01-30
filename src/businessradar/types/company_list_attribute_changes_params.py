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
    """A cursor value used for pagination.

    Include the `next_key` value from your previous request to retrieve the
    subsequent page of results. If this value is `null`, the first page of results
    is returned.
    """
