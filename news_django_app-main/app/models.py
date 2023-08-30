from django.db import models
class Category(models.Model):
    title = models.CharField(max_length=300, verbose_name="Наименование")
    def __str__(self):
        return self.title

class News(models.Model):
    title = models.CharField(max_length=300, verbose_name="Наименование")
    category = models.ForeignKey(verbose_name="Категория", to=Category, on_delete=models.CASCADE, null=True, blank=True, default=None)
    def __str__(self):
        return self.title

# Create your models here.
