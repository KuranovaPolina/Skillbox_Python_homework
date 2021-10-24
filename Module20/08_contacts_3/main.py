def add_function(dict, add_name, add_phone):
    if add_name in dict.keys():
        print("Такой человек уже есть.")
    else:
        dict[add_name] = add_phone


def search_function(dict, search):
    endings = ('а', 'ая')
    result = []

    if search.endswith(endings[0]):
        search = search.rsplit(endings[0])[0]
    elif search.endswith(endings[1]):
        search = search.rsplit(endings[1])[0]

    for i in dict.keys():
        if search in i.split(" ")[0].lower():
            result.append(i)

    if not result:
        print('Поиск не дал результатов')
    else:
        for i in result:
            print("{0} - {1}".format(i, dict[i]))


contacts = {
    'Сидоров Никита': '+71111234567',
    'Петрова Дарья': '+71117654321'
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

# зачтено
