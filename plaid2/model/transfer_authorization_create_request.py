from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field
from .transfer_authorization_device import TransferAuthorizationDevice
from .transfer_authorization_user_in_request import TransferAuthorizationUserInRequest


class TransferAuthorizationCreateRequest(BaseModel):
    """The currency of the transfer amount. The default value is "USD"."""

    iso_currency_code: Optional[str] = None
    """The network or rails used for the transfer. Valid options are `ach` or `same-day-ach`. The cutoff for same-day transfers is 7:45 AM Pacific Time and the cutoff for next-day transfers is 5:45 PM Pacific Time. It is recommended to submit a transfer at least 15 minutes before the cutoff time in order to ensure that it will be processed before the cutoff. Any transfer that is indicated as `same-day-ach` and that misses the same-day cutoff, but is submitted in time for the next-day cutoff, will be sent over next-day rails and will not incur same-day charges. Note that both legs of the transfer will be downgraded if applicable."""
    network: str
    """Plaid's unique identifier for the origination account for this authorization. If not specified, the default account will be used."""
    origination_account_id: Optional[str] = None
    """The Plaid `account_id` for the account that will be debited or credited."""
    account_id: Optional[str] = None
    """The legal name and other information for the account holder."""
    user: TransferAuthorizationUserInRequest
    """The Plaid `access_token` for the account that will be debited or credited."""
    access_token: Optional[str] = None
    """Information about the device being used to initiate the authorization."""
    device: Optional[TransferAuthorizationDevice] = None
    """Specifies the use case of the transfer. Required for transfers on an ACH network.
    
    `"ccd"` - Corporate Credit or Debit - fund transfer between two corporate bank accounts
    
    `"ppd"` - Prearranged Payment or Deposit - the transfer is part of a pre-existing relationship with a consumer, eg. bill payment
    
    `"tel"` - Telephone-Initiated Entry
    
    `"web"` - Internet-Initiated Entry - debits from a consumer’s account where their authorization is obtained over the Internet"""
    ach_class: str
    """Required for guaranteed ACH customers. If the end user is initiating the specific transfer themselves via an interactive UI, this should be `true`; for automatic recurring payments where the end user is not actually initiating each individual transfer, it should be `false`."""
    user_present: Optional[bool] = None
    """Plaid’s unique identifier for a payment profile."""
    payment_profile_id: Optional[str] = None
    """The type of transfer. This will be either `debit` or `credit`.  A `debit` indicates a transfer of money into the origination account; a `credit` indicates a transfer of money out of the origination account."""
    type: str
    """The amount of the transfer (decimal string with two digits of precision e.g. "10.00")."""
    amount: str

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        kwargs.setdefault("by_alias", True)
        return super().json(**kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        kwargs.setdefault("by_alias", True)
        return super().dict(**kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "TransferAuthorizationCreateRequest":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(
        cls, b: Union[bytes, str], **kwargs: Any
    ) -> "TransferAuthorizationCreateRequest":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
