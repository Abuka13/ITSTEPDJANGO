from django.urls import path
from django_app import views
urlpatterns = [
    path('home/', views.home),
    path('listsuggest/', views.list_suggests),
    path('listcomplaint/', views.list_complaints),
    path('sendsuggest/', views.suggest_create, name='suggest_create'),
    path('sendcomplaint/', views.complaint_create, name='complaint_create'),
]