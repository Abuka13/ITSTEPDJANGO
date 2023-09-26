from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

def home(request):
    return HttpResponse("OK")

def api(request):
    return JsonResponse(data={"name": "DRF"}, safe=True)
