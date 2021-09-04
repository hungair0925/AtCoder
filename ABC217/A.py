s, t =  list(input().split())
words = [s, t]
sorted_words = sorted(words)

if words == sorted_words:
    print("Yes")
else:
    print("No")