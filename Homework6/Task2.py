# Дан список, вывести отдельно буквы и цифры, пользуясь filter.
# [12,'sadf',5643] ---> ['sadf'] ,[12,5643]

data = [12,'sadf',5643, 'jdg']

list_digits = list(filter(lambda x: not isinstance(x, str), data))
list_symbols = list(filter(lambda x: type(x) is str, data))
print(list_digits,',', list_symbols)
