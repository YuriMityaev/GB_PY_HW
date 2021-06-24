from sys import argv


def salary():
    try:
        arg_1, arg_2, arg_3 = map(float, argv[1:])
        print(f"Заработная плата с учетом бонуса составляет = {arg_1 * arg_2 + arg_3}")
    except ValueError:
        print("Введите последовательно заработную плату в час, количество отработанных часов, бонус - числами")


salary()
