from django.contrib.auth.models import User
from rest_framework import serializers
from django_app import models


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.News
        fields = '__all__'  # ['id', 'user', 'title', 'is_pay']