n, a, b = map(int, input().split())

result = 0

def get_sum_decimal_digit(num):
    sum_digit = 0

    while num > 0:
        mod = num % 10
        sum_digit += mod

        num = num // 10
    return sum_digit

for i in range(1, n + 1):
    sum_decimal_digit = get_sum_decimal_digit(i)
    if sum_decimal_digit >= a and sum_decimal_digit <= b:
        result += i

print(result)

