n, a, b = list(map(int, input().split()))

numbers = []

def calc_digit_total(digit):
    total = 0
    digit_num = digit
    while digit_num >= 10:
        total += digit_num % 10
        digit_num = digit_num // 10
    total += digit_num
    return total
        
for digit in range(1, n + 1):
    digit_total = calc_digit_total(digit)
    if digit_total >= a and digit_total <= b:
        numbers.append(digit)

print(sum(numbers))