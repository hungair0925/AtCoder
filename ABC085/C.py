def multi_input_int():
    return map(int, input().split())

N, Y = multi_input_int()

is_none_pair = True

for x in range(N + 1):
    if not is_none_pair:
        break

    for y in range(N - x + 1):
        z = N - (x + y)
        amount = 10000 * x + 5000 * y + 1000 * z
        if amount == Y:
            is_none_pair = False
            print(x, y, z)

if is_none_pair:
    print(-1 , -1, -1)