n = int(input("Введите положительное число"))
n1 = n % 10
n2 = n // 10
while n > 0:
    if n % 10 > n1:
        n1 = n % 10
    n = n // 10
print(n1)
