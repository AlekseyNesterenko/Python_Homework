# Требуется найти наименьший натуральный делитель целого числа N, отличный от 1.
# Пример:
# Для n = 15: Ответ: 3
# Для n = 35: Ответ: 5

try:
    num = int(input('Введите целое число: \n'))
    for i in range(2,num+1):
        if num % i == 0:
            print(f'Наименьший натуральный делитель: {i}')
            break
except Exception:
    print('Нужно ввести целое чило!')