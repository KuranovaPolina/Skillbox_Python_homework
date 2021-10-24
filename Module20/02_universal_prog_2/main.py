import math


def is_prime(number):
    number_is_prime = True
    d = 2
    for i in range(int(math.sqrt(number)) + 1):
        if number % d == 0 and d != number:
            number_is_prime = False
            break
        d += 1
    return number_is_prime


def f(object_list):
    return [list(object_list)[i] for i in range(2, len(list(object_list))) if is_prime(i)]


test_tuple = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

print(f(test_tuple))

# зачтено
