user_string = input("Input string: ")
user_string = user_string.lower()

user_string_list = user_string.split(" ")

for i in range(len(user_string_list)):
    word_list = list(user_string_list[i])
    word_list[0] = word_list[0].upper()
    user_string_list[i] = "".join(word_list)

user_string_2 = " ".join(user_string_list)

print("Result:", user_string_2)

# зачтено
