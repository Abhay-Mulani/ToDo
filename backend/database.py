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

# --- Table creation logic ---
def create_tables():
    conn = get_db()
    if conn is None:
        print("Could not connect to DB to create tables.")
        return
    try:
        cursor = conn.cursor()
        # Add username column if it doesn't exist
        cursor.execute("""
            DO $$
            BEGIN
                IF NOT EXISTS (
                    SELECT 1 FROM information_schema.columns 
                    WHERE table_name='auth' AND column_name='username'
                ) THEN
                    ALTER TABLE auth ADD COLUMN username VARCHAR(255);
                END IF;
            END$$;
        """)
        # Create auth table (with username)
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS auth (
                id SERIAL PRIMARY KEY,
                username VARCHAR(255),
                email VARCHAR(255) UNIQUE NOT NULL,
                password VARCHAR(255) NOT NULL
            );
        ''')
        # Create todo table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS todo (
                id SERIAL PRIMARY KEY,
                title VARCHAR(255) NOT NULL,
                descr TEXT,
                status VARCHAR(50),
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                user_email VARCHAR(255) REFERENCES auth(email)
            );
        ''')
        conn.commit()
        cursor.close()
        print("Tables checked/created successfully.")
    except Exception as e:
        print(f"Error creating tables: {e}")
    finally:
        conn.close()

# Call table creation at import time
create_tables()
