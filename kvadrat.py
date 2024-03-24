digits = '8 -11 4 3 6'

d_list = digits.split(' ')

d_kv_list = []
for i, d in enumerate(d_list):
    d_kv_list.append(int(d)**2)

print(*d_kv_list)
