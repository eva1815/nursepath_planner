from typing import List, Tuple

from repositories.db_connection import get_connection


class ProgramRepository:
    def add_program(self, name: str, school_name: str, required_average: float) -> None:
        query = """
        INSERT INTO nursing_programs (name, school_name, required_average)
        VALUES (%s, %s, %s)
        """
        conn = get_connection()
        try:
            with conn:
                with conn.cursor() as cur:
                    cur.execute(query, (name, school_name, required_average))
        finally:
            conn.close()

    def get_all_programs(self) -> List[Tuple[int, str, str, float]]:
        query = """
        SELECT id, name, school_name, required_average
        FROM nursing_programs
        ORDER BY id
        """
        conn = get_connection()
        try:
            with conn.cursor() as cur:
                cur.execute(query)
                return cur.fetchall()
        finally:
            conn.close()

    def get_program_by_id(self, program_id: int):
        query = """
        SELECT id, name, school_name, required_average
        FROM nursing_programs
        WHERE id = %s
        """
        conn = get_connection()
        try:
            with conn.cursor() as cur:
                cur.execute(query, (program_id,))
                return cur.fetchone()
        finally:
            conn.close()
