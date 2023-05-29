from django.urls import path
from . import views

urlpatterns = [
    path('return-file/', views.return_file_data),
    path('return-json-file/', views.return_json_file_data),
]
