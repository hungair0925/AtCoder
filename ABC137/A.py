a, b = map(int, input().split())

a_plus_b = a + b
a_minus_b = a - b
a_multiple_b = a * b

print(max([a_plus_b, a_minus_b, a_multiple_b]))