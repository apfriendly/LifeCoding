# Дата некоторого дня характеризуется двумя натуральными числами: m (порядковый номер месяца) и n (число). По введенным m и n (в одну строку через пробел) определить:
# а) дату предыдущего дня (принять, что m и n не характеризуют 1 января);
# б) дату следующего дня (принять, что m и n не характеризуют 31 декабря).
# В задаче принять, что год не является високосным. Вывести предыдущую дату и следующую дату (в формате: mm.dd, где m - число месяца; d - номер дня) в одну строчку через пробел.
# P.S. Число дней в месяцах не високосного года, начиная с января: 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31


days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
b, a = map(int, input().split())
if a == 1:
    pday = days[b-2]
    pmh = b - 1
    fday = 2
    fmh = b
elif a == days[b-1]:
    pday = a-1
    pmh = b
    fday = 1
    fmh = b+1
else:
    pday = a-1
    pmh = b
    fday = a+1
    fmh = b
print(f"{str(pmh).rjust(2, '0')}.{str(pday).rjust(2, '0')} {str(fmh).rjust(2, '0')}.{str(fday).rjust(2, '0')}")
