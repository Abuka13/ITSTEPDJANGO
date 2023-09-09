from django.contrib import admin
from django_app import models
admin.site.register(models.Student)
admin.site.register(models.Professor)
admin.site.register(models.Course)

# Register your models here.