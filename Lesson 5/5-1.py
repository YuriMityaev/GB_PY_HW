with open("file_1.txt", "w", encoding="utf-8") as f:
    while True:
        line = input("Введите значение или пустую строку для завершения: ")
        if not line:
            break
    #print(line, file=f)
        f.write(f"{line}\n")
        f.close()
