from django.contrib import admin
from django.urls import path, include
from django_app import views

urlpatterns = [

    path('post/', views.addData),
    path('complaint/', views.complaints),
    path('complaint/<str:pk>', views.complaint_pk),
]
