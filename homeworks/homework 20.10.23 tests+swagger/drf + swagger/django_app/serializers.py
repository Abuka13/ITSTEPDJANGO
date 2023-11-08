from django.contrib.auth.models import User
from rest_framework import serializers
from django_app import models


class ComplaintsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Complaints
        fields = '__all__'  # ['id', 'user', 'title', 'is_pay']