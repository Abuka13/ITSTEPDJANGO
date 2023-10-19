from django.urls import path
from django_app import views
urlpatterns = [
    path('home/', views.home, name='home'),
    path('profile/', views.login_f, name='login'),


    #TODO АУТИНТЕФИКАЦИЯ
    path('login/', views.login_f, name='login'),
    path('logout/', views.logout_f, name='logout'),
    path('register/', views.register_f, name='register'),

]