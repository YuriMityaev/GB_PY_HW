my_list = [6, 5, 4, 4, 3, 2, 1]
add_number = int(input("Введите новый элементв в рейтинг"))
i = 0
for a in my_list:
    if add_number <= a:
        i += 1
    else:
        break
my_list.insert(i, add_number)
print(my_list)
