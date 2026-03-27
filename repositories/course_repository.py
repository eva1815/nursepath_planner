# Repository Pattern:
# This repository manages prerequisite course data in the database.

from typing import List, Tuple

from repositories.db_connection import get_connection


class CourseRepository:
    def add_course(
        self,
        program_id: int,
        course_name: str,
        grade: float,
        minimum_required_grade: float,
    ) -> None:
        query = """
        INSERT INTO prerequisite_courses (program_id, course_name, grade, minimum_required_grade)
        VALUES (%s, %s, %s, %s)
        """
        conn = get_connection()
        try:
            with conn:
                with conn.cursor() as cur:
                    cur.execute(query, (program_id, course_name, grade, minimum_required_grade))
        finally:
            conn.close()

    def get_courses_by_program(self, program_id: int) -> List[Tuple[int, int, str, float, float]]:
        query = """
        SELECT id, program_id, course_name, grade, minimum_required_grade
        FROM prerequisite_courses
        WHERE program_id = %s
        ORDER BY id
        """
        conn = get_connection()
        try:
            with conn.cursor() as cur:
                cur.execute(query, (program_id,))
                return cur.fetchall()
        finally:
            conn.close()
