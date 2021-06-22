def func_1(x, y):
    try:
        x, y = float(x), int (y)
        st = x ** y
    except ValueError:
        return "Введите значение Х как положительное число, и значение Y как отрицательное целое число"
    return st


print(func_1(input("Введите положительное число = "), input("Введите отрицательное целое число =")))