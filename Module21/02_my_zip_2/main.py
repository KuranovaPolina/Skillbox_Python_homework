def my_zip(*arg):
    arg = list(map(list, arg))
    try:
        yield tuple(map(lambda x: x.pop(0), arg))
        yield from my_zip(*arg)
    except:
        return


input_string = 'abcd'
input_tuple = (1, 2, 10)
input_dict = {'a': 1, 'b': 2, 'c': 3}
input_list = [4, 6, 8, 10, 11]
print(my_zip(input_string, input_tuple, input_dict, input_list))
for i in my_zip(input_string, input_tuple, input_dict, input_list):
    print(i)
