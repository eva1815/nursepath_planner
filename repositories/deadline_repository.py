# Repository Pattern:
# This repository handles storing and retrieving deadline data.

from typing import List, Tuple

from repositories.db_connection import get_connection


class DeadlineRepository:
    def add_deadline(self, program_id: int, title: str, due_date: str) -> None:
        query = """
        INSERT INTO deadlines (program_id, title, due_date)
        VALUES (%s, %s, %s)
        """
        conn = get_connection()
        try:
            with conn:
                with conn.cursor() as cur:
                    cur.execute(query, (program_id, title, due_date))
        finally:
            conn.close()

    def get_deadlines_by_program(self, program_id: int) -> List[Tuple[int, int, str, str]]:
        query = """
        SELECT id, program_id, title, due_date
        FROM deadlines
        WHERE program_id = %s
        ORDER BY due_date
        """
        conn = get_connection()
        try:
            with conn.cursor() as cur:
                cur.execute(query, (program_id,))
                return cur.fetchall()
        finally:
            conn.close()
