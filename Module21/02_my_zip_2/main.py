def my_zip(*arg):
    arg = list(map(list, arg))
    try:
        yield tuple(map(lambda x: x.pop(0), arg))
        yield from my_zip(*arg)
    except:
        return


input_string = 'abcd'
input_tuple = (1, 2, 10)
print(my_zip(input_string, input_tuple))
for i in my_zip(input_string, input_tuple):
    print(i)

# зачтено
