import random


count = 0
with open('result.txt', 'w') as file:
    while count < 777:
        random_exception = random.randint(1, 39)
        if random_exception == 1:
            raise Exception("End")
        elif random_exception == 2:
            raise ArithmeticError("End")
        elif random_exception == 3:
            raise TypeError("End")
        else:
            number = int(input("Number:"))
            count += number
            file.write(str(number) + '\n')
