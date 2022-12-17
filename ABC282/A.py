import string

alphabets = list(string.ascii_uppercase)
k = int(input())

print(''.join((alphabets[:k])))

