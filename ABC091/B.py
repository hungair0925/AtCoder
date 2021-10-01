n = int(input())
blues = [input() for _ in range(n)]
m= int(input())
reds = [input() for _ in range(m)]

count_by_card = {}

for blue in blues:
    if count_by_card.get(blue) == None:
        count_by_card[blue] = 1
    else:
        count_by_card[blue] += 1

for red in reds:
    if count_by_card.get(red) == None:
        count_by_card[red] = -1
    else:
        count_by_card[red] -= 1

def is_all_minus(values):
    bool_arrays = []
    for value in values:
        if value < 0:
            bool_arrays.append(True)
        else:
            bool_arrays.append(False)
    return all(bool_arrays)

if is_all_minus(count_by_card.values()):
    print(0)
else:
    print(max(count_by_card.values()))


