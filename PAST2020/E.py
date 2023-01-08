n, m, q = map(int, input().split())

points = [[] for _ in range(n)]

for _ in range(m):
    u, v = map(int, input().split())
    
    u -= 1
    v -= 1

    points[u].append(v)
    points[v].append(u)

point_colors = list(map(int, input().split()))

for i in range(q):
    query = input().split()

    point_index = int(query[1]) - 1
    current_color = point_colors[point_index]

    if query[0] == '1':
        print(current_color)  
        for adjoin_point_index in points[point_index]:
            point_colors[adjoin_point_index] = current_color
    elif query[0] == '2':
        print(current_color)
        update_color = int(query[2])
        point_colors[point_index] = update_color
