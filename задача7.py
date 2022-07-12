# 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
    #     *Пример:*
    #     - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

from math import *

number = int(input("Введите число: "))

def list_factorial(number: int):
    list_numbers = []
    for element in range (1, number+1):
        list_numbers.append(factorial(element))
    return list_numbers
print(list_factorial(number))

