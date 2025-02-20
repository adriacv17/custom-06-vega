import os
import pathlib
import sqlite3
import utils.utils_config as config
from utils.utils_logger import log_info, log_error

def init_db(db_path: pathlib.Path):
    """Initialize the SQLite database and create the table if it doesn't exist."""
    try:
        os.makedirs(os.path.dirname(db_path), exist_ok=True)
        with sqlite3.connect(str(db_path)) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS streamed_messages (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    message TEXT,
                    author TEXT,
                    timestamp TEXT,
                    temperature REAL,
                    pressure REAL
                )
            """)
            conn.commit()
        log_info(f"Database initialized at {db_path}.")
    except Exception as e:
        log_error(f"Failed to initialize SQLite database: {e}")

def insert_message(message: dict, db_path: pathlib.Path):
    """Insert a processed message into the SQLite database."""
    try:
        with sqlite3.connect(str(db_path)) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO streamed_messages (message, author, timestamp, temperature, pressure)
                VALUES (?, ?, ?, ?, ?)
            """, (message["message"], message["author"], message["timestamp"], message["temperature"], message["pressure"]))
            conn.commit()
        log_info(f"Message inserted: {message}")
    except Exception as e:
        log_error(f"Failed to insert message into SQLite: {e}")

def retrieve_messages(db_path: pathlib.Path):
    """Retrieve all messages from the database."""
    try:
        with sqlite3.connect(str(db_path)) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM streamed_messages")
            rows = cursor.fetchall()
            return rows
    except Exception as e:
        log_error(f"Failed to retrieve messages from SQLite: {e}")
        return []
