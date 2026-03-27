import os

import psycopg2
from dotenv import load_dotenv


load_dotenv()


def get_connection():
    database_url = os.getenv("DATABASE_URL")
    if not database_url:
        raise ValueError(
            "DATABASE_URL was not found. Please create a .env file with your Neon PostgreSQL connection string."
        )
    return psycopg2.connect(database_url)
