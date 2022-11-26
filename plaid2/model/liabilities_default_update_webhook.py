from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field
from .liabilities_account_ids_with_updated_liabilities import (
    LiabilitiesAccountIdsWithUpdatedLiabilities,
)
from .plaid_error import PlaidError


class LiabilitiesDefaultUpdateWebhook(BaseModel):
    """We use standard HTTP response codes for success and failure notifications, and our errors are further classified by `error_type`. In general, 200 HTTP codes correspond to success, 40X codes are for developer- or user-related failures, and 50X codes are for Plaid-related issues.  Error fields will be `null` if no error has occurred."""

    error: Optional[PlaidError] = None
    """An array of `account_id`'s for accounts that contain new liabilities.'"""
    account_ids_with_new_liabilities: List[str]
    """An object with keys of `account_id`'s that are mapped to their respective liabilities fields that changed.
    
    Example: `{ "XMBvvyMGQ1UoLbKByoMqH3nXMj84ALSdE5B58": ["past_amount_due"] }`
    """
    account_ids_with_updated_liabilities: LiabilitiesAccountIdsWithUpdatedLiabilities
    """`LIABILITIES`"""
    webhook_type: str
    """The `item_id` of the Item associated with this webhook, warning, or error"""
    item_id: str
    """`DEFAULT_UPDATE`"""
    webhook_code: str

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        kwargs.setdefault("by_alias", True)
        return super().json(**kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        kwargs.setdefault("by_alias", True)
        return super().dict(**kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "LiabilitiesDefaultUpdateWebhook":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(
        cls, b: Union[bytes, str], **kwargs: Any
    ) -> "LiabilitiesDefaultUpdateWebhook":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
