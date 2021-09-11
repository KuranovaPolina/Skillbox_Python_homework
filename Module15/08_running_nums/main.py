def shift (digits):
    last_digit = digits[-1]
    del digits[-1]
    digits.insert(0, last_digit)

    return digits

K = int(input("Shift: "))

digits = [1, 4, -3, 0, 10]

print("Start list:", digits)

for _ in range(K):
    shift(digits)

print("Shifted list:", digits)