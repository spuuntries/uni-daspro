import re

inp = [int(e) for e in re.split(r" +", input())]
a = inp[0]
b = inp[1]
c = inp[2]

if a + b >= c and a + c >= b and b + c >= a:
    print("Tri-Force dapat terbentuk!")
else:
    print("Tri-Force gagal terbentuk :(")
