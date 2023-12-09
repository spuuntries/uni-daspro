n = int(input())
matrices = []

for _ in range(n):
    N, M = map(int, input().split())
    mat = [list(map(int, input().split())) for _i in range(N)]
    matrices.append((M, mat))

for p in matrices:
    rot = p[0]
    mat = p[1]

    for _ in range(rot):
        mat = [[mat[j][i] for j in range(len(mat))] for i in range(len(mat[0]))][::-1]

    [print(" ".join(map(str, row))) for row in mat]
