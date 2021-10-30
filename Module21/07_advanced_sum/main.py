def sum_(*args):
    def make_list(lst):
        all_element_list = []
        for element in lst:
            if isinstance(element, list):
                all_element_list.extend(make_list(element))
            else:
                all_element_list.append(element)

        return all_element_list

    result = 0
    for value in make_list(list(args)):
        result += value

    return result


print(sum_([[1, 2, [3]], [1], 3]))
