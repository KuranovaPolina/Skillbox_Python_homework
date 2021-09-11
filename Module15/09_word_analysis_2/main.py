word = input("Input word: ")
letters_list = list(word)

lenght = len(letters_list)

steps = lenght // 2

is_polindrom = True

for i in range(steps):
    if letters_list[i] != letters_list[-(i + 1)]:
        is_polindrom = False
        break

if is_polindrom:
    print("Palindrom")
else:
    print("Not palindrom")