from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field
from .credit_document_metadata import CreditDocumentMetadata
from .credit_pay_stub_employee import CreditPayStubEmployee
from .credit_pay_stub_employer import CreditPayStubEmployer
from .w_2_box_12 import W2Box12
from .w_2_state_and_local_wages import W2StateAndLocalWages


class CreditW2(BaseModel):
    """Tips from social security."""

    social_security_tips: Optional[str] = None
    """Wages from tips and other compensation."""
    wages_tips_other_comp: Optional[str] = None
    """Object representing metadata pertaining to the document."""
    document_metadata: CreditDocumentMetadata
    """Wages from social security."""
    social_security_wages: Optional[str] = None
    """An identifier of the document referenced by the document metadata."""
    document_id: str
    """Dependent care benefits."""
    dependent_care_benefits: Optional[str] = None
    """Data about the employee."""
    employee: CreditPayStubEmployee
    box_12: List[W2Box12]
    """Statutory employee."""
    statutory_employee: Optional[str] = None
    """Allocated tips."""
    allocated_tips: Optional[str] = None
    """Nonqualified plans."""
    nonqualified_plans: Optional[str] = None
    """Other."""
    other: Optional[str] = None
    """Wages and tips from medicare."""
    medicare_wages_and_tips: Optional[str] = None
    state_and_local_wages: List[W2StateAndLocalWages]
    """The tax year of the W2 document."""
    tax_year: Optional[str] = None
    """Information about the employer on the pay stub."""
    employer: CreditPayStubEmployer
    """Retirement plan."""
    retirement_plan: Optional[str] = None
    """Medicare tax withheld for the tax year."""
    medicare_tax_withheld: Optional[str] = None
    """Social security tax withheld for the tax year."""
    social_security_tax_withheld: Optional[str] = None
    """An employee identification number or EIN."""
    employer_id_number: Optional[str] = None
    """Federal income tax withheld for the tax year."""
    federal_income_tax_withheld: Optional[str] = None
    """Contents from box 9 on the W2."""
    box_9: Optional[str] = None
    """Third party sick pay."""
    third_party_sick_pay: Optional[str] = None

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        kwargs.setdefault("by_alias", True)
        return super().json(**kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        kwargs.setdefault("by_alias", True)
        return super().dict(**kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "CreditW2":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "CreditW2":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
