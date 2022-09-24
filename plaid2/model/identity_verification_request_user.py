from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field
from .user_address import UserAddress
from .user_id_number import UserIdNumber
from .user_name import UserName


class IdentityVerificationRequestUser(BaseModel):
    email_address: Optional[str] = None
    """A phone number in E.164 format."""
    phone_number: Optional[str] = None
    """The full name provided by the user. If the user has not submitted their name, this field will be null. Otherwise, both fields are guaranteed to be filled."""
    name: Optional[UserName] = None
    """Home address for the user."""
    address: Optional[UserAddress] = None
    """ID number submitted by the user, currently used only for the Identity Verification product. If the user has not submitted this data yet, this field will be `null`. Otherwise, both fields are guaranteed to be filled."""
    id_number: Optional[UserIdNumber] = None
    """An identifier to help you connect this object to your internal systems. For example, your database ID corresponding to this object."""
    client_user_id: str
    """A date in the format YYYY-MM-DD (RFC 3339 Section 5.6)."""
    date_of_birth: Optional[str] = None

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        kwargs.setdefault("by_alias", True)
        return super().json(**kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        kwargs.setdefault("by_alias", True)
        return super().dict(**kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "IdentityVerificationRequestUser":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(
        cls, b: Union[bytes, str], **kwargs: Any
    ) -> "IdentityVerificationRequestUser":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
