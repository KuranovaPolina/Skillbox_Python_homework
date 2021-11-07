import os
import string

path = os.path.abspath("text.txt")
file = open(path, 'r')
file_text = file.read()
file.close()

file_text = file_text.lower()
letters = list(string.ascii_lowercase)

result = {}
letter_count = 0
for letter in file_text:
    if letter in letters:
        if letter in result.keys():
            result[letter] = result.pop(letter) + 1
        else:
            result[letter] = 1
        letter_count += 1

tmp_result = {}
sorted_result_keys = sorted(result)
for letter in sorted_result_keys:
    tmp_result[letter] = round(result[letter] / letter_count, 3)

result = tmp_result
sorted_result = sorted(result, key=result.get, reverse=True)

path = os.path.abspath("analysis.txt")
file = open(path, 'w')
for letter in sorted_result:
    file.write(f"{letter} {result[letter]}\n")
file.close()
print(result)

# зачтено
