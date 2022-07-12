#5. Реализуйте алгоритм перемешивания списка.
import random

number = int(input("Введите число: "))

def list_num(number: int):
    list_numbers = []
    for element in range (0, number):
        list_numbers.append(element)
    random.shuffle(list_numbers)
    return list_numbers
print(list_num(number))

