from dataclasses import dataclass
from typing import Optional


@dataclass
class Deadline:
    id: Optional[int]
    program_id: int
    title: str
    due_date: str
