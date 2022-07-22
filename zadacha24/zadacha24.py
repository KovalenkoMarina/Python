# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.


def rle_encode(data): 
    encoding = ''
    prev_char = '' 
    count = 1 
    if not data: return '' 
    
    for char in data:   
        if char != prev_char: 
            if prev_char: 
                encoding += str(count) + prev_char 
            count = 1 
            prev_char = char 
        else: 
            count += 1 
    else: 
        encoding += str(count) + prev_char 
        return encoding

path_1 = 'zadacha24/file-24-1.txt'

with open(path_1, 'r') as data:
    data = data.readline()

path = 'zadacha24/file-24-2.txt'

with open(path, 'a') as f:
     f.write(rle_encode(data))



