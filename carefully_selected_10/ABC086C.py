n = int(input())

step_num = 0
current_t = 0
current_x = 0
current_y = 0

for i in range(n):
    t, x, y = list(map(int, input().split()))
    same_parity = t % 2 == (x + y) % 2
    abs_xy = abs(x - current_x) + abs(y - current_y)

    if abs_xy <= (t - current_t) and same_parity:
        step_num += 1
    
    current_t, current_x, current_y = t, x, y

if step_num == n:
    print("Yes")
else:
    print("No")

