"""
計算量: O(N^2)
"""

n, total = list(map(int, input().split()))

xyz = []

for i in range(0, n + 1):
    for j in range(0, n + 1):
        k = n - i - j
        if k < 0:
            continue

        current_total = 10000 * i + 5000 * j + 1000 * k
        if current_total == total:
            xyz.append(f"{i} {j} {k}")
            break

if len(xyz) == 0:
    print("-1 -1 -1")
else:
    print(xyz[0])