from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field


class InvestmentTransactionSubtype(str, Enum):
    account_fee = "account fee"
    adjustment = "adjustment"
    assignment = "assignment"
    buy = "buy"
    buy_to_cover = "buy to cover"
    contribution = "contribution"
    deposit = "deposit"
    distribution = "distribution"
    dividend = "dividend"
    dividend_reinvestment = "dividend reinvestment"
    exercise = "exercise"
    expire = "expire"
    fund_fee = "fund fee"
    interest = "interest"
    interest_receivable = "interest receivable"
    interest_reinvestment = "interest reinvestment"
    legal_fee = "legal fee"
    loan_payment = "loan payment"
    long_term_capital_gain = "long-term capital gain"
    long_term_capital_gain_reinvestment = "long-term capital gain reinvestment"
    management_fee = "management fee"
    margin_expense = "margin expense"
    merger = "merger"
    miscellaneous_fee = "miscellaneous fee"
    non_qualified_dividend = "non-qualified dividend"
    non_resident_tax = "non-resident tax"
    pending_credit = "pending credit"
    pending_debit = "pending debit"
    qualified_dividend = "qualified dividend"
    rebalance = "rebalance"
    return_of_principal = "return of principal"
    request = "request"
    sell = "sell"
    sell_short = "sell short"
    send = "send"
    short_term_capital_gain = "short-term capital gain"
    short_term_capital_gain_reinvestment = "short-term capital gain reinvestment"
    spin_off = "spin off"
    split_ = "split"
    stock_distribution = "stock distribution"
    tax = "tax"
    tax_withheld = "tax withheld"
    transfer = "transfer"
    transfer_fee = "transfer fee"
    trust_fee = "trust fee"
    unqualified_gain = "unqualified gain"
    withdrawal = "withdrawal"
