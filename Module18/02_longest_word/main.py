string = input("Input string: ")

string_list = string.split(" ")

maxi = 0
for word in string_list:
    if len(word) > maxi:
        maxi = len(word)

print(maxi)