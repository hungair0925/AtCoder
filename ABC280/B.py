n = int(input())
s_nums = list(map(int, input().split()))

a_1 = s_nums[0]

result = []

for i in range(len(s_nums) - 1, 0, -1):
    a = s_nums[i] - s_nums[i - 1]
    result.append(a)

result.append(a_1)

print(*result[::-1])