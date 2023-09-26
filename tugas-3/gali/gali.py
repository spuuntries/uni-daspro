import re

_, y = re.split(r" +", input())
# Loop sebanyak y kali, dimana tiap kali loop minta input, lalu di-split.
# Setelah split, tiap elemen dijadikan integer. (Baca dari paling luar ke dalam)
mat = [[int(n) for n in re.split(r" +", input())] for _ in range(int(y))]
size = int(input())


def submat(arr, p, q):
    matrices = []
    m, n = len(arr), len(arr[0])

    for i in range(m - p + 1):
        for j in range(n - q + 1):
            submatr = []
            for k in range(p):
                submatr.append(
                    arr[i + k][j : j + q]
                )  # Ambil baris i + k, terus ambil kolom j sampai j + q - 1
            matrices.append(submatr)

    return matrices


submatrix = submat(mat, size, size)
tot = 0

for m in submatrix:
    subtot = 0
    for r in m:
        subtot += sum(r)
    tot = subtot if subtot > tot else tot

print(tot)
