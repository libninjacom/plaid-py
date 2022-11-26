from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field
from .deductions import Deductions
from .earnings import Earnings
from .employee import Employee
from .employment_details import EmploymentDetails
from .income_breakdown import IncomeBreakdown
from .net_pay import NetPay
from .pay_period_details import PayPeriodDetails
from .paystub_details import PaystubDetails
from .paystub_employer import PaystubEmployer
from .paystub_verification import PaystubVerification
from .paystub_ytd_details import PaystubYtdDetails


class Paystub(BaseModel):
    """An object representing details that can be found on the paystub."""

    paystub_details: Optional[PaystubDetails] = None
    """The amount of income earned year to date, as based on paystub data."""
    ytd_earnings: Optional[PaystubYtdDetails] = None
    """An object representing both a breakdown of earnings on a paystub and the total earnings."""
    earnings: Earnings
    income_breakdown: Optional[List[IncomeBreakdown]] = None
    """An object with the deduction information found on a paystub."""
    deductions: Deductions
    """An object representing information about the net pay amount on the paystub."""
    net_pay: NetPay
    """An object containing details on the paystub's verification status. This object will only be populated if the [`income_verification.access_tokens`](/docs/api/tokens/#link-token-create-request-income-verification-access-tokens) parameter was provided during the `/link/token/create` call or if a problem was detected with the information supplied by the user; otherwise it will be `null`."""
    verification: Optional[PaystubVerification] = None
    """An object representing employment details found on a paystub."""
    employment_details: Optional[EmploymentDetails] = None
    """Information about the employer on the paystub"""
    employer: PaystubEmployer
    """An identifier of the document referenced by the document metadata."""
    doc_id: str
    """Data about the employee."""
    employee: Employee
    """Details about the pay period."""
    pay_period_details: PayPeriodDetails

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        kwargs.setdefault("by_alias", True)
        return super().json(**kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        kwargs.setdefault("by_alias", True)
        return super().dict(**kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "Paystub":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "Paystub":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
