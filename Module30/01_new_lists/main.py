from typing import List
from functools import reduce


def compos(a: int, b: int) -> int:
    result = a * b
    return result


floats: List[float] = [12.3554, 4.02, 5.777, 2.12, 3.13, 4.44, 11.0001]
names: List[str] = ["Vanes", "Alen", "Jana", "William", "Richards", "Joy"]
numbers: List[int] = [22, 33, 10, 6894, 11, 2, 1]

first_list: List[float] = list(map(lambda x: round(x ** 3, 3), floats))
second_list: List[str] = list(filter(lambda x: len(x) >= 5, names))
third_list: int = reduce(compos, numbers)  # зачем делать список, если ответ - число
# вариант со списком
# third_list: List[int] = list(reduce(compos, numbers))

print(first_list)
print(second_list)
print(third_list)

# зачтено
