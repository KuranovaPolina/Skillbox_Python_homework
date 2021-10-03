start_string = input("Input string: ")
count = 0
new_string = ""
i = 0
lens = len(start_string)

while True:
    letter = start_string[i]
    count += 1

    if i == lens - 1:
        new_string += start_string[i] + str(count)
        break
    elif start_string[i] != start_string[i + 1]:
        new_string += start_string[i] + str(count)
        count = 0

    i += 1

print(new_string)

# зачтено
