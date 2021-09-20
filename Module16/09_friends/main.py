N = int(input("N = "))
K = int(input("K = "))

balance = []
for _ in range(N):
    balance.append(0)

for i in range(K):
    print(f"\n{i + 1}")
    to_whom = int(input("to whom: "))
    from_who = int(input("from who: "))
    how_much = int(input("how much: "))

    balance[to_whom - 1] -= how_much
    balance[from_who - 1] += how_much

for i in range(N):
    print(f"{i + 1} : {balance[i]}")

# зачтено
