# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import TYPE_CHECKING, Any, Mapping
from typing_extensions import Self, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    Omit,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
    not_given,
)
from ._utils import is_given, get_async_library
from ._compat import cached_property
from ._version import __version__
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import APIStatusError, BusinessRadarError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)

if TYPE_CHECKING:
    from .resources import news, companies, compliance, portfolios
    from .resources.companies import CompaniesResource, AsyncCompaniesResource
    from .resources.news.news import NewsResource, AsyncNewsResource
    from .resources.compliance import ComplianceResource, AsyncComplianceResource
    from .resources.portfolios.portfolios import PortfoliosResource, AsyncPortfoliosResource

__all__ = [
    "Timeout",
    "Transport",
    "ProxiesTypes",
    "RequestOptions",
    "BusinessRadar",
    "AsyncBusinessRadar",
    "Client",
    "AsyncClient",
]


class BusinessRadar(SyncAPIClient):
    # client options
    api_key: str

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous BusinessRadar client instance.

        This automatically infers the `api_key` argument from the `BUSINESSRADAR_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("BUSINESSRADAR_API_KEY")
        if api_key is None:
            raise BusinessRadarError(
                "The api_key client option must be set either by passing api_key to the client or by setting the BUSINESSRADAR_API_KEY environment variable"
            )
        self.api_key = api_key

        if base_url is None:
            base_url = os.environ.get("BUSINESS_RADAR_BASE_URL")
        if base_url is None:
            base_url = f"https://api.businessradar.com"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def news(self) -> NewsResource:
        from .resources.news import NewsResource

        return NewsResource(self)

    @cached_property
    def companies(self) -> CompaniesResource:
        from .resources.companies import CompaniesResource

        return CompaniesResource(self)

    @cached_property
    def compliance(self) -> ComplianceResource:
        from .resources.compliance import ComplianceResource

        return ComplianceResource(self)

    @cached_property
    def portfolios(self) -> PortfoliosResource:
        from .resources.portfolios import PortfoliosResource

        return PortfoliosResource(self)

    @cached_property
    def with_raw_response(self) -> BusinessRadarWithRawResponse:
        return BusinessRadarWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BusinessRadarWithStreamedResponse:
        return BusinessRadarWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        return {"Authorization": f"Bearer {api_key}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncBusinessRadar(AsyncAPIClient):
    # client options
    api_key: str

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async AsyncBusinessRadar client instance.

        This automatically infers the `api_key` argument from the `BUSINESSRADAR_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("BUSINESSRADAR_API_KEY")
        if api_key is None:
            raise BusinessRadarError(
                "The api_key client option must be set either by passing api_key to the client or by setting the BUSINESSRADAR_API_KEY environment variable"
            )
        self.api_key = api_key

        if base_url is None:
            base_url = os.environ.get("BUSINESS_RADAR_BASE_URL")
        if base_url is None:
            base_url = f"https://api.businessradar.com"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def news(self) -> AsyncNewsResource:
        from .resources.news import AsyncNewsResource

        return AsyncNewsResource(self)

    @cached_property
    def companies(self) -> AsyncCompaniesResource:
        from .resources.companies import AsyncCompaniesResource

        return AsyncCompaniesResource(self)

    @cached_property
    def compliance(self) -> AsyncComplianceResource:
        from .resources.compliance import AsyncComplianceResource

        return AsyncComplianceResource(self)

    @cached_property
    def portfolios(self) -> AsyncPortfoliosResource:
        from .resources.portfolios import AsyncPortfoliosResource

        return AsyncPortfoliosResource(self)

    @cached_property
    def with_raw_response(self) -> AsyncBusinessRadarWithRawResponse:
        return AsyncBusinessRadarWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBusinessRadarWithStreamedResponse:
        return AsyncBusinessRadarWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        return {"Authorization": f"Bearer {api_key}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class BusinessRadarWithRawResponse:
    _client: BusinessRadar

    def __init__(self, client: BusinessRadar) -> None:
        self._client = client

    @cached_property
    def news(self) -> news.NewsResourceWithRawResponse:
        from .resources.news import NewsResourceWithRawResponse

        return NewsResourceWithRawResponse(self._client.news)

    @cached_property
    def companies(self) -> companies.CompaniesResourceWithRawResponse:
        from .resources.companies import CompaniesResourceWithRawResponse

        return CompaniesResourceWithRawResponse(self._client.companies)

    @cached_property
    def compliance(self) -> compliance.ComplianceResourceWithRawResponse:
        from .resources.compliance import ComplianceResourceWithRawResponse

        return ComplianceResourceWithRawResponse(self._client.compliance)

    @cached_property
    def portfolios(self) -> portfolios.PortfoliosResourceWithRawResponse:
        from .resources.portfolios import PortfoliosResourceWithRawResponse

        return PortfoliosResourceWithRawResponse(self._client.portfolios)


class AsyncBusinessRadarWithRawResponse:
    _client: AsyncBusinessRadar

    def __init__(self, client: AsyncBusinessRadar) -> None:
        self._client = client

    @cached_property
    def news(self) -> news.AsyncNewsResourceWithRawResponse:
        from .resources.news import AsyncNewsResourceWithRawResponse

        return AsyncNewsResourceWithRawResponse(self._client.news)

    @cached_property
    def companies(self) -> companies.AsyncCompaniesResourceWithRawResponse:
        from .resources.companies import AsyncCompaniesResourceWithRawResponse

        return AsyncCompaniesResourceWithRawResponse(self._client.companies)

    @cached_property
    def compliance(self) -> compliance.AsyncComplianceResourceWithRawResponse:
        from .resources.compliance import AsyncComplianceResourceWithRawResponse

        return AsyncComplianceResourceWithRawResponse(self._client.compliance)

    @cached_property
    def portfolios(self) -> portfolios.AsyncPortfoliosResourceWithRawResponse:
        from .resources.portfolios import AsyncPortfoliosResourceWithRawResponse

        return AsyncPortfoliosResourceWithRawResponse(self._client.portfolios)


class BusinessRadarWithStreamedResponse:
    _client: BusinessRadar

    def __init__(self, client: BusinessRadar) -> None:
        self._client = client

    @cached_property
    def news(self) -> news.NewsResourceWithStreamingResponse:
        from .resources.news import NewsResourceWithStreamingResponse

        return NewsResourceWithStreamingResponse(self._client.news)

    @cached_property
    def companies(self) -> companies.CompaniesResourceWithStreamingResponse:
        from .resources.companies import CompaniesResourceWithStreamingResponse

        return CompaniesResourceWithStreamingResponse(self._client.companies)

    @cached_property
    def compliance(self) -> compliance.ComplianceResourceWithStreamingResponse:
        from .resources.compliance import ComplianceResourceWithStreamingResponse

        return ComplianceResourceWithStreamingResponse(self._client.compliance)

    @cached_property
    def portfolios(self) -> portfolios.PortfoliosResourceWithStreamingResponse:
        from .resources.portfolios import PortfoliosResourceWithStreamingResponse

        return PortfoliosResourceWithStreamingResponse(self._client.portfolios)


class AsyncBusinessRadarWithStreamedResponse:
    _client: AsyncBusinessRadar

    def __init__(self, client: AsyncBusinessRadar) -> None:
        self._client = client

    @cached_property
    def news(self) -> news.AsyncNewsResourceWithStreamingResponse:
        from .resources.news import AsyncNewsResourceWithStreamingResponse

        return AsyncNewsResourceWithStreamingResponse(self._client.news)

    @cached_property
    def companies(self) -> companies.AsyncCompaniesResourceWithStreamingResponse:
        from .resources.companies import AsyncCompaniesResourceWithStreamingResponse

        return AsyncCompaniesResourceWithStreamingResponse(self._client.companies)

    @cached_property
    def compliance(self) -> compliance.AsyncComplianceResourceWithStreamingResponse:
        from .resources.compliance import AsyncComplianceResourceWithStreamingResponse

        return AsyncComplianceResourceWithStreamingResponse(self._client.compliance)

    @cached_property
    def portfolios(self) -> portfolios.AsyncPortfoliosResourceWithStreamingResponse:
        from .resources.portfolios import AsyncPortfoliosResourceWithStreamingResponse

        return AsyncPortfoliosResourceWithStreamingResponse(self._client.portfolios)


Client = BusinessRadar

AsyncClient = AsyncBusinessRadar
