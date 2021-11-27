class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age


class Employee(Person):
    def salary_count(self):
        pass


class Manager(Employee):
    def salary_count(self):
        return 13000


class Agent(Employee):
    def __init__(self, name, surname, age, volume_of_sales):
        super().__init__(name, surname, age)
        self.volume_of_sales = volume_of_sales

    def salary_count(self):
        return 5000 + 0.05 * self.volume_of_sales


class Worker(Employee):
    def __init__(self, name, surname, age, hours):
        super().__init__(name, surname, age)
        self.hours = hours

    def salary_count(self):
        return 100 * self.hours


objects = []
managers = []
agents = []
workers = []


manager1 = Manager("name1", "surname1", 1)
manager2 = Manager("name2", "surname2", 2)
manager3 = Manager("name3", "surname3", 3)

agent1 = Agent("name1", "surname1", 1, 1)
agent2 = Agent("name2", "surname2", 2, 2)
agent3 = Agent("name3", "surname3", 3, 3)

worker1 = Worker("name1", "surname1", 1, 1)
worker2 = Worker("name2", "surname2", 2, 2)
worker3 = Worker("name3", "surname3", 3, 3)

objects.append(manager1)
objects.append(manager2)
objects.append(manager3)

objects.append(agent1)
objects.append(agent2)
objects.append(agent3)

objects.append(worker1)
objects.append(worker2)
objects.append(worker3)

for i in objects:
    print(i.salary_count())
