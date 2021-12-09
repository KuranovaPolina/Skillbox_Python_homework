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
first_line = QHofstadter([1, 2])
for _ in range(20):
    try:
        print(next(first_line))
    except StopIteration:
        break
