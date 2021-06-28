from random import randint


with open("file_5.txt", "w+", encoding="utf-8") as f:
    f.write(" ".join([str(randint(1, 1000)) for i in range(1001)]))
    f.seek(0)
    print(sum(map(int, f.readline().split())))
