# Ext

## V3

Types:

```python
from businessradar.types.ext import (
    PortfolioCompanyDetailRequest,
    V3GetSchemaResponse,
    V3ListSavedArticleFiltersResponse,
)
```

Methods:

- <code title="get /ext/v3/registrations/{registration_id}">client.ext.v3.<a href="./src/businessradar/resources/ext/v3/v3.py">get_registration</a>(registration_id) -> <a href="./src/businessradar/types/ext/v3/registration.py">Registration</a></code>
- <code title="get /ext/v3/schema">client.ext.v3.<a href="./src/businessradar/resources/ext/v3/v3.py">get_schema</a>(\*\*<a href="src/businessradar/types/ext/v3_get_schema_params.py">params</a>) -> <a href="./src/businessradar/types/ext/v3_get_schema_response.py">V3GetSchemaResponse</a></code>
- <code title="get /ext/v3/saved_article_filters">client.ext.v3.<a href="./src/businessradar/resources/ext/v3/v3.py">list_saved_article_filters</a>(\*\*<a href="src/businessradar/types/ext/v3_list_saved_article_filters_params.py">params</a>) -> <a href="./src/businessradar/types/ext/v3_list_saved_article_filters_response.py">V3ListSavedArticleFiltersResponse</a></code>

### Articles

Types:

```python
from businessradar.types.ext.v3 import (
    Article,
    CategoryTree,
    FeedbackTypeEnum,
    LanguageEnum,
    ArticleListResponse,
    ArticleCreateFeedbackResponse,
    ArticleRetrieveRelatedResponse,
)
```

Methods:

- <code title="get /ext/v3/articles">client.ext.v3.articles.<a href="./src/businessradar/resources/ext/v3/articles/articles.py">list</a>(\*\*<a href="src/businessradar/types/ext/v3/article_list_params.py">params</a>) -> <a href="./src/businessradar/types/ext/v3/article_list_response.py">ArticleListResponse</a></code>
- <code title="post /ext/v3/articles/feedback/">client.ext.v3.articles.<a href="./src/businessradar/resources/ext/v3/articles/articles.py">create_feedback</a>(\*\*<a href="src/businessradar/types/ext/v3/article_create_feedback_params.py">params</a>) -> <a href="./src/businessradar/types/ext/v3/article_create_feedback_response.py">ArticleCreateFeedbackResponse</a></code>
- <code title="get /ext/v3/articles/{article_id}/related/">client.ext.v3.articles.<a href="./src/businessradar/resources/ext/v3/articles/articles.py">retrieve_related</a>(article_id) -> <a href="./src/businessradar/types/ext/v3/article_retrieve_related_response.py">ArticleRetrieveRelatedResponse</a></code>

#### Analytics

Types:

```python
from businessradar.types.ext.v3.articles import AnalyticsGetCountByDateResponse
```

Methods:

- <code title="get /ext/v3/articles/analytics/dates/">client.ext.v3.articles.analytics.<a href="./src/businessradar/resources/ext/v3/articles/analytics.py">get_count_by_date</a>(\*\*<a href="src/businessradar/types/ext/v3/articles/analytics_get_count_by_date_params.py">params</a>) -> <a href="./src/businessradar/types/ext/v3/articles/analytics_get_count_by_date_response.py">AnalyticsGetCountByDateResponse</a></code>

#### Export

Types:

```python
from businessradar.types.ext.v3.articles import ArticleExport, DataExportFileType, MediaTypeEnum
```

Methods:

- <code title="post /ext/v3/articles/export/">client.ext.v3.articles.export.<a href="./src/businessradar/resources/ext/v3/articles/export.py">create</a>(\*\*<a href="src/businessradar/types/ext/v3/articles/export_create_params.py">params</a>) -> <a href="./src/businessradar/types/ext/v3/articles/article_export.py">ArticleExport</a></code>
- <code title="get /ext/v3/articles/export/{external_id}">client.ext.v3.articles.export.<a href="./src/businessradar/resources/ext/v3/articles/export.py">retrieve</a>(external_id) -> <a href="./src/businessradar/types/ext/v3/articles/article_export.py">ArticleExport</a></code>

