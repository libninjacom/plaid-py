from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field


class BankTransferEventListDirection(str, Enum):
    inbound = "inbound"
    outbound = "outbound"
