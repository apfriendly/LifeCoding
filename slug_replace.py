# Вводится строка (слаг). 
# Замените в этой строке все двойные дефисы (--) и тройные (---) на одинарные (-). 
# Подумайте, в какой последовательности следует выполнять эти замены. 
# Результат преобразования выведите на экран.


s = input()
s1 = s.replace('---','-')
print(s1.replace('--','-'))
