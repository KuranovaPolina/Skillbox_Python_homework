people = []
N = int(input("N = "))
K = int(input("K = "))
print(f"Every {K} person")

for i in range(1, N + 1):
    people.append(i)

start = 0
while len(people) > 1:
    print(f"\nNow circle: {people}")
    print(f"Start from {people[start]}")

    delete = (start + K - 1) % len(people)
    if people[delete] == people[-1]:
        start = 0
    else:
        start = delete
    print(f"{people[delete]} go out")
    people.remove(people[delete])

print(f"\n{people[0]} stayed")