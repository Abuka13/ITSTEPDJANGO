from django.contrib import admin
from app import models
admin.site.register(models.News)
admin.site.register(models.Category)
# Register your models here.
