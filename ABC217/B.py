contests = ["ABC" , "ARC" , "AGC" , "AHC"]

s1 = input()
s2 = input()
s3 = input()

opened_contests = [s1, s2, s3]

for op_contens in opened_contests:
    contests.remove(op_contens)

print(contests[0])