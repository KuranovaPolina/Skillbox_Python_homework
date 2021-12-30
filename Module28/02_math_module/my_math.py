import math


class MyMath:
    def circle_len(self, size=0) -> float:
        return 2 * math.pi * size

    def circle_square(self, size=0) -> float:
        return math.pi * size ** 2

    def cube_volume(self, size=0) -> float:
        return size ** 3

    def sphere_size(self, size=0) -> float:
        return 4 * math.pi * size ** 2
