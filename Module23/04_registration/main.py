def check_func(line):
    line_list = line.split(" ")
    line_len = len(line_list)
    if line_list[-1] == '\n':
        line_len -= 1
    if len(line_list) != 3:
        raise IndexError
    elif not line_list[0].isalpha():
        raise NameError
    elif not ("@" and "." in list(line_list[1])):
        raise SyntaxError
    elif int(line_list[2]) < 10 or int(line_list[2]) > 99:
        raise ValueError


right_file = open('registrations_good.log', 'w', encoding='UTF-8')
errors_file = open('registrations_bad.log', 'w', encoding='UTF-8')
with open('registrations.txt', 'r', encoding='UTF-8') as file:
    for i_line in file:
        try:
            if i_line[-1] == '\n':
                i_line = i_line[:-1]
            check_func(i_line)
        except FileNotFoundError:
            print("File not found")
        except IndexError:
            errors_file.write(i_line + "\tIndexError\n")
        except NameError:
            errors_file.write(i_line + "\tNameError\n")
        except SyntaxError:
            errors_file.write(i_line + "\tSyntaxError\n")
        except ValueError:
            errors_file.write(i_line + "\tValueError\n")
        else:
            right_file.write(i_line + "\n")
right_file.close()
errors_file.close()
