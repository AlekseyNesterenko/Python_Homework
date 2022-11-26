# Требуется посчитать сумму чётных чисел, расположенных между числами 1 и N включительно.

num = int(input('Введите число: \n'))
list =[]
sum = 0
for i in range(1,num+1):
    if i % 2 == 0:
        list.append(i)
        sum += i
print(f'четные числа от 1 до {num}: {list}')
print(f'сумма четных чисел = {sum}')