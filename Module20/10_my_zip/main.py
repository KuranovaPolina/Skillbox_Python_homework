def my_zip(string, tpl):
    string_list = list(string)
    result = []

    for i in range(min(len(string_list), len(tpl))):
        new_pair = (string_list[i], tpl[i])
        result.append(new_pair)

    return result


input_string = input("String: ")
number_tuple = tuple((input("Tuple: "))[1:][:-1].split(", "))

print(zip(tuple(input_string), number_tuple))
for i in my_zip(input_string, number_tuple):
    print(i)

