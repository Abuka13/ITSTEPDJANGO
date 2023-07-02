
from django_app import models
from django.shortcuts import render
from openpyxl import Workbook
from django.http import HttpResponse

from .models import Publish

def export_data_to_excel(request):

    data = Publish.objects.all()
    workbook = Workbook()
    sheet = workbook.active
    headers = ['user', 'title', 'description','price','date','time']
    sheet.append(headers)
    for item in data:
        row = [item.user, item.title, item.description, item.price, item.date, item.time]
        sheet.append(row)
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename="data.xlsx"'
    workbook.save(response)

    return response
def post_publish(request):
    return HttpResponse('abuka')
def update_publish(request):
    pass
def get_requests(request):
    #todo выборка
    select1_raw = """
    SELECT id, user, title, description, price FROM Publish
    """
    select_orm = models.Publish.objects.all()
    return render(request, 'list.html', context={"select_orm": select_orm})

def get_request(request, pk):
    # id(1) - зарезервирована
    # todo выборка
    select1_raw = """
    SELECT id, user, title, description, price FROM Publish
    WHERE id = 1
    """
    select1_orm = models.Publish.objects.get(id=int(pk))
    print(type(select1_orm))
    print(select1_orm)


    return render(request, "list.html", context={"req": select1_orm})
