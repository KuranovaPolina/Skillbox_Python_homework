cells = []
N = int(input("N = "))

for i in range(N):
    cells.append(int(input(f"{i + 1} cell's effectiveness: ")))

print("Bad cells: ", end = '')
for i in range(N):
    if cells[i] < i + 1:
        print(cells[i], end = ' ')