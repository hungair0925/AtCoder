n = int(input())
a = int(input())

n_leave = n % 500

if n_leave <= a:
    print("Yes")
else:
    print("No")