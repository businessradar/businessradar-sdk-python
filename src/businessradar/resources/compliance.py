# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from datetime import datetime
from typing_extensions import Literal

import httpx

from ..types import compliance_list_params, compliance_create_params, compliance_list_results_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import path_template, maybe_transform, async_maybe_transform
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
from ..types.compliance_list_response import ComplianceListResponse
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
        adverse_media_monitoring_enabled: bool | Omit = omit,
        company_id: Optional[str] | Omit = omit,
        directors_screening_enabled: bool | Omit = omit,
        entities: Iterable[compliance_create_params.Entity] | Omit = omit,
        name: Optional[str] | Omit = omit,
        ownership_screening_threshold: Optional[float] | Omit = omit,
        sanction_monitoring_enabled: bool | Omit = omit,
        ubo_screening_enabled: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ComplianceCreateResponse:
        """
        ### Create Compliance Check (Asynchronous)

        Initiate a new compliance screening using one of two methods:

        1. **Company-based screening**: Provide a `company_id` to screen the company.
           Optionally enable screening of related entities (UBOs and directors) via
           `ubo_screening_enabled` and `directors_screening_enabled`. You can optionally
           include a list of additional `entities` to be screened alongside the company.

        2. **Custom entity screening**: Provide a list of `entities` without a
           `company_id` to screen specific individuals or organizations that are not
           necessarily affiliated with a company in our database.

        Once posted, Business Radar processes the request in the background.

        To check the progress and/or retrieve the final result, you can use the
        [GET /compliance/{external_id}](/ext/v3/#/ext/ext_v3_compliance_retrieve)
        endpoint.

        Args:
          adverse_media_monitoring_enabled: If enabled, adverse media monitoring will be activated for all system-created
              entities (company, directors, UBOs).

          directors_screening_enabled: If directors should be screened.

          name: Custom name for this compliance check.

          ownership_screening_threshold: The threshold for ultimate ownership to enable for screening.

          sanction_monitoring_enabled: If enabled, sanctions monitoring will be activated for all system-created
              entities (company, directors, UBOs).

          ubo_screening_enabled: If enabled, UBOs discovered for the company will be screened.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/ext/v3/compliance",
            body=maybe_transform(
                {
                    "adverse_media_monitoring_enabled": adverse_media_monitoring_enabled,
                    "company_id": company_id,
                    "directors_screening_enabled": directors_screening_enabled,
                    "entities": entities,
                    "name": name,
                    "ownership_screening_threshold": ownership_screening_threshold,
                    "sanction_monitoring_enabled": sanction_monitoring_enabled,
                    "ubo_screening_enabled": ubo_screening_enabled,
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
        ### Compliance Check Status

        Check the current status, progress, and high-level scores of a specific
        compliance check.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not external_id:
            raise ValueError(f"Expected a non-empty value for `external_id` but received {external_id!r}")
        return self._get(
            path_template("/ext/v3/compliance/{external_id}", external_id=external_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ComplianceRetrieveResponse,
        )

    def list(
        self,
        *,
        adverse_media_monitoring_enabled: bool | Omit = omit,
        compliance_score: Literal["high", "low", "medium"] | Omit = omit,
        created_at_gte: Union[str, datetime] | Omit = omit,
        created_at_lte: Union[str, datetime] | Omit = omit,
        next_key: str | Omit = omit,
        order: Literal["asc", "desc"] | Omit = omit,
        results_changed_at_gte: Union[str, datetime] | Omit = omit,
        results_changed_at_lte: Union[str, datetime] | Omit = omit,
        sanction_monitoring_enabled: bool | Omit = omit,
        sorting: Literal["created_at", "finished_at", "results_changed_at"] | Omit = omit,
        status: Literal["completed", "failed", "in_progress", "pending", "queued", "searching_directors"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncNextKey[ComplianceListResponse]:
        """
        ### Compliance Checks

        **GET** — Retrieve a paginated list of compliance checks created via this API
        key. Supports filtering by status and date ranges, and sorting by key
        timestamps.

        **POST** — Initiate a new compliance screening using one of two methods:

        1. **Company-based screening**: Provide a `company_id` to screen the company.
           Optionally enable screening of related entities (UBOs and directors) via
           `ubo_screening_enabled` and `directors_screening_enabled`. You can also
           include additional custom `entities` to be screened alongside the company.

        2. **Custom entity screening**: Provide a list of `entities` without a
           `company_id` to screen specific individuals or organizations that are not
           necessarily affiliated with a company in our database.

        Args:
          adverse_media_monitoring_enabled: Filter checks that have entities with adverse media monitoring enabled (pending
              or active).

          compliance_score: Filter by compliance score.

          created_at_gte: Filter checks created at or after this time.

          created_at_lte: Filter checks created at or before this time.

          next_key: A cursor value used for pagination. Include the `next_key` value from your
              previous request to retrieve the subsequent page of results. If this value is
              `null`, the first page of results is returned.

          order: Sorting order.

          results_changed_at_gte: Filter checks with results changed at or after this time.

          results_changed_at_lte: Filter checks with results changed at or before this time.

          sanction_monitoring_enabled: Filter checks that have entities with sanction monitoring enabled (pending or
              active).

          sorting: Sorting field.

          status: Filter by compliance check status.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/ext/v3/compliance",
            page=SyncNextKey[ComplianceListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "adverse_media_monitoring_enabled": adverse_media_monitoring_enabled,
                        "compliance_score": compliance_score,
                        "created_at_gte": created_at_gte,
                        "created_at_lte": created_at_lte,
                        "next_key": next_key,
                        "order": order,
                        "results_changed_at_gte": results_changed_at_gte,
                        "results_changed_at_lte": results_changed_at_lte,
                        "sanction_monitoring_enabled": sanction_monitoring_enabled,
                        "sorting": sorting,
                        "status": status,
                    },
                    compliance_list_params.ComplianceListParams,
                ),
            ),
            model=ComplianceListResponse,
        )

    def list_results(
        self,
        external_id: str,
        *,
        entity: str | Omit = omit,
        exclude_automated_false_positives: bool | Omit = omit,
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
        """### List Compliance Results

        Retrieve all findings for a compliance check.

        Results can be filtered by entity,
        type of finding (e.g., Sanction, PEP), and confidence score.

        Args:
          entity: Filter by entity external ID

          exclude_automated_false_positives: Filter out automated false positive rated results

          min_confidence: Filter by minimum confidence score (0.0 - 1.0)

          next_key: A cursor value used for pagination. Include the `next_key` value from your
              previous request to retrieve the subsequent page of results. If this value is
              `null`, the first page of results is returned.

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
            path_template("/ext/v3/compliance/{external_id}/results", external_id=external_id),
            page=SyncNextKey[ComplianceListResultsResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "entity": entity,
                        "exclude_automated_false_positives": exclude_automated_false_positives,
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
        adverse_media_monitoring_enabled: bool | Omit = omit,
        company_id: Optional[str] | Omit = omit,
        directors_screening_enabled: bool | Omit = omit,
        entities: Iterable[compliance_create_params.Entity] | Omit = omit,
        name: Optional[str] | Omit = omit,
        ownership_screening_threshold: Optional[float] | Omit = omit,
        sanction_monitoring_enabled: bool | Omit = omit,
        ubo_screening_enabled: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ComplianceCreateResponse:
        """
        ### Create Compliance Check (Asynchronous)

        Initiate a new compliance screening using one of two methods:

        1. **Company-based screening**: Provide a `company_id` to screen the company.
           Optionally enable screening of related entities (UBOs and directors) via
           `ubo_screening_enabled` and `directors_screening_enabled`. You can optionally
           include a list of additional `entities` to be screened alongside the company.

        2. **Custom entity screening**: Provide a list of `entities` without a
           `company_id` to screen specific individuals or organizations that are not
           necessarily affiliated with a company in our database.

        Once posted, Business Radar processes the request in the background.

        To check the progress and/or retrieve the final result, you can use the
        [GET /compliance/{external_id}](/ext/v3/#/ext/ext_v3_compliance_retrieve)
        endpoint.

        Args:
          adverse_media_monitoring_enabled: If enabled, adverse media monitoring will be activated for all system-created
              entities (company, directors, UBOs).

          directors_screening_enabled: If directors should be screened.

          name: Custom name for this compliance check.

          ownership_screening_threshold: The threshold for ultimate ownership to enable for screening.

          sanction_monitoring_enabled: If enabled, sanctions monitoring will be activated for all system-created
              entities (company, directors, UBOs).

          ubo_screening_enabled: If enabled, UBOs discovered for the company will be screened.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/ext/v3/compliance",
            body=await async_maybe_transform(
                {
                    "adverse_media_monitoring_enabled": adverse_media_monitoring_enabled,
                    "company_id": company_id,
                    "directors_screening_enabled": directors_screening_enabled,
                    "entities": entities,
                    "name": name,
                    "ownership_screening_threshold": ownership_screening_threshold,
                    "sanction_monitoring_enabled": sanction_monitoring_enabled,
                    "ubo_screening_enabled": ubo_screening_enabled,
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
        ### Compliance Check Status

        Check the current status, progress, and high-level scores of a specific
        compliance check.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not external_id:
            raise ValueError(f"Expected a non-empty value for `external_id` but received {external_id!r}")
        return await self._get(
            path_template("/ext/v3/compliance/{external_id}", external_id=external_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ComplianceRetrieveResponse,
        )

    def list(
        self,
        *,
        adverse_media_monitoring_enabled: bool | Omit = omit,
        compliance_score: Literal["high", "low", "medium"] | Omit = omit,
        created_at_gte: Union[str, datetime] | Omit = omit,
        created_at_lte: Union[str, datetime] | Omit = omit,
        next_key: str | Omit = omit,
        order: Literal["asc", "desc"] | Omit = omit,
        results_changed_at_gte: Union[str, datetime] | Omit = omit,
        results_changed_at_lte: Union[str, datetime] | Omit = omit,
        sanction_monitoring_enabled: bool | Omit = omit,
        sorting: Literal["created_at", "finished_at", "results_changed_at"] | Omit = omit,
        status: Literal["completed", "failed", "in_progress", "pending", "queued", "searching_directors"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[ComplianceListResponse, AsyncNextKey[ComplianceListResponse]]:
        """
        ### Compliance Checks

        **GET** — Retrieve a paginated list of compliance checks created via this API
        key. Supports filtering by status and date ranges, and sorting by key
        timestamps.

        **POST** — Initiate a new compliance screening using one of two methods:

        1. **Company-based screening**: Provide a `company_id` to screen the company.
           Optionally enable screening of related entities (UBOs and directors) via
           `ubo_screening_enabled` and `directors_screening_enabled`. You can also
           include additional custom `entities` to be screened alongside the company.

        2. **Custom entity screening**: Provide a list of `entities` without a
           `company_id` to screen specific individuals or organizations that are not
           necessarily affiliated with a company in our database.

        Args:
          adverse_media_monitoring_enabled: Filter checks that have entities with adverse media monitoring enabled (pending
              or active).

          compliance_score: Filter by compliance score.

          created_at_gte: Filter checks created at or after this time.

          created_at_lte: Filter checks created at or before this time.

          next_key: A cursor value used for pagination. Include the `next_key` value from your
              previous request to retrieve the subsequent page of results. If this value is
              `null`, the first page of results is returned.

          order: Sorting order.

          results_changed_at_gte: Filter checks with results changed at or after this time.

          results_changed_at_lte: Filter checks with results changed at or before this time.

          sanction_monitoring_enabled: Filter checks that have entities with sanction monitoring enabled (pending or
              active).

          sorting: Sorting field.

          status: Filter by compliance check status.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/ext/v3/compliance",
            page=AsyncNextKey[ComplianceListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "adverse_media_monitoring_enabled": adverse_media_monitoring_enabled,
                        "compliance_score": compliance_score,
                        "created_at_gte": created_at_gte,
                        "created_at_lte": created_at_lte,
                        "next_key": next_key,
                        "order": order,
                        "results_changed_at_gte": results_changed_at_gte,
                        "results_changed_at_lte": results_changed_at_lte,
                        "sanction_monitoring_enabled": sanction_monitoring_enabled,
                        "sorting": sorting,
                        "status": status,
                    },
                    compliance_list_params.ComplianceListParams,
                ),
            ),
            model=ComplianceListResponse,
        )

    def list_results(
        self,
        external_id: str,
        *,
        entity: str | Omit = omit,
        exclude_automated_false_positives: bool | Omit = omit,
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
        """### List Compliance Results

        Retrieve all findings for a compliance check.

        Results can be filtered by entity,
        type of finding (e.g., Sanction, PEP), and confidence score.

        Args:
          entity: Filter by entity external ID

          exclude_automated_false_positives: Filter out automated false positive rated results

          min_confidence: Filter by minimum confidence score (0.0 - 1.0)

          next_key: A cursor value used for pagination. Include the `next_key` value from your
              previous request to retrieve the subsequent page of results. If this value is
              `null`, the first page of results is returned.

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
            path_template("/ext/v3/compliance/{external_id}/results", external_id=external_id),
            page=AsyncNextKey[ComplianceListResultsResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "entity": entity,
                        "exclude_automated_false_positives": exclude_automated_false_positives,
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
        self.list = to_raw_response_wrapper(
            compliance.list,
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
        self.list = async_to_raw_response_wrapper(
            compliance.list,
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
        self.list = to_streamed_response_wrapper(
            compliance.list,
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
        self.list = async_to_streamed_response_wrapper(
            compliance.list,
        )
        self.list_results = async_to_streamed_response_wrapper(
            compliance.list_results,
        )
