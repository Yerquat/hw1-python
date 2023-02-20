n = int(input('Введите трехзначное число: '))
summa = 0
while (n != 0):
    m = n % 10
    summa = summa + m
    n = n // 10
else:
    print(f'Сумма цифр заданного числа равна: {summa}')