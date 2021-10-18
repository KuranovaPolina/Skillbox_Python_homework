people = {
    'Сидоров Никита': 35,
    'Сидорова Алина': 34,
    'Сидоров Павел': 10,
    'Петров Виктор': 15,
    'Петрова Дарья': 16
}

endings = ('а', 'ая')

search = input('Введите фамилию: ').lower()
result = []

if search.endswith(endings[0]):
    search = search.rsplit(endings[0])[0]
elif search.endswith(endings[1]):
    search = search.rsplit(endings[1])[0]

for i in people:
    if search in i.split(" ")[0].lower():
        result.append(i + ' ' + str(people[i]))

if not result:
    print('Поиск не дал результатов')
else:
    for i in result:
        print(i)
