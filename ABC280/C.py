s = input()
t = input()

result = None

for i in range(len(t)):
    if i > len(s) - 1:
        result = len(t)
        break
    if s[i] != t[i] and i == 0:
        result = 1
        break
    if s[i] != t[i]:
        result = i + 1
        break

print(result)
