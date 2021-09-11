def filmfounder(film, films):
    find = False
    for i in films:
        if i == film:
            find = True
    return find

films = ['Крепкий орешек', 'Назад в будущее', 'Таксист',
         'Леон', 'Богемская рапсодия', 'Город грехов',
         'Мементо', 'Отступники', 'Деревня']

favourite_films = []

print("List of films: ", films)

print("Adding favourite films. Input 'Add' to finish")

while True:
    film = input("Film name: ")
    if film == 'Add':
        break
    elif not filmfounder(film, films):
        print("Error. Film was not found")
        #break
    else:
        favourite_films.append(film)

print("List of favourite films", favourite_films)