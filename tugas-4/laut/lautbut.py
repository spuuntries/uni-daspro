import re


def bien(n):  # Integer to binary
    rem = n
    res = ""
    while True:
        res += str(rem % 2)
        rem //= 2
        if rem == 0:
            break
    res = list(res)
    res.reverse()
    return "".join(res)


_ = input()
catches = [bien(int(e)) for e in re.split(r" +", input())]

res = 0

for c in catches:
    for n in c:
        if n == "1":
            res += 1

print(res)
