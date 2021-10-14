N = int(input("N = "))

pizzaTimeDict = {}

for i in range(N):
    order = input("{0} order: ".format(i + 1)).split(" ")
    if order[0] in pizzaTimeDict.keys():
        if order[1] in pizzaTimeDict[order[0]].keys():
            pizzaTimeDict[order[0]][order[1]] = int(order[2]) + int(pizzaTimeDict[order[0]].pop(order[1]))
        else:
            pizzaTimeDict[order[0]][order[1]] = order[2]
    else:
        pizzaTimeDict[order[0]] = {order[1]: order[2]}

for i in sorted(pizzaTimeDict.keys()):
    print("{0}:".format(i))
    for j in sorted(pizzaTimeDict[i].keys()):
        print("\t{0}:{1}".format(j, pizzaTimeDict[i][j]))