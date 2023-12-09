# This and the cpp one would TLE for large numbers.
n = int(input())
inputs = [list(map(int, input().split())) for _ in range(n)]

for i in inputs:
    positions = list(range(1, i[0] + 1))
    target = i[1]
    rest = []
    layup = False

    while len(rest) < target:
        print(rest)
        head = positions.pop(0)
        if not layup:
            rest.append(head)
        else:
            positions.append(head)
        layup = not layup

    print(rest[-1])
