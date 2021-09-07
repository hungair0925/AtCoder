n = int(input())
mochis = [int(input()) for _ in range(n)]
buckets = [None for _ in range(100)]

for mochi in mochis:
    buckets[mochi - 1] = mochi

buckets = list(filter(lambda x: x != None, buckets))
print(len(buckets))