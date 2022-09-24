from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field
from .wallet_transaction_counterparty_bacs import WalletTransactionCounterpartyBacs
from .wallet_transaction_counterparty_international import (
    WalletTransactionCounterpartyInternational,
)


class WalletTransactionCounterpartyNumbers(BaseModel):
    """The account number and sort code of the counterparty's account"""

    bacs: Optional[WalletTransactionCounterpartyBacs] = None
    """International Bank Account Number for a Wallet Transaction"""
    international: Optional[WalletTransactionCounterpartyInternational] = None

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        kwargs.setdefault("by_alias", True)
        return super().json(**kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        kwargs.setdefault("by_alias", True)
        return super().dict(**kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "WalletTransactionCounterpartyNumbers":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(
        cls, b: Union[bytes, str], **kwargs: Any
    ) -> "WalletTransactionCounterpartyNumbers":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
