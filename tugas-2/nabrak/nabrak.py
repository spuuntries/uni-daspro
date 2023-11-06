import re

inp = []

for _ in range(2):
    split = re.split(r" +", input())
    inp.append([(int(split[0]), int(split[1])), (int(split[2]), int(split[3]))])


def cross(a, b):
    return a[0] * b[1] - b[0] * a[1]


def dire(a, b, c):  # Posisi c relatif terhadap ab
    return cross((b[0] - a[0], b[1] - a[1]), (c[0] - a[0], c[1] - a[1]))


def on_segm(a, b, c):  # Cek jika titik di garis ab
    return min(a[0], b[0]) <= c[0] <= max(a[0], b[0]) and min(a[1], b[1]) <= c[
        1
    ] <= max(a[1], b[1])


def intersect(a, b, c, d):
    d1 = dire(a, b, c)
    d2 = dire(a, b, d)
    d3 = dire(c, d, a)
    d4 = dire(c, d, b)

    if ((d1 > 0 and d2 < 0) or (d1 < 0 and d2 > 0)) and (
        (d3 > 0 and d4 < 0) or (d3 < 0 and d4 > 0)
    ):
        return True
    # Jika posisi relatif terhadap garis 0,
    # dan posisi titik berada pada segmen garis
    # (dicek apakah ada di segmen garis karena posisi relatif 0 berarti kolinier,
    # tetapi belum tentu berpotongan),
    # maka kolinier dan berpotongan
    elif d1 == 0 and on_segm(a, b, c):
        return True
    elif d2 == 0 and on_segm(a, b, d):
        return True
    elif d3 == 0 and on_segm(c, d, a):
        return True
    elif d4 == 0 and on_segm(c, d, b):
        return True
    else:
        return False


if intersect(inp[0][0], inp[0][1], inp[1][0], inp[1][1]):
    print("awas nabrak")
else:
    print("gaspol bangg")
