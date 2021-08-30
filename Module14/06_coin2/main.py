import math

print("Введите координаты монетки:")
X = float(input("X: "))
Y = float(input("Y: "))
r = float(input("Введите радиус: "))

if math.sqrt(X ** 2 + Y ** 2) <= r:
    print("Монетка где-то рядом")
else:
    print("Монетки в области нет")
