# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

list = [i for i in map(int, input('Введите числа через пробел: \n').split())]
product_pairs = []
for i in range(len(list)//2+1):
    a = list[i] * list[len(list)-1-i]
    product_pairs.append(a)
if len(list) % 2 == 0:
    product_pairs.pop(len(product_pairs)-1)  # небольшой костыль, но по-доугому получалось намного больше кода
print(product_pairs)



