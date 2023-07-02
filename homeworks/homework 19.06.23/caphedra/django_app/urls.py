from django.contrib import admin
from django.urls import path
from django_app import views

urlpatterns = [

    path('', views.post_publish),
    path('client/requests', views.get_requests),
    path('excel', views.export_data_to_excel),
]