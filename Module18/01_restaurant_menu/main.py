menu = input("Доступное меню: ")

menu_list = menu.split(";")
user_menu = ', '.join(menu_list)

print("На данный момент в меню есть: {0}".format(user_menu))

# зачтено
