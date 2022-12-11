from collections import defaultdict

def input_int():
    return int(input())
def multi_line_input_str(n):
    return [input() for _ in range(n)]

n = input_int()
words  = multi_line_input_str(n)

sorted_words = []

for word in words:
    sorted_word = "".join(sorted(word))
    sorted_words.append(sorted_word)

count_by_words = defaultdict(int)

for sorted_word in sorted_words:
    count_by_words[sorted_word] += 1

result = 0

for k, v in count_by_words.items():
    result += v * (v - 1) // 2

print(result)
