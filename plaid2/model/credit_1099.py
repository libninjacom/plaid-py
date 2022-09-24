from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field
from .credit_1099_filer import Credit1099Filer
from .credit_1099_payer import Credit1099Payer
from .credit_1099_recipient import Credit1099Recipient
from .credit_document_metadata import CreditDocumentMetadata


class Credit1099(BaseModel):
    """Amount reported for July."""

    july_amount: Optional[float] = None
    """Amount in card not present transactions."""
    card_not_present_transaction: Optional[float] = None
    """Amount in royalties by payer."""
    royalties: Optional[float] = None
    """Amount reported for May."""
    may_amount: Optional[float] = None
    """Formatted (XXX) XXX-XXXX. Phone number of the PSE (Payment Settlement Entity)."""
    pse_telephone_number: Optional[str] = None
    """Amount reported for October."""
    october_amount: Optional[float] = None
    """Primary state of business."""
    primary_state: Optional[str] = None
    """Amount in rent by payer."""
    rents: Optional[float] = None
    """Amount of medical and healthcare payments from payer."""
    medical_and_healthcare_payments: Optional[float] = None
    """Form 1099 Type"""
    form_1099_type: Optional[str] = None
    """Whether or not payer made direct sales over $5000 of consumer products."""
    payer_made_direct_sales_of_5000_or_more_of_consumer_products_to_buyer: Optional[
        str
    ] = None
    """An object representing a recipient used in both 1099-K and 1099-MISC tax documents."""
    recipient: Optional[Credit1099Recipient] = None
    """Amount of fishing boat proceeds from payer."""
    fishing_boat_proceeds: Optional[float] = None
    """Amount of crop insurance proceeds."""
    crop_insurance_proceeds: Optional[float] = None
    """An identifier of the document referenced by the document metadata."""
    document_id: Optional[str] = None
    """Amount of golden parachute payments made by payer."""
    excess_golden_parachute_payments: Optional[float] = None
    """Amount of state tax withheld of payer for secondary state."""
    state_tax_withheld_lower: Optional[float] = None
    """Amount of 409A deferrals earned by payer."""
    section_409_a_deferrals: Optional[float] = None
    """State income reported for primary state."""
    state_income: Optional[float] = None
    """Amount reported for January."""
    january_amount: Optional[float] = None
    """Amount in other income by payer."""
    other_income: Optional[float] = None
    """Amount of gross proceeds paid to an attorney by payer."""
    gross_proceeds_paid_to_an_attorney: Optional[float] = None
    """Amount of substitute payments made by payer."""
    substitute_payments_in_lieu_of_dividends_or_interest: Optional[float] = None
    """Number of payment transactions made."""
    number_of_payment_transactions: Optional[str] = None
    """Gross amount reported."""
    gross_amount: Optional[float] = None
    """Amount reported for April."""
    april_amount: Optional[float] = None
    """Amount reported for June."""
    june_amount: Optional[float] = None
    """Primary state ID."""
    primary_state_id: Optional[str] = None
    """State income tax reported for primary state."""
    primary_state_income_tax: Optional[float] = None
    """State income tax reported for secondary state."""
    secondary_state_income_tax: Optional[float] = None
    """Amount of federal income tax withheld from payer."""
    federal_income_tax_withheld: Optional[float] = None
    """Amount reported for November."""
    november_amount: Optional[float] = None
    """Amount reported for December."""
    december_amount: Optional[float] = None
    """Secondary state of business."""
    secondary_state: Optional[str] = None
    """Amount reported for August."""
    august_amount: Optional[float] = None
    """Amount of nonemployee compensation from payer."""
    nonemployee_compensation: Optional[float] = None
    """Amount reported for September."""
    september_amount: Optional[float] = None
    """Object representing metadata pertaining to the document."""
    document_metadata: Optional[CreditDocumentMetadata] = None
    """State income reported for secondary state."""
    state_income_lower: Optional[float] = None
    """Amount reported for March."""
    march_amount: Optional[float] = None
    """An object representing a filer used by 1099-K tax documents."""
    filer: Optional[Credit1099Filer] = None
    """Secondary state ID."""
    secondary_state_id: Optional[str] = None
    """Amount of 409A income earned by payer."""
    section_409_a_income: Optional[float] = None
    """Secondary state ID."""
    payer_state_number_lower: Optional[str] = None
    """One of the values will be provided Payment card Third party network"""
    transactions_reported: Optional[str] = None
    """Merchant category of filer."""
    merchant_category_code: Optional[str] = None
    """Tax year of the tax form."""
    tax_year: Optional[str] = None
    """An object representing a payer used by 1099-MISC tax documents."""
    payer: Optional[Credit1099Payer] = None
    """Amount of state tax withheld of payer for primary state."""
    state_tax_withheld: Optional[float] = None
    """Name of the PSE (Payment Settlement Entity)."""
    pse_name: Optional[str] = None
    """Amount reported for February."""
    february_amount: Optional[float] = None
    """Primary state ID."""
    payer_state_number: Optional[str] = None

    def json(self, **kwargs: Any) -> str:
        """Return a json string representation of the object. Takes same keyword arguments as pydantic.BaseModel.json"""
        kwargs.setdefault("by_alias", True)
        return super().json(**kwargs)

    def dict(self, **kwargs: Any) -> Dict[str, Any]:
        """Return a dict representation of the object. Takes same keyword arguments as pydantic.BaseModel.dict"""
        kwargs.setdefault("by_alias", True)
        return super().dict(**kwargs)

    @classmethod
    def parse_obj(cls, data: Any) -> "Credit1099":
        """Parse a dict into the object. Takes same keyword arguments as pydantic.BaseModel.parse_obj"""
        return super().parse_obj(data)

    @classmethod
    def parse_raw(cls, b: Union[bytes, str], **kwargs: Any) -> "Credit1099":
        """Parse a json string into the object. Takes same keyword arguments as pydantic.BaseModel.parse_raw"""
        return super().parse_raw(b, **kwargs)
