def func_1():
    a = 0
    while True:
        list_1 = input("Введите число, для выхода, введите 'q': ").split()
        for n in list_1:
            if n == 'q':
                return a
            else:
                try:
                    a += int(n)
                except ValueError:
                    print("Для выхода из программы, введите 'q'")
        print(f"Сумма чисел равна = {a}")


print(func_1())
