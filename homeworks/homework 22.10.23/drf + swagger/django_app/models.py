from django.db import models

class Complaints(models.Model):
    CATEGORY_CHOICES = [
        ('Политика', 'Политика'),
        ('Экономика', 'Экономика'),
        ('Спорт', 'Спорт'),
        ('Наука и технологии', 'Наука и технологии'),
        ('Культура и искусство', 'Культура и искусство'),
        ('Здоровье и медицина', 'Здоровье и медицина'),
        ('Образование', 'Образование'),
        ('Природа', 'Природа'),
        ('Развлечения', 'Развлечения'),
        ('Туризм', 'Туризм'),
    ]
    author = models.CharField(max_length=100)
    headline = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    description = models.TextField()
    date = models.DateTimeField(verbose_name="Дата")
