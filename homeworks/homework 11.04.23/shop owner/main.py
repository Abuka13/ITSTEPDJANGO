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

        with psycopg2.connect(
            user="postgres",
            password="Takanashi_13",
            host="127.0.0.1",
            port="5432",
            database="book_shop"
        ) as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO book_posts (title,description,price,count) VALUES (%s, %s, %s, %s);",
                    (title, description, price, count)
                )
        return redirect(url_for('book_list')


        )
@app.route('/list', methods=['GET', "POST"])  # TODO Read (GET) [SELECT] Общий список книг (сокращённый формат)
def book_list():
    title = request.form.get("title", "").strip()
    with contextlib.closing(sqlite3.connect('database.db')) as connection:
        with connection as cursor:
            rows = cursor.execute("""
    SELECT id, title, description, author FROM book_posts
    WHERE title LIKE ? ORDER BY id ASC;
                """, (f"%{title}%",))
            records = rows.fetchall()
            _books = []
            for record in records:
                new_dict = {
                    "id": record[0],
                    "title": record[1],
                    "description": record[2][:15:1] + "..." if len(record[2]) > 15 else record[2],
                    "author": record[3]
                }
                _books.append(new_dict)

@app.route('/detail/<int:pk>', methods=['GET'])
def detail(pk: int):


    with psycopg2.connect(
            user="postgres",
            password="Takanashi_13",
            host="127.0.0.1",
            port="5432",
            database="book_shop"
    ) as connection:
        with connection.cursor() as cursor:
            cursor.execute("SELECT id, title, description, price, count FROM book_posts WHERE id = %s;", (pk,))
            record = cursor.fetchone()
            # print(records)
            _book = {
                "id": record[0],
                "title": record[1],
                "description": record[2],
                "price": record[3],
                "count": record[4],
            }



    return render_template('book_detail.html', book=_book)


if __name__=="__main__":
    app.run(port=5000)
