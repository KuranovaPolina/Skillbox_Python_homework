import random


class Person:
    def __init__(self, name, house, satiety=50):
        self.Name = name
        self.Satiety = satiety
        self.House = house

    def eat(self):
        self.Satiety += 1
        self.House.Eat -= 1

    def work(self):
        self.Satiety -= 1
        self.House.Eat += 1

    def play(self):
        self.Satiety -= 1

    def go_to_the_store(self):
        self.House.Eat += 1
        self.House.Money -= 1


class House:
    def __init__(self, eat=50, money=0):
        self.Eat = eat
        self.Money = money


def action(person, act):
    if person.Satiety < 20:
        person.eat()
    elif person.House.Eat < 10:
        person.go_to_the_store()
    elif person.House.Money < 50:
        person.work()
    elif act == 1:
        person.work()
    elif act == 2:
        person.eat()
    else:
        person.play()


house1 = House()
person1 = Person("Artem", house1)
person2 = Person("No name", house1)

for _ in range(365):
    action1 = random.randint(1, 6)
    action2 = random.randint(1, 6)

    action(person1, action1)
    action(person2, action2)

    if person1.Satiety < 0:
        print(f"{person1.Name} died")
        break
    else:
        print(f"{person1.Name} - {person1.Satiety}")
    if person2.Satiety < 0:
        print(f"{person2.Name} died")
        break
    else:
        print(f"{person2.Name} - {person2.Satiety}")

# зачтено
