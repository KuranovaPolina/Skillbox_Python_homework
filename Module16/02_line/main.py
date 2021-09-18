def addlist(list, start, end, step):
    for i in range(start, end + 1, step):
        list.append(i)

def sort(numbers, N):
    for j in range(N):
        F = 0
        for i in range(N - j):
            if numbers[i] > numbers[i + 1]:
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
                F += 1

        if F == 0:
            break

first_class = []
second_class = []

addlist(first_class, 160, 176, 2)
addlist(second_class, 162, 180, 3)

new_list = []
new_list.extend(first_class)
new_list.extend(second_class)
sort(new_list, len(new_list) - 1)
print(new_list)