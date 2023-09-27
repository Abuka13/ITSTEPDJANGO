from django.db import models


class Publication(models.Model):
    title = models.CharField(max_length=30)

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Article(models.Model):
    headline = models.CharField(max_length=100)
    publications = models.ManyToManyField(Publication)
    categories = models.ManyToManyField(Category)
    description = models.TextField(verbose_name="Описание")
    date = models.DateTimeField(verbose_name="Дата")

    class Meta:
        ordering = ["headline"]

    def __str__(self):
        return self.headline
