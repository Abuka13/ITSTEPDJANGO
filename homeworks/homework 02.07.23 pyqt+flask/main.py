import json
from flask import Flask, jsonify

app = Flask(__name__)

# Загружаем данные из файла currency_list.json
with open('currency_list.json', 'r') as file:
    currency_data = json.load(file)
    valute = 'USD'
    exchange_rate = currency_data['rates'][valute]
    print(exchange_rate)


@app.route('/', methods=['GET'])
def get_currency_list():
    return jsonify(currency_data)

if __name__ == '__main__':
    app.run(debug=True)
