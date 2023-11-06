import re


def bien(n):  # Integer to binary
    rem = n
    res = []
    while True:
        res.append(str(rem % 2))
        rem //= 2
        if rem == 0:
            break
    res.reverse()
    return "".join(res)


# bien(10)
#                          hasil            bulat
# 10 % 2 [0]    (10 / 2 =   5    =>          5)
# 5 % 2 [0,1]    (5 / 2 =   2.5   =>         2)
# 2 % 2 [0,1,0]   (2 / 2 =    1    =>        1)
# 1 % 2 [0,1,0,1]  (1 / 2 =   0.5   =>       0)
# [0,1,0,1] => [1,0,1,0] => 1010

_ = input()
catches = [list(bien(int(e))) for e in input().split()]


def count(catches):
    res = 0
    for c in catches:
        for n in c:
            if n == "1":
                res += 1
    return res


print(count(catches))
