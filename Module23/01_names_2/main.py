def func(line):
    line_len = len(line)
    if line[-1] == '\n':
        line_len -= 1
    try:
        if line_len < 3:
            raise BaseException
    except BaseException:
        print(f"{len_number} line - len < 3")
        errors_file.write(f"{len_number} line - len < 3" + "\n")
    return line_len


len_number = 0
general_len = 0
file_text = ""
errors_file = open('errors.logs', 'w')
try:
    with open('people.txt', 'r') as file:
        for i_line in file:
            len_number += 1
            general_len += func(i_line)

except FileNotFoundError:
    print("File not found")

finally:
    print(general_len)
