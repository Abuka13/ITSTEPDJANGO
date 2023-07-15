#TODO task1
# def biggest_dict(**kwargs):
#     global my_dict
#
#     for key, value in kwargs.items():
#         my_dict[key] = value
#     return my_dict
#
# my_dict = {}
# biggest_dict(first_one = 'we can do it')
# print(my_dict)


#TODO task2#############################################################################################################

my_dict = {
    1: 'Astana',
    2: 'Almaty',
    17:'Shymkent',
    16:'Oskemen',
    8:'Taraz'
}

keys = list(my_dict.keys())
values = list(my_dict.values())
first_k = keys[0]
last_k = keys[-1]
first_v = values[0]
last_v = values[-1]

my_dict[first_k] = last_v
my_dict[last_k] = first_v

my_dict.pop(1)

my_dict['new_key'] = 'new_value'
print(my_dict)

#TODO task3#############################################################################################################
import json

class Country:
    def __init__(self):
        self.data = {}

    def add_country(self, country, capital):
        self.data[country] = capital

    def remove_country(self, country):
        if country in self.data:
            del self.data[country]
        else:
            print(f"{country} is not found.")

    def search_country(self, country):
        if country in self.data:
            return self.data[country]
        else:
            return f"{country} is not found."

    def edit_country(self, country, new_capital):
        if country in self.data:
            self.data[country] = new_capital
        else:
            print(f"{country} is not found.")

    def save_data(self, filename):
        with open(filename, "w") as file:
            json.dump(self.data, file)

    def load_data(self, filename):
        with open(filename, "r") as file:
            self.data = json.load(file)

 
data = Country()
data.add_country("Россия", "Москва")
data.add_country("Франция", "Париж")
data.add_country("Великобритания", "Лондон")
capital = data.search_country("Россия")
print(f"Столица России: {capital}")
data.edit_country("Франция", "Ницца")
data.remove_country("Великобритания")
data.save_data("country_data.json")
data.load_data("country_data.json")
capital = data.search_country("Франция")
print(f"Столица Франции: {capital}")
