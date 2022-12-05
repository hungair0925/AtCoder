def input_str():
    return input()

def multi_input_int():
    return map(int, input().split())

s = input_str()
a, b = multi_input_int()

s_a = s[a - 1]
s_b = s[b - 1]

list_s = list(s)
list_s[a - 1] = s_b
list_s[b - 1] = s_a

print(''.join(list_s))