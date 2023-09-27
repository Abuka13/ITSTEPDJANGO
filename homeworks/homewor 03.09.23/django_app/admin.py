from django.contrib import admin
from django_app import models
admin.site.register(models.Publication)
admin.site.register(models.Article)
admin.site.register(models.Category)