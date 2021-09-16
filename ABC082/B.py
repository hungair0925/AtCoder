s = input()
t = input()

"sの並び替えで取りうる最小"
"tの並び替えで取りうる最大"
s_sort = "".join(sorted(s))
t_sort = "".join(sorted(t, reverse=True))

if s_sort < t_sort:
    print("Yes")
else:
    print("No")