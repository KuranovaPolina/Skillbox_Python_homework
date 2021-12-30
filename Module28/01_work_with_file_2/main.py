from typing import TextIO


class File:
    def __init__(self, filename: str) -> None:
        self.filename = filename
        self.file = None
        self.found = False

    def __enter__(self) -> tuple[TextIO, bool]:
        try:
            self.file = open(self.filename, encoding='utf-8')
            self.found = True
        except FileNotFoundError:
            self.file = open(self.filename, 'w', encoding='utf-8')
        return self.file, self.found

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        self.file.close()


with File('example.txt') as info:
    if not info[1]:
        info[0].write('Всем привет')
    else:
        print(info[0].read())
