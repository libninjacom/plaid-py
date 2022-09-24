from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field
from .plaid_error import PlaidError


class InvestmentsDefaultUpdateWebhook(BaseModel):
    """`INVESTMENTS_TRANSACTIONS`"""

    webhook_type: str
    """`DEFAULT_UPDATE`"""
    webhook_code: str
    """The `item_id` of the Item associated with this webhook, warning, or error"""
    item_id: str
    """We use standard HTTP response codes for success and failure notifications, and our errors are further classified by `error_type`. In general, 200 HTTP codes correspond to success, 40X codes are for developer- or user-related failures, and 50X codes are for Plaid-related issues.  Error fields will be `null` if no error has occurred."""
    error: Optional[PlaidError] = None
    """The number of canceled transactions reported since the last time this webhook was fired."""
    canceled_investments_transactions: float
    """The number of new transactions reported since the last time this webhook was fired."""
    new_investments_transactions: float

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        kwargs.setdefault("by_alias", True)
        return super().json(**kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        kwargs.setdefault("by_alias", True)
        return super().dict(**kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "InvestmentsDefaultUpdateWebhook":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(
        cls, b: Union[bytes, str], **kwargs: Any
    ) -> "InvestmentsDefaultUpdateWebhook":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
