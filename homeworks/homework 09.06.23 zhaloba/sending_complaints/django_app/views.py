import contextlib
import datetime
import re
import time

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
import sqlite3

import requests

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from bs4 import BeautifulSoup



def home(request):
    return render(request, "home.html")


def sending_complaints(request):
    if request.method == "GET":
        return render(request, "send.html")
    elif request.method == "POST":
        author = request.POST.get("author")
        description = request.POST.get("description")
        number = request.POST.get("number")
        city = request.POST.get("city")
        date = request.POST.get("date")
        time = request.POST.get("time")

        with contextlib.closing(sqlite3.connect('database1.db')) as connection:
            with connection as cursor:
                cursor.execute("INSERT INTO book_posts (title, description, price, count) VALUES (?, ?, ?, ?);", (title, description, price, count))






