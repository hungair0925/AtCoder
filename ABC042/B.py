n, l = list(map(int ,input().split()))
words = [input() for _ in range(n)]
print("".join(sorted(words)))