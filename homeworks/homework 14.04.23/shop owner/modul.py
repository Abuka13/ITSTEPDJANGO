candidats_list = ['Аскаров', 'Бекмуханов', 'Ернур', 'Пешая', 'Карим', 'Шаримазданов']
askarov = 0
bekmuhanov = 0
ernur = 0
peshaya = 0
karim = 0
sharimazdanov = 0
while True:
    list = []
    print(candidats_list)
    print('выберите кандидата(напишите его имя, либо напишите exit для выхода)')
    vote = input('вы отдаете голос за: ')
    list.append(vote)
    if vote == 'Аскаров':
        askarov+=1
    elif vote == 'Бекмуханов':
        bekmuhanov+=1
    elif vote == 'Ернур':
        ernur+=1
    elif vote == 'Пешая':
        peshaya+=1
    elif vote == 'Карим':
        karim+=1
    elif vote == 'Шаримазданов':
        sharimazdanov+=1
    elif vote == 'exit':
        break



def find_max_and_variable_name(**kwargs):
    max_value = max(kwargs.values())
    max_variable = max(kwargs, key=kwargs.get)

    return max_value, max_variable

max_value, max_variable = find_max_and_variable_name(askarov=askarov, bekmuhanov=bekmuhanov, ernur=ernur, peshaya=peshaya, karim=karim, sharimazdanov=sharimazdanov)
print(f"Количество голосов: {max_value}")
print(f"Победитель: {max_variable}")