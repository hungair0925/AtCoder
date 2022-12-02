h, w = list(map(int, input().split()))
board = [list(input()) for _ in range(h)]

rows = ''

for h_index in range(h):
    row = ''
    for w_index in range(w):
        count = 0
        current_point = board[h_index][w_index]
        if current_point == '#':
            row += '#'
            continue
    
        if not (h_index + 1 >= h):
            bottom_point = board[h_index + 1][w_index]
            count += bottom_point.count('#')
        if not (h_index - 1 < 0):
            top_point = board[h_index - 1][w_index]
            count += top_point.count('#')
        if not (w_index + 1 >= w):
            right_point = board[h_index][w_index + 1]
            count += right_point.count('#')
        if not (w_index - 1 < 0):
            left_point = board[h_index][w_index - 1]
            count += left_point.count('#')
        if not (h_index + 1 >= h) and not (w_index + 1 >= w):
            bottom_right_point = board[h_index + 1][w_index + 1]
            count += bottom_right_point.count('#')
        if not (h_index - 1 < 0) and not (w_index + 1 >= w):
            top_right_point = board[h_index - 1][w_index + 1]
            count += top_right_point.count('#')
        if not (h_index + 1 >= h) and not (w_index - 1 < 0):
            bottom_left_point = board[h_index + 1][w_index - 1]
            count += bottom_left_point.count('#')
        if not (h_index - 1 < 0) and not (w_index - 1 < 0):
            top_left_point = board[h_index - 1][w_index - 1]
            count += top_left_point.count('#')
        row += str(count)
    rows += f'{row}\n'

print(rows.rstrip())