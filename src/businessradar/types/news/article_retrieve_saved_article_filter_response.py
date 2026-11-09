# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel
from .articles.article_filters import ArticleFilters

__all__ = ["ArticleRetrieveSavedArticleFilterResponse"]


class ArticleRetrieveSavedArticleFilterResponse(BaseModel):
    """### Saved Article Filter Detail

    A saved article filter with the filters it applies, in the same format as the
    `filters` of an article export. Article search parameters such as `category`
    replace the matching saved filter values.
    """

    external_id: str

    filters: ArticleFilters
    """### Article Filters

    Used to validate and process filters for article searches. Supports filtering by
    query text, countries, languages, specific companies (DUNS), and portfolios.
    """

    name: str
