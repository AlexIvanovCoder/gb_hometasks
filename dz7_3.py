class Cell:
    def __init__(self, cell_num):
        self.cell_num = cell_num

    def __add__(self, other):
        return Cell(self.cell_num + other.cell_num)

    def __sub__(self, other):
        if self.cell_num < other.cell_num:
            raise ValueError('The second argument is less than the first one')
        else:
            return Cell(self.cell_num - other.cell_num)

    def __mul__(self, other):
        return Cell(self.cell_num * other.cell_num)

    def __truediv__(self, other):
        return Cell(int(self.cell_num / other.cell_num))

    def __str__(self):
        return str(self.cell_num)

    def make_order(self, char_in_row):
        full_rows = self.cell_num // char_in_row
        left_cells = self.cell_num % char_in_row
        lst = ["*" * char_in_row for i in range(full_rows)]
        if left_cells > 0:
            lst.append("*" * left_cells)
        return '\n'.join(lst)


cl1 = Cell(5)
cl2 = Cell(4)
cl3 = Cell(7)
print(cl1 + cl2)
print(cl1 - cl2)
print(cl1 * cl2)
print(cl1 / cl2)
c4 = cl1 + cl2
print(c4.make_order(4))
