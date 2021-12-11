def QHofstadter(s: list) -> int or None:
    if s == [1, 1]:
        elements = s
        while True:
            try:
                new_el = elements[-elements[-1]] + elements[-elements[-2]]
                elements.append(new_el)
                yield new_el
            except IndexError:
                break
    else:
        return


first_line = QHofstadter([1, 1])
for _ in range(20):
    try:
        print(next(first_line))
    except StopIteration:
        break
