list_1 = [2, 5, 7, 10]
list_2 = [3, 8, 4, 9]
to_find = 56


def finder(list1: list, list2: list) -> int:
    for x in list1:
        for y in list2:
            print(x, y, x * y)
            yield x * y


for result in finder(list_1, list_2):
    if result == to_find:
        print('Found!!!')
        break

# зачтено
