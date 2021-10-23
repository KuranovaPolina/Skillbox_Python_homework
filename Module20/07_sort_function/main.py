def tpl_sort(tpl):
    for element in tpl:
        if not isinstance(element, int):
            return tpl
    return tuple(sorted(tpl))


test_tpl = (17, 34, 6, 2, 3, 4, 5, 6, '19.9', 10)
print(tpl_sort(test_tpl))

# зачтено
