nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]],
             [[11, 12, 13], [14, 15], [16, 17, 18]]]


def make_list(lst):
    all_element_list = []
    for element in lst:
        if isinstance(element, list):
            all_element_list.extend(make_list(element))
        else:
            all_element_list.append(element)

    return all_element_list


print(make_list(nice_list))

# зачтено
