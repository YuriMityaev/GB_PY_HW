def my_func(arg_1, arg_2, arg_3):
    func_list = [arg_1, arg_2, arg_3]
    try:
        func_list.remove(min(func_list))
        return sum(func_list)
    except TypeError:
        return "Ошибка ввода, введите, пожалуйста, числовое значение"


print(my_func(233, 3, 11))
