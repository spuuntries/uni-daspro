# v2, tanpa cheet
import re

_ = input()
days = [int(n) for n in re.split(r" +", input())]
last = input()

day = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"]


# FPB
def fpb(*numbers):
    a = numbers[0]
    for b in numbers[1:]:
        while b != 0:
            a, b = b, a % b
    return a


# KPK
def kpk(*numbers):
    res = numbers[0]
    for n in numbers[1:]:
        res = res * n // fpb(res, n)
    return res


print(day[(day.index(last) + kpk(*days)) % 7])
