from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field
from .payment_consent_periodic_amount_amount import PaymentConsentPeriodicAmountAmount


class PaymentConsentPeriodicAmount(BaseModel):
    """Where the payment consent period should start.

    `CALENDAR`: line up with a calendar.

    `CONSENT`: on the date of consent creation."""

    alignment: str
    """Payment consent periodic interval."""
    interval: str
    """Maximum cumulative amount for all payments in the specified interval."""
    amount: PaymentConsentPeriodicAmountAmount

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        kwargs.setdefault("by_alias", True)
        return super().json(**kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        kwargs.setdefault("by_alias", True)
        return super().dict(**kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "PaymentConsentPeriodicAmount":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(
        cls, b: Union[bytes, str], **kwargs: Any
    ) -> "PaymentConsentPeriodicAmount":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
