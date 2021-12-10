import os


def file_len_count(file_pass: str) -> int:
    count = 0
    with open(file_pass) as f:
        for line in f.readlines():
            if line != "\n" and line[0] != "#":
                count += 1
    return count


def files(dir: str) -> int:
    dir_files = os.listdir(dir)
    for file in dir_files:
        file_path = os.path.abspath(file)
        if os.path.isfile(file_path) and file_path.split('.')[-1] == "py":
            yield file_len_count(file_path)


result = 0
for i in files('../../Module14/01_os_info'):
    result += i
print(result)

# TODO: По пути в папке Module14/01_os_info у вас одни .py файл, в нем вообще всего 13 строк.
#  А по условиям задачи подходит лишь 10 строк.
#  Ваша программа выдает ответ 18.
