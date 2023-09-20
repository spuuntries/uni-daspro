import math
import re

inp = [[int(n) for n in re.split(r" +", input())] for _ in range(4)]
bj = inp.pop()


def dist(p1, p2):
    return math.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)


def area(p1, p2, p3):
    return abs(
        p1[0] * (p2[1] - p3[1]) + p2[0] * (p3[1] - p1[1]) + p3[0] * (p1[1] - p2[1])
    )


def quad(x, y):
    if x > 0:
        if y > 0:
            return 1
        if y < 0:
            return 4
    if x < 0:
        if y > 0:
            return 2
        if y < 0:
            return 3


tot = area(*inp)

print(f"TITIK PENGAWAS: kuadran {' '.join([str(quad(*t)) for t in inp])}")

ins = "Yo Ndak Tau Kok Tanya Saya"
spec = ""

t1 = area(bj, inp[0], inp[1])
t2 = area(bj, inp[1], inp[2])
t3 = area(bj, inp[2], inp[0])

if t1 + t2 + t3 == tot:
    ins = "KEPUNG BJARKAN!!!"
    if len(list(filter(lambda x: x == 0, [t1, t2, t3]))) > 1:
        spec = "Dia Segaris Dengan Kalian"
    else:
        spec = "Tapi Dia Tidak Segaris Dengan Kalian"

for e in [(inp[i], inp[j]) for i in range(len(inp)) for j in range(i + 1, len(inp))]:
    p1 = e[0]
    p2 = e[1]
    p1p2 = dist(p1, p2)
    p2p3 = dist(p2, bj)
    p1p3 = dist(p1, bj)
    if p1p2 + p2p3 == p1p3:
        spec = "Dia Masih Segaris Dengan Kalian"


print(f"{ins}{', ' + spec if len(spec) > 0 else ''}")
