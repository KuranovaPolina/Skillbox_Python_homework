vowels = ["a", "у", "о", "и", "э","ы", "я", "ю", "е", "ё"]

text = input("Введите текст: ")

text_list = list(text)

text_vowels_list = [letter for letter in text_list if letter in vowels]

print("Список гласных букв:", text_vowels_list)
print("Длина списка:", len(text_vowels_list))
