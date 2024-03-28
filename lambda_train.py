# Напиши лямбда-выражение, которое принимает строку и возвращает ее первую букву (в верхнем регистре).
# Затем используй лямбда-выражение для преобразования списка слов в список их первых букв.
# Например, из списка ["apple", "banana", "cherry"] должно получиться ['A', 'B', 'C'].

words = ["apple", "banana", "cherry", "date", "fig"]
get_first_letter = lambda x: x[0].upper()
first_letters = list(map(get_first_letter, words))
print(first_letters)


# Напиши лямбда-выражение, которое принимает букву и возвращает количество слов в списке, содержащих эту букву.
# Например, для буквы "a" результат должен быть 3, потому что в списке есть слова "apple", "banana" и "date".

words = ["apple", "banana", "cherry", "date", "fig"]
letter = input()
count = len(list(filter(lambda word: letter in word, words)))
print(count)


# Напиши лямбда-выражение, которое принимает строку и возвращает True, если строка является палиндромом,
# и False в противном случае. Палиндром - это слово, которое читается одинаково слева направо и справа налево.
# Например, "radar" и "level" являются палиндромами.

revers_ = lambda x: x == x[::-1]
print(revers_('12321'))
