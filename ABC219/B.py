s1 = input()
s2 = input()
s3 = input()
t = list(input())

s_lists = [s1, s2, s3]
result = ''

for ele in t:
    result += s_lists[int(ele) - 1]

print(result)