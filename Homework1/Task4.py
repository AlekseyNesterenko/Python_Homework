#Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

#проба try - except 

try:
    quarter_number = int(input('Введите номер четверти координатной плоскости: \n'))
    if quarter_number == 1:
        print('x > 0 и y > 0')
    elif quarter_number == 2:
        print('x < 0 и y > 0')
    elif quarter_number == 3:
        print('x < 0 и y < 0')
    elif quarter_number == 4:
        print('x > 0 и y < 0')
    else:
        print('Это не номер четверти координатной плоскости!')
except Exception:
    print('Нужно ввести число!')