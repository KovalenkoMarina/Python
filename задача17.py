#Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.


N = int(input('Введите число: '))
def numbs(N):
    s = []
    i = 2
    while i * i <= N:
        while N % i == 0:
            s.append(i)
            N = N/i
        i += 1
    if N > 1:
        s.append(int(N))
    return s
print(numbs(N))

