n = int(input())
mochis = [int(input()) for _ in range(n)]
buckets = {}

for mochi in mochis:
    buckets[mochi] = mochi

print(len(buckets))