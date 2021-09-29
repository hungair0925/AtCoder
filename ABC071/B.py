s = input()
template = list("abcdefghijklmnopqrstuvwxyz")

for alphabet in s:
    if alphabet in template:
        template.remove(alphabet)

if len(template) == 0:
    print("None")
else:
    print(template[0])