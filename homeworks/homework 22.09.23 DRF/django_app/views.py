from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django_app.models import News
from .serializers import NewsSerializer


@api_view(['GET'])
def getData(request):
    new =   News.objects.all()
    serializer = NewsSerializer(new, many=True)
    return Response(serializer.data)



@api_view(['POST'])
def addData(request):
    serializer = NewsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)