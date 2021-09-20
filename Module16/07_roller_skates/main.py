roller_number = int(input("Roller's namber: "))
sizes = []

for i in range(roller_number):
    sizes.append(int(input(f"Size {i + 1}: ")))

people_number = int(input("\nPeople namber: "))
people = []

for i in range(people_number):
    people.append(int(input(f"{i + 1} person's size: ")))

count = 0
for person in people:
    for size in range(len(sizes)):
        if sizes[size] >= person:
            sizes.remove(sizes[size])
            count += 1
            break

print("\nAnswer:", count)

# зачтено
