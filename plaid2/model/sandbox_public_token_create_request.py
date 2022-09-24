from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field
from .sandbox_public_token_create_request_options import (
    SandboxPublicTokenCreateRequestOptions,
)


class SandboxPublicTokenCreateRequest(BaseModel):
    """The ID of the institution the Item will be associated with"""

    institution_id: str
    """An optional set of options to be used when configuring the Item. If specified, must not be `null`."""
    options: Optional[SandboxPublicTokenCreateRequestOptions] = None
    """The products to initially pull for the Item. May be any products that the specified `institution_id`  supports. This array may not be empty."""
    initial_products: List[str]
    """Your Plaid API `client_id`. The `client_id` is required and may be provided either in the `PLAID-CLIENT-ID` header or as part of a request body."""
    client_id: Optional[str] = None
    """Your Plaid API `secret`. The `secret` is required and may be provided either in the `PLAID-SECRET` header or as part of a request body."""
    secret: Optional[str] = None
    """The user token associated with the User data is being requested for."""
    user_token: Optional[str] = None

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        kwargs.setdefault("by_alias", True)
        return super().json(**kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        kwargs.setdefault("by_alias", True)
        return super().dict(**kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "SandboxPublicTokenCreateRequest":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(
        cls, b: Union[bytes, str], **kwargs: Any
    ) -> "SandboxPublicTokenCreateRequest":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
