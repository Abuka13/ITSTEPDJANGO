import contextlib


import sqlite3

from django.shortcuts import render, redirect


from django.shortcuts import render


def success_page(request):
    return render(request, 'success_page.html')

def home(request):
    return render(request, "home.html")


def sending_complaints(request):
    if request.method == "GET":
        return render(request, 'send.html')
    elif request.method == "POST":
        author = request.POST.get("author")
        description = request.POST.get("description")
        number = request.POST.get("number")
        city = request.POST.get("city")
        date = request.POST.get("date")
        time = request.POST.get("time")

        with contextlib.closing(sqlite3.connect('database/complain.db')) as connection:
            with connection as cursor:
                cursor.execute("INSERT INTO complaints (author, description, number, city, date, time) VALUES (?, ?, ?, ?, ?, ?);", (author, description,number, city, date, time))
        return redirect(success_page)







