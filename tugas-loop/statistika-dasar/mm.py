import re

_ = int(input())
inp = [int(n) for n in re.split(r" +", input())]

mx = mn = inp[0]

for n in inp:
    if mx < n:
        mx = n
    if mn > n:
        mn = n

print(mx, mn)
