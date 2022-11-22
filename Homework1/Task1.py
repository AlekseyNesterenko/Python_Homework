# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

#проба try - except 

try:
    list_of_days = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']
    week_day = int(input('Введите номер дня недели от 1 до 7: \n'))
    if week_day == 6 or week_day == 7:
        print(f'{list_of_days[week_day-1]} - Ура, выходной :)')
    else:
        print(f'{list_of_days[week_day-1]} - Нужно работать :(')
except Exception:
    print('Нужно ввести номер дня недели от 1 до 7!')