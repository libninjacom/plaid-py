from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field
from .screening_hit_analysis import ScreeningHitAnalysis
from .screening_hit_data import ScreeningHitData


class WatchlistScreeningHit(BaseModel):
    """An ISO8601 formatted timestamp."""

    first_active: str
    """The current state of review. All watchlist screening hits begin in a `pending_review` state but can be changed by creating a review. When a hit is in the `pending_review` state, it will always show the latest version of the watchlist data Plaid has available and be compared against the latest customer information saved in the watchlist screening. Once a hit has been marked as `confirmed` or `dismissed` it will no longer be updated so that the state is as it was when the review was first conducted."""
    review_status: str
    """ID of the associated screening hit."""
    id: str
    """The identifier provided by the source sanction or watchlist. When one is not provided by the source, this is `null`."""
    source_uid: Optional[str] = None
    """An ISO8601 formatted timestamp."""
    historical_since: Optional[str] = None
    """Information associated with the watchlist hit"""
    data: Optional[ScreeningHitData] = None
    """Shorthand identifier for a specific screening list for individuals."""
    list_code: str
    """A universal identifier for a watchlist individual that is stable across searches and updates."""
    plaid_uid: str
    """Analysis information describing why a screening hit matched the provided user information"""
    analysis: Optional[ScreeningHitAnalysis] = None
    """An ISO8601 formatted timestamp."""
    inactive_since: Optional[str] = None

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        kwargs.setdefault("by_alias", True)
        return super().json(**kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        kwargs.setdefault("by_alias", True)
        return super().dict(**kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "WatchlistScreeningHit":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "WatchlistScreeningHit":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
