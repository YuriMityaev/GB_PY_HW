from random import randint

list_1 = [randint(-20, 30) for _ in range(20)]
new_list = [arg for arg in list_1 if list_1.count(arg) == 1]
print(f"Исходный список - {list_1} \n Список без повторений - {new_list}")