### Companies

Types:

```python
from businessradar.types.ext.v3 import (
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

- <code title="post /ext/v3/companies">client.ext.v3.companies.<a href="./src/businessradar/resources/ext/v3/companies.py">create</a>(\*\*<a href="src/businessradar/types/ext/v3/company_create_params.py">params</a>) -> <a href="./src/businessradar/types/ext/v3/registration.py">Registration</a></code>
- <code title="get /ext/v3/companies/{external_id}">client.ext.v3.companies.<a href="./src/businessradar/resources/ext/v3/companies.py">retrieve</a>(external_id) -> <a href="./src/businessradar/types/ext/v3/company_retrieve_response.py">CompanyRetrieveResponse</a></code>
- <code title="get /ext/v3/companies">client.ext.v3.companies.<a href="./src/businessradar/resources/ext/v3/companies.py">list</a>(\*\*<a href="src/businessradar/types/ext/v3/company_list_params.py">params</a>) -> <a href="./src/businessradar/types/ext/v3/company_list_response.py">CompanyListResponse</a></code>

### Compliance

Types:

```python
from businessradar.types.ext.v3 import (
    ComplianceCheckScoreEnum,
    ComplianceCreateResponse,
    ComplianceRetrieveResponse,
)
```

Methods:

- <code title="post /ext/v3/compliance">client.ext.v3.compliance.<a href="./src/businessradar/resources/ext/v3/compliance.py">create</a>(\*\*<a href="src/businessradar/types/ext/v3/compliance_create_params.py">params</a>) -> <a href="./src/businessradar/types/ext/v3/compliance_create_response.py">ComplianceCreateResponse</a></code>
- <code title="get /ext/v3/compliance/{external_id}">client.ext.v3.compliance.<a href="./src/businessradar/resources/ext/v3/compliance.py">retrieve</a>(external_id) -> <a href="./src/businessradar/types/ext/v3/compliance_retrieve_response.py">ComplianceRetrieveResponse</a></code>

### Portfolios

Types:

```python
from businessradar.types.ext.v3 import PermissionEnum, Portfolio, PortfolioListResponse
```

Methods:

- <code title="post /ext/v3/portfolios">client.ext.v3.portfolios.<a href="./src/businessradar/resources/ext/v3/portfolios/portfolios.py">create</a>(\*\*<a href="src/businessradar/types/ext/v3/portfolio_create_params.py">params</a>) -> <a href="./src/businessradar/types/ext/v3/portfolio.py">Portfolio</a></code>
- <code title="get /ext/v3/portfolios">client.ext.v3.portfolios.<a href="./src/businessradar/resources/ext/v3/portfolios/portfolios.py">list</a>(\*\*<a href="src/businessradar/types/ext/v3/portfolio_list_params.py">params</a>) -> <a href="./src/businessradar/types/ext/v3/portfolio_list_response.py">PortfolioListResponse</a></code>

#### Companies

Types:

```python
from businessradar.types.ext.v3.portfolios import CompanyListResponse
```

Methods:

- <code title="post /ext/v3/portfolios/{portfolio_id}/companies">client.ext.v3.portfolios.companies.<a href="./src/businessradar/resources/ext/v3/portfolios/companies.py">create</a>(portfolio_id, \*\*<a href="src/businessradar/types/ext/v3/portfolios/company_create_params.py">params</a>) -> <a href="./src/businessradar/types/ext/v3/registration.py">Registration</a></code>
- <code title="get /ext/v3/portfolios/{portfolio_id}/companies">client.ext.v3.portfolios.companies.<a href="./src/businessradar/resources/ext/v3/portfolios/companies.py">list</a>(portfolio_id, \*\*<a href="src/businessradar/types/ext/v3/portfolios/company_list_params.py">params</a>) -> <a href="./src/businessradar/types/ext/v3/portfolios/company_list_response.py">CompanyListResponse</a></code>
- <code title="delete /ext/v3/portfolios/{portfolio_id}/companies/{external_id}">client.ext.v3.portfolios.companies.<a href="./src/businessradar/resources/ext/v3/portfolios/companies.py">delete</a>(external_id, \*, portfolio_id) -> None</code>
