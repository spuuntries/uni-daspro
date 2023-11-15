# Practically a DFS implementation, just that the valid moves are only down and right.
# BFS *can* be utilized here, I just wanted to try DFS because it didn't specify shortest path in the problem description.
m, n = map(int, input().split())
maze = [list(map(int, input().split())) for _ in range(n)]


def reconstruct(start, target, parents, path=None):
    if path is None:
        path = []

    if target != start:
        path.insert(0, target)
        target = parents[target]
        return reconstruct(start, target, parents, path)

    path.insert(0, start)
    return path


def solve(maze, current=(0, 0), last_branch=None, parents=None, visited=None):
    if not maze or not maze[0] or not maze[0][0]:
        return None

    if visited is None:
        visited = [(0, 0)]

    if last_branch is None:
        last_branch = []

    if parents is None:
        parents = {}

    if current[0] == len(maze) - 1 and current[1] == len(maze[0]) - 1:
        return reconstruct((0, 0), (len(maze) - 1, len(maze[0]) - 1), parents)

    if len(maze) == 1 and len(maze[0]) == 1:
        return visited

    neighbors = list(
        map(
            lambda y: y[0],
            filter(
                lambda x: bool(x[1]) and x[0] not in visited,
                dict.items(
                    {
                        (current[0] + 1, current[1]): maze[current[0] + 1][current[1]]
                        if current[0] != len(maze) - 1
                        else None,  # Checks down
                        (current[0], current[1] + 1): maze[current[0]][current[1] + 1]
                        if current[1] != len(maze[0]) - 1
                        else None,  # Checks right
                    }
                ),
            ),
        )
    )
    # This bit is a bit ugly (but is actually more fun to read ngl),
    # I recommend looking at mtg() in `dayat/dayat.py` for better flow,
    # but basically:
    # current = (y, x)                                    => y is inverted, so going down is actually +1
    # 1.) {(y + 1, x): node1, (y, x + 1): node2}          => If not at walls of maze, but if so, the entry becomes None
    # 2.) [((y + 1, x), node1), ((y, x + 1), node2)]      => dict.items()
    # 3.) [((y + 1, x), node1), ((y, x + 1), node2)]      => Filter out Nones and all in visited.
    # 4.) [(y + 1, x), (y, x + 1)]                        => Grab the first element of every tuple

    if current not in visited:
        visited += [current]

    if not neighbors:
        if last_branch:
            last = last_branch.pop()
            return solve(maze, last, last_branch, parents, visited)
        else:
            return None

    if len(neighbors) == 2:
        last_branch += [current]

    for n in neighbors:
        parents[n] = current

    # The neighbors[-1] is actually crucial in determining which path the algorithm chooses first,
    # (and consequently, the path you end up with), since in this case we'll always check the route to the right first.
    # But really, it doesn't matter if you're not worried about the resulting path.
    return solve(maze, neighbors[-1], last_branch, parents, visited)


grid = [[0] * m for _ in range(n)]
res = solve(maze)
if not res:
    print("Hari ini Bunda nggak masak")
    exit()
for i in res:
    grid[i[0]][i[1]] = 1
print("\n".join([" ".join(map(str, x)) for x in grid]))
