from django.http import JsonResponse
from django_app import models
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


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
            return redirect(rooms)
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

def data(request):
    return JsonResponse(data={"data": "Python is awesome!"}, safe=False)


def rooms(request):
    return render(request, "home.html", context={"rooms": models.Room.objects.all()})


@login_required
def room(request, slug):
    room_obj = models.Room.objects.get(slug=slug)
    messages = models.Message.objects.filter(room=room_obj)[:2][::-1]
    return render(
        request,
        "room.html",
        context={"room": room_obj, "messages": messages}
    )


