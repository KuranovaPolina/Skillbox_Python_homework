class Person:
    def __init__(self, name, house, satiety=30, happiness=100):
        self.name = name
        self.satiety = satiety
        self.house = house
        self.happiness = happiness

    def eat(self):
        if self.house.meal > 30:
            self.house.meal -= 30
            self.satiety += 30
            self.house.all_meal += 30
        else:
            self.satiety += self.house.meal
            self.house.all_meal += self.house.meal
            self.house.meal = 0

    def petting_the_cat(self):
        self.happiness += 5
        self.satiety -= 10

    def is_died(self):
        if self.satiety < 0 or self.happiness < 10:
            return True

    def is_dirt(self):
        if self.house.dirt > 90:
            self.happiness -= 10


class Husband(Person):
    def play(self):
        self.satiety -= 10
        self.happiness += 20

    def work(self):
        self.satiety -= 10
        self.house.money += 150
        self.house.all_money += 150


class Wife(Person):
    def go_to_the_store(self, cat_meal=False):
        self.satiety -= 10
        self.house.money -= 10
        if cat_meal:
            self.house.cat_meal += 10
        else:
            self.house.meal += 10

    def buy_fur_coat(self):
        self.satiety -= 10
        self.house.money -= 350
        self.happiness += 60
        self.house.all_fur_coat += 1

    def clear_house(self):
        self.satiety -= 10
        if self.house.dirt > 100:
            self.house.dirt -= 100
        else:
            self.house.dirt = 0


class Cat:
    def __init__(self, name, house, satiety=30):
        self.name = name
        self.house = house
        self.satiety = satiety

    def eat(self):
        if self.house.cat_meal > 10:
            self.house.cat_meal -= 10
            self.satiety += 20
            self.house.all_meal += 10
        else:
            self.satiety += 2 * self.house.cat_meal
            self.house.all_meal += self.house.cat_meal
            self.house.cat_meal = 0

    def sleep(self):
        self.satiety -= 10

    def tear_up_the_wallpaper(self):
        self.satiety -= 10
        self.house.dirt += 5

    def is_died(self):
        if self.satiety < 0:
            return True


class House:
    all_fur_coat = 0
    all_money = 0
    all_meal = 0

    def __init__(self, meal=50, money=100, cat_meal=30, dirt=0):
        self.meal = meal
        self.money = money
        self.cat_meal = cat_meal
        self.dirt = dirt

    def add_dirt(self):
        self.dirt += 5

    def result(self):
        print(f"all_money {self.all_money}\nall_meal {self.all_meal}\nall_fur_coat {self.all_fur_coat}")
