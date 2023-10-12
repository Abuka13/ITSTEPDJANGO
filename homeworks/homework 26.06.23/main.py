import contextlib
import sqlite3
from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__,template_folder='templates')


@app.route("/home", methods=['GET'])
def home():
    context = "Добро пожаловать на домашнюю страницу"
    return render_template("home.html",context=context)


@app.route("/list", methods=['GET'])
def list():
    with contextlib.closing(sqlite3.connect('database/database1.db')) as connection:
        with connection as cursor:
            rows = cursor.execute("""
                SELECT id, title, description, status FROM todo
                ORDER BY id DESC
                """)
            records: list[tuple] = rows.fetchall()
            todos = [
                {"id": row[0], "title": row[1], "description": row[2], "status": row[3]}
                for row in records
            ]

    return render_template("list.html", todos= todos)


@app.route('/create', methods=['GET', 'POST'])
async def create_post():
    if request.method == "GET":
        return render_template('create.html')
    elif request.method == "POST":
        title = request.form['title'].strip()
        description = request.form['description'].strip()
        status = True if request.form["status"].strip() == "on" else False

        with contextlib.closing(sqlite3.connect('database/database1.db')) as connection:
            with connection as cursor:
                cursor.execute("""
                    INSERT INTO todo (title, description, status) VALUES (?, ?, ?);
                    """, (title, description, status))

        return redirect(url_for('list'))

if __name__ == '__main__':
    app.run(debug=True)