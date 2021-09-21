n = int(input())
numbers = list(map(int, input().split()))
max_n = max(numbers)
min_n = min(numbers)

print(abs(max_n - min_n))