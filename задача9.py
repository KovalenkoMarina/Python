# 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях. Позиции вводит пользователь через пробел.

number = int(input("Введите число: "))
a = int(input('Введите номера позиций для умножения: '))
b = int(input('Введите номера позиций для умножения: '))
def list_num(number: int):
    list_numbers = []
    for i in range (-number, number+1):
        list_numbers.append(i)
    multiply = list_numbers[a]*list_numbers[b]
    return multiply

print(list_num(number))