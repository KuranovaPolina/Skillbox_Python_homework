import random


class Soldier:
    points = 100


def battle(victim):
    victim.points -= 20


soldier1 = Soldier()
soldier2 = Soldier()

while True:
    striker = random.randint(1, 2)
    if striker == 1:
        battle(soldier2)
        print("soldier 1 attacked - soldier 2: ", soldier2.points)
    else:
        battle(soldier1)
        print("soldier 2 attacked - soldier 1: ", soldier1.points)
    if soldier1.points <= 0:
        print("End! Second win")
        break
    elif soldier2.points <= 0:
        print("End! First win")
        break
