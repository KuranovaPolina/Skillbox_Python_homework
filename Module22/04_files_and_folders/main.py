import os

# path = input("Input path: ")
path = os.path.join('..', '..', 'Module14')
files = os.listdir(path)
size = 0
folder_count = 0
file_count = 0
for file in files:
    file_path = os.path.join(path, file)
    size += os.path.getsize(file_path) / 1024
    if os.path.isfile(file_path):
        file_count += 1
    else:
        folder_count += 1

print(size)
print(folder_count)
print(file_count)

# TODO: Не считает размер и количество файлов
