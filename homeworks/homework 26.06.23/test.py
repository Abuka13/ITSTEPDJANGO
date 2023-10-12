import sqlite3
import contextlib

with contextlib.closing(sqlite3.connect('database/database1.db')) as connection:
    with connection as cursor:
        cursor.execute("""

CREATE TABLE IF NOT EXISTS todo
    (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL UNIQUE,
        description TEXT DEFAULT '',
        status BOOLEAN DEFAULT 0
    );
                """)
