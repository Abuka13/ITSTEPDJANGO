import sqlite3


def create_sqlite_db_users():
    with sqlite3.connect('database/complain.db') as connection:
        cursor = connection.cursor()
        cursor.execute('''
CREATE TABLE complaints (id INTEGER PRIMARY KEY AUTOINCREMENT, author CHAR(255), description CHAR(255), number INT, city TEXT, date TEXT, time TEXT)
''')


create_sqlite_db_users()
