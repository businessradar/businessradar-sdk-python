# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["CompanyMatchParams"]


class CompanyMatchParams(TypedDict, total=False):
    address_county: str
    """County."""

    address_locality: str
    """City / locality."""

    address_region: str
    """Region / state / province."""

    confidence_lower_level_threshold_value: int
    """Minimum Dun & Bradstreet confidence code (1-10)."""

    country: str
    """ISO 2-letter Country Code (e.g., NL, US)."""

    customer_reference: str
    """Your own reference linking to a tracked company."""

    duns_number: str
    """9-digit Dun And Bradstreet Number to match."""

    email: str
    """Company email address."""

    name: str
    """Company name to match."""

    postal_code: str
    """Postal / ZIP code."""

    registration_number: str
    """Local Registration Number."""

    registration_number_type: str
    """Type of the registration number."""

    street_address_line1: str
    """First line of the street address."""

    street_address_line2: str
    """Second line of the street address."""

    telephone_number: str
    """Telephone number."""

    url: str
    """Company website URL."""
