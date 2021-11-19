import math


class Circle:

    def __init__(self, x=0, y=0, r=1):
        self.X = x
        self.Y = y
        self.R = r

    def square(self):
        return (math.pi * self.R ** 2) / 2

    def perimeter(self):
        return 2 * math.pi * self.R

    def zoom(self, k):
        self.R *= k

    def cross(self, different_circle):
        point_len = math.sqrt((self.X - different_circle.X) ** 2 + (self.Y - different_circle.Y) ** 2)
        if (abs(self.R + different_circle.R) >= point_len) and (abs(self.R - different_circle.R) <= point_len):
            return True
        return False

# circle1 = Circle(1, 1, 2)
# print(circle1.square())
# print(circle1.perimeter())
# circle1.zoom(2)
# print(circle1.R)
# circle2 = Circle(1, 8, 2)
# print(circle1.cross(circle2))