from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field
from .payment_consent_max_payment_amount import PaymentConsentMaxPaymentAmount
from .payment_consent_periodic_amount import PaymentConsentPeriodicAmount
from .payment_consent_valid_date_time import PaymentConsentValidDateTime


class PaymentInitiationConsentConstraints(BaseModel):
    """Life span for the payment consent. After the `to` date the payment consent expires and can no longer be used for payment initiation."""

    valid_date_time: Optional[PaymentConsentValidDateTime] = None
    """Maximum amount of a single payment initiated using the payment consent."""
    max_payment_amount: PaymentConsentMaxPaymentAmount
    """A list of amount limitations per period of time."""
    periodic_amounts: List[PaymentConsentPeriodicAmount]

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        kwargs.setdefault("by_alias", True)
        return super().json(**kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        kwargs.setdefault("by_alias", True)
        return super().dict(**kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "PaymentInitiationConsentConstraints":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(
        cls, b: Union[bytes, str], **kwargs: Any
    ) -> "PaymentInitiationConsentConstraints":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
