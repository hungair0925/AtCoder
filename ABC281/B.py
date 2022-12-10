from collections import defaultdict
import string

def input_int():
    return int(input())

def input_str():
    return input()

def multi_input_int():
    return map(int, input().split())

def multi_input_str():
    return input().split()

def multi_line_input_int(n):
    return [int(input()) for _ in range(n)]

upper_alphabets = list(string.ascii_uppercase)

def contain_str(middle_str):
    for a in middle_str:
        if a in upper_alphabets:
            return True
    return False

def judge(s):
    is_upper_first = s[0] in upper_alphabets
    is_upper_last = s[-1] in upper_alphabets
    middle_str = s[1:len(s) - 1]
    if not contain_str(middle_str) and middle_str[0] != '0' and 100000 <= int(middle_str) <= 999999:
        is_range_num = True
    else:
        is_range_num = False
    return is_upper_first and is_range_num and is_upper_last

s = input_str()

if len(s) < 8:
    print("No")
elif judge(s):
    print("Yes")
else:
    print("No")
