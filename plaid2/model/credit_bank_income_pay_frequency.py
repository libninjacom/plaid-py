from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field


class CreditBankIncomePayFrequency(str, Enum):
    weekly = "WEEKLY"
    biweekly = "BIWEEKLY"
    semi_monthly = "SEMI_MONTHLY"
    monthly = "MONTHLY"
    unknown = "UNKNOWN"
