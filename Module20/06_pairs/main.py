original_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# 1
new_list1 = [(original_list[i], original_list[i + 1]) for i in range(0, 10, 2)]
print(new_list1)

# 2
new_list2_even = [2 * i for i in range(5)]
new_list2_odd = [2 * i + 1 for i in range(5)]
new_list2 = list(zip(new_list2_even, new_list2_odd))
print(new_list2)

# 3
pair1 = (original_list[0], original_list[1])
pair2 = (original_list[2], original_list[3])
pair3 = (original_list[4], original_list[5])
pair4 = (original_list[6], original_list[7])
pair5 = (original_list[8], original_list[9])

new_list3 = [pair1, pair2, pair3, pair4, pair5]
print(new_list3)

# 4
new_list4_dict = dict()
for index, value in enumerate(original_list):
    if index % 2 == 0:
        new_list4_dict[index] = value

new_list4 = [(key, value + 1) for key, value in new_list4_dict.items()]
print(new_list4)

# зачтено
