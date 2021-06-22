def func_1(arg_1, arg_2):
    try:
        arg_1, arg_2 = int(arg_1), int(arg_2)
        arg_3 = arg_1 / arg_2
        return round(arg_3, 1)
    except ValueError:
        return "Ошибка ввода, повторите ввод"
    except ZeroDivisionError:
        return "Деление на 0 запрещено, введите иное значение"


print(func_1(input(f"Введите чеслитель: "), input(f"Введите делитель: ")))
