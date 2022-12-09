# Все задачи решать с помощью использования лямбд, filter, map, zip, enumerate, List Comprehension
# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11


num = "".join(filter(str.isdecimal, input('Введите вещественное число: \n '))) 
# сумма цифр с использованием map
list_digits = sum(map(int, num))       
print(f'Сумма цифр = {list_digits}')

# сумма цифр с импользованием List Comprehension
list_digits = [int(i) for i in num]     
print(f'Сумма цифр = {sum(list_digits)}')