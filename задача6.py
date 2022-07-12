# 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
    #     *Пример:*
    #     - 6782 -> 23
#     - 0,56 -> 11

N = float(input("Введите число: "))
number = int(str(N).replace(".", ""))

def sum_elements(number: int):
    sum = 0
    #a = len(str(number))
    for i in range (0, len(str(number))):
        sum += number % 10
        number = number//10
    return sum
print(sum_elements(number))