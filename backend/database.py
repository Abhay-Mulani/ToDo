import psycopg2
from config import PGHOST, PGUSER, PGPASSWORD, PGDATABASE, PGPORT

def get_db():
    """Get PostgreSQL database connection"""
    try:
        connection = psycopg2.connect(
            host=PGHOST,
            user=PGUSER,
            password=PGPASSWORD,
            dbname=PGDATABASE,
            port=PGPORT
        )
        return connection
    except Exception as e:
        print(f"Error connecting to PostgreSQL db: {e}")
        return None
