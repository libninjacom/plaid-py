from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field
from .transfer_failure import TransferFailure


class TransferEvent(BaseModel):
    """Plaid’s unique identifier for this event. IDs are sequential unsigned 64-bit integers."""

    event_id: int
    """The datetime when this event occurred. This will be of the form `2006-01-02T15:04:05Z`."""
    timestamp: str
    """The account ID associated with the transfer."""
    account_id: str
    """Plaid’s unique identifier for a transfer."""
    transfer_id: str
    """The failure reason if the event type for a transfer is `"failed"` or `"returned"`. Null value otherwise."""
    failure_reason: Optional[TransferFailure] = None
    """Plaid’s unique identifier for a sweep."""
    sweep_id: Optional[str] = None
    """The type of event that this transfer represents.
    
    `pending`: A new transfer was created; it is in the pending state.
    
    `cancelled`: The transfer was cancelled by the client.
    
    `failed`: The transfer failed, no funds were moved.
    
    `posted`: The transfer has been successfully submitted to the payment network.
    
    `returned`: A posted transfer was returned.
    
    `swept`: The transfer was swept to / from the sweep account.
    
    `return_swept`: Due to the transfer being returned, funds were pulled from or pushed back to the sweep account."""
    event_type: str
    """The ID of the origination account that this balance belongs to."""
    origination_account_id: Optional[str] = None
    """A signed amount of how much was `swept` or `return_swept` (decimal string with two digits of precision e.g. "-5.50")."""
    sweep_amount: Optional[str] = None
    """The type of transfer. This will be either `debit` or `credit`.  A `debit` indicates a transfer of money into the origination account; a `credit` indicates a transfer of money out of the origination account."""
    transfer_type: str
    """The amount of the transfer (decimal string with two digits of precision e.g. "10.00")."""
    transfer_amount: str

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        kwargs.setdefault("by_alias", True)
        return super().json(**kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        kwargs.setdefault("by_alias", True)
        return super().dict(**kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "TransferEvent":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "TransferEvent":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
