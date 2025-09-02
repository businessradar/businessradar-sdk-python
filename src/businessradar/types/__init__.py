# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from . import news
from .. import _compat
from .shared import PortfolioCompanyDetailRequest as PortfolioCompanyDetailRequest
from .portfolio import Portfolio as Portfolio
from .blank_enum import BlankEnum as BlankEnum
from .country_enum import CountryEnum as CountryEnum
from .registration import Registration as Registration
from .industry_code import IndustryCode as IndustryCode
from .permission_enum import PermissionEnum as PermissionEnum
from .company_list_params import CompanyListParams as CompanyListParams
from .company_create_params import CompanyCreateParams as CompanyCreateParams
from .company_list_response import CompanyListResponse as CompanyListResponse
from .portfolio_list_params import PortfolioListParams as PortfolioListParams
from .portfolio_create_params import PortfolioCreateParams as PortfolioCreateParams
from .compliance_create_params import ComplianceCreateParams as ComplianceCreateParams
from .company_retrieve_response import CompanyRetrieveResponse as CompanyRetrieveResponse
from .compliance_create_response import ComplianceCreateResponse as ComplianceCreateResponse
from .compliance_check_score_enum import ComplianceCheckScoreEnum as ComplianceCheckScoreEnum
from .compliance_retrieve_response import ComplianceRetrieveResponse as ComplianceRetrieveResponse

# Rebuild cyclical models only after all modules are imported.
# This ensures that, when building the deferred (due to cyclical references) model schema,
# Pydantic can resolve the necessary references.
# See: https://github.com/pydantic/pydantic/issues/11250 for more context.
if _compat.PYDANTIC_V2:
    news.article.Article.model_rebuild(_parent_namespace_depth=0)
    news.category_tree.CategoryTree.model_rebuild(_parent_namespace_depth=0)
else:
    news.article.Article.update_forward_refs()  # type: ignore
    news.category_tree.CategoryTree.update_forward_refs()  # type: ignore
