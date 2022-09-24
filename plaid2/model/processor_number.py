from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field
from .numbers_ach_nullable import NumbersAchNullable
from .numbers_bacs_nullable import NumbersBacsNullable
from .numbers_eft_nullable import NumbersEftNullable
from .numbers_international_nullable import NumbersInternationalNullable


class ProcessorNumber(BaseModel):
    """Identifying information for transferring money to or from a Canadian bank account via EFT."""

    eft: Optional[NumbersEftNullable] = None
    """Identifying information for transferring money to or from a US account via ACH or wire transfer."""
    ach: Optional[NumbersAchNullable] = None
    """Identifying information for transferring money to or from a UK bank account via BACS."""
    bacs: Optional[NumbersBacsNullable] = None
    """Identifying information for transferring money to or from an international bank account via wire transfer."""
    international: Optional[NumbersInternationalNullable] = None

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        kwargs.setdefault("by_alias", True)
        return super().json(**kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        kwargs.setdefault("by_alias", True)
        return super().dict(**kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "ProcessorNumber":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "ProcessorNumber":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
