def my_zip(string, tpl):
    string_list = list(string)
    result = []

    for i in range(min(len(string_list), len(tpl))):
        new_pair = (string_list[i], tpl[i])
        result.append(new_pair)

    return result


input_string = 'abcd'
number_tuple = (1, 2)

print(zip(tuple(input_string), number_tuple))
for i in my_zip(input_string, number_tuple):
    print(i)

# зачтено
