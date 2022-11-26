from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field


class StandaloneInvestmentTransactionType(BaseModel):
    """Activity that modifies a position, but not through buy/sell activity e.g. options exercise, portfolio transfer"""

    transfer: str
    """Buying an investment"""
    buy: str
    """Selling an investment"""
    sell: str
    """Activity that modifies a cash position"""
    cash: str
    """A cancellation of a pending transaction"""
    cancel: str
    """Fees on the account, e.g. commission, bookkeeping, options-related."""
    fee: str

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        kwargs.setdefault("by_alias", True)
        return super().json(**kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        kwargs.setdefault("by_alias", True)
        return super().dict(**kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "StandaloneInvestmentTransactionType":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(
        cls, b: Union[bytes, str], **kwargs: Any
    ) -> "StandaloneInvestmentTransactionType":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
