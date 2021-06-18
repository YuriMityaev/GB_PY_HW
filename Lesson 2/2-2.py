new_list = list(input("Введите число = "))
for a in range(1, len(new_list), 3):
    new_list[a - 1], new_list[a] = new_list[a], new_list[a - 1]
print(new_list)
