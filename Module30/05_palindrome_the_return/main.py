import collections


def can_be_poly(string: str) -> bool:
    letters = collections.Counter(string)

    count = len(list(filter(lambda x: int(letters[x]) % 2 != 0, letters)))

    if count > 1:
        return False
    else:
        return True


print(can_be_poly('abb'))
print(can_be_poly('abbbc'))

# зачтено
