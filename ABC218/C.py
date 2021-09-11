"""
ACならず..
"""
n = int(input())

s = []
t = []

def count_row(row):
    count_data = {}
    for r in row:
        if not r[0] in count_data:
            count_data[r[0]] = 0
        count_data[r[0]] += 1
    count_data = sorted(count_data.items(), key=lambda x:x[0])
    length = []
    for d in count_data:
        length.append(d[1])
        
for i in range(1, n * 2 + 1):
    if i <= n:
        s_row = list(input())
        for j, s_r in enumerate(s_row):
            if s_r == '#':
                s.append([i, j + 1])
    else:
        t_row = list(input())
        for j, t_r in enumerate(t_row):
            if t_r == '#':
                t.append([i - 5, j + 1])

while count_row(s) != count_row(t):
    for i, s_row in enumerate(s):
        s_x = n - s_row[1] + 1
        s_y = s_row[0]
        s[i] = [s_x, s_y]

diff = t[0][0] - s[0][0] + t[0][1] - s[0][1]
can = True

for i in range(1, len(s)):
    d_x = t[i][0] - s[i][0]
    d_y = t[i][1] - s[i][1]
    if diff != (d_x + d_y):
        can = False
        break

print(can)

  
    
    