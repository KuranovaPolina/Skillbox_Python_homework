import math


class Square:
    def __init__(self, length: float) -> None:
        self.__length = length

    @property
    def length(self) -> float:
        return self.__length

    @length.setter
    def length(self, length: float) -> None:
        if length < 0:
            print("Error")
        else:
            self.__length = length

    def perimeter(self) -> float:
        return 4 * self.__length

    def square(self) -> float:
        return self.__length ** 2


class Triangle:
    def __init__(self, base: float, height: float):
        self.__base = base
        self.__height = height

    @property
    def base(self) -> float:
        return self.__base

    @base.setter
    def base(self, base: float) -> None:
        if base < 0:
            print("Error")
        else:
            self.__base = base

    @property
    def height(self) -> float:
        return self.__height

    @height.setter
    def height(self, height: float) -> None:
        if height < 0:
            print("Error")
        else:
            self.__height = height

    def perimeter(self) -> float:
        return self.__base + 2 * math.sqrt((self.__base / 2) ** 2 + self.__height ** 2)

    def square(self) -> float:
        return 0.5 * self.__base * self.__height


class Cube:
    def __init__(self, sq: Square):
        self.figures = [sq, sq, sq, sq, sq, sq]

    def square(self):
        return self.figures[0].square() * 6


class Pyramid:
    def __init__(self, sq: Square, tr: Triangle):
        self.figures = [sq, tr, tr, tr, tr]

    def square(self):
        return self.figures[0].square() + self.figures[1].square()

# зачтено
