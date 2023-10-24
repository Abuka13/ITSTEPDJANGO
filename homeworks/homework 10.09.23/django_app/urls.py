from django.urls import path
from django_app import views
urlpatterns = [
    path('home/', views.home, name='home'),
    path('home/profile/<int:user_id>/', views.profile, name='profile'),
    path('create_avatar/<str:pk>', views.create_avatar, name='create_avatar'),
    path('addpost/', views.add_post, name='add_post'),

    #TODO АУТИНТЕФИКАЦИЯ
    path('login/', views.login_f, name='login'),
    path('logout/', views.logout_f, name='logout'),
    path('register/', views.register_f, name='register'),

]