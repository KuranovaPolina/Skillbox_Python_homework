import os

path = os.path.abspath('numbers.txt')
file = open(path, 'r')
file_text = file.read()
file.close()
result = 0
for i_element in file_text:
    if i_element.isdigit():
        result += int(i_element)

path = os.path.abspath('answer.txt')
file = open(path, 'w')
file.write(f"result {result}")
file.close()

# зачтено
