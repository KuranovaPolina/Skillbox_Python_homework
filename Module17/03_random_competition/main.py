import random

first_list = [round(random.uniform(5, 10), 2) for _ in range(20)]
second_list = [round(random.uniform(5, 10), 2) for _ in range(20)]

result_list = [max(first_list[i], second_list[i]) for i in range(20)]

print("first team: ", first_list)
print("second team:", second_list)
print("result:", result_list)