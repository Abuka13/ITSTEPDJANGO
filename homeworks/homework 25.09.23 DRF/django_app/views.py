
from django.views.decorators.csrf import csrf_exempt
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from django_app.models import Complaints
from . import serializers, models
from .serializers import ComplaintsSerializer

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response

response_schema_dict = {
    "200": openapi.Response(
        description="custom 200 description",
        examples={
            "application/json": {
                "200_key1": "200_value_1",
                "200_key2": "200_value_2",
            }
        },
    ),
    "205": openapi.Response(
        description="custom 205 description",
        examples={
            "application/json": {
                "205_key1": "205_value_1",
                "205_key2": "205_value_2",
            }
        },
    ),
    "205": openapi.Response(
        description="custom 205 description",
        examples={
            "application/json": {
                "205_key1": "205_value_1",
                "205_key2": "205_value_2",
            }
        },
    ),
}
@swagger_auto_schema(  # документация
    method="GET",
    manual_parameters=[
        openapi.Parameter("search_by", openapi.IN_QUERY, description="Поиск по этому параметру", type=openapi.TYPE_STRING, default="")
    ],  # Описание входных данных
    responses={200: serializers.ComplaintsSerializer, 400: "Error detail"},  # Описание выходных данных
)
@api_view(['GET'])
def complaints(request):
    new =  Complaints.objects.all()
    serializer = ComplaintsSerializer(new, many=True)
    search_by = request.query_params.get("search_by", "")  # query params
    news_objs = models.Complaints.objects.filter(author__icontains=search_by)  # DB -> Python
    news_jsons = serializers.ComplaintsSerializer(news_objs, many=True).data  # Python -> JSON

    combined_data = {
        "complaints": serializer.data,
        "search_results": news_jsons
    }

    return Response(combined_data, status=status.HTTP_200_OK)




@swagger_auto_schema(
    method="POST",
    request_body=serializers.ComplaintsSerializer,  # Описание входных данных
    responses={201: "Успех", 400: "Error detail"},  # Описание выходных данных
)
@api_view(http_method_names=["POST"])
def addData(request):
    serializer = ComplaintsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)





@api_view(http_method_names=["GET", "PUT", "DELETE"])
def complaint_pk(request: Request, pk: str) -> Response:
    if request.method == "GET":
        return Response(data=serializers.ComplaintsSerializer(models.Complaints.objects.get(id=int(pk)), many=False).data, status=status.HTTP_200_OK)
    elif request.method == "PUT":

        complaint_obj = models.Complaints.objects.get(id=int(pk))

        author = str(request.data.get('author', ''))
        if len(author) > 0:
            complaint_obj.author = author

        headline = str(request.data.get('headline', ''))
        if len(headline) > 0:
            complaint_obj.headline = headline

        category = str(request.data.get('category', ''))
        if len(category) > 0:
            complaint_obj.category = category

        description = str(request.data.get('description', ''))
        if len(description) > 0:
            complaint_obj.description = description

        complaint_obj.save()

        return Response(data={"message": "successfully updated."}, status=status.HTTP_200_OK)
    elif request.method == "DELETE":
        models.Complaints.objects.get(id=int(pk)).delete()
        return Response(data={"message": "successfully deleted."}, status=status.HTTP_200_OK)
    else:
        return Response(data={"message": "HTTP_405_METHOD_NOT_ALLOWED"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)