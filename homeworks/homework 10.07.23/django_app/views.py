from django.shortcuts import render

# Создаем здесь представления.
def home(request):
    return render(request,"home.html")