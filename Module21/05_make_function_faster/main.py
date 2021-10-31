def calculating_math_func_start(data):
    result = 1
    for index in range(1, data + 1):
        result *= index
    result /= data ** 3
    result = (result ** 10)
    return result


def calculating_math_func(data, factorials={1: 1}):
    if data in factorials:
        result = factorials[data]
    else:
        result = 1
        for index in range(data, 0, -1):
            if index in factorials:
                result *= factorials[index]
                break
            else:
                result *= index
        factorials[data] = result
    result /= data ** 3
    result = result ** 10
    return result, factorials


print(calculating_math_func_start(6))
print(calculating_math_func(5)[0])
print(calculating_math_func(6)[0])

# зачтено
