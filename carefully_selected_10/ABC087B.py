a = int(input())
b = int(input())
c = int(input())
x = int(input())

total_count = 0

for a_num in range(a + 1):
    for b_num in range(b + 1):
        for c_num in range(c + 1):
            total_amount = a_num * 500 + b_num * 100 + c_num * 50
            if x == total_amount:
                total_count += 1

print(total_count)