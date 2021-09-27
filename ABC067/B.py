n, k = list(map(int, input().split()))
ls = list(map(int, input().split()))
sorted_ls = sorted(ls)
max_ls = []

for i in range(1, k + 1):
    max_ls.append(sorted_ls[-i])

print(sum(max_ls))