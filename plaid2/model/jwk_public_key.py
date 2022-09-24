from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field


class JwkPublicKey(BaseModel):
    """The x member contains the x coordinate for the elliptic curve point."""

    x: str
    """The kid (Key ID) member can be used to match a specific key. This can be used, for instance, to choose among a set of keys within the JWK during key rollover."""
    kid: str
    """The y member contains the y coordinate for the elliptic curve point."""
    y: str
    """The timestamp when the key was created, in Unix time."""
    created_at: int
    """The timestamp when the key expired, in Unix time."""
    expired_at: Optional[int] = None
    """The alg member identifies the cryptographic algorithm family used with the key."""
    alg: str
    """The kty (key type) parameter identifies the cryptographic algorithm family used with the key, such as RSA or EC."""
    kty: str
    """The use (public key use) parameter identifies the intended use of the public key."""
    use: str
    """The crv member identifies the cryptographic curve used with the key."""
    crv: str

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        kwargs.setdefault("by_alias", True)
        return super().json(**kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        kwargs.setdefault("by_alias", True)
        return super().dict(**kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "JWKPublicKey":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "JWKPublicKey":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
