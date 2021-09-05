n = int(input())
a_numbers = list(map(int, input().split()))

odd_flag = False
div_num = 0

while 1:
    for a_num in a_numbers:
        if a_num % 2 != 0:
            odd_flag = True

    if  odd_flag:
        break

    for index, a_num in enumerate(a_numbers):
        a_numbers[index] = a_num // 2
    
    div_num += 1
    
print(div_num)     