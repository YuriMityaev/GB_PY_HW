def int_func():
    for arg_1 in input("Введите слово с пробелами латинскими буквами: \n").split():
        ch = 0
        for arg_2 in arg_1:
            if 97 <= ord(arg_2) <= 122:
                ch += 1
        print(arg_1.title() if ch == len(arg_1) else f"{arg_1} - Введите, пожалуйста, только маленькие латинские буквы.")


int_func()
