N = input("N = ")

data = {
    "Да": [],
    "Нет": []
}

while True:
    question = input("Нужное число есть среди вот этих чисел: ")

    if question != "Помогите!":
        answer = input("Ответ Артёма: ")
        data[answer].extend(question.split(" "))
    else:
        break

result = sorted(list(set(data["Да"]) - set(data["Нет"])))
for i in result:
    print(i, end=" ")

# TODO: Не выдаёт результат предполагаемых чисел:
"""
N = 10
Нужное число есть среди вот этих чисел: 1 2 3
Ответ Артёма: Нет
Нужное число есть среди вот этих чисел: 5 7 8 9 10
Ответ Артёма: Нет
Нужное число есть среди вот этих чисел: Помогите
"""