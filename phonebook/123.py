import csv

name = ""
phone = ""

print('Выберите действие ')
a = int(input("""0 - новый контакт
1 - просмотр книги
    """))
    
if a == 1:
    with open('phonebook/some.txt',  'r') as f1:
        b = f1.read()
        print(b)

elif a == 0:
    name = str(input('Запишите имя: '))
    phone = str(input('Запишите номер телефона: '))
    with open('phonebook/some.txt', 'a', newline='') as f:
        f.write(name)
        f.write(" - ")
        f.write(phone)
        f.write("\n")

else:
    print("ERROR")
        

