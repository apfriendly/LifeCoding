# Вводятся названия рек в одну строчку через пробел. 
# Необходимо все их отсортировать по именам (по возрастанию) и в отсортированном списке удалить первый элемент. Результат отобразить на экране в одну строчку через пробел.

rivers = input().split()

rivers.sort()
rivers.pop(0)

print(*rivers)
