# Напишите программу, удаляющую из текста все слова, содержащие "абв".

word = 'абв ура! Питон оченьабв круто. Люблюабв питон'
col = word.split()

new_col = []
search = 'абв'

new_col = [item for item in col if 'абв' not in item]
print(new_col)