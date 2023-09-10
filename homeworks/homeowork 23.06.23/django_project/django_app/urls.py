from django.contrib import admin
from django.urls import path
from django_app import views

urlpatterns = [
    path('data/', views.print_data),

]