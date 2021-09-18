"""
ACならず
"""
x = list(input())
n = int(input())

members = [input() for _ in range(n)]
members_value = []

for member in members:
    total = []
    for char in member:
        total.append(x.index(char))
    members_value.append(total)

print(members_value)