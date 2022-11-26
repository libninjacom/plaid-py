from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field


class TransferSweep(BaseModel):
    created: str
    """The datetime when the sweep occurred, in RFC 3339 format."""

    amount: str
    """Signed decimal amount of the sweep as it appears on your sweep account ledger (e.g. "-10.00")
    
    If amount is not present, the sweep was net-settled to zero and outstanding debits and credits between the sweep account and Plaid are balanced."""

    id: str
    """Identifier of the sweep."""

    iso_currency_code: str
    """The currency of the sweep, e.g. "USD"."""

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        kwargs.setdefault("by_alias", True)
        return super().json(**kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        kwargs.setdefault("by_alias", True)
        return super().dict(**kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "TransferSweep":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "TransferSweep":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
