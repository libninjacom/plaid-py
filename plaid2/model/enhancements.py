from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field
from .location import Location
from .personal_finance_category import PersonalFinanceCategory


class Enhancements(BaseModel):
    """The merchant name, as extracted by Plaid from the raw description."""

    merchant_name: Optional[str] = None
    """A link to the logo associated with this transaction. The logo will always be 100x100 resolution."""
    logo_url: Optional[str] = None
    """A hierarchical array of the categories to which this transaction belongs. For a full list of categories, see [`/categories/get`](https://plaid.com/docs/api/products/transactions/#categoriesget)."""
    category: List[str]
    """Information describing the intent of the transaction. Most relevant for personal finance use cases, but not limited to such use cases.
    
    See the [`taxonomy csv file`](https://plaid.com/documents/transactions-personal-finance-category-taxonomy.csv) for a full list of personal finance categories."""
    personal_finance_category: Optional[PersonalFinanceCategory] = None
    """The check number of the transaction. This field is only populated for check transactions."""
    check_number: Optional[str] = None
    """The website associated with this transaction."""
    website: Optional[str] = None
    """The channel used to make a payment.
    `online:` transactions that took place online.
    
    `in store:` transactions that were made at a physical location.
    
    `other:` transactions that relate to banks, e.g. fees or deposits."""
    payment_channel: str
    """A representation of where a transaction took place"""
    location: Location
    """A link to the icon associated with the primary personal finance category. The logo will always be 100x100 resolution."""
    personal_finance_category_icon_url: Optional[str] = None
    """The ID of the category to which this transaction belongs. For a full list of categories, see [`/categories/get`](https://plaid.com/docs/api/products/transactions/#categoriesget)."""
    category_id: Optional[str] = None

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        kwargs.setdefault("by_alias", True)
        return super().json(**kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        kwargs.setdefault("by_alias", True)
        return super().dict(**kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "Enhancements":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "Enhancements":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
