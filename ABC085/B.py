def input_int():
    return int(input())

def multi_line_input_int(n):
    return [int(input()) for _ in range(n)]

n = input_int()
mochi_diameters = multi_line_input_int(n)
count_by_diameter = {}

for diamter in mochi_diameters:
    if diamter not in count_by_diameter:
        count_by_diameter[diamter] = 1
    else:
        count_by_diameter[diamter] += 1

print(len(count_by_diameter))