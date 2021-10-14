N = input("N = ")

data = {
    "Да":[],
    "Нет":[]
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
    print(i, end = " ")