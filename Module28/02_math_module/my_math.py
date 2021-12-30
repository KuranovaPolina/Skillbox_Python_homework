import math


class MyMath:
    @classmethod
    def circle_len(cls, size=0) -> float:
        return 2 * math.pi * size

    @classmethod
    def circle_square(cls, size=0) -> float:
        return math.pi * size ** 2

    @classmethod
    def cube_volume(cls, size=0) -> float:
        return size ** 3

    @classmethod
    def sphere_size(cls, size=0) -> float:
        return 4 * math.pi * size ** 2
