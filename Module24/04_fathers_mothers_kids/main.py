class Parent:
    def __init__(self, name, age, children=[]):
        self.Name = name
        self.Age = age
        self.Children = children

    def information(self):
        print(f"Name {self.Name}, age {self.Age}\nChildren:")
        for children in self.Children:
            print(children.Name)

    def calm_child(self, child):
        child.Calm = 0

    def feed_child(self, child):
        child.UnHunger = 0

    def add_children(self, child):
        try:
            if child.Age <= (self.Age - 16):
                self.Children.append(child)
            else:
                raise BaseException
        except BaseException:
            print("Strange child age")


class Child:
    def __init__(self, name, age, calm=0, un_hunger=0):
        self.Name = name
        self.Age = age
        self.Calm = calm
        self.UnHunger = un_hunger


parent1 = Parent(1, 20)
print(parent1.Age)
parent1.information()
child1 = Child(145678, 3)
parent1.add_children(child1)
parent1.information()

# зачтено
