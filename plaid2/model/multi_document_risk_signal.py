from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field
from .document_risk_signal import DocumentRiskSignal
from .risk_signal_document_reference import RiskSignalDocumentReference


class MultiDocumentRiskSignal(BaseModel):
    """Array of attributes that indicate whether or not there is fraud risk with a set of documents"""

    risk_signals: List[DocumentRiskSignal]
    """Array of objects containing attributes that could indicate if a document is fraudulent"""
    document_references: List[RiskSignalDocumentReference]

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        kwargs.setdefault("by_alias", True)
        return super().json(**kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        kwargs.setdefault("by_alias", True)
        return super().dict(**kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "MultiDocumentRiskSignal":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(
        cls, b: Union[bytes, str], **kwargs: Any
    ) -> "MultiDocumentRiskSignal":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
