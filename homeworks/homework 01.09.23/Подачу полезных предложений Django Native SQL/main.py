import sqlite3


def create_sqlite_db_users():
    with sqlite3.connect('database/suggestion.db') as connection:
        cursor = connection.cursor()
        cursor.execute('''
CREATE TABLE suggests (id INTEGER PRIMARY KEY AUTOINCREMENT, author CHAR(255), title CHAR(255), image BYTEA, description TEXT, date TEXT)
''')


create_sqlite_db_users()
