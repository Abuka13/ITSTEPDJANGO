from django.shortcuts import render
from django_app import models
def home(request):
    return render(request, 'home.html')

def list(request):
    select_orm = models.Article.objects.all()
    select_orn = models.Category.objects.all()
    return render(request, 'list.html', context={"select_orm": select_orm})