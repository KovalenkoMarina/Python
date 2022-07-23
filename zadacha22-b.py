#Вариант для игры с ботом, наделенным интеллектом

import random


ost = 2021

a = int(input("Введите число от 1 до 28: "))
ost = ost - a
if a > 20:
    b = 49-a
    print('b = ', b)
    ost = ost - b
    while ost > 28:
        a = int(input("Введите число от 1 до 28: "))
        ost = ost - a
        b = 29-a
        print('b = ', b)
        ost = ost - b
if a < 20:
    b = 20-a
    print('b = ', b)
    ost = ost - b
    while ost > 28:
        a = int(input("Введите число от 1 до 28: "))
        ost = ost - a
        b = 29-a
        print('b = ', b)
        ost = ost - b
# если первый игрок вводит 20, то он автоматически выигрывает
if ost == 0:
    print("Остаток = ", ost, 'Выиграл компьютер')
else:
    a = int(input("Введите остаток: "))
    print("ВЫ ВЫИГРАЛИ!!!")