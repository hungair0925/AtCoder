# Not AC

k = int(input())

factorial_amount = 1

for i in range(1, k + 1):
    factorial_amount *= i
    if factorial_amount % k == 0:
        print(i)
        break