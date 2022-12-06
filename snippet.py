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