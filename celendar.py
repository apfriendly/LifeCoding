# Вывести на экран календарь, имея месяц и год

import calendar

year = int(input('Введите год: '))
month = int(input('Введите месяц: '))

print(calendar.month(year, month))

