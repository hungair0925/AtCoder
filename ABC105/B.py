n = int(input())

result = "No"

for i in range(0, 25):
    for j in range(0, 25):
        cake = i * 4
        donuts = j * 7
        if n == (cake + donuts):
            result = "Yes"
            break
print(result)