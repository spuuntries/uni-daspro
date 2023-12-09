# Failed attempt at emulating the diagonal on a round-robin table.

n = int(input())
inputs = [list(map(int, input().split())) for _ in range(n)]

for i in inputs:
    N, K = i
    # Pattern-based solution.
    if N % 2 != 0:
        print(2 * K - 1 if K <= (N // 2) + 1 else (2 * (K - 1 - (N // 2 + 1))))
    else:
        if K <= (N // 2):
            print(2 * K - 1)
        else:
            positions = list(range(2, N, 2))
