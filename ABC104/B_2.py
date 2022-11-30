s = input()

def is_ac(s):
    is_first_a = s[0] == 'A' and s.count('A') == 1
    is_from_to_c = s[2:len(s) - 1].count('C') == 1
    is_all_lower_without_a_c = list(map(str.islower, s)).count(True) == len(s) - 2 
    if not is_first_a: return False
    if not is_from_to_c: return False
    if not is_all_lower_without_a_c: return False

    return True

if is_ac(s):
    print('AC')
else:
    print('WA')