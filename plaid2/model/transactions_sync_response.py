from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field
from .removed_transaction import RemovedTransaction
from .transaction import Transaction


class TransactionsSyncResponse(BaseModel):
    """Transactions that have been modified on the item since `cursor` ordered by ascending last modified time."""

    modified: List[Transaction]
    """Represents if more than requested count of transaction updates exist. If true, the additional updates can be fetched by making an additional request with `cursor` set to `next_cursor`."""
    has_more: bool
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive."""
    request_id: str
    """Transactions that have been added to the item since `cursor` ordered by ascending last modified time."""
    added: List[Transaction]
    """Transactions that have been removed from the item since `cursor` ordered by ascending last modified time."""
    removed: List[RemovedTransaction]
    """Cursor used for fetching any future updates after the latest update provided in this response."""
    next_cursor: str

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        kwargs.setdefault("by_alias", True)
        return super().json(**kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        kwargs.setdefault("by_alias", True)
        return super().dict(**kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "TransactionsSyncResponse":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(
        cls, b: Union[bytes, str], **kwargs: Any
    ) -> "TransactionsSyncResponse":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
