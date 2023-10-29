from django.urls import path
from django_app import views
urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('welcome/', views.welcome, name='welcome'),
    path('computers/', views.computer_club, name='computers'),

    path('three/', views.three, name='three'),
    path('five/', views.five, name='five'),


    path('create_account/', views.create_account, name='create_account'),

    path('login/', views.login_f, name='login'),
    path('logout/', views.logout_f, name='logout'),
    path('logoutf/', views.logout_ff, name='logoutf'),
    path('register/', views.register_f, name='register'),

]