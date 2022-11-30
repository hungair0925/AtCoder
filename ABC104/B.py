s = input()

is_first_a = s[0] == 'A' and s.count('A') == 1
is_from_to_c = s[2:len(s) - 1].count('C') == 1

if is_first_a and is_from_to_c:
    removed_a = s.replace('A', '')
    removed_c = removed_a.replace('C', '')
    is_all_lower = True
    for s_part in removed_c:
       if not s_part.islower():
            is_all_lower = False
    if not is_all_lower:
        print('WA')
    else:
        print('AC')
else:
    print('WA')