from django.urls import reverse
from django.shortcuts import get_object_or_404
from django_app import models
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
import random
import string



def home(request):
    return render(request, 'home.html')

def welcome(request):
    return render(request, 'welcome.html')


def create_account(request):


    # Генерация случайного логина
    login_length = 8
    characters = string.ascii_letters + string.digits
    random_login = ''.join(random.choice(characters) for _ in range(login_length))

    # Генерация случайного пароля
    characters = string.ascii_letters + string.digits
    random_password = ''.join(random.choice(characters) for _ in range(login_length))
    User.objects.create(
        username=random_login,
        password=make_password(random_password),
    )
    return render(request, 'check.html', context={"login":random_login, "password":random_password})

def computer_club(request):
    return render(request, 'computers.html')

@login_required
def logout_f(request):
    logout(request)
    return redirect(register_f)
def login_f(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password) #пытается взять имя и пароль из базы данных
        if user is not None:
            login(request, user)
            return redirect(home)
        else:
            raise Exception("Данные для входа неправильные!")
    else:
        raise Exception("Method not supported")
def register_f(request):

    if request.method == "GET":
        return render(request, "register.html")
    elif request.method == "POST":
        username = request.POST.get('username')
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        User.objects.create(
            username=username,
            password=make_password(password),
            first_name=name,
            last_name=surname,
            email=email
        )
        return redirect(login_f)
    else:
        raise Exception("Method not allowed!")