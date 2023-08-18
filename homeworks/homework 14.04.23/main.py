from bs4 import BeautifulSoup
import requests

# Отправляем GET-запрос на страницу с прогнозом погоды
url = 'https://www.gismeteo.kz/weather-astana-5164/10-days/'
response = requests.get(url)

# Создаем объект Beautiful Soup для анализа HTML-кода
soup = BeautifulSoup(response.text, 'html.parser')

# Ищем информацию о погоде на 18 августа
forecast_blocks = soup.find_all('div', class_='wforecast')

for block in forecast_blocks:
    date_element = block.find('div', class_='ws_date')
    if date_element and '18 августа' in date_element.text:
        temperature = block.find('span', class_='unit unit_temperature_c')
        description = block.find('div', class_='wicon')

        # Извлекаем текст информации о погоде
        temperature_text = temperature.text if temperature else 'Не найдено'
        description_text = description.get('title') if description else 'Не найдено'


        print('Погода в Астане на 18 августа:')
        print(f'Температура: {temperature_text}')
        print(f'Описание: {description_text}')







