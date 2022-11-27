k = int(input())
a, b = map(int, input().split())
index = 1

while True:  
    killo_meter = k * index
    
    if killo_meter > b:
        print("NG")
        break

    if killo_meter >= a and killo_meter <= b:
        print("OK")
        break
    
    index += 1
    