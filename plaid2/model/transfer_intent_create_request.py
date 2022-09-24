from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field
from .transfer_metadata import TransferMetadata
from .transfer_user_in_request import TransferUserInRequest


class TransferIntentCreateRequest(BaseModel):
    """When `true`, the transfer requires a `GUARANTEED` decision by Plaid to proceed (Guaranteed ACH customers only)."""

    require_guarantee: Optional[bool] = None
    """Your Plaid API `secret`. The `secret` is required and may be provided either in the `PLAID-SECRET` header or as part of a request body."""
    secret: Optional[str] = None
    """A description for the underlying transfer. Maximum of 8 characters."""
    description: str
    """Your Plaid API `client_id`. The `client_id` is required and may be provided either in the `PLAID-CLIENT-ID` header or as part of a request body."""
    client_id: Optional[str] = None
    """Specifies the use case of the transfer. Required for transfers on an ACH network.
    
    `"ccd"` - Corporate Credit or Debit - fund transfer between two corporate bank accounts
    
    `"ppd"` - Prearranged Payment or Deposit - the transfer is part of a pre-existing relationship with a consumer, eg. bill payment
    
    `"tel"` - Telephone-Initiated Entry
    
    `"web"` - Internet-Initiated Entry - debits from a consumer’s account where their authorization is obtained over the Internet"""
    ach_class: str
    """The legal name and other information for the account holder."""
    user: TransferUserInRequest
    """The Metadata object is a mapping of client-provided string fields to any string value. The following limitations apply:
    - The JSON values must be Strings (no nested JSON objects allowed)
    - Only ASCII characters may be used
    - Maximum of 50 key/value pairs
    - Maximum key length of 40 characters
    - Maximum value length of 500 characters
    """
    metadata: Optional[TransferMetadata] = None
    """The Plaid `account_id` for the account that will be debited or credited."""
    account_id: Optional[str] = None
    """The amount of the transfer (decimal string with two digits of precision e.g. "10.00")."""
    amount: str
    """Plaid’s unique identifier for the origination account for the intent. If not provided, the default account will be used."""
    origination_account_id: Optional[str] = None
    """The currency of the transfer amount, e.g. "USD" """
    iso_currency_code: Optional[str] = None
    """The direction of the flow of transfer funds.
    
    - `PAYMENT` – Transfers funds from an end user's account to your business account.
    
    - `DISBURSEMENT` – Transfers funds from your business account to an end user's account."""
    mode: str

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        kwargs.setdefault("by_alias", True)
        return super().json(**kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        kwargs.setdefault("by_alias", True)
        return super().dict(**kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "TransferIntentCreateRequest":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(
        cls, b: Union[bytes, str], **kwargs: Any
    ) -> "TransferIntentCreateRequest":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
