# Вводится список целых чисел в одну строчку через пробел. Необходимо оставить в нем только двузначные числа.
# Реализовать программу с использованием функции filter. Результат отобразить на экране в виде последовательности
# оставшихся чисел в одну строчку через пробел.
# [1,2,3,4,22,234,24] ----> [22, 24]
# Все задачи решать с помощью использования лямбд, filter, map, zip, enumerate, List Comprehension

numbers = [int(i) for i in  input('Введите целые числа через пробел: \n ').split()]
new_list = list(filter(lambda x: 9 < x < 100, numbers))
print(new_list)

