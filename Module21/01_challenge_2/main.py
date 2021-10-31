def out_func(num):
    if num != 1:
        out_func(num - 1)
    print(num)


out_func(5)

# зачтено
