import os
import string

path = os.path.join('..', '02_zen_of_python', 'zen.txt')

zen_file = open(path, 'r')

lines_count = 0
word_count = 0
result = {}
letter_count = 0

for i_line in zen_file:
    word_count += len(i_line.split(" "))

    lines_count += 1

    i_line = i_line.lower()
    letters = list(string.ascii_lowercase)
    for letter in i_line:
        if letter in letters:
            if letter in result.keys():
                result[letter] = result.pop(letter) + 1
            else:
                result[letter] = 1
            letter_count += 1

zen_file.close()

print("lines:", lines_count)
print("word:", word_count)
print("letters:", letter_count)
sorted_result = sorted(result, key=result.get)
print("letter:", sorted_result[0])
