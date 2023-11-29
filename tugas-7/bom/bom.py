m, n = map(int, input().split())
matrix = [input().split() for _ in range(m)]
number = 0

for i in range(m):
    for j in range(n):
        if matrix[i][j] == "X":
            neighbors = list(
                filter(
                    lambda x: x == "0",
                    [
                        matrix[i + 1][j] if i < m - 1 else None,
                        matrix[i - 1][j] if i > 0 else None,
                        matrix[i][j + 1] if j < len(matrix[0]) - 1 else None,
                        matrix[i][j - 1] if j > 0 else None,
                        matrix[i + 1][j + 1]
                        if i < m - 1 and j < len(matrix[0]) - 1
                        else None,
                        matrix[i + 1][j - 1] if i < m - 1 and j > 0 else None,
                        matrix[i - 1][j + 1]
                        if i > 0 and j < len(matrix[0]) - 1
                        else None,
                        matrix[i - 1][j - 1] if i > 0 and j > 0 else None,
                    ],
                )
            )

            number += len(neighbors)

print(number)
