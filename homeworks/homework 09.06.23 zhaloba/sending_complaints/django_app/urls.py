from django.urls import path
from django_app import views
urlpatterns = [
    path('home/', views.home),
    path('send/', views.sending_complaints),
    path('valute/', views.valute),
]