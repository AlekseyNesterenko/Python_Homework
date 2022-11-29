# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

list = [i for i in map(int, input('Введите числа через пробел: \n').split())]
product_pairs = []
for i in range(len(list) // 2 + 1):
    product_pairs[i] = list[i] * list[-i-1]
    product_pairs.append(product_pairs[i])
print(list)
print(product_pairs)



#доделать