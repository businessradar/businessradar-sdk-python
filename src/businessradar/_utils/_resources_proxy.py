from __future__ import annotations

from typing import Any
from typing_extensions import override

from ._proxy import LazyProxy


class ResourcesProxy(LazyProxy[Any]):
    """A proxy for the `businessradar.resources` module.

    This is used so that we can lazily import `businessradar.resources` only when
    needed *and* so that users can just import `businessradar` and reference `businessradar.resources`
    """

    @override
    def __load__(self) -> Any:
        import importlib

        mod = importlib.import_module("businessradar.resources")
        return mod


resources = ResourcesProxy().__as_proxied__()
