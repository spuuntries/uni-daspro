# DFS-based.

n, m = list(map(int, input().split()))
mat = [list(map(int, e)) for e in [input().split() for _ in range(n)]]
islands = {}
visited = []


def dfs(start, maze, neighbors=None, current=None, last_branch=None, parents=None):
    if not current:
        current = start

    if not last_branch:
        last_branch = []

    if not parents:
        parents = {}

    def reconstruct(start, end, parents, result=None):
        if not result:
            result = [start]

        if start == end:
            return result

        if parents is not None:
            result.insert(0, parents[start])
            return reconstruct(parents[start], end, parents, result)
        else:
            return result

    neighbors = list(
        map(
            lambda y: y[0],
            filter(
                lambda x: bool(x[1]) and x[0] not in visited,
                dict.items(
                    {
                        (current[0], current[1] - 1): maze[current[0]][current[1] - 1]
                        if current[1] != 0
                        else None,  # Checks left
                        (current[0], current[1] + 1): maze[current[0]][current[1] + 1]
                        if current[1] != len(maze[0]) - 1
                        else None,  # Checks right
                        (current[0] - 1, current[1]): maze[current[0] - 1][current[1]]
                        if current[0] != 0
                        else None,  # Checks up
                        (current[0] + 1, current[1]): maze[current[0] + 1][current[1]]
                        if current[0] != len(maze) - 1
                        else None,  # Checks down
                    }
                ),
            ),
        )
    )

    if not neighbors:
        if not last_branch:
            visited.append(current)
            return reconstruct(current, start, parents)
        else:
            new_branch = last_branch.pop()
            return dfs(start, maze, neighbors, new_branch, last_branch, parents)

    if len(neighbors) > 2:
        last_branch.append(current)

    if current not in visited:
        visited.append(current)

    for n in neighbors:
        parents[n] = current

    return dfs(start, maze, neighbors, neighbors[-1], last_branch, parents)


if not mat or not mat[0]:
    islands = []
else:
    for i, r in enumerate(mat):
        for j, c in enumerate(r):
            if c and (i, j) not in visited:
                visited.append((i, j))
                islands[(i, j)] = dfs((i, j), mat)

print(f"Banyak Pulau: {len(islands)}")
print(
    f"Luas Pulau: {' '.join([str(len(e)) for e in dict.values(islands)]) if islands else '0'}"
)
