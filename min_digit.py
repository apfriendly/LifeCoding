# Вводится список в виде вещественных чисел в одну строку через пробел. 
# С помощью цикла for необходимо найти наименьшее значение в этом списке. 
# Полученный результат вывести на экран.  
# Реализовать программу без использования функции min, max и сортировки.


digits = input()

list_digits = digits.split(' ')

min_digit = list_digits[0]
for digit in list_digits:
    if float(digit) < float(min_digit):
        min_digit = digit

print(min_digit)
