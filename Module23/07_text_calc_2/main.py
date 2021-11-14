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
            except (IndexError, ZeroDivisionError):
                answer = input(f"{i_line} has error. Change? (Yes/No)")
                if answer.lower() == "yes":
                    new_line = input("New line: ")
                    try:
                        result += count_func(new_line)
                    except (IndexError, ZeroDivisionError):
                        pass
    print(result)
except FileNotFoundError:
    print("File not found")


'''
def error_func(line):
    tmp_result = 0
    tmp_answer = input(f"{line} has error. Change? (Yes/No)")
    if tmp_answer.lower() == "yes":
        tmp_new_line = input("New line: ")
        try:
            tmp_result += count_func(tmp_new_line)
            return tmp_result
        except (IndexError, ZeroDivisionError):
            error_func(tmp_new_line)
'''
