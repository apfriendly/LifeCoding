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


# Напиши код, используя лямбда-выражение, чтобы отфильтровать список и оставить только строки,
# которые начинаются с заглавной буквы (подсказка: используй метод isupper() для строк)

words = ["Apple", "banana", "Cherry", "Date", "Fig"]
upper_word = list(filter(lambda word: word.istitle(), words))
print(upper_word)


# Напиши код, используя лямбда-выражение, чтобы отсортировать список по второму элементу каждого кортежа

items = [("book", 20), ("pen", 5), ("pencil", 2), ("notebook", 10)]
sorted_items = list(sorted(items, key=lambda item: item[1]))
print(sorted_items)


# Напиши код, используя лямбда-выражение, чтобы найти максимальное число в списке
# Подсказка: используй функцию max() и передай ей ключ (key) с лямбда-выражением
#
numbers = [10, 5, 25, 15, 30, 20]
maximum = lambda x: max(x)
print(maximum(numbers))
