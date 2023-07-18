import contextlib
from flask import Flask, render_template, request, redirect, url_for
import psycopg2
import sqlite3
app=Flask(__name__,template_folder='templates')

@app.route("/")
def home():
    return render_template('home.html')
@app.route('/create', methods=['GET', 'POST'])  # TODO Create (POST) [INSERT] Страница формой для создания книг
def create():
    if request.method == "GET":
        return render_template('create.html')
    elif request.method == "POST":

        title = request.form['title'].strip()
        description = request.form['description'].strip()
        price = request.form['price'].strip()
        count = request.form['count'].strip()

        with contextlib.closing(sqlite3.connect('database1.db')) as connection:
            with connection as cursor:
                cursor.execute("INSERT INTO book_posts (title, description, price, count) VALUES (?, ?, ?, ?);", (title, description, price, count))

        return redirect(url_for('book_list'))

@app.route('/list', methods=['GET', "POST"])  # TODO Read (GET) [SELECT] Общий список книг (сокращённый формат)
def book_list():

    title = request.form.get("title", "").strip()

    with contextlib.closing(sqlite3.connect('database1.db')) as connection:
        with connection as cursor:
            rows = cursor.execute("""
SELECT id, title, description, price, count FROM book_posts
WHERE title LIKE ? ORDER BY id ASC;
            """, (f"%{title}%",))
            records = rows.fetchall()

            _books = []
            for record in records:
                new_dict = {
                    "id": record[0],
                    "title": record[1],
                    "description": record[2][:15:1] + "..." if len(record[2]) > 15 else record[2],
                    "price": record[3],
                    "count": record[4]
                }
                _books.append(new_dict)



    categories = ["Детективы", "Фентези", "Исторические"]

    return render_template('list.html', books=_books, search=title, categories=categories)





if __name__=="__main__":
    app.run(port=5000)
    #sql3_ex()
