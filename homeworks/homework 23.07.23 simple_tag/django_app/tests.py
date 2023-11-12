from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse

from django_app import models
from django_app.models import PostComments
from django_app.models import Suggests
from django.core.files.storage import default_storage

class UserModelTestCase(TestCase):
    username = "Abuka"
    password = "Abuka13"

    def setUp(self):  # преднастройка
        User.objects.create(username=self.username, password=make_password(self.password))

    def test_model_create(self):
        print("""Тестируем модель на корректное создание пользователя""")
        user = User.objects.get(username=self.username)
        self.assertEqual(user.username, self.username)  # функция для сравнения

class SuggestsModelTestCase(TestCase):
    author = "Abuka"
    title = "Abuka13"
    image = "'images/products/dnsh9hr.jpg'"
    description = "Описание"
    date = "09.09.2017"

    def setUp(self):  # преднастройка
        models.Suggests.objects.create(
            author=self.author,
            title=self.title,
            description=self.description,
            date=self.date,
            image=self.image,
        )

    def test_model_create(self):
        print("""Тестируем модель на корректное создание пользователя""")
        author = models.Suggests.objects.get(author=self.author)
        self.assertEqual(User.username, self.author)  # функция для сравнения

class CommentsModelTestCase(TestCase):
    post = "Спорт"
    author = "Abuka13"
    text = "Текст"
    rating = "-1"
    date_time = "09.09.2017"

    def setUp(self):  # преднастройка
        models.PostComments.objects.create(post=PostComments.post,author=self.author, text=self.text, rating=self.rating, date_time=self.date_time)

    def test_model_create(self):
        print("""Тестируем модель на корректное создание пользователя""")
        author = models.PostComments.objects.get(author=self.author)
        self.assertEqual(User.username, self.author)  # функция для сравн

