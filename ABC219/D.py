"""
ACならず...
"""
n = int(input())
takoyaki, taiyaki = list(map(int, input().split()))

lunches = [list(map(int, input().split())) for _ in range(n)]
can_buy_num = 0

tako = 0
tai = 0

for i, lunch in enumerate(lunches):
    lun_tako, lun_tai = lunch
    tako += lun_tako
    tai += lun_tai
    
    if tako >= takoyaki and tai >= taiyaki:
        print(i + 1)
        break
    
        