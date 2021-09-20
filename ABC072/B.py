s = input()
result = ""

for i, ele in enumerate(s):
    if (i + 1) % 2 == 1:
        result += ele

print(result)