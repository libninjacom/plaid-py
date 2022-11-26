from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field


class InvestmentTransaction(BaseModel):
    """The ID of the Investment transaction, unique across all Plaid transactions. Like all Plaid identifiers, the `investment_transaction_id` is case sensitive."""

    investment_transaction_id: str
    """The `account_id` of the account against which this transaction posted."""
    account_id: str
    """The `security_id` to which this transaction is related."""
    security_id: Optional[str] = None
    """The number of units of the security involved in this transaction."""
    quantity: float
    """A legacy field formerly used internally by Plaid to identify certain canceled transactions."""
    cancel_transaction_id: Optional[str] = None
    """The complete value of the transaction. Positive values when cash is debited, e.g. purchases of stock; negative values when cash is credited, e.g. sales of stock. Treatment remains the same for cash-only movements unassociated with securities."""
    amount: float
    """The combined value of all fees applied to this transaction"""
    fees: Optional[float] = None
    """Value is one of the following:
    `buy`: Buying an investment
    `sell`: Selling an investment
    `cancel`: A cancellation of a pending transaction
    `cash`: Activity that modifies a cash position
    `fee`: A fee on the account
    `transfer`: Activity which modifies a position, but not through buy/sell activity e.g. options exercise, portfolio transfer
    
    For descriptions of possible transaction types and subtypes, see the [Investment transaction types schema](https://plaid.com/docs/api/accounts/#investment-transaction-types-schema)."""
    type: str
    """For descriptions of possible transaction types and subtypes, see the [Investment transaction types schema](https://plaid.com/docs/api/accounts/#investment-transaction-types-schema)."""
    subtype: str
    """The price of the security at which this transaction occurred."""
    price: float
    """The unofficial currency code associated with the holding. Always `null` if `iso_currency_code` is non-`null`. Unofficial currency codes are used for currencies that do not have official ISO currency codes, such as cryptocurrencies and the currencies of certain countries.
    
    See the [currency code schema](https://plaid.com/docs/api/accounts#currency-code-schema) for a full listing of supported `iso_currency_code`s."""
    unofficial_currency_code: Optional[str] = None
    """The ISO-4217 currency code of the transaction. Always `null` if `unofficial_currency_code` is non-`null`."""
    iso_currency_code: Optional[str] = None
    """The [ISO 8601](https://wikipedia.org/wiki/ISO_8601) posting date for the transaction."""
    date: str
    """The institution’s description of the transaction."""
    name: str

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        kwargs.setdefault("by_alias", True)
        return super().json(**kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        kwargs.setdefault("by_alias", True)
        return super().dict(**kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "InvestmentTransaction":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "InvestmentTransaction":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
