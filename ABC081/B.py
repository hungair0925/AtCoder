n = int(input())
a_numbers = list(map(int, input().split()))

count = 0
while 1:
    is_odd = False
    for i in range(0, n):
        if a_numbers[i] % 2 == 1:
            is_odd = True

    if is_odd:
        break

    for i in range(0, n):
        a_numbers[i] = a_numbers[i] // 2
    count += 1

print(count)