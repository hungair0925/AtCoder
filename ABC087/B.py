a = int(input())
b = int(input())
c = int(input())
x = int(input())

count = 0

for a_index in range(0, a + 1):
    for b_index in range(0, b + 1):
        for c_index in range(0, c + 1):
            amount = a_index * 500 + b_index * 100 + c_index * 50
            if amount == x:
                count += 1

print(count)