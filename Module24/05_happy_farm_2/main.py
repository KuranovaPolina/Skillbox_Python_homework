from farm import Gardener, Potato, PotatoGarden


potato_garden1 = PotatoGarden(5)
gardener1 = Gardener("Ivan", potato_garden1)
print(gardener1.Garden.Potatoes)
while not gardener1.Garden.are_all_ripe():
    gardener1.care()
gardener1.harvest()
print(gardener1.Garden.Potatoes)
