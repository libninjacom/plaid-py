from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field


class InitialUpdateWebhook(BaseModel):
    """The number of new, unfetched transactions available."""

    new_transactions: float
    """`INITIAL_UPDATE`"""
    webhook_code: str
    """`TRANSACTIONS`"""
    webhook_type: str
    """The error code associated with the webhook."""
    error: Optional[str] = None
    """The `item_id` of the Item associated with this webhook, warning, or error"""
    item_id: str

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        kwargs.setdefault("by_alias", True)
        return super().json(**kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        kwargs.setdefault("by_alias", True)
        return super().dict(**kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "InitialUpdateWebhook":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "InitialUpdateWebhook":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
