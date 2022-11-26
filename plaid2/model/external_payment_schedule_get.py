from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field
from .external_payment_schedule_base import ExternalPaymentScheduleBase


class ExternalPaymentScheduleGet(BaseModel):
    """The schedule that the payment will be executed on. If a schedule is provided, the payment is automatically set up as a standing order. If no schedule is specified, the payment will be executed only once."""

    external_payment_schedule_base: Optional[ExternalPaymentScheduleBase] = None

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        kwargs.setdefault("by_alias", True)
        return super().json(**kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        kwargs.setdefault("by_alias", True)
        return super().dict(**kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "ExternalPaymentScheduleGet":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(
        cls, b: Union[bytes, str], **kwargs: Any
    ) -> "ExternalPaymentScheduleGet":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
