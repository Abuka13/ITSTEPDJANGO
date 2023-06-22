from django.db import models

# Create your models here.
class Publish(models.Model):
    user = models.CharField(max_length=250)
    author = models.CharField(max_length=250)
    title = models.CharField(max_length=250)
    genre = models.CharField(max_length=250)
    date = models.DateField()
    time = models.TimeField()
    datetime = models.DateTimeField()

    class Meta:
        app_label = "django_app"
        verbose_name = "Опубликовать книгу"

    def __str__(self):
        return f"Id: {self.id}\n" \
               f"\nUser: {self.user}\n" \
               f"\nAuthor:{self.author}\n" \
               f"\nDate: {self.date}\n" \
               "\n\n\n\n"


table_for_requests = """
create table publish(
id int AUTOINCREMENT
author VARCHAR(255),
title VARCHAR(255),
genre VARCHAR(255),
)
"""
