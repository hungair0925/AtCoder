n, a, b = map(int, input().split())

result = 0

for i in range(1, n + 1):
    separated_digit = list(map(int, list(str(i))))
    total = sum(separated_digit)
    if total >= a and total <= b:
        result += i

print(result)