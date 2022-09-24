from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field


class EntityWatchlistScreeningSearchTerms(BaseModel):
    """The name of the organization being screened."""

    legal_name: str
    email_address: Optional[str] = None
    url: Optional[str] = None
    """ID of the associated entity program."""
    entity_watchlist_program_id: str
    document_number: Optional[str] = None
    """The current version of the search terms. Starts at `1` and increments with each edit to `search_terms`."""
    version: float
    phone_number: Optional[str] = None
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
    def parse_obj(cls, data: Any) -> "EntityWatchlistScreeningSearchTerms":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(
        cls, b: Union[bytes, str], **kwargs: Any
    ) -> "EntityWatchlistScreeningSearchTerms":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
