shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300],
        ['педаль', 100], ['седло', 1500], ['рама', 12000],
        ['обод', 2000], ['шатун', 200], ['седло', 2700]]

detail = input("Detail: ")
count = 0
summ = 0

for i in shop:
    if i[0] == detail:
        count += 1
        summ += i[1]

print("Count: ", count)
print("Price: ", summ)

# зачтено
