odd_list = []

N = int(input("N = "))

for i in range (1, N + 1):
    if i % 2 != 0:
        odd_list.append(i)

print(odd_list)