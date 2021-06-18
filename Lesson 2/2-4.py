str = input("Введите слово - ")
for a, b in enumerate(str, 1):
    print(a, b) if len(b) <= 10 else print(a, (b[:10]))
