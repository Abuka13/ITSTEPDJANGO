from django.db import models

# Create your models here.
class Publish(models.Model):
    user = models.CharField(max_length=250)
    title = models.CharField(max_length=250)
    description = models.CharField(max_length=250)
    price = models.IntegerField()
    date = models.DateField()
    time = models.TimeField()
    datetime = models.DateTimeField()

    class Meta:
        app_label = "django_app"
        verbose_name = "Предложение по экологии"

    def __str__(self):
        return f"Id: {self.id}\n" \
               f"\nUser: {self.user}\n" \
               f"\nDescription:{self.description}\n" \
               f"\nDate: {self.date}\n" \
               "\n\n\n\n"


table_for_requests = """
create table publish(
id int AUTOINCREMENT
user VARCHAR(255),
title VARCHAR(255),
description VARCHAR(255),
price INTEGER,
)
"""