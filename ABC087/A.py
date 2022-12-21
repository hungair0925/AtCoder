x = int(input())
a = int(input())
b = int(input())

x_minus_a = x - a
b_amount = x_minus_a // b

print(x_minus_a - (b_amount * b))