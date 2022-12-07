# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена 
# и записать в файл (или вывести в терминал) многочлен степени k.
# Пример:
# - k = 2  => 2*x² + 4*x + 5
# - k = 3  => 41*x^3 + 6*x² + 2*x + 98

from random import randint

k = int(input('Введите максимальную степень многочлена: \n'))
result = []
for i in range(k, 0, -1):
    coef = randint(0, 100)
    if coef == 0:
        continue
    elif coef == 1:
        result.append('')
    else:
        result.append(f'{coef}*x^{i}' if i != 1 else f'{coef}*x')
result.append(f'{randint(0, 101)}')

with open ('file.txt', 'w') as data:
    data.write(" + ".join(result) + "")