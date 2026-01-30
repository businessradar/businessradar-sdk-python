# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal

import httpx

from ..types import compliance_create_params, compliance_list_results_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..pagination import SyncNextKey, AsyncNextKey
from .._base_client import AsyncPaginator, make_request_options
from ..types.compliance_create_response import ComplianceCreateResponse
from ..types.compliance_retrieve_response import ComplianceRetrieveResponse
from ..types.compliance_list_results_response import ComplianceListResultsResponse

__all__ = ["ComplianceResource", "AsyncComplianceResource"]


class ComplianceResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ComplianceResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/businessradar/businessradar-sdk-python#accessing-raw-response-data-eg-headers
        """
        return ComplianceResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ComplianceResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/businessradar/businessradar-sdk-python#with_streaming_response
        """
        return ComplianceResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        all_entities_screening_enabled: bool | Omit = omit,
        company_id: Optional[str] | Omit = omit,
        directors_screening_enabled: bool | Omit = omit,
        entities: Iterable[compliance_create_params.Entity] | Omit = omit,
        ownership_screening_threshold: Optional[float] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ComplianceCreateResponse:
        """
        Create a new compliance check.

        Args:
          all_entities_screening_enabled: If enabled all found entities UBOs, directors, shareholders will be screened.
              This can have an high cost impact.

          directors_screening_enabled: If directors should be screened.

          ownership_screening_threshold: The threshold for ultimate ownership to enable for screening.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/ext/v3/compliance",
            body=maybe_transform(
                {
                    "all_entities_screening_enabled": all_entities_screening_enabled,
                    "company_id": company_id,
                    "directors_screening_enabled": directors_screening_enabled,
                    "entities": entities,
                    "ownership_screening_threshold": ownership_screening_threshold,
                },
                compliance_create_params.ComplianceCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ComplianceCreateResponse,
        )

    def retrieve(
        self,
        external_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ComplianceRetrieveResponse:
        """
        Get compliance check details.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not external_id:
            raise ValueError(f"Expected a non-empty value for `external_id` but received {external_id!r}")
        return self._get(
            f"/ext/v3/compliance/{external_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ComplianceRetrieveResponse,
        )

    def list_results(
        self,
        external_id: str,
        *,
        entity: str | Omit = omit,
        min_confidence: float | Omit = omit,
        next_key: str | Omit = omit,
        order: Literal["asc", "desc"] | Omit = omit,
        result_type: Literal["adverse_media", "enforcement", "govt_owned", "pep", "sanction"] | Omit = omit,
        sorting: Literal["confidence", "created_at", "source_date"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncNextKey[ComplianceListResultsResponse]:
        """
        List compliance results.

        Args:
          entity: Filter by entity external ID

          min_confidence: Filter by minimum confidence score (0.0 - 1.0)

          next_key: The next_key is an cursor used to make it possible to paginate to the next
              results, pass the next_key from the previous request to retrieve next results.

          order: Sorting order

          result_type: Filter by result type

          sorting: Sorting field

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not external_id:
            raise ValueError(f"Expected a non-empty value for `external_id` but received {external_id!r}")
        return self._get_api_list(
            f"/ext/v3/compliance/{external_id}/results",
            page=SyncNextKey[ComplianceListResultsResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "entity": entity,
                        "min_confidence": min_confidence,
                        "next_key": next_key,
                        "order": order,
                        "result_type": result_type,
                        "sorting": sorting,
                    },
                    compliance_list_results_params.ComplianceListResultsParams,
                ),
            ),
            model=ComplianceListResultsResponse,
        )


class AsyncComplianceResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncComplianceResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/businessradar/businessradar-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncComplianceResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncComplianceResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/businessradar/businessradar-sdk-python#with_streaming_response
        """
        return AsyncComplianceResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        all_entities_screening_enabled: bool | Omit = omit,
        company_id: Optional[str] | Omit = omit,
        directors_screening_enabled: bool | Omit = omit,
        entities: Iterable[compliance_create_params.Entity] | Omit = omit,
        ownership_screening_threshold: Optional[float] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ComplianceCreateResponse:
        """
        Create a new compliance check.

        Args:
          all_entities_screening_enabled: If enabled all found entities UBOs, directors, shareholders will be screened.
              This can have an high cost impact.

          directors_screening_enabled: If directors should be screened.

          ownership_screening_threshold: The threshold for ultimate ownership to enable for screening.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/ext/v3/compliance",
            body=await async_maybe_transform(
                {
                    "all_entities_screening_enabled": all_entities_screening_enabled,
                    "company_id": company_id,
                    "directors_screening_enabled": directors_screening_enabled,
                    "entities": entities,
                    "ownership_screening_threshold": ownership_screening_threshold,
                },
                compliance_create_params.ComplianceCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ComplianceCreateResponse,
        )

    async def retrieve(
        self,
        external_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ComplianceRetrieveResponse:
        """
        Get compliance check details.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not external_id:
            raise ValueError(f"Expected a non-empty value for `external_id` but received {external_id!r}")
        return await self._get(
            f"/ext/v3/compliance/{external_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ComplianceRetrieveResponse,
        )

    def list_results(
        self,
        external_id: str,
        *,
        entity: str | Omit = omit,
        min_confidence: float | Omit = omit,
        next_key: str | Omit = omit,
        order: Literal["asc", "desc"] | Omit = omit,
        result_type: Literal["adverse_media", "enforcement", "govt_owned", "pep", "sanction"] | Omit = omit,
        sorting: Literal["confidence", "created_at", "source_date"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[ComplianceListResultsResponse, AsyncNextKey[ComplianceListResultsResponse]]:
        """
        List compliance results.

        Args:
          entity: Filter by entity external ID

          min_confidence: Filter by minimum confidence score (0.0 - 1.0)

          next_key: The next_key is an cursor used to make it possible to paginate to the next
              results, pass the next_key from the previous request to retrieve next results.

          order: Sorting order

          result_type: Filter by result type

          sorting: Sorting field

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not external_id:
            raise ValueError(f"Expected a non-empty value for `external_id` but received {external_id!r}")
        return self._get_api_list(
            f"/ext/v3/compliance/{external_id}/results",
            page=AsyncNextKey[ComplianceListResultsResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "entity": entity,
                        "min_confidence": min_confidence,
                        "next_key": next_key,
                        "order": order,
                        "result_type": result_type,
                        "sorting": sorting,
                    },
                    compliance_list_results_params.ComplianceListResultsParams,
                ),
            ),
            model=ComplianceListResultsResponse,
        )


class ComplianceResourceWithRawResponse:
    def __init__(self, compliance: ComplianceResource) -> None:
        self._compliance = compliance

        self.create = to_raw_response_wrapper(
            compliance.create,
        )
        self.retrieve = to_raw_response_wrapper(
            compliance.retrieve,
        )
        self.list_results = to_raw_response_wrapper(
            compliance.list_results,
        )


class AsyncComplianceResourceWithRawResponse:
    def __init__(self, compliance: AsyncComplianceResource) -> None:
        self._compliance = compliance

        self.create = async_to_raw_response_wrapper(
            compliance.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            compliance.retrieve,
        )
        self.list_results = async_to_raw_response_wrapper(
            compliance.list_results,
        )


class ComplianceResourceWithStreamingResponse:
    def __init__(self, compliance: ComplianceResource) -> None:
        self._compliance = compliance

        self.create = to_streamed_response_wrapper(
            compliance.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            compliance.retrieve,
        )
        self.list_results = to_streamed_response_wrapper(
            compliance.list_results,
        )


class AsyncComplianceResourceWithStreamingResponse:
    def __init__(self, compliance: AsyncComplianceResource) -> None:
        self._compliance = compliance

        self.create = async_to_streamed_response_wrapper(
            compliance.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            compliance.retrieve,
        )
        self.list_results = async_to_streamed_response_wrapper(
            compliance.list_results,
        )
