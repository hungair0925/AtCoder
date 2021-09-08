"""
実行時間制限超過
計算量: O(N^3)
"""

n, total = list(map(int, input().split()))

xyz = []

for i in range(0, n + 1):
    for j in range(0, n + 1):
        for k in range(0, n + 1):
            if (i + j + k) > n:
                break
            
            current_total = 10000 * i + 5000 * j + 1000 * k
            if current_total == total and (i + j + k) == n:
                xyz.append(f"{i} {j} {k}")
                break
if len(xyz) == 0:
    print("-1 -1 -1")
else:
    print(xyz[0])