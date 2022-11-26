a, b = map(int, input().split())
multiple_a_b = a * b

if multiple_a_b % 2 == 0:
    print("Even")
else:
    print("Odd")