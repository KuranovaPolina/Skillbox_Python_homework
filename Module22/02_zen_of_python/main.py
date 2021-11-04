import os

path = os.path.abspath('zen.txt')

zen_file = open(path, 'r')

lines = []
for i_line in zen_file:
    lines.append(i_line)

zen_file.close()

for i_line in lines[::-1]:
    print(i_line, end='')
