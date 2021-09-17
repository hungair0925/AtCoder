n = int(input())

counts = []

for i in range(1, n + 1):
    if i % 2 == 0:
        current_num = i
        divide_count = 0
        while current_num % 2 == 0:
            current_num = current_num // 2
            divide_count += 1
        counts.append(divide_count)
    else:
        counts.append(0)

print(counts.index(max(counts)) + 1)
