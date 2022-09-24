from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field


class SecurityOverride(BaseModel):
    """12-character ISIN, a globally unique securities identifier."""

    isin: Optional[str] = None
    """9-character CUSIP, an identifier assigned to North American securities."""
    cusip: Optional[str] = None
    """The security’s trading symbol for publicly traded securities, and otherwise a short identifier if available."""
    ticker_symbol: Optional[str] = None
    """7-character SEDOL, an identifier assigned to securities in the UK."""
    sedol: Optional[str] = None
    """Either a valid `iso_currency_code` or `unofficial_currency_code`"""
    currency: Optional[str] = None
    """A descriptive name for the security, suitable for display."""
    name: Optional[str] = None

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        kwargs.setdefault("by_alias", True)
        return super().json(**kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        kwargs.setdefault("by_alias", True)
        return super().dict(**kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "SecurityOverride":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "SecurityOverride":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
