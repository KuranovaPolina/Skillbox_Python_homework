def new_tuple_func(start_tuple, number):
    entry_count = start_tuple.count(number)

    new_tuple = ()

    if entry_count == 1:
        new_tuple = start_tuple[start_tuple.index(number):]
    elif entry_count > 1:
        first_enter = start_tuple.index(number)
        new_tuple = start_tuple[first_enter:start_tuple.index(number, first_enter + 1) + 1]

    return new_tuple


first_tuple = (1, 2, 3, 4, 5, 6, 2, 5, 4, 7, 9, 1)
N = int(input("N: "))
print(new_tuple_func(first_tuple, N))

# зачтено
