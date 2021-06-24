from functools import reduce


def list_1(arg_1, arg_2):
    return arg_1 * arg_2


new_list = [arg for arg in range(100, 1001, 2)]
print(f"Список четных чисел ниже \n {new_list} \n Произведение всех четных чисел от 100 до 1000 ниже \n {reduce(list_1, new_list)}")
