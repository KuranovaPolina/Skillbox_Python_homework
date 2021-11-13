def count_func(line):
    line_list = line.split(" ")
    line_len = len(line_list)
    if line_list[-1] == '\n':
        line_len -= 1
    if len(line_list) != 3 or not (line_list[1] in operands) or \
            not (line_list[0].isdigit() and line_list[2].isdigit()):
        raise IndexError
    elif line_list[1] == "+":
        return int(line_list[0]) + int(line_list[2])
    elif line_list[1] == "-":
        return int(line_list[0]) - int(line_list[2])
    elif line_list[1] == "*":
        return int(line_list[0]) * int(line_list[2])
    elif line_list[1] == "/":
        if line_list[2] == "0":
            raise ZeroDivisionError
        else:
            return int(line_list[0]) / int(line_list[2])
    elif line_list[1] == "**":
        return int(line_list[0]) ** int(line_list[2])
    elif line_list[1] == "%":
        if line_list[2] == "0":
            raise ZeroDivisionError
        else:
            return int(line_list[0]) % int(line_list[2])
    elif line_list[1] == "//":
        if line_list[2] == "0":
            raise ZeroDivisionError
        else:
            return int(line_list[0]) // int(line_list[2])


operands = ["+", "-", "*", "/", "**", "%", "//"]
result = 0
try:
    with open('calc.txt', 'r') as file:
        for i_line in file:
            try:
                if i_line[-1] == '\n':
                    i_line = i_line[:-1]
                result += count_func(i_line)
            except IndexError:
                print("Wrong format")
            except ZeroDivisionError:
                print("Zero division error")
    print(result)
except FileNotFoundError:
    print("File not found")

