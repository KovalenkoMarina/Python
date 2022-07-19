# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100)
#  многочлена и записать в файл многочлен степени k.

# Пример:

# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random

k = int(input('Введите степень много члена: '))
list_1 =['= 0']
x = str()
for i in range(0, k+1):
    A = random.randint(0, 100)
    if i == 0:
        list_1.append(f'{A} ')
    if i == 1:
        list_1.append(f'{A}*x + ')
    if i > 1:
        list_1.append(f'{A}*x^{i} + ')

list_1.reverse()
s = ''.join(list_1)
#print(s)


path = 'file-19.txt'

with open(path, 'a') as f:
     f.write(s)

