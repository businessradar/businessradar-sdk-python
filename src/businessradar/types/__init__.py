# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from . import news
from .. import _compat
from .ubo import Ubo as Ubo
from .shared import PortfolioCompanyDetailRequest as PortfolioCompanyDetailRequest
from .webhook import Webhook as Webhook
from .portfolio import Portfolio as Portfolio
from .blank_enum import BlankEnum as BlankEnum
from .country_enum import CountryEnum as CountryEnum
from .registration import Registration as Registration
from .industry_code import IndustryCode as IndustryCode
from .permission_enum import PermissionEnum as PermissionEnum
from .webhook_delivery import WebhookDelivery as WebhookDelivery
from .company_list_params import CompanyListParams as CompanyListParams
from .webhook_list_params import WebhookListParams as WebhookListParams
from .webhook_subscription import WebhookSubscription as WebhookSubscription
from .company_create_params import CompanyCreateParams as CompanyCreateParams
from .company_list_response import CompanyListResponse as CompanyListResponse
from .portfolio_list_params import PortfolioListParams as PortfolioListParams
from .webhook_create_params import WebhookCreateParams as WebhookCreateParams
from .webhook_update_params import WebhookUpdateParams as WebhookUpdateParams
from .compliance_list_params import ComplianceListParams as ComplianceListParams
from .portfolio_create_params import PortfolioCreateParams as PortfolioCreateParams
from .compliance_create_params import ComplianceCreateParams as ComplianceCreateParams
from .compliance_list_response import ComplianceListResponse as ComplianceListResponse
from .portfolio_company_detail import PortfolioCompanyDetail as PortfolioCompanyDetail
from .company_retrieve_response import CompanyRetrieveResponse as CompanyRetrieveResponse
from .compliance_create_response import ComplianceCreateResponse as ComplianceCreateResponse
from .compliance_entity_retrieve import ComplianceEntityRetrieve as ComplianceEntityRetrieve
from .compliance_check_score_enum import ComplianceCheckScoreEnum as ComplianceCheckScoreEnum
from .compliance_retrieve_response import ComplianceRetrieveResponse as ComplianceRetrieveResponse
from .webhook_delivery_status_enum import WebhookDeliveryStatusEnum as WebhookDeliveryStatusEnum
from .webhook_partial_update_params import WebhookPartialUpdateParams as WebhookPartialUpdateParams
from .company_create_feedback_params import CompanyCreateFeedbackParams as CompanyCreateFeedbackParams
from .compliance_list_results_params import ComplianceListResultsParams as ComplianceListResultsParams
from .company_create_feedback_response import CompanyCreateFeedbackResponse as CompanyCreateFeedbackResponse
from .compliance_list_results_response import ComplianceListResultsResponse as ComplianceListResultsResponse
from .webhook_regenerate_secret_response import WebhookRegenerateSecretResponse as WebhookRegenerateSecretResponse
from .webhook_subscription_request_param import WebhookSubscriptionRequestParam as WebhookSubscriptionRequestParam
from .company_list_attribute_changes_params import (
    CompanyListAttributeChangesParams as CompanyListAttributeChangesParams,
)
from .company_list_attribute_changes_response import (
    CompanyListAttributeChangesResponse as CompanyListAttributeChangesResponse,
)
from .company_list_missing_company_investigations_params import (
    CompanyListMissingCompanyInvestigationsParams as CompanyListMissingCompanyInvestigationsParams,
)
from .company_create_missing_company_investigation_params import (
    CompanyCreateMissingCompanyInvestigationParams as CompanyCreateMissingCompanyInvestigationParams,
)
from .company_list_missing_company_investigations_response import (
    CompanyListMissingCompanyInvestigationsResponse as CompanyListMissingCompanyInvestigationsResponse,
)
from .company_create_missing_company_investigation_response import (
    CompanyCreateMissingCompanyInvestigationResponse as CompanyCreateMissingCompanyInvestigationResponse,
)
from .company_retrieve_missing_company_investigation_response import (
    CompanyRetrieveMissingCompanyInvestigationResponse as CompanyRetrieveMissingCompanyInvestigationResponse,
)

# Rebuild cyclical models only after all modules are imported.
# This ensures that, when building the deferred (due to cyclical references) model schema,
# Pydantic can resolve the necessary references.
# See: https://github.com/pydantic/pydantic/issues/11250 for more context.
if _compat.PYDANTIC_V1:
    news.article.Article.update_forward_refs()  # type: ignore
    news.category_tree.CategoryTree.update_forward_refs()  # type: ignore
else:
    news.article.Article.model_rebuild(_parent_namespace_depth=0)
    news.category_tree.CategoryTree.model_rebuild(_parent_namespace_depth=0)
