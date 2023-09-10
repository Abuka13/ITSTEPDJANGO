from bs4 import BeautifulSoup
import requests
from django.shortcuts import render, redirect
a = []

def get_api(request):


    url = 'http://127.0.0.1:5000/'

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    any_word = soup.find_all('a', href="#word")
    for i in range(4):
        an_word = list(filter(lambda x: len(x)>1,  any_word[i].text.split(' ')))[0].strip()
        a.append(an_word)

    keys = ['name', 'Surname', 'hobby', 'number']

    my_dict = {key: value for key, value in zip(keys, a)}
    return my_dict
data = get_api(requests)
def print_data(request):
    return render(request, "data.html", context={"data": data})