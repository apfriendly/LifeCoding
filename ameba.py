# Одноклеточная амеба каждые 3 часа делится на 2 клетки. 
# Определить, сколько клеток будет через n часов (n - целое положительное число, вводимое с клавиатуры). 
# Считать, что изначально была одна амеба. Результат вывести на экран. 
# Задачу необходимо решить с использованием цикла while.


n = int(input())

ameba = 1
i = 3

while i < n:
    ameba *= 2
    i += 3
      
print(ameba)
