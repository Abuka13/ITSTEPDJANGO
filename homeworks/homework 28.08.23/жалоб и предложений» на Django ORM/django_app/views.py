from django.shortcuts import render
from django_app import models


from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
def home(request):
    return render(request, 'home.html')

def list_suggests(request):
    select_orm = models.Suggests.objects.all()
    return render(request, 'list_suggests.html', context={"select_orm": select_orm})

def suggest_create(request: HttpRequest) -> HttpResponse:
    if request.method == "GET":
        return render(request, "send_suggests.html")
    elif request.method == "POST":
        author = str(request.POST["author"])
        title = str(request.POST["title"])
        description = str(request.POST["description"])
        date = str(request.POST["date"])
        image = request.FILES["image"]

        models.Suggests.objects.create(
            author=author,
            title=title,
            description=description,
            date=date,
            image=image,
            )
        return redirect(list_suggests)


def list_complaints(request):
    select_orm = models.Complaints.objects.all()
    return render(request, 'list_complaints.html', context={"select_orm": select_orm})

def complaint_create(request: HttpRequest) -> HttpResponse:
    if request.method == "GET":
        return render(request, "send_complaints.html")
    elif request.method == "POST":
        author = str(request.POST["author"])
        title = str(request.POST["title"])
        description = str(request.POST["description"])
        date = str(request.POST["date"])
        image = request.FILES["image"]

        models.Complaints.objects.create(
            author=author,
            title=title,
            description=description,
            date=date,
            image=image,
            )
        return redirect(list_complaints)
