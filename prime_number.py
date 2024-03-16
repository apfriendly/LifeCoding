def checking_prime_number(num):

    if num != 0 and num % 1 == 0 and num % num == 0:
        print(f'Это {int(num)} натуральное число')
    else:
        print(f'Число {num} не является натуральным')


user_input = float(input('Введите число: '))
checking_prime_number(user_input)
