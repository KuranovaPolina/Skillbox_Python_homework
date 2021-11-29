import math


class Car:
    def __init__(self, x, y, a, rad=True):
        self.x = x
        self.y = y
        if rad:
            self.a = a
        else:
            self.a = a * math.pi / 180

    def move(self, l):
        self.x += l * math.cos(self.a)
        self.y += l * math.sin(self.a)

    def turn(self, b, rad=True):
        if rad:
            self.a += b
        else:
            self.a += b * math.pi / 180


class Bus(Car):
    def __init__(self, x, y, a, passenger_count=0, money=0, rad=True):
        super().__init__(self, x, y, a, rad)
        self.passenger_count = passenger_count
        self.money = money

    def enter(self, number):
        self.passenger_count += number

    def go_out(self, number):
        if self.passenger_count - number > 0:
            self.passenger_count -= number
        else:
            self.passenger_count = 0

    def move(self, l):
        super().move(l)
        self.money += 1 * self.passenger_count * l

# зачтено
