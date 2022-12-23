n = int(input())

amount_one_thousand_yen = n // 1000
if n % 1000 > 0:
    amount_one_thousand_yen += 1

print(amount_one_thousand_yen * 1000 - n)