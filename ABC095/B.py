n, x = list(map(int, input().split()))
ms = [int(input()) for _ in range(n)]
can_make_ms = []

leave_gram = x -  sum(ms)

if leave_gram == 0:
    print(n)
else:
    for m in ms:
        can_make_m = leave_gram // m
        can_make_ms.append(can_make_m)
    print(n + max(can_make_ms))
        