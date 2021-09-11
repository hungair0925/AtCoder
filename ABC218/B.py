p = list(map(int, input().split()))

template = 'abcdefghijklmnopqrstuvwxyz'

s = ''

for p_x in p:
    s += template[p_x - 1]
print(s)