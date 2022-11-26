from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field
from .payment_initiation_consent_constraints import PaymentInitiationConsentConstraints


class PaymentInitiationConsent(BaseModel):
    """The ID of the recipient the payment consent is for."""

    recipient_id: str
    """A reference for the payment consent."""
    reference: str
    """An array of payment consent scopes."""
    scopes: List[str]
    """The consent ID."""
    consent_id: str
    """Limitations that will be applied to payments initiated using the payment consent."""
    constraints: PaymentInitiationConsentConstraints
    """Consent creation timestamp, in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format."""
    created_at: str
    """The status of the payment consent.
    
    `UNAUTHORISED`: Consent created, but requires user authorisation.
    
    `REJECTED`: Consent authorisation was rejected by the user and/or the bank.
    
    `AUTHORISED`: Consent is active and ready to be used.
    
    `REVOKED`: Consent has been revoked and can no longer be used.
    
    `EXPIRED`: Consent is no longer valid."""
    status: str

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        kwargs.setdefault("by_alias", True)
        return super().json(**kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        kwargs.setdefault("by_alias", True)
        return super().dict(**kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "PaymentInitiationConsent":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(
        cls, b: Union[bytes, str], **kwargs: Any
    ) -> "PaymentInitiationConsent":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
