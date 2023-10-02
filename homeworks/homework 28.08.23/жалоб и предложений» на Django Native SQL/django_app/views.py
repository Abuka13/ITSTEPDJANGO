import contextlib
import sqlite3
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect

def home(request):
    return render(request, 'home.html')



def suggest_create(request: HttpRequest) -> HttpResponse:
    if request.method == "GET":
        return render(request, "send_suggests.html")
    elif request.method == "POST":
        author = str(request.POST["author"])
        title = str(request.POST["title"])
        description = str(request.POST["description"])
        date = str(request.POST["date"])


        with contextlib.closing(sqlite3.connect('database/suggestion.db')) as connection:
            with connection as cursor:
                cursor.execute("INSERT INTO suggests (author, title,description, date) VALUES (?, ?, ?, ?);",
                               (author, title, description, date))
        return redirect(list_suggests)

def list_suggests(request):


    with contextlib.closing(sqlite3.connect('database/suggestion.db')) as connection:
        with connection as cursor:
            rows = cursor.execute("""
    SELECT id, author, title, description, date FROM suggests""")
            records = rows.fetchall()

            _suggests = []
            for record in records:
                new_dict = {
                    "id": record[0],
                    "author": record[1],
                    "title": record[2],
                    "description": record[3][:15:1] + "..." if len(record[2]) > 15 else record[2],
                    "date": record[4]
                }
                _suggests.append(new_dict)

    return render(request, 'list_suggests.html', {'select_orm': _suggests})

def list_complaints(request):
    with contextlib.closing(sqlite3.connect('database/complaint.db')) as connection:
        with connection as cursor:
            rows = cursor.execute("""
    SELECT id, author, title, description, date FROM complaints""")
            records = rows.fetchall()

            _complaints = []
            for record in records:
                new_dict = {
                    "id": record[0],
                    "author": record[1],
                    "title": record[2],
                    "description": record[3][:15:1] + "..." if len(record[2]) > 15 else record[2],
                    "date": record[4]
                }
                _complaints.append(new_dict)

    return render(request, 'list_complaints.html', {'select_orm': _complaints})

def complaint_create(request: HttpRequest) -> HttpResponse:
    if request.method == "GET":
        return render(request, "send_complaints.html")
    elif request.method == "POST":
        author = str(request.POST["author"])
        title = str(request.POST["title"])
        description = str(request.POST["description"])
        date = str(request.POST["date"])


        with contextlib.closing(sqlite3.connect('database/complaint.db')) as connection:
            with connection as cursor:
                cursor.execute("INSERT INTO complaints (author, title, description, date) VALUES (?, ?, ?, ?);", (author, title, description, date))
        return redirect(list_complaints)