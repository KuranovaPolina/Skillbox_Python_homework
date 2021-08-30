def reverse(N):
    whole = True
    whole_line = ''
    frac_line = ''

    for digit in N:
        if digit != '.' and whole == True:
            whole_line += digit
        elif digit != '.' and whole == False:
            frac_line += digit
        else:
            whole = False

    whole_line = whole_line[::-1]
    frac_line = frac_line[::-1]

    N = (whole_line + '.' + frac_line)
    return N

N = float(input("N = "))
K = float(input("K = "))

N = float(reverse(str(N)))
print("Reversed N =", N)

K = float(reverse(str(K)))
print("Reversed K =", K)

print("Sum =", N + K)


