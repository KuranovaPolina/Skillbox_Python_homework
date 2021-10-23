def add_function(dict, add_name, add_phone):
    if add_name in dict.keys():
        print("Такой человек уже есть.")
    else:
        dict[add_name] = {
            'phone_number': add_phone
        }


def search_function(dict, search):
    result = []

    for i in dict.keys():
        if search == i.split(" ")[0].lower():
            result.append(i)

    if result == []:
        print('Поиск не дал результатов')
    else:
        for i in result:
            print("{0} - {1}".format(i, dict[i]['phone_number']))


contacts = {
    'Сидоров Никита': {
        'phone_number': '+71111234567'
    },

    'Петрова Дарья': {
        'phone_number': '+71117654321'
    }
}

while True:
    action = int(input("Выберите действие: "
                       "\n1 - добавить контакт\n"
                       "2 - поиск человека по фамилии\n"))

    if action == 1:
        name = input("Фамилия: ") + " " + input("Имя: ")
        phone = input("Номер: ")
        add_function(contacts, name, phone)
        print(contacts)
    elif action == 2:
        search = input('Введите фамилию: ').lower()
        search_function(contacts, search)
    else:
        print("Такого выбора нет в меню")

# TODO: Поиск по фамилии должен быть такой же как и в 5 задании.
#  То есть женские фамилии также должны выводиться:
"""
Выберите действие: 
1 - добавить контакт
2 - поиск человека по фамилии
1
Фамилия: Иванов
Имя: Иван
Номер: 23
{'Сидоров Никита': {'phone_number': '+71111234567'}, 'Петрова Дарья': {'phone_number': '+71117654321'}, 'Иванов Иван': {'phone_number': '23'}}
Выберите действие: 
1 - добавить контакт
2 - поиск человека по фамилии
1
Фамилия: Иванова
Имя: Анна
Номер: 23942
{'Сидоров Никита': {'phone_number': '+71111234567'}, 'Петрова Дарья': {'phone_number': '+71117654321'}, 'Иванов Иван': {'phone_number': '23'}, 'Иванова Анна': {'phone_number': '23942'}}
Выберите действие: 
1 - добавить контакт
2 - поиск человека по фамилии
2
Введите фамилию: иванов
Иванов Иван - 23
Выберите действие: 
1 - добавить контакт
2 - поиск человека по фамилии
"""
