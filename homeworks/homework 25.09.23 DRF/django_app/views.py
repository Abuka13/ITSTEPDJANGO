


from django_app.models import Complaints
from . import serializers, models
from .serializers import ComplaintsSerializer

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response


@api_view(['GET'])
def complaints(request):
    new =  Complaints.objects.all()
    serializer = ComplaintsSerializer(new, many=True)
    return Response(serializer.data)



@api_view(['POST'])
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