# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Generic, TypeVar, Optional
from typing_extensions import override

from ._base_client import BasePage, PageInfo, BaseSyncPage, BaseAsyncPage

__all__ = ["SyncNextKey", "AsyncNextKey"]

_T = TypeVar("_T")


class SyncNextKey(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    results: List[_T]
    next_key: Optional[str] = None

    @override
    def _get_page_items(self) -> List[_T]:
        results = self.results
        if not results:
            return []
        return results

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        next_key = self.next_key
        if not next_key:
            return None

        return PageInfo(params={"next_key": next_key})


class AsyncNextKey(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    results: List[_T]
    next_key: Optional[str] = None

    @override
    def _get_page_items(self) -> List[_T]:
        results = self.results
        if not results:
            return []
        return results

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        next_key = self.next_key
        if not next_key:
            return None

        return PageInfo(params={"next_key": next_key})
