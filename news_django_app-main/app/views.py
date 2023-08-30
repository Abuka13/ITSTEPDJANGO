from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

"""

# 1. Сайт для подачи и просмотра новостей по категориям

User == django

Category == custom
(
id
name
)

Tag == custom (ключевое слово)
(
id
name
)

News == custom
(
id
title
category -- OneToMany
tags -- ManyToMany
)

"""



def home(request):
    return HttpResponse("<h1>Home Page</h1>")