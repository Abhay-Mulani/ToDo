import sqlite3
import os

# Get the directory where this script is located
DB_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(DB_DIR, "todos.db")

def get_db():
    """Get SQLite database connection"""
    try:
        connection = sqlite3.connect(DB_PATH)
        connection.row_factory = sqlite3.Row  # This allows accessing columns by name
        return connection
    except Exception as e:
        print(f"Error in connecting to SQLite db and the error is {e}")
        return None

def init_db():
    """Initialize the database with required tables"""
    conn = get_db()
    if conn:
        cursor = conn.cursor()
        
        # Create todo table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS todo (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title VARCHAR(30),
                descr VARCHAR(60),
                status VARCHAR(30)
            )
        ''')
        
        # Create auth table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS auth (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user VARCHAR(60),
                email VARCHAR(30) UNIQUE,
                password VARCHAR(60)
            )
        ''')
        
        # Insert sample data if todo table is empty
        cursor.execute('SELECT COUNT(*) FROM todo')
        if cursor.fetchone()[0] == 0:
            cursor.execute('''
                INSERT INTO todo (title, descr, status) VALUES 
                ('class_start', 'class starts at 5:30PM', 'open'),
                ('class_end', 'class ends at 7:30PM', 'open')
            ''')
        
        conn.commit()
        conn.close()
        print("Database initialized successfully!")
        return True
    return False
