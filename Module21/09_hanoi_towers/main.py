def move(n, x, y):
    if n != 0:
        move(n - 1, x, 6 - x - y)
        print(n, x, y)
        move(n - 1, 6 - x - y, y)


N = int(input("N = "))
move(N, 1, 3)

# зачтено
