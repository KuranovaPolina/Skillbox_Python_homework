def addlist(list, lenght):
    for i in range(lenght):
        list.append(int(input(f"{i+1}: ")))

first_list = []
second_list = []

addlist(first_list, 3)
addlist(second_list, 7)

print(first_list)
print(second_list)

first_list.extend(second_list)
first_list = list(set(first_list))
print(first_list)