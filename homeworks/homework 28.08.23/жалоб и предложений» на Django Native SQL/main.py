import sqlite3


def create_complaint_db_users():
    with sqlite3.connect('database/complaint.db') as connection:
        cursor = connection.cursor()
        cursor.execute('''
CREATE TABLE complaints (id INTEGER PRIMARY KEY AUTOINCREMENT, author CHAR(255), title CHAR(255), description TEXT, date TEXT)
''')


create_complaint_db_users()


