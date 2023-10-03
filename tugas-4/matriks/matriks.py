n = int(input())
inputs = [input().split(" ") for _ in range(n)]


def spiralOrder(matrix):
    result = []
    while matrix:
        result += matrix.pop(
            0
        )  # Ambil baris teratas, kemudian hilangkan baris tersebut
        print(matrix)
        if matrix and matrix[0]:  # Cek apakah masih ada baris tersisa
            for row in matrix:
                result.append(row.pop())  # Untuk tiap baris, diambil kolom terakhir
        if matrix:  # Cek matriks masih ada barisan atau tidak
            result += matrix.pop()[::-1]
        if matrix and matrix[0]:
            for row in matrix[::-1]:
                result.append(row.pop(0))
    return result


print(" ".join(spiralOrder(inputs)))
