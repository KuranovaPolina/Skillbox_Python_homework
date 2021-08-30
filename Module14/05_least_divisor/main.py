N = int(input("N = "))

i = 2
while True:
    if N % i == 0:
        break
    else:
        i += 1

print("The smallest divisor:", i)
