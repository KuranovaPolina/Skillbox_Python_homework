N = int(input("N = "))

print("Input list:")
first_list = [int(input(f"{i + 1}: ")) for i in range(N)]
print(first_list)

count0 = first_list.count(0)

second_list = [number for number in first_list if number != 0]
second_list += [0 for _ in range(count0)]

print(second_list)

third_list = [number for number in second_list if number != 0]
print(third_list)