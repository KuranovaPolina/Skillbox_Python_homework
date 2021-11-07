import string
import os

upper_letters = list(string.ascii_uppercase)
lower_letters = list(string.ascii_lowercase)

path = os.path.abspath('text.txt')
file = open(path, 'r')
path2 = os.path.abspath('cipher_text.txt')
file2 = open(path2, 'a')
step = 1
for i_line in file:
    new_line = []
    for letter in i_line:
        if letter.isupper():
            new_line.append(upper_letters[(upper_letters.index(letter) + step) % len(upper_letters)])
        elif letter.islower():
            new_line.append(lower_letters[(lower_letters.index(letter) + step) % len(lower_letters)])
        else:
            new_line.append(letter)
    new_line = ''.join(new_line)
    file2.write(new_line)
    step += 1

file.close()
file2.close()

# зачтено
