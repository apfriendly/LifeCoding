# Напиши лямбда-выражение, которое принимает строку и возвращает ее первую букву (в верхнем регистре).
# Затем используй лямбда-выражение для преобразования списка слов в список их первых букв.
# Например, из списка ["apple", "banana", "cherry"] должно получиться ['A', 'B', 'C'].

words = ["apple", "banana", "cherry", "date", "fig"]
get_first_letter = lambda x: x[0].upper()
first_letters = list(map(get_first_letter, words))
print(first_letters)
