digits = '-5.67 3.5 6.89 -3.0'

list_digits = digits.split(' ')

for i, digit in enumerate(list_digits):
    if float(digit) < 0:
        list_digits[i] = '-1.0'

print(*list_digits)
