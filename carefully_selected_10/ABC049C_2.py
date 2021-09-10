s = input()
rev_s = s[::-1]

words = ["dream", "dreamer", "erase", "eraser"]
rev_words = []
t = ""

for word in words:
    rev_words.append(word[::-1])

next_index = 0

for i, r_s in enumerate(rev_s):
    if i < next_index and i > 0:
        continue

    for r_w in rev_words:
        if rev_s[next_index:next_index + len(r_w)] == r_w:
            t += r_w
            next_index += len(r_w)

if len(t) == len(s):
    print("YES")
else:
    print("NO")
            

