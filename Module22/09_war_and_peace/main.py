import os
import zipfile

path = os.path.abspath("voyna-i-mir.zip")
path2 = os.path.join("..", "09_war_and_peace")

archive = path
with zipfile.ZipFile(archive, 'r') as zip_file:
    zip_file.extractall(path2)

path = os.path.abspath("voyna-i-mir.txt")
file = open(path, 'r', encoding='UTF-8')
file_text = file.read()
file.close()

result = {}
letter_count = 0
for letter in file_text:
    if letter in result.keys():
        result[letter] = result.pop(letter) + 1
    else:
        result[letter] = 1
    letter_count += 1

sorted_result = sorted(result, key=result.get, reverse=True)
path = os.path.abspath("analysis.txt")
file = open(path, 'w', encoding='UTF-8')
for letter in sorted_result:
    file.write(f"{letter} {result[letter]}\n")
file.close()

# зачтено
