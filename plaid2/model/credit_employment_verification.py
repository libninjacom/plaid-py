from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field
from .credit_employer_verification import CreditEmployerVerification
from .credit_platform_ids import CreditPlatformIds


class CreditEmploymentVerification(BaseModel):
    """End of employment, if applicable. Provided in ISO 8601 format (YYY-MM-DD)."""

    end_date: Optional[str] = None
    """The object containing a set of ids related to an employee."""
    platform_ids: CreditPlatformIds
    """ID of the payroll provider account."""
    account_id: Optional[str] = None
    """Start of employment in ISO 8601 format (YYYY-MM-DD)."""
    start_date: Optional[str] = None
    """An object containing employer data."""
    employer: CreditEmployerVerification
    """Current employment status."""
    status: Optional[str] = None
    """The type of employment for the individual.
    `"FULL_TIME"`: A full-time employee.
    `"PART_TIME"`: A part-time employee.
    `"CONTRACTOR"`: An employee typically hired externally through a contracting group.
    `"TEMPORARY"`: A temporary employee.
    `"OTHER"`: The employee type is not one of the above defined types."""
    employee_type: Optional[str] = None
    """Current title of employee."""
    title: Optional[str] = None
    """The date of the employee's most recent paystub in ISO 8601 format (YYYY-MM-DD)."""
    last_paystub_date: Optional[str] = None

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        kwargs.setdefault("by_alias", True)
        return super().json(**kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        kwargs.setdefault("by_alias", True)
        return super().dict(**kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "CreditEmploymentVerification":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(
        cls, b: Union[bytes, str], **kwargs: Any
    ) -> "CreditEmploymentVerification":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
