# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
    
#     *Пример:*
    
#     - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

n = int(input('Введите число: '))

def fib(n):
    if n in [1, 2]:
        return 1
    if n == 0:
        return 0
    else:
        return fib(n-1) + fib(n-2)
list_1 = []
for e in range(0, n+1):
    list_1.append(fib(e))

list_2 = []
for e in range(1, n + 1):
    list_2.append(fib(e)*((-1)**(e+1)))

list_2.reverse()

print(list_2 + list_1)