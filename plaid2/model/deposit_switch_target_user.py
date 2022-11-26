from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field
from .deposit_switch_address_data import DepositSwitchAddressData


class DepositSwitchTargetUser(BaseModel):
    """The given name (first name) of the user."""

    given_name: str
    """The email address of the user."""
    email: str
    """The phone number of the user. The endpoint can accept a variety of phone number formats, including E.164."""
    phone: str
    """The family name (last name) of the user."""
    family_name: str
    """The user's address."""
    address: Optional[DepositSwitchAddressData] = None
    """The taxpayer ID of the user, generally their SSN, EIN, or TIN."""
    tax_payer_id: Optional[str] = None

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        kwargs.setdefault("by_alias", True)
        return super().json(**kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        kwargs.setdefault("by_alias", True)
        return super().dict(**kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "DepositSwitchTargetUser":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(
        cls, b: Union[bytes, str], **kwargs: Any
    ) -> "DepositSwitchTargetUser":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
