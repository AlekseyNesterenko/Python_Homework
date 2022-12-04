# Вычислить число Pi c заданной точностью d, не используя ф. round()
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

from math import pi
num = int(input('Введите количество знков после запятой pi: \n'))
n = f'.{num+1}'
print(pi)
print(format(pi, n))