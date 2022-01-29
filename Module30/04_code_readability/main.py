from typing import List

result1: List[int] = list(filter(lambda x: all(x % i != 0 for i in range(2, x)), range(2, 1000)))

print(result1)

result2: List[int] = [2]
for num in range(3, 1000):
    if all(num % i != 0 for i in result2):
        result2.append(num)

print(result2)

# зачтено
