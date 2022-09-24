from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field
from .credit_filter import CreditFilter
from .depository_filter import DepositoryFilter
from .investment_filter import InvestmentFilter
from .loan_filter import LoanFilter


class LinkTokenAccountFilters(BaseModel):
    """A filter to apply to `loan`-type accounts"""

    loan: Optional[LoanFilter] = None
    """A filter to apply to `investment`-type accounts (or `brokerage`-type accounts for API versions 2018-05-22 and earlier)."""
    investment: Optional[InvestmentFilter] = None
    """A filter to apply to `depository`-type accounts"""
    depository: Optional[DepositoryFilter] = None
    """A filter to apply to `credit`-type accounts"""
    credit: Optional[CreditFilter] = None

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        kwargs.setdefault("by_alias", True)
        return super().json(**kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        kwargs.setdefault("by_alias", True)
        return super().dict(**kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "LinkTokenAccountFilters":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(
        cls, b: Union[bytes, str], **kwargs: Any
    ) -> "LinkTokenAccountFilters":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
