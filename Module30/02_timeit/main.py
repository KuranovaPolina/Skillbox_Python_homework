import timeit

# from functools import reduce


# def conc(a: str, b: str) -> str:
#     result = a + "-" + b
#     return result


res1: float = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
res2: float = timeit.timeit('"-".join([str(n) for n in range(100)])', number=10000)
res3: float = timeit.timeit('"-".join(map(str, range(100)))', number=10000)
# res4: float = timeit.timeit('lambda: "-".join(map(str, range(100)))', number=10000)
# res5: float = timeit.timeit('reduce(conc, (map(str, [n for n in range(100)])))', number=10000)

print(res1)
print(res2)
print(res3)
# print(res4)
# print(lambda: "-".join(map(str, range(100))))

# зачтено
