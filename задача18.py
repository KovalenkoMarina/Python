# Задайте последовательность чисел. 
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.


numbers = [1, 2, 3, 2, 5, 3, 4, 5, 6]

def uniqum_numbers(numbers):
    uniqum = []
    for number in numbers:
        if number not in uniqum:
            uniqum.append(number)
        else:
            uniqum.remove(number)
    return uniqum
print(uniqum_numbers(numbers))