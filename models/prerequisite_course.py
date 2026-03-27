from dataclasses import dataclass
from typing import Optional


@dataclass
class PrerequisiteCourse:
    id: Optional[int]
    program_id: int
    course_name: str
    grade: float
    minimum_required_grade: float
