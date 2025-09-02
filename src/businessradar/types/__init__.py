# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from . import ext
from .. import _compat

# Rebuild cyclical models only after all modules are imported.
# This ensures that, when building the deferred (due to cyclical references) model schema,
# Pydantic can resolve the necessary references.
# See: https://github.com/pydantic/pydantic/issues/11250 for more context.
if _compat.PYDANTIC_V2:
    ext.v3.article.Article.model_rebuild(_parent_namespace_depth=0)
    ext.v3.category_tree.CategoryTree.model_rebuild(_parent_namespace_depth=0)
    ext.v3.article_list_response.ArticleListResponse.model_rebuild(_parent_namespace_depth=0)
else:
    ext.v3.article.Article.update_forward_refs()  # type: ignore
    ext.v3.category_tree.CategoryTree.update_forward_refs()  # type: ignore
    ext.v3.article_list_response.ArticleListResponse.update_forward_refs()  # type: ignore
