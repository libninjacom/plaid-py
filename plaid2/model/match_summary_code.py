from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field


class MatchSummaryCode(str, Enum):
    match = "match"
    partial_match = "partial_match"
    no_match = "no_match"
    no_data = "no_data"
    no_input = "no_input"
