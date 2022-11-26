from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field
from .address import Address
from .pslf_status import PslfStatus
from .student_loan_repayment_model import StudentLoanRepaymentModel
from .student_loan_status import StudentLoanStatus


class LiabilityOverride(BaseModel):
    """The interest rate on the loan as a percentage. Can only be set if `type` is `student`."""

    nominal_apr: float
    """The original loan principal. Can only be set if `type` is `student`."""
    principal: float
    """The cash APR percentage value. Can only be set if `type` is `credit`."""
    cash_apr: float
    """Student loan repayment information used to configure Sandbox test data for the Liabilities product"""
    repayment_model: StudentLoanRepaymentModel
    """Override the `minimum_payment_amount` field. Can only be set if `type` is `credit` or `student`."""
    minimum_payment_amount: float
    """The balance transfer APR percentage value. Can only be set if `type` is `credit`. Can only be set if `type` is `credit`."""
    balance_transfer_apr: float
    """The date on which the loan was initially lent, in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) (YYYY-MM-DD) format. Can only be set if `type` is `student`."""
    origination_date: str
    """Override the `expected_payoff_date` field. Can only be set if `type` is `student`."""
    expected_payoff_date: str
    """Override the `guarantor` field. Can only be set if `type` is `student`."""
    guarantor: str
    """Override the `is_federal` field. Can only be set if `type` is `student`."""
    is_federal: bool
    """An object representing the status of the student loan"""
    loan_status: StudentLoanStatus
    """Override the `payment_reference_number` field. Can only be set if `type` is `student`."""
    payment_reference_number: str
    """Override the `repayment_plan.description` field. Can only be set if `type` is `student`."""
    repayment_plan_description: str
    """Override the `is_overdue` field"""
    is_overdue: bool
    """Override the `repayment_plan.type` field. Can only be set if `type` is `student`. Possible values are: `"extended graduated"`, `"extended standard"`, `"graduated"`, `"income-contingent repayment"`, `"income-based repayment"`, `"interest only"`, `"other"`, `"pay as you earn"`, `"revised pay as you earn"`, or `"standard"`."""
    repayment_plan_type: str
    """Information about the student's eligibility in the Public Service Loan Forgiveness program. This is only returned if the institution is Fedloan (`ins_116527`). """
    pslf_status: PslfStatus
    """Override the `sequence_number` field. Can only be set if `type` is `student`."""
    sequence_number: str
    """The special APR percentage value. Can only be set if `type` is `credit`."""
    special_apr: float
    """If set, interest capitalization begins at the given number of months after loan origination. By default interest is never capitalized. Can only be set if `type` is `student`."""
    interest_capitalization_grace_period_months: float
    """The type of the liability object, either `credit` or `student`. Mortgages are not currently supported in the custom Sandbox."""
    type: str
    """Override the `last_payment_amount` field. Can only be set if `type` is `credit`."""
    last_payment_amount: float
    """Override the `loan_name` field. Can only be set if `type` is `student`."""
    loan_name: str
    """A physical mailing address."""
    servicer_address: Address
    """The purchase APR percentage value. For simplicity, this is the only interest rate used to calculate interest charges. Can only be set if `type` is `credit`."""
    purchase_apr: float

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        kwargs.setdefault("by_alias", True)
        return super().json(**kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        kwargs.setdefault("by_alias", True)
        return super().dict(**kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "LiabilityOverride":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "LiabilityOverride":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
