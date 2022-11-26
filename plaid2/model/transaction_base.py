from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field
from .location import Location
from .payment_meta import PaymentMeta


class TransactionBase(BaseModel):
    """The string returned by the financial institution to describe the transaction. For transactions returned by `/transactions/get`, this field is in beta and will be omitted unless the client is both enrolled in the closed beta program and has set `options.include_original_description` to `true`."""

    original_description: Optional[str] = None
    """The unofficial currency code associated with the transaction. Always `null` if `iso_currency_code` is non-`null`. Unofficial currency codes are used for currencies that do not have official ISO currency codes, such as cryptocurrencies and the currencies of certain countries.
    
    See the [currency code schema](https://plaid.com/docs/api/accounts#currency-code-schema) for a full listing of supported `iso_currency_code`s."""
    unofficial_currency_code: Optional[str] = None
    """The check number of the transaction. This field is only populated for check transactions."""
    check_number: Optional[str] = None
    """The ISO-4217 currency code of the transaction. Always `null` if `unofficial_currency_code` is non-null."""
    iso_currency_code: Optional[str] = None
    """The ID of a posted transaction's associated pending transaction, where applicable."""
    pending_transaction_id: Optional[str] = None
    """When `true`, identifies the transaction as pending or unsettled. Pending transaction details (name, type, amount, category ID) may change before they are settled."""
    pending: bool
    """Transaction information specific to inter-bank transfers. If the transaction was not an inter-bank transfer, all fields will be `null`.
    
    If the `transactions` object was returned by a Transactions endpoint such as `/transactions/get`, the `payment_meta` key will always appear, but no data elements are guaranteed. If the `transactions` object was returned by an Assets endpoint such as `/asset_report/get/` or `/asset_report/pdf/get`, this field will only appear in an Asset Report with Insights."""
    payment_meta: Optional[PaymentMeta] = None
    """The settled value of the transaction, denominated in the transactions's currency, as stated in `iso_currency_code` or `unofficial_currency_code`. Positive values when money moves out of the account; negative values when money moves in. For example, debit card purchases are positive; credit card payments, direct deposits, and refunds are negative."""
    amount: float
    """The name of the account owner. This field is not typically populated and only relevant when dealing with sub-accounts."""
    account_owner: Optional[str] = None
    """The unique ID of the transaction. Like all Plaid identifiers, the `transaction_id` is case sensitive."""
    transaction_id: str
    """The merchant name or transaction description.
    
    If the `transactions` object was returned by a Transactions endpoint such as `/transactions/get`, this field will always appear. If the `transactions` object was returned by an Assets endpoint such as `/asset_report/get/` or `/asset_report/pdf/get`, this field will only appear in an Asset Report with Insights."""
    name: Optional[str] = None
    """The ID of the account in which this transaction occurred."""
    account_id: str
    """A representation of where a transaction took place"""
    location: Optional[Location] = None
    """A hierarchical array of the categories to which this transaction belongs. For a full list of categories, see [`/categories/get`](https://plaid.com/docs/api/products/transactions/#categoriesget).
    
    If the `transactions` object was returned by an Assets endpoint such as `/asset_report/get/` or `/asset_report/pdf/get`, this field will only appear in an Asset Report with Insights."""
    category: Optional[List[str]] = None
    """The ID of the category to which this transaction belongs. For a full list of categories, see [`/categories/get`](https://plaid.com/docs/api/products/transactions/#categoriesget).
    
    If the `transactions` object was returned by an Assets endpoint such as `/asset_report/get/` or `/asset_report/pdf/get`, this field will only appear in an Asset Report with Insights."""
    category_id: Optional[str] = None
    """For pending transactions, the date that the transaction occurred; for posted transactions, the date that the transaction posted. Both dates are returned in an [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format ( `YYYY-MM-DD` )."""
    date: str
    """The merchant name, as extracted by Plaid from the `name` field."""
    merchant_name: Optional[str] = None
    """Please use the `payment_channel` field, `transaction_type` will be deprecated in the future.
    
    `digital:` transactions that took place online.
    
    `place:` transactions that were made at a physical location.
    
    `special:` transactions that relate to banks, e.g. fees or deposits.
    
    `unresolved:` transactions that do not fit into the other three types.
    """
    transaction_type: Optional[str] = None

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        kwargs.setdefault("by_alias", True)
        return super().json(**kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        kwargs.setdefault("by_alias", True)
        return super().dict(**kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "TransactionBase":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "TransactionBase":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
