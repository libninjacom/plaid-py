from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field
from .watchlist_screening_audit_trail import WatchlistScreeningAuditTrail
from .watchlist_screening_search_terms import WatchlistScreeningSearchTerms


class WatchlistScreeningIndividualResponse(BaseModel):
    """Information about the last change made to the parent object specifying what caused the change as well as when it occurred."""

    audit_trail: WatchlistScreeningAuditTrail
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive."""
    request_id: str
    """ID of the associated screening."""
    id: str
    """Search terms for creating an individual watchlist screening"""
    search_terms: WatchlistScreeningSearchTerms
    assignee: Optional[str] = None
    """A status enum indicating whether a screening is still pending review, has been rejected, or has been cleared."""
    status: str
    client_user_id: Optional[str] = None

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        kwargs.setdefault("by_alias", True)
        return super().json(**kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        kwargs.setdefault("by_alias", True)
        return super().dict(**kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "WatchlistScreeningIndividualResponse":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(
        cls, b: Union[bytes, str], **kwargs: Any
    ) -> "WatchlistScreeningIndividualResponse":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
