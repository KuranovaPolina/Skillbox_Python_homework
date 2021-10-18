import math


def is_prime(number):
    number_is_prime = True
    d = 2
    for i in range(int(math.sqrt(number))+1):
        if number % d == 0 and d != number:
            number_is_prime = False
            break
        d += 1
    return number_is_prime


def f(object_list):
    return [list(object_list)[i] for i in range(len(list(object_list))) if is_prime(i)]


test_tuple = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
test_sting = "0123456789"
test_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
test_dictionary = {
    '0': '0.',
    '1': '1.',
    '2': '2.',
    '3': '3.',
    '4': '4.',
    '5': '5.',
    '6': '6.',
    '7': '7.',
    '8': '8.',
    '9': '9.'
}

print(f(test_tuple))
print(f(test_sting))
print(f(test_list))
print(f(test_dictionary))