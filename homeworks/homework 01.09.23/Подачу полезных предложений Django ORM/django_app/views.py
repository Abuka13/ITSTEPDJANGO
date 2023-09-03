from django.shortcuts import render
from django_app import models
import sqlite3
from django.http import HttpResponse, JsonResponse
def home(request):
    return render(request, 'home.html')

def list(request):
    select_orm = models.Suggests.objects.all()
    return render(request, 'list.html', context={"select_orm": select_orm})
