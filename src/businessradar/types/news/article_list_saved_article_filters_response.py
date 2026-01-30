# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["ArticleListSavedArticleFiltersResponse"]


class ArticleListSavedArticleFiltersResponse(BaseModel):
    """### Saved Article Filter

    Represents a named set of article search filters that can be reused.
    """

    external_id: str

    name: str
