# С клавиатуры вводятся две буквы (в одну строку через пробел).
# Вывести на экран следующую строку:
# "Коды: <буква1> = <код буквы1>, <буква2> = <код буквы2>"


a, z = map(str, input().split())
print(f"Коды: {a} = {ord(a)}, {z} = {ord(z)}")
