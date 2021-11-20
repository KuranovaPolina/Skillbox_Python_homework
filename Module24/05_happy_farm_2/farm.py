class Gardener:
    def __init__(self, name, garden):
        self.Name = name
        self.Garden = garden

    def care(self):
        self.Garden.grow_all()

    def harvest(self):
        self.Garden.Potatoes = []


class Potato:
    states = {0: 'No', 1: 'Sprout', 2: 'Green', 3: 'ripe'}

    def __init__(self, index):
        self.Index = index
        self.State = 0

    def grow(self):
        if self.State < 3:
            self.State += 1
        self.print_state()

    def print_state(self):
        print(f"{self.Index + 1} potato {Potato.states[self.State]}")

    def is_ripe(self):
        if self.State == 3:
            return True
        return False


class PotatoGarden:
    def __init__(self, count):
        self.Potatoes = [Potato(index) for index in range(count)]

    def grow_all(self):
        print("Potato is growing")
        for i_potato in self.Potatoes:
            i_potato.grow()

    def are_all_ripe(self):
        if not all([i_potato.is_ripe() for i_potato in self.Potatoes]):
            print("Potatoes not is ripe")
            return False
        else:
            print("Potatoes is ripe")
            return True
