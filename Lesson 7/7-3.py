class Cell:
    def __init__(self, num):
        self.num = num

    def mo(self, rows):
        return "\n".join(['Клетка' * rows for _ in range(self.num // rows)]) + '\n' + "Клетка" * (self.num % rows)

    def __str__(self):
        return f"{self.num}"

    def __add__(self, other):
        print("Сумма клеток равна:")
        return Cell(self.num + other.num)

    def __sub__(self, other):
        print("Разница клеток равна:")
        return Cell(self.num - other.num) if self.num - other.num > 0 else "Не хватает ячеек в 1 клетке"

    def __mul__(self, other):
        print("Произведение клеток равно:")
        return Cell(self.num * other.num)

    def __floordiv__(self, other):
        print("Остаточно деление клеток равно:")
        return Cell(self.num // other.num)

cell_1 = Cell(21)
cell_2 = Cell(45)

print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 // cell_2)
print(cell_2.mo(9))
