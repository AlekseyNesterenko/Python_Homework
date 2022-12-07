# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

# Входные данные хранятся в отдельных текстовых файлах.
# stroka = "aaabbbbccbbb"
# ....
# stroka = "3a4b2c3b"
# Восстановить
# Ввёл: stroka = "3a4b2c3b"
# Вывод: stroka = "aaabbbbccbbb"

def Compression(text):  # сжатие
    data = ''
    i = 0
    while i < len(text):
        count = 0
        while i+1 <len(text) and text[i] == text[i+1]:
            count +=1
            i += 1
        data += str(count) + text[i]
        i += 1
    return data

def Recovery(text):  # восстановление
    data = ''
    i = 0
    while i < len(text):
        data += str(text[i+1]) * int(text[i])
        i += 2
    return data

with open('Compression.txt', 'r', encoding='UTF-8') as file1:
    print(Compression(file1.read()))

with open('Recovery.txt', 'r', encoding='UTF-8') as file2:
    print(Compression(file2.read()))
