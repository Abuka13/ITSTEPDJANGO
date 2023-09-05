import contextlib
import sqlite3
from django.shortcuts import render, redirect
import requests

def home(request):
    return render(request, 'home.html')





def success(request):
    return render(request, 'success.html')

def sending_suggests(request):
    if request.method == "GET":
        return render(request, 'send.html')
    elif request.method == "POST":
        author = request.POST.get("author")
        title = request.POST.get("title")
        description = request.POST.get("description")
        image = request.POST.get("image")
        date = request.POST.get("date")


        with contextlib.closing(sqlite3.connect('database/suggestion.db')) as connection:
            with connection as cursor:
                cursor.execute("INSERT INTO suggests (author, title, image, description, date) VALUES (?, ?, ?, ?, ?);", (author, title,image, description, date))
        return redirect(success)


def suggests_list(request):

    title = request.POST.get("title", "").strip()

    with contextlib.closing(sqlite3.connect('database/suggestion.db')) as connection:
        with connection as cursor:
            rows = cursor.execute("""
SELECT id, author, title, image, description, date FROM suggests
WHERE title LIKE ? ORDER BY id ASC;
            """, (f"%{title}%",))
            records = rows.fetchall()

            _books = []
            for record in records:
                new_dict = {
                    "id": record[0],
                    "author": record[1],
                    "title": record[2],
                    "image": record[3],
                    "description": record[4][:15:1] + "..." if len(record[2]) > 15 else record[2],
                    "date": record[5]
                }
                _books.append(new_dict)





    return render(request,'list.html',{'suggestions': _books, 'search': title})