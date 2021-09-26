string = input("string: ")

first_h = string.index("h")
second_h = string.rindex("h")

new_string = string[:first_h + 1] + string[second_h - 1: first_h: -1] + string[second_h:]

print("new string:", new_string)

# зачтено
