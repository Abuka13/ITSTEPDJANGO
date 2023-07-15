# def superset(set1, set2):
#
#     if set1.issuperset(set2):
#         print(f"Объект {set1.difference(set2)} является чистым супермножеством")
#     else:
#         print("Супермножество не обнаружено")
#     if set1 == set2:
#         print("Множества равны")
# set1 = {1,3,5,7,9}
# set2 = {2,4,6,8,10}
#
# superset(set1, set2)


#TODO TASK2 ################################################################################

dictionary = {}

def add():
    e_word = input("Введите слово на английском: ")
    ft = input("Введите перевод на французский: ")
    dictionary[e_word] = ft
    print("Слово добавлено в словарь.")

def remove():
    e_word = input("Введите слово на английском для удаления: ")
    if e_word in dictionary:
        del dictionary[e_word]
        print("Слово удалено из словаря.")
    else:
        print("Слово не найдено в словаре.")

def search():
    e_word = input("Введите слово на английском для поиска: ")
    if e_word in dictionary:
        ft = dictionary[e_word]
        print(f"Перевод слова '{e_word}' на французский: {ft}")


def replace():
    e_word = input("Введите слово на английском: ")
    if e_word in dictionary:
        nft = input("Введите перевод на французский: ")
        dictionary[e_word] = nft



while True:
    choice = input("Введите номер(1- добавить, 2 - удалить, 3 - найти, 4 - заменить, 5 - завершить): ")
    if choice == "1":
        add()
    elif choice == "2":
        remove()
    elif choice == "3":
        search()
    elif choice == "4":
        replace()
    elif choice == "5":
        break
#TODO TASK3###########################################################################################

def set_gen(numbers):
    result = set()
    for num in numbers:
        c = numbers.count(num)
        if c == 1:
            result.add(num)
        else:
            result.add(str(num) * c)
    return result

numbers = [1, 2, 3, 4, 4, 4, 5, 6, 6]
print(set_gen(numbers)) # выводит {1, 2, 3, '444', 5, '66'}
