n = int(input())
inp = [input().split() for _ in range(n)]


def patA(bar, kol):
    print("Pattern no: 1")
    for b in range(bar):
        if b % 2 == 0:
            print(" ", end="")
        for k in range(kol):
            if k % 2 == 0:
                print(".", end="")
            else:
                print("-", end="")
            if k == kol - 1:
                print()


def patB(bar, kol):
    print("Pattern no: 2")
    for b in range(bar):
        if b % 2 != 0:
            print(" ", end="")
        for k in range(kol):
            if k % 2 == 0:
                print("-", end="")
            else:
                print(".", end="")
            if k == kol - 1:
                print()


for i in inp:
    pola = i[0]
    bar = int(i[1])
    kol = int(i[2])
    mapping = {"A": patA, "B": patB}
    mapping[pola](bar, kol)
