import os


def gen_files_path(catalog: str, dir='C:'+os.path.sep, find=False) -> tuple:
    folder_files = os.listdir(dir)
    for folder_file in folder_files:
        folder_file_path = os.path.join(dir, folder_file)
        if os.path.isfile(folder_file_path):
            yield folder_file_path, find
        elif folder_file == catalog:
            find = True
            yield folder_file_path, find
            break
        else:
            try:
                for i_path, find in gen_files_path(catalog, folder_file_path):
                    print(i_path)
            except PermissionError:
                print("  ")
        if find:
            break


for i_path in gen_files_path("06_magic", "C:\Polina\python_basic"):
    print(i_path[0])
