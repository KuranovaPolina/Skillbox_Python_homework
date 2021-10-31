def find_fibonacci_num(pos):
    if pos in (1, 2):
        return 1
    return find_fibonacci_num(pos - 1) + find_fibonacci_num(pos - 2)


num_pos = int(input("Location: "))
print("Number:", find_fibonacci_num(num_pos))

# зачтено
