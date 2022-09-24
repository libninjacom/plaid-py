from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field


class Location(BaseModel):
    """The latitude where the transaction occurred."""

    lat: Optional[float] = None
    """The street address where the transaction occurred."""
    address: Optional[str] = None
    """The city where the transaction occurred."""
    city: Optional[str] = None
    """The postal code where the transaction occurred. In API versions 2018-05-22 and earlier, this field is called `zip`."""
    postal_code: Optional[str] = None
    """The longitude where the transaction occurred."""
    lon: Optional[float] = None
    """The region or state where the transaction occurred. In API versions 2018-05-22 and earlier, this field is called `state`."""
    region: Optional[str] = None
    """The merchant defined store number where the transaction occurred."""
    store_number: Optional[str] = None
    """The ISO 3166-1 alpha-2 country code where the transaction occurred."""
    country: Optional[str] = None

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        kwargs.setdefault("by_alias", True)
        return super().json(**kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        kwargs.setdefault("by_alias", True)
        return super().dict(**kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "Location":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "Location":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
