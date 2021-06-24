def gener(number):
    f_num = 1
    for arg in range(number + 1):
        yield f"{arg} = {f_num}"
        f_num *= arg + 1


for arg2 in gener(int(input("Факториал № - "))):
    print(arg2)
