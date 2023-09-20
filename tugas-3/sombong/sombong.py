import re

inp = [int(e) for e in re.split(r" +", input())]

if inp[0] % (inp[1] + 1) == 0:
    print("Abeng")
else:
    print("Bahresi")
