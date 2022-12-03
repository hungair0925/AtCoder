h, w = list(map(int, input().split()))

board = [input() for i in range(h)]
count = 0

for row in board:
    count += row.count('#')

print(count)