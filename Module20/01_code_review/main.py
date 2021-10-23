students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology, swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}


def f(diction):
    lst = []
    string = ''
    for i in diction:
        lst += diction[i]['interests']
        string += diction[i]['surname']
    length = len(string)
    return lst, length


interest_list, general_length = f(students)
print(interest_list, general_length)

# зачтено
