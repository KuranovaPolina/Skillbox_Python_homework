string = input('Input string: ')

letters = {}

for letter in string:
    if letter in letters.keys():
        letters[letter] = int(letters.pop(letter)) + 1
    else:
        letters[letter] = 1

count = 0
for letter in letters.keys():
    if (int(letters[letter]) % 2) != 0:
        count += 1

if count > 1:
    print("You can't make a palindrom")
else:
    print("You can make a palindrom")

# зачтено
