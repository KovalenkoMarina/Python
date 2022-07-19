# Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.

from numpy.polynomial import Polynomial


path_1 = 'zadacha20/file-20-1.txt'

with open(path_1, 'r') as f1:
    a = f1.readline()
a = a.split()
a = a[:-2]
a = a[::2]


path_2 = 'zadacha20/file-20-2.txt'

with open(path_2, 'r') as f2:
    b = f2.readline()
b = b.split()
b = b[:-2]
b = b[::2]

c = []
d = []

for i in range(0, len(a)):
    c.append(int(a[i][0]))
for i in range(0, len(b)):
    d.append(int(b[i][0]))
c.reverse()
d.reverse()


p1 = Polynomial(c)
p2 = Polynomial(d)
p = str(p1 + p2)

path = 'zadacha20/file-20-3.txt'

with open(path, 'a') as f:
     f.write(p)


