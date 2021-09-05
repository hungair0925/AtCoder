n, a, b = list(map(int, input().split()))

numbers = []
for digit in range(1, n + 1):
    digit_str = str(digit)
    digit_total = 0
    for di_str in digit_str:
        digit_total += int(di_str)
    
    if digit_total >= a and digit_total <= b:
        numbers.append(digit)

print(sum(numbers))