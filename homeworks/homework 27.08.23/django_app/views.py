from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

import random










def home(request):
    pass
def valute(request):

    random_word = "abuka"

    return render(request, 'valute.html', context={"filename": random_word})





