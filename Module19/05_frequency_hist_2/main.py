def print_dic(dic_name):
    dic_name_list = sorted(dic_name.keys())
    for letter in dic_name_list:
        print("{0} : {1}".format(letter, dic_name[letter]))


text = input("text: ")
letters = {}

for letter in list(text):
    if letter in letters.keys():
        letters[letter] += 1
    else:
        letters[letter] = 1

letters_inv = {}

for letter in letters.keys():
    count = letters[letter]
    if count in letters_inv:
        letters_inv[count].append(letter)
    else:
        letters_inv[count] = [letter]

print("Original:")
print_dic(letters)

print("\nInverted:")
print_dic(letters_inv)

# зачтено
