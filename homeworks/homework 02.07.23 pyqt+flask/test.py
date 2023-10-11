import json
with open('currency_list.json', 'r') as file:
    currency_data = json.load(file)
    valute = 'USD'
    exchange_rate = currency_data['rates'][valute]
    print(exchange_rate)