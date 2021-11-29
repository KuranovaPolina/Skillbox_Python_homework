import random
from cohabitation import *


def action(person, act):
    if person.satiety < 20:
        person.eat()
    elif person.happiness < 50:
        if person.house.money > 350 and isinstance(person, Wife):
            person.buy_fur_coat()
        else:
            person.petting_the_cat()
    elif person.house.meal < 10 and isinstance(person, Wife):
        person.go_to_the_store()
        if person.house.cat_meal < 10:
            person.go_to_the_store(True)
    elif person.house.money < 50 and isinstance(person, Husband):
        person.work()
    elif act == 1 and isinstance(person, Husband):
        person.work()
    elif act == 1 and isinstance(person, Wife):
        person.clear_house()
    elif act == 2 and isinstance(person, Husband):
        person.play()
    elif act == 2 and isinstance(person, Wife):
        if person.house.money > 350:
            person.buy_fur_coat()
        else:
            person.petting_the_cat()
    else:
        person.eat()
        person.petting_the_cat()


def cat_action(cat, act):
    if cat.satiety < 20:
        cat.eat()
    elif act == 1:
        cat.sleep()
    elif act == 2:
        cat.tear_up_the_wallpaper()
    else:
        cat.sleep()


def child_action(child, act):
    if child.satiety < 20:
        child.eat()
    elif act == 1:
        child.petting_the_cat()
    elif act == 2:
        child.eat()
    else:
        child.petting_the_cat()


house1 = House()
husband1 = Husband("Artem", house1)
wife1 = Wife("Wife", house1)
cat1 = Cat("Cat", house1)
cat2 = Cat("Cat2", house1)
cat3 = Cat("Cat3", house1)
child1 = Person("Child", house1)

for _ in range(365):
    print(_)
    husband1_action = random.randint(1, 3)
    wife1_action = random.randint(1, 3)
    cat1_action = random.randint(1, 6)
    cat2_action = random.randint(1, 6)
    cat3_action = random.randint(1, 6)
    child1_action = random.randint(1, 6)

    action(husband1, husband1_action)
    action(wife1, wife1_action)
    cat_action(cat1, cat1_action)
    cat_action(cat2, cat2_action)
    cat_action(cat3, cat3_action)
    child_action(child1, child1_action)

    house1.add_dirt()
    husband1.is_dirt()
    wife1.is_dirt()

    if husband1.is_died():
        print(f"Artem is died - happiness: {husband1.happiness}, satiety: {husband1.satiety}")
        if wife1.is_died():
            print(f"{wife1.name} is died - happiness: {wife1.happiness}, satiety: {wife1.satiety}")
        if cat1.is_died():
            print(f"{cat1.name} is died - satiety: {cat1.satiety}")
        if cat2.is_died():
            print(f"{cat2.name} is died - satiety: {cat2.satiety}")
        if cat3.is_died():
            print(f"{cat3.name} is died - satiety: {cat3.satiety}")
        if child1.is_died():
            print(f"{child1.name} is died - satiety: {child1.satiety}")
        break

    elif wife1.is_died():
        print(f"{wife1.name} is died - happiness: {wife1.happiness}, satiety: {wife1.satiety}")
        if cat1.is_died():
            print(f"{cat1.name} is died - satiety: {cat1.satiety}")
        if cat2.is_died():
            print(f"{cat2.name} is died - satiety: {cat2.satiety}")
        if cat3.is_died():
            print(f"{cat3.name} is died - satiety: {cat3.satiety}")
        if child1.is_died():
            print(f"{child1.name} is died - satiety: {child1.satiety}")
        break

    elif cat1.is_died():
        print(f"{cat1.name} is die - satiety: {cat1.satiety}")
        if cat2.is_died():
            print(f"{cat2.name} is died - satiety: {cat2.satiety}")
        if cat3.is_died():
            print(f"{cat3.name} is died - satiety: {cat3.satiety}")
        if child1.is_died():
            print(f"{child1.name} is died - satiety: {child1.satiety}")
        break

    elif cat2.is_died():
        print(f"{cat2.name} is died - satiety: {cat2.satiety}")
        if cat3.is_died():
            print(f"{cat3.name} is died - satiety: {cat3.satiety}")
        if child1.is_died():
            print(f"{child1.name} is died - satiety: {child1.satiety}")
        break

    elif cat3.is_died():
        print(f"{cat3.name} is died - satiety: {cat3.satiety}")
        if child1.is_died():
            print(f"{child1.name} is died - satiety: {child1.satiety}")
        break

    elif child1.is_died():
        print(f"{child1.name} is died - satiety: {child1.satiety}")
        break

print()
house1.result()

# зачтено
