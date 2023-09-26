import re

inp = []

for _ in range(2):
    split = re.split(r" +", input())
    inp.append([(int(split[0]), int(split[1])), (int(split[2]), int(split[3]))])


def cross(a, b):
    return a[0] * b[1] - b[0] * a[1]
