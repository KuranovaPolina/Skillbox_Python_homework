def digit_count(N, i):
    count = 0
    while N > 0:
        digit = N % 10
        N //= 10
        if digit == i:
            count += 1
    return count

def same_digit(N):
    is3 = False
    for i in range(10):
        count = digit_count(N, i)
        if count == 3:
            is3 = True
            break
    return is3

start = int(input("Введите первый год: "))
end = int(input("Введите второй год: "))

for year in range(start, end + 1):
    if same_digit(year) == True:
        print(year)