from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field


class WeakAliasDetermination(str, Enum):
    none = "none"
    source = "source"
    plaid = "plaid"
