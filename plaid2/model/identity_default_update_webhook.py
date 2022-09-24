from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field
from .account_ids_with_updated_identity import AccountIdsWithUpdatedIdentity
from .plaid_error import PlaidError


class IdentityDefaultUpdateWebhook(BaseModel):
    """`IDENTITY`"""

    webhook_type: str
    """An object with keys of `account_id`'s that are mapped to their respective identity attributes that changed.
    
    Example: `{ "XMBvvyMGQ1UoLbKByoMqH3nXMj84ALSdE5B58": ["PHONES"] }`
    """
    account_ids_with_updated_identity: AccountIdsWithUpdatedIdentity
    """We use standard HTTP response codes for success and failure notifications, and our errors are further classified by `error_type`. In general, 200 HTTP codes correspond to success, 40X codes are for developer- or user-related failures, and 50X codes are for Plaid-related issues.  Error fields will be `null` if no error has occurred."""
    error: Optional[PlaidError] = None
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
    def parse_obj(cls, data: Any) -> "IdentityDefaultUpdateWebhook":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(
        cls, b: Union[bytes, str], **kwargs: Any
    ) -> "IdentityDefaultUpdateWebhook":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
