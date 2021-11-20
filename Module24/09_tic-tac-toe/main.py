class Field:
    def __init__(self):
        self.Cells = [['.', '.', '.'],
                      ['.', '.', '.'],
                      ['.', '.', '.']]

    def put(self, x, y, element):
        if self.Cells[y - 1][x - 1] == '.':
            self.Cells[y - 1][x - 1] = element
        else:
            raise BaseException

    def print_field(self):
        for y in range(3):
            for x in range(3):
                print(self.Cells[y][x], end='\t')
            print("")

    def check_win(self):
        win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
        for cell in win_coord:
            cell1 = cell[0]
            cell2 = cell[1]
            cell3 = cell[2]
            if self.Cells[cell1 // 3][cell1 % 3] == \
                    self.Cells[cell2 // 3][cell2 % 3] == \
                    self.Cells[cell3 // 3][cell3 % 3] != '.':
                return True
        return False


field = Field()
field.print_field()

count = 0
while count != 9:
    x = int(input("x = "))
    y = int(input("y = "))
    if (x < 1 or x > 3) or (y < 1 or y > 3):
        print("wrong cell")
    else:
        element = input("element: ")
        try:
            field.put(x, y, element)
            print("")
            field.print_field()
        except BaseException:
            print("cell is not free")
        else:
            count += 1

        if field.check_win():
            print(f"End... Win {element}!")
            break

# зачтено
