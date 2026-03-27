from repositories.db_connection import get_connection


CREATE_PROGRAMS_TABLE = """
CREATE TABLE IF NOT EXISTS nursing_programs (
    id SERIAL PRIMARY KEY,
    name VARCHAR(150) NOT NULL,
    school_name VARCHAR(150) NOT NULL,
    required_average NUMERIC(5,2) NOT NULL
);
"""

CREATE_COURSES_TABLE = """
CREATE TABLE IF NOT EXISTS prerequisite_courses (
    id SERIAL PRIMARY KEY,
    program_id INTEGER NOT NULL REFERENCES nursing_programs(id) ON DELETE CASCADE,
    course_name VARCHAR(150) NOT NULL,
    grade NUMERIC(5,2) NOT NULL,
    minimum_required_grade NUMERIC(5,2) NOT NULL
);
"""

CREATE_DEADLINES_TABLE = """
CREATE TABLE IF NOT EXISTS deadlines (
    id SERIAL PRIMARY KEY,
    program_id INTEGER NOT NULL REFERENCES nursing_programs(id) ON DELETE CASCADE,
    title VARCHAR(150) NOT NULL,
    due_date DATE NOT NULL
);
"""


def initialize_database():
    conn = get_connection()
    try:
        with conn:
            with conn.cursor() as cur:
                cur.execute(CREATE_PROGRAMS_TABLE)
                cur.execute(CREATE_COURSES_TABLE)
                cur.execute(CREATE_DEADLINES_TABLE)
    finally:
        conn.close()
