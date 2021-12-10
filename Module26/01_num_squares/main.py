class Iter:
    def __init__(self, N: int) -> None:
        self.__N = N
        self.__counter = 0

    # TODO: Здесь возвращается либо число, либо ничего
    def __next__(self):
        if self.__counter < self.__N:
            self.__counter += 1
            return self.__counter ** 2
        else:
            raise StopIteration

    # TODO: Для аннотации в данном случае используется название класса в кавычках
    def __iter__(self):
        return self


def iter2func(N: int) -> int:
    for i in range(1, N + 1):
        yield i ** 2


N = int(input("N = "))
# it1 = Iter(N)
# for i in it1:
#     print(i)

# it2 = iter2func(N)
# for i in it2:
#     print(i)

it3 = (x ** 2 for x in range(1, N + 1))
for i in it3:
    print(i)

# что делать с аннотацией next и init
