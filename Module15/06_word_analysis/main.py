def letter_count(letter, letters_list):
    count = 0

    for i in letters_list:
        if i == letter:
            count += 1

    return count

word = input("Input word: ")
letters_list = list(word)

count0 = 0
for letter in letters_list:
    if letter_count(letter, letters_list) == 1:
        count0 += 1

print("Number of unic letters:", count0)