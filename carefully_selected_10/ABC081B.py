n = int(input())
a_numbers = list(map(int, input().split()))
div_nums = []


for a_num in a_numbers:
    divide_num = 0
    target_num = a_num

    while target_num % 2 == 0:
        divide_num += 1
        target_num = target_num // 2

    div_nums.append(divide_num)    

        
print(min(div_nums))