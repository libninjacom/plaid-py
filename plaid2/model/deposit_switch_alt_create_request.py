from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field
from .deposit_switch_create_request_options import DepositSwitchCreateRequestOptions
from .deposit_switch_target_account import DepositSwitchTargetAccount
from .deposit_switch_target_user import DepositSwitchTargetUser


class DepositSwitchAltCreateRequest(BaseModel):
    """The deposit switch destination account"""

    target_account: DepositSwitchTargetAccount
    """The deposit switch target user"""
    target_user: DepositSwitchTargetUser
    """ISO-3166-1 alpha-2 country code standard."""
    country_code: Optional[str] = None
    """Options to configure the `/deposit_switch/create` request. If provided, cannot be `null`."""
    options: Optional[DepositSwitchCreateRequestOptions] = None

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        kwargs.setdefault("by_alias", True)
        return super().json(**kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        kwargs.setdefault("by_alias", True)
        return super().dict(**kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "DepositSwitchAltCreateRequest":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(
        cls, b: Union[bytes, str], **kwargs: Any
    ) -> "DepositSwitchAltCreateRequest":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
