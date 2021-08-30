def digit_sum(N):
    summ = 0
    while N > 0:
        summ += N % 10
        N //= 10
    return summ

def digit_count(N):
    count = 0
    while N > 0:
        count += 1
        N //= 10
    return count

N = int(input("Input number: "))

summ = digit_sum(N)
print("\nSum of digit:", summ)

count = digit_count(N)
print("Digit count:", count)

print("Difference:", summ - count)
