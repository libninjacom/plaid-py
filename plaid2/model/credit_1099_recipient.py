from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field
from .credit_pay_stub_address import CreditPayStubAddress


class Credit1099Recipient(BaseModel):
    """Checked if 2nd TIN exists."""

    second_tin_exists: Optional[str] = None
    """Tax identification number of recipient."""
    tin: Optional[str] = None
    """Name of recipient."""
    name: Optional[str] = None
    """Address on the pay stub."""
    address: Optional[CreditPayStubAddress] = None
    """Account number number of recipient."""
    account_number: Optional[str] = None
    """Checked if FACTA is a filing requirement."""
    facta_filing_requirement: Optional[str] = None

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        kwargs.setdefault("by_alias", True)
        return super().json(**kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        kwargs.setdefault("by_alias", True)
        return super().dict(**kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "Credit1099Recipient":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "Credit1099Recipient":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
