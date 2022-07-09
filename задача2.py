#Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.


# X = int(input('введите X - '))
# Y = int(input('введите Y - '))
# Z = int(input('введите Z - '))
# if (not (X or Y or Z)) == (not X and not Y and not Z):
#     print("True")
# else:
#     print('False')

a = []
for i in range(1,100):
    a.append(i)

count = 0
count1 = 0

for X in range(0, len(a)):
    for Y in range(0, len(a)):
        for Z in range(0, len(a)):
            if (not (X or Y or Z)) == (not X and not Y and not Z):
                count += 1
            else:
                count1 += 1
if count1 == 0:
    print("True")
else:
    print('False')