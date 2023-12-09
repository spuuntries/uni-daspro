import math

_ = input()
sx, sy, rw, rh = list(map(int, input().split()))
tx, ty = list(map(int, input().split()))
tot = rw * rh


def area(p1, p2, p3):
    return abs(
        0.5
        * (p1[0] * (p2[1] - p3[1]) + p2[0] * (p3[1] - p1[1]) + p3[0] * (p1[1] - p2[1]))
    )


dist = math.sqrt(
    abs(max(sx, tx) - min(sx, tx)) ** 2 + (abs(max(sy, ty) - min(sy, ty)) ** 2)
)

rect_points = [
    (sx - rw // 2, sy + rh // 2),
    (sx + rw // 2, sy + rh // 2),
    (sx + rw // 2, sy - rh // 2),
    (sx - rw // 2, sy - rh // 2),
]

# Try for every point of rect sides
t1 = area((tx, ty), rect_points[0], rect_points[1])
t2 = area((tx, ty), rect_points[1], rect_points[2])
t3 = area((tx, ty), rect_points[2], rect_points[3])
t4 = area((tx, ty), rect_points[3], rect_points[0])


if sum([t1, t2, t3, t4]) == tot:
    # When the sum is the same as area(rect), that means that the point is inside the rect.
    print("KAMU SUDAH SAMPAI")
else:
    print(f"{dist:.2f} METER LAGI")
