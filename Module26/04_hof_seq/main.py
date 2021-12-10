def QHofstadter(s: list) -> int:
    elements = s
    while True:
        try:
            new_el = elements[-elements[-1]] + elements[-elements[-2]]
            elements.append(new_el)
            yield new_el
        except IndexError:
            break


# не понимаю, почему она должна останавливаться на [1, 2], а не на [1, 3]
# TODO: В класс передается список из двух элементов,
#  которые являются первым и вторым элементом последовательности соответственно.
#  И если вы внимательно почитаете теорию по ссылке
#  https://ru.wikipedia.org/wiki/%D0%9F%D0%BE%D1%81%D0%BB%D0%B5%D0%B4%D0%BE%D0%B2%D0%B0%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D0%BE%D1%81%D1%82%D1%8C_%D0%A5%D0%BE%D1%84%D1%88%D1%82%D0%B0%D0%B4%D1%82%D0%B5%D1%80%D0%B0#%D0%9F%D0%BE%D1%81%D0%BB%D0%B5%D0%B4%D0%BE%D0%B2%D0%B0%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D0%BE%D1%81%D1%82%D1%8C_Q_%D0%A5%D0%BE%D1%84%D1%88%D1%82%D0%B0%D0%B4%D1%82%D0%B5%D1%80%D0%B0
#  то увидите что у данной последовательности первый и второй элементы строго равны 1,
#  поэтому всё остальное - невалидно
first_line = QHofstadter([1, 2])
for _ in range(20):
    try:
        print(next(first_line))
    except StopIteration:
        break
