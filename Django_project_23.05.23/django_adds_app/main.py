import json

data = list(range(1, 101))  # Создаем список чисел от 1 до 100

# Записываем данные в JSON-файл
with open('../numbers.json', 'w') as file:
    json.dump(data, file)