# Shared Types

```python
from businessradar.types import PortfolioCompanyDetailRequest
```

# News

## Articles

Types:

```python
from businessradar.types.news import (
    Article,
    CategoryTree,
    FeedbackTypeEnum,
    LanguageEnum,
    ArticleCreateFeedbackResponse,
    ArticleListSavedArticleFiltersResponse,
    ArticleRetrieveRelatedResponse,
)
```

Methods:

- <code title="get /ext/v3/articles">client.news.articles.<a href="./src/businessradar/resources/news/articles/articles.py">list</a>(\*\*<a href="src/businessradar/types/news/article_list_params.py">params</a>) -> <a href="./src/businessradar/types/news/article.py">SyncNextKey[Article]</a></code>
- <code title="post /ext/v3/articles/feedback/">client.news.articles.<a href="./src/businessradar/resources/news/articles/articles.py">create_feedback</a>(\*\*<a href="src/businessradar/types/news/article_create_feedback_params.py">params</a>) -> <a href="./src/businessradar/types/news/article_create_feedback_response.py">ArticleCreateFeedbackResponse</a></code>
- <code title="get /ext/v3/saved_article_filters">client.news.articles.<a href="./src/businessradar/resources/news/articles/articles.py">list_saved_article_filters</a>(\*\*<a href="src/businessradar/types/news/article_list_saved_article_filters_params.py">params</a>) -> <a href="./src/businessradar/types/news/article_list_saved_article_filters_response.py">SyncNextKey[ArticleListSavedArticleFiltersResponse]</a></code>
- <code title="get /ext/v3/articles/{article_id}/related/">client.news.articles.<a href="./src/businessradar/resources/news/articles/articles.py">retrieve_related</a>(article_id) -> <a href="./src/businessradar/types/news/article_retrieve_related_response.py">ArticleRetrieveRelatedResponse</a></code>

### Analytics

Types:

```python
from businessradar.types.news.articles import AnalyticsGetCountByDateResponse
```

Methods:

- <code title="get /ext/v3/articles/analytics/dates/">client.news.articles.analytics.<a href="./src/businessradar/resources/news/articles/analytics.py">get_count_by_date</a>(\*\*<a href="src/businessradar/types/news/articles/analytics_get_count_by_date_params.py">params</a>) -> <a href="./src/businessradar/types/news/articles/analytics_get_count_by_date_response.py">AnalyticsGetCountByDateResponse</a></code>

### Export

Types:

```python
from businessradar.types.news.articles import ArticleExport, DataExportFileType, MediaTypeEnum
```

Methods:

- <code title="post /ext/v3/articles/export/">client.news.articles.export.<a href="./src/businessradar/resources/news/articles/export.py">create</a>(\*\*<a href="src/businessradar/types/news/articles/export_create_params.py">params</a>) -> <a href="./src/businessradar/types/news/articles/article_export.py">ArticleExport</a></code>
- <code title="get /ext/v3/articles/export/{external_id}">client.news.articles.export.<a href="./src/businessradar/resources/news/articles/export.py">retrieve</a>(external_id) -> <a href="./src/businessradar/types/news/articles/article_export.py">ArticleExport</a></code>

# Companies

Types:

```python
from businessradar.types import (
    BlankEnum,
    CountryEnum,
    IndustryCode,
    Registration,
    RegistrationRequest,
    CompanyRetrieveResponse,
    CompanyListResponse,
)
```

Methods:

- <code title="post /ext/v3/companies">client.companies.<a href="./src/businessradar/resources/companies.py">create</a>(\*\*<a href="src/businessradar/types/company_create_params.py">params</a>) -> <a href="./src/businessradar/types/registration.py">Registration</a></code>
- <code title="get /ext/v3/companies/{external_id}">client.companies.<a href="./src/businessradar/resources/companies.py">retrieve</a>(external_id) -> <a href="./src/businessradar/types/company_retrieve_response.py">CompanyRetrieveResponse</a></code>
- <code title="get /ext/v3/companies">client.companies.<a href="./src/businessradar/resources/companies.py">list</a>(\*\*<a href="src/businessradar/types/company_list_params.py">params</a>) -> <a href="./src/businessradar/types/company_list_response.py">SyncNextKey[CompanyListResponse]</a></code>
- <code title="get /ext/v3/registrations/{registration_id}">client.companies.<a href="./src/businessradar/resources/companies.py">retrieve_registration</a>(registration_id) -> <a href="./src/businessradar/types/registration.py">Registration</a></code>

# Compliance

Types:

```python
from businessradar.types import (
    ComplianceCheckScoreEnum,
    ComplianceCreateResponse,
    ComplianceRetrieveResponse,
)
```

Methods:

- <code title="post /ext/v3/compliance">client.compliance.<a href="./src/businessradar/resources/compliance.py">create</a>(\*\*<a href="src/businessradar/types/compliance_create_params.py">params</a>) -> <a href="./src/businessradar/types/compliance_create_response.py">ComplianceCreateResponse</a></code>
- <code title="get /ext/v3/compliance/{external_id}">client.compliance.<a href="./src/businessradar/resources/compliance.py">retrieve</a>(external_id) -> <a href="./src/businessradar/types/compliance_retrieve_response.py">ComplianceRetrieveResponse</a></code>

# Portfolios

Types:

```python
from businessradar.types import PermissionEnum, Portfolio
```

Methods:

- <code title="post /ext/v3/portfolios">client.portfolios.<a href="./src/businessradar/resources/portfolios/portfolios.py">create</a>(\*\*<a href="src/businessradar/types/portfolio_create_params.py">params</a>) -> <a href="./src/businessradar/types/portfolio.py">Portfolio</a></code>
- <code title="get /ext/v3/portfolios">client.portfolios.<a href="./src/businessradar/resources/portfolios/portfolios.py">list</a>(\*\*<a href="src/businessradar/types/portfolio_list_params.py">params</a>) -> <a href="./src/businessradar/types/portfolio.py">SyncNextKey[Portfolio]</a></code>

## Companies

Types:

```python
from businessradar.types.portfolios import CompanyListResponse
```

Methods:

- <code title="post /ext/v3/portfolios/{portfolio_id}/companies">client.portfolios.companies.<a href="./src/businessradar/resources/portfolios/companies.py">create</a>(portfolio_id, \*\*<a href="src/businessradar/types/portfolios/company_create_params.py">params</a>) -> <a href="./src/businessradar/types/registration.py">Registration</a></code>
- <code title="get /ext/v3/portfolios/{portfolio_id}/companies">client.portfolios.companies.<a href="./src/businessradar/resources/portfolios/companies.py">list</a>(portfolio_id, \*\*<a href="src/businessradar/types/portfolios/company_list_params.py">params</a>) -> <a href="./src/businessradar/types/portfolios/company_list_response.py">SyncNextKey[CompanyListResponse]</a></code>
- <code title="delete /ext/v3/portfolios/{portfolio_id}/companies/{external_id}">client.portfolios.companies.<a href="./src/businessradar/resources/portfolios/companies.py">delete</a>(external_id, \*, portfolio_id) -> None</code>
