from django.shortcuts import render
import sqlite3
from django.http import HttpResponse, JsonResponse
def home(request):
    return render(request, 'home.html')

