import os


def folder_size_f(folder_path):
    folder_files = os.listdir(folder_path)
    folder_size = 0
    folder_file_count = 0
    for folder_file in folder_files:
        folder_file_path = os.path.join(folder_path, folder_file)
        if os.path.isfile(folder_file_path):
            folder_size += os.path.getsize(folder_file_path)
            folder_file_count += 1
        else:
            folder_results = folder_size_f(folder_file_path)
            folder_size += folder_results[0]
            folder_file_count += folder_results[1]

    return folder_size, folder_file_count


# path = input("Input path: ")
path = os.path.join('..', '..', 'Module14')
print(path)
files = os.listdir(path)
size = 0
folder_count = 0
file_count = 0

for file in files:
    file_path = os.path.join(path, file)
    if os.path.isfile(file_path):
        file_count += 1
        size += os.path.getsize(file_path)
    else:
        folder_count += 1
        results = folder_size_f(file_path)
        size += results[0]
        file_count += results[1]

print(size / 1024)
print(folder_count)
print(file_count)

# TODO: Количество файлов не считает:
"""
..\..\Module22
10.765625
7
0
"""
