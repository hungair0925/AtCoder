num_length = int(input())
p = list(map(int, input().split()))
q = [None for _ in range(num_length)]

for i in range(num_length):
    insert_index = p[i] - 1
    insert_value = str(i + 1)
    q[insert_index] = insert_value

print(" ".join(q))