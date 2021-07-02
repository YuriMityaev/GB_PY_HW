from random import randint


list_1 = [randint(0, 1000) for _ in range (0, randint(2, 20))]
new_list = [list_1[num] for num  in range (1, len(list_1)) if list_1[num]>list_1[num - 1]]
print(new_list)