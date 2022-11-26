from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field


class PaymentInitiationPaymentReverseResponse(BaseModel):
    """The status of the refund.

    `PROCESSING`: The refund is currently being processed. The refund will automatically exit this state when processing is complete.

    `INITIATED`: The refund has been successfully initiated.

    `EXECUTED`: Indicates that the refund has been successfully executed.

    `FAILED`: The refund has failed to be executed. This error is retryable once the root cause is resolved."""

    status: str
    """A unique ID identifying the refund"""
    refund_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive."""
    request_id: str

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        kwargs.setdefault("by_alias", True)
        return super().json(**kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        kwargs.setdefault("by_alias", True)
        return super().dict(**kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "PaymentInitiationPaymentReverseResponse":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(
        cls, b: Union[bytes, str], **kwargs: Any
    ) -> "PaymentInitiationPaymentReverseResponse":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
