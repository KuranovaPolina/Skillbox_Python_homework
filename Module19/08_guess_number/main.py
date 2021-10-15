N = int(input("N = "))

data = {
    "Да": ["{0}".format(i + 1) for i in range(N)],
    "Нет": []
}

step = 0
while True:
    question = input("Нужное число есть среди вот этих чисел: ")

    if question != "Помогите!":
        answer = input("Ответ Артёма: ")
        if step == 0 and answer == "Да":
            data["Да"] = question.split(" ")
        else:
            data[answer].extend(question.split(" "))
    else:
        break

result = sorted(list(set(data["Да"]) - set(data["Нет"])))
for i in result:
    print(i, end=" ")
