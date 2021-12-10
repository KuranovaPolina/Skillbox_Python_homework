import os


def file_len_count(file_pass: str):
    count = 0
    with open(file_pass) as f:
        for line in f.readlines():
            if line != "\n" and line[0] != "#":
                count += 1
    return count


def files(dir):
    dir_files = os.listdir(dir)
    for file in dir_files:
        file_path = os.path.abspath(file)
        if os.path.isfile(file_path) and file_path.split('.')[-1] == "py":
            yield file_len_count(file_path)


result = 0
for i in files(os.path.dirname(os.path.abspath(__file__))):
    result += i
print(result)