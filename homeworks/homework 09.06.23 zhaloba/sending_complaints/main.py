import sqlite3


def create_sqlite_db_users():
    with sqlite3.connect('database/complain.db') as connection:
        cursor = connection.cursor()
        cursor.execute('''
CREATE TABLE complaints (id INTEGER PRIMARY KEY, author TEXT, description TEXT, city TEXT, date TEXT, time TEXT)
''')


create_sqlite_db_users()
