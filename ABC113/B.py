n = int(input())
t, a = list(map(int, input().split()))
hs = list(map(int, input().split()))

highs = []

for h in hs:
    high = a - (t - (h * 0.006))
    highs.append(abs(high))

print(highs.index(min(highs)) + 1)
    