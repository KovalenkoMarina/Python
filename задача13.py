# Задайте список из вещественных чисел. Напишите программу, которая найдёт 
# разницу между максимальным и минимальным значением дробной части элементов.
    
#     *Пример:*
    
#     - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

list_1 = [1.1, 1.2, 3.1, 5, 10.01]
list_2 = []
for i in range(0, len(list_1)):
    list_2.append(round(list_1[i] % 1, 2))
    for j in range(0, len(list_2)):
        if list_2[j] == 0:
            del list_2[j]

max = 0
min = 1
for i in range(0, len(list_2)):
    if list_2[i] > max:
        max = list_2[i]
    if list_2[i] < min:
        min = list_2[i]
print(max - min)

