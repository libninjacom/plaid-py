from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field
from .payroll_income_account_data import PayrollIncomeAccountData
from .payroll_income_object import PayrollIncomeObject
from .payroll_item_status import PayrollItemStatus


class PayrollItem(BaseModel):
    """The `item_id` of the Item associated with this webhook, warning, or error"""

    item_id: str
    payroll_income: List[PayrollIncomeObject]
    """A reference id to reference what payroll data was returned from this endpoint"""
    pull_id: str
    """Details about the status of the payroll item."""
    status: Optional[PayrollItemStatus] = None
    accounts: List[PayrollIncomeAccountData]

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        kwargs.setdefault("by_alias", True)
        return super().json(**kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        kwargs.setdefault("by_alias", True)
        return super().dict(**kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "PayrollItem":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "PayrollItem":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
