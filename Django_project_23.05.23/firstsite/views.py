from django.http import HttpResponse
import json
from django.http import JsonResponse


def return_file_data(request):
    with open('data.txt', 'r') as file:
        file_data = file.read()
    return HttpResponse(file_data)




def return_json_file_data(request):
    with open('numbers.json', 'r') as file:
        json_data = json.load(file)
    return JsonResponse(json_data)