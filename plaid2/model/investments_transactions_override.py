from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field
from .security_override import SecurityOverride


class InvestmentsTransactionsOverride(BaseModel):
    """The type of the investment transaction. Possible values are:
    `buy`: Buying an investment
    `sell`: Selling an investment
    `cash`: Activity that modifies a cash position
    `fee`: A fee on the account
    `transfer`: Activity that modifies a position, but not through buy/sell activity e.g. options exercise, portfolio transfer"""

    type: str
    """Either a valid `iso_currency_code` or `unofficial_currency_code`"""
    currency: str
    """The combined value of all fees applied to this transaction."""
    fees: Optional[float] = None
    """Specify the security associated with the holding or investment transaction. When inputting custom security data to the Sandbox, Plaid will perform post-data-retrieval normalization and enrichment. These processes may cause the data returned by the Sandbox to be slightly different from the data you input. An ISO-4217 currency code and a security identifier (`ticker_symbol`, `cusip`, `isin`, or `sedol`) are required."""
    security: Optional[SecurityOverride] = None
    """The institution's description of the transaction."""
    name: str
    """Posting date for the transaction. Must be formatted as an [ISO 8601](https://wikipedia.org/wiki/ISO_8601) date."""
    date: str
    """The number of units of the security involved in this transaction. Must be positive if the type is a buy and negative if the type is a sell."""
    quantity: float
    """The price of the security at which this transaction occurred."""
    price: float

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        kwargs.setdefault("by_alias", True)
        return super().json(**kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        kwargs.setdefault("by_alias", True)
        return super().dict(**kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "InvestmentsTransactionsOverride":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(
        cls, b: Union[bytes, str], **kwargs: Any
    ) -> "InvestmentsTransactionsOverride":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
