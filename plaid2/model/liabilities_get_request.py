from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field
from .liabilities_get_request_options import LiabilitiesGetRequestOptions


class LiabilitiesGetRequest(BaseModel):
    """An optional object to filter `/liabilities/get` results. If provided, `options` cannot be null."""

    options: Optional[LiabilitiesGetRequestOptions] = None
    """The access token associated with the Item data is being requested for."""
    access_token: str

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        kwargs.setdefault("by_alias", True)
        return super().json(**kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        kwargs.setdefault("by_alias", True)
        return super().dict(**kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "LiabilitiesGetRequest":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "LiabilitiesGetRequest":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
