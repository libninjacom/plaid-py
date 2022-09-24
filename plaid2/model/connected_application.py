from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field
from .scopes_nullable import ScopesNullable


class ConnectedApplication(BaseModel):
    """The date this application was linked in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) (YYYY-MM-DD) format in UTC."""

    created_at: str
    """The scopes object"""
    scopes: Optional[ScopesNullable] = None
    """A string provided by the connected app stating why they use their respective enabled products."""
    reason_for_access: Optional[str] = None
    """A human-readable name of the application for display purposes"""
    display_name: Optional[str] = None
    """The name of the application"""
    name: str
    """The URL for the application's website"""
    application_url: Optional[str] = None
    """A URL that links to the application logo image."""
    logo_url: Optional[str] = None
    """This field will map to the application ID that is returned from /item/applications/list, or provided to the institution in an oauth redirect."""
    application_id: str

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        kwargs.setdefault("by_alias", True)
        return super().json(**kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        kwargs.setdefault("by_alias", True)
        return super().dict(**kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "ConnectedApplication":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "ConnectedApplication":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
