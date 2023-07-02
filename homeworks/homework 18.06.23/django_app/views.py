from django.http import HttpResponse
from django.shortcuts import render
from django_app import models
import openpyxl





def post_publish(request):
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet['A1'] = "user"
    sheet['A1'] = "title"
def get_requests(request):
    #todo выборка
    select1_raw = """
    SELECT id, title, description, price, is_success, datetime FROM Publish
    """
    select_orm = models.Publish.objects.all()
    return render(request, 'list.html', context={"select_orm": select_orm})

def get_request(request, pk):
    # id(1) - зарезервирована
    # todo выборка
    select1_raw = """
    SELECT id, title, author, gen, date, datetime FROM Publish
    WHERE id = 1
    """
    select1_orm = models.Publish.objects.get(id=int(pk))
    print(type(select1_orm))
    print(select1_orm)
    # select1_orm.title
    # select1_orm.price
    # select1_orm.is_success
    # todo выборка

    return render(request, "list.html", context={"req": select1_orm})


