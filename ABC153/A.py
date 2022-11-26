hitpoint, attack_point_per_once = map(int, input().split())

if hitpoint % attack_point_per_once == 0:
    print(int(hitpoint / attack_point_per_once))
elif hitpoint <= attack_point_per_once:
    print(1)
else:
    print(int(hitpoint / attack_point_per_once) + 1)