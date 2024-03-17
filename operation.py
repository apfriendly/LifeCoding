operation = '10 + 25 - 12 + 20 - 1 + 3'

s = ''
for i, o in enumerate(operation):
    if o.isdigit():
        s += o
    elif o == ' ':
        del(o)
    else:
        s += ' ' + o
sn = s.split()
sum_sn = 0
for i in sn:
    sum_sn += int(i)

print(sum_sn)
