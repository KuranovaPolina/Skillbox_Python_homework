import random


def one_day():
    rand1 = random.randint(1, 50)

    file = open('karma.log', 'a')
    if rand1 == 1:
        file.write("KillError\n")
    elif rand1 == 2:
        file.write("DrunkError\n")
    elif rand1 == 3:
        file.write("CarCrashError\n")
    elif rand1 == 4:
        file.write("GluttonyError\n")
    elif rand1 == 5:
        file.write("DepressionError\n")
    file.close()

    rand2 = random.randint(1, 7)
    return rand2


KARMA_LEVEL = 500
karma = 0

file = open('karma.log', 'w')
file.write("")
file.close()

while karma < KARMA_LEVEL:
    karma += one_day()

# зачтено
