inp = input()
ends = inp.split(" ")
res = 0

for e in range(int(ends[0]), int(ends[1]) + 1):
    if e % 2 != 0:
        res += e

print(res)
