def f_is_polindrom(list, start):
    is_polindrom = True
    steps = (len(list) - start) // 2
    for i in range(steps):
        if list[i + start] != list[-(i + 1)]:
            is_polindrom = False
            break
    return is_polindrom


N = int(input("N = "))
list = []

for _ in range(N):
    list.append(int(input("Number: ")))

print("\nline: ", end="")
for i in list:
    print(i, end=" ")

stop = 0
for i in range(N):
    if f_is_polindrom(list, i):
        stop = i
        break

print("\nAdd:", stop, "\nnumbers: ", end="")
for i in range(stop - 1, -1, -1):
    print(list[i], end=' ')

# зачтено
