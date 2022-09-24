from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field
from .recipient_bacs_nullable import RecipientBacsNullable


class ExternalPaymentRefundDetails(BaseModel):
    """The International Bank Account Number (IBAN) for the account."""

    iban: Optional[str] = None
    """The name of the account holder."""
    name: str
    """An object containing a BACS account number and sort code. If an IBAN is not provided or if this recipient needs to accept domestic GBP-denominated payments, BACS data is required."""
    bacs: Optional[RecipientBacsNullable] = None

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        kwargs.setdefault("by_alias", True)
        return super().json(**kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        kwargs.setdefault("by_alias", True)
        return super().dict(**kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "ExternalPaymentRefundDetails":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(
        cls, b: Union[bytes, str], **kwargs: Any
    ) -> "ExternalPaymentRefundDetails":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
