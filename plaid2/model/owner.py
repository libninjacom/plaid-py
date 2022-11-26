from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field
from .address import Address
from .email import Email
from .phone_number import PhoneNumber


class Owner(BaseModel):
    """A list of names associated with the account by the financial institution. These should always be the names of individuals, even for business accounts. If the name of a business is reported, please contact Plaid Support. In the case of a joint account, Plaid will make a best effort to report the names of all account holders.

    If an Item contains multiple accounts with different owner names, some institutions will report all names associated with the Item in each account's `names` array."""

    names: List[str]
    """A list of email addresses associated with the account by the financial institution. May be an empty array if no relevant information is returned from the financial institution."""
    emails: List[Email]
    """A list of phone numbers associated with the account by the financial institution. May be an empty array if no relevant information is returned from the financial institution."""
    phone_numbers: List[PhoneNumber]
    """Data about the various addresses associated with the account by the financial institution. May be an empty array if no relevant information is returned from the financial institution."""
    addresses: List[Address]

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        kwargs.setdefault("by_alias", True)
        return super().json(**kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        kwargs.setdefault("by_alias", True)
        return super().dict(**kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "Owner":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "Owner":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
