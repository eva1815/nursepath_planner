from dataclasses import dataclass
from typing import Optional


@dataclass
class NursingProgram:
    id: Optional[int]
    name: str
    school_name: str
    required_average: float
