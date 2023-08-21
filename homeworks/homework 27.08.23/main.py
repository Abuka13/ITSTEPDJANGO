from bs4 import BeautifulSoup
import requests
def get_api(request):


    url = 'http://127.0.0.1:8000/api/valute/'

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    any_word = soup.find_all('a', href="#word")
    an_word = list(filter(lambda x: len(x)>1,  any_word[0].text.split(' ')))[0].strip()
    return an_word
print(get_api(requests))