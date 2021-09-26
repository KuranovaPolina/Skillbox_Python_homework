N = int(input("N = "))
K = int(input("K = "))

sticks = ["I" for _ in range(N)]

for i in range(K):
    L_i = int(input(f"{i + 1}: start = "))
    R_i = int(input("end = "))

    sticks[L_i - 1: R_i] = ["." for _ in range(L_i - 1, R_i)]

print("Result: ", end = "")
for i in sticks:
    print(i, end = "")