from django.db import models




class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Article(models.Model):
    headline = models.CharField(max_length=100)

    categories = models.ManyToManyField(verbose_name="Тип", to=Category, blank=True)
    description = models.TextField(verbose_name="Описание")
    date = models.DateTimeField(verbose_name="Дата")

    class Meta:
        ordering = ["headline"]

    def __str__(self):
        return self.headline
