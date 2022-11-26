from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field
from .employer_verification import EmployerVerification
from .platform_ids import PlatformIds


class EmploymentVerification(BaseModel):
    """Current title of employee."""

    title: Optional[str] = None
    """An object containing a set of ids related to an employee"""
    platform_ids: Optional[PlatformIds] = None
    """End of employment, if applicable. Provided in ISO 8601 format (YYY-MM-DD)."""
    end_date: Optional[str] = None
    """Start of employment in ISO 8601 format (YYYY-MM-DD)."""
    start_date: Optional[str] = None
    """Current employment status."""
    status: Optional[str] = None
    """An object containing employer data."""
    employer: Optional[EmployerVerification] = None

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        kwargs.setdefault("by_alias", True)
        return super().json(**kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        kwargs.setdefault("by_alias", True)
        return super().dict(**kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "EmploymentVerification":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "EmploymentVerification":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
