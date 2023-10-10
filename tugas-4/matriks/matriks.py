n = int(input())
inputs = [input().split(" ") for _ in range(n)]


def spiralOrder(matrix):
    result = []
    while matrix:
        result += matrix.pop(
            0
        )  # Ambil baris teratas, kemudian hilangkan baris tersebut
        if matrix and matrix[0]:  # Cek apakah masih ada baris tersisa
            for row in matrix:
                result.append(row.pop())  # Untuk tiap baris, diambil kolom terakhir
        if matrix:  # Cek matriks masih ada barisan atau tidak
            result += matrix.pop()[::-1]  # Kita ambil yang terakhir, terus dibalik
        if matrix and matrix[0]:  # Cek apakah masih ada baris tersisa
            for row in matrix[::-1]:
                result.append(
                    row.pop(0)
                )  # Dari bawah, ambil kolom pertama dari tiap baris
    return result


# 1  2  3   4
# 5  6  7   8
# 9  10 11  12
# 13 14 15  16

# [1, 2, 3, 4] # 1. Ambil baris pertama
# 5  6  7   8
# 9  10 11  12
# 13 14 15  16

# [1, 2, 3, 4, 8, 12, 16] # 2. Ambil kolom terakhir
# 5  6  7
# 9  10 11
# 13 14 15

# [1, 2, 3, 4, 8, 12, 16, 15, 14, 13] # 3. Ambil baris terakhir yg dibalik
# 5  6  7
# 9  10 11

# [1, 2, 3, 4, 8, 12, 16, 15, 14, 13] # 4 .Dari bawah, ambil kolom pertama dari tiap baris
# 5  6  7
# 9  10 11

# [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5] # 5. Dari bawah, ambil kolom pertama dari tiap baris
# 6  7
# 10 11

# [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7] # Ulang step 1
# 10 11

# [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11] # Ulang step 2
# 10

# [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10] # Ulang step 3, karena udah abis matriksnya, stop.

print(" ".join(spiralOrder(inputs)))
