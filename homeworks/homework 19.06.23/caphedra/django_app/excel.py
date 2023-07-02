import openpyxl
from django.http import HttpResponse
from django.shortcuts import render
from django_app import model





workbook = openpyxl.Workbook()
sheet = workbook.active
sheet['A1'] = "user"
sheet['B1'] = "user"
sheet['C1'] = "description"
sheet['D1'] = "price"
sheet['E1'] = "date"
sheet['F1'] = "time"


select1_raw = """
    SELECT id, user, title, description, price FROM Publish
    """
select_orm = models.Publish.objects.all()




workbook.save('data.xlsx')