# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между
#  ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21
print('введите координаты точки А')
A = list()
for i in range(2):
     A.append(float(input('-->')))

print('введите координаты точки B')
B = list()
for i in range(2):
     B.append(float(input('-->')))

print (((A[0] - B[0])**2 + (A[1] - B[1])**2) ** (0.5))