import re

_ = input()
catches = [list(bin(int(e))[2:]) for e in re.split(r" +", input())]


def count(catches):
    res = 0
    for c in catches:
        for n in c:
            if n == "1":
                res += 1
    return res


print(count(catches))
