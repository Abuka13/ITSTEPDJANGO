import sqlite3






def create_sqlite_db_courses():
    with sqlite3.connect('database/architecture.db') as connection:
        cursor = connection.cursor()
        cursor.execute('''
CREATE TABLE courses (
    id SERIAL PRIMARY KEY,
    title VARCHAR(100),
    description VARCHAR(255),
    teachers VARCHAR(255)
)''')


create_sqlite_db_courses()
